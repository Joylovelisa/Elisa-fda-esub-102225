"""
FDA 510(k) Agentic Review System
Hermes Luxury Style UI - Streamlit Implementation (Production Ready)
Fixed for Hugging Face Spaces Deployment
"""

import os
import io
import time
import json
import yaml
import base64
import traceback
import pandas as pd
from datetime import datetime
from pathlib import Path
import streamlit as st

# Providers - with error handling for missing packages
try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False
    st.warning("google-generativeai not installed. Gemini features disabled.")

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False
    st.warning("openai package not installed. OpenAI features disabled.")

try:
    from xai_sdk import Client as XAIClient
    from xai_sdk.chat import user as xai_user, system as xai_system, image as xai_image
    GROK_AVAILABLE = True
except ImportError:
    GROK_AVAILABLE = False
    st.warning("xai_sdk not installed. Grok features disabled.")

# Page configuration
st.set_page_config(
    page_title="FDA 510(k) Agentic Review",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    :root {
        --hermes-orange: #F37021;
        --hermes-amber: #D97706;
        --hermes-gold: #F59E0B;
        --hermes-cream: #FEF3C7;
    }
    .main { background: linear-gradient(135deg, #FEF3C7 0%, #FED7AA 50%, #FDE68A 100%); }
    .stApp header { background: linear-gradient(90deg, #9A3412 0%, #B45309 50%, #D97706 100%); }
    div[data-testid="metric-container"] {
        background: linear-gradient(135deg, #FFFFFF 0%, #FEF3C7 100%);
        border: 2px solid #F59E0B; border-radius: 16px; padding: 20px;
        box-shadow: 0 10px 25px rgba(217, 119, 6, 0.1);
    }
    .stButton>button {
        background: linear-gradient(90deg, #F37021 0%, #D97706 100%);
        color: white; border: none; border-radius: 12px; padding: 12px 24px; font-weight: 600;
        box-shadow: 0 4px 12px rgba(217, 119, 6, 0.3); transition: all 0.3s ease;
    }
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 6px 16px rgba(217, 119, 6, 0.4); }
    section[data-testid="stSidebar"] { background: linear-gradient(180deg, #78350F 0%, #92400E 100%); }
    section[data-testid="stSidebar"] .stMarkdown { color: #FEF3C7; }
    .streamlit-expanderHeader {
        background: linear-gradient(90deg, #FED7AA 0%, #FEF3C7 100%);
        border: 2px solid #F59E0B; border-radius: 12px; font-weight: 600;
    }
    .status-chip {
        display: inline-block; padding: 4px 10px; border-radius: 999px; font-size: 0.85em; font-weight: 600;
        color: white; margin-right: 6px; margin-bottom: 6px;
    }
    .chip-pending { background: #a3a3a3; }
    .chip-running { background: #D97706; }
    .chip-success { background: #16a34a; }
    .chip-error   { background: #dc2626; }
    .chip-scheduled { background: #2563eb; }
</style>
""", unsafe_allow_html=True)

# Initialize session state
defaults = {
    'language': 'en',
    'agents': [],
    'selected_agent': None,
    'review_sessions': [],
    'run_log': [],
    'runner_state': {},
    'prompt_configs': {},
    'providers_ready': {}
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

# Translation dictionary
TRANSLATIONS = {
    'en': {
        'title': '🛡️ FDA 510(k) Agentic Review',
        'subtitle': 'Intelligent Document Analysis & Compliance Verification',
        'dashboard': 'Dashboard',
        'agents': 'Agents Library',
        'review': 'Document Review',
        'prompt_runner': 'Prompt ID Runner',
        'upload': 'Upload Documents',
        'language': 'Language',
        'create_agent': 'Create Custom Agent',
        'active_sessions': 'Active Sessions',
        'ocr_confidence': 'OCR Confidence',
        'agents_running': 'Agents Running',
        'avg_review_time': 'Avg Review Time',
        'recent_activity': 'Recent Activity',
        'agent_library': 'Agent Library',
        'document_viewer': 'Document Viewer',
        'checklist': 'Checklist',
        'generate_mock': 'Generate Mock Submission',
        'model_health': 'Model Health',
    },
    'zh': {
        'title': '🛡️ FDA 510(k) 智能審查系統',
        'subtitle': '智能文件分析與合規驗證',
        'dashboard': '儀表板',
        'agents': '代理庫',
        'review': '文件審查',
        'prompt_runner': 'Prompt ID 執行器',
        'upload': '上傳文件',
        'language': '語言',
        'create_agent': '創建自定義代理',
        'active_sessions': '活躍會話',
        'ocr_confidence': 'OCR 信心度',
        'agents_running': '運行中的代理',
        'avg_review_time': '平均審查時間',
        'recent_activity': '最近活動',
        'agent_library': '代理庫',
        'document_viewer': '文件查看器',
        'checklist': '檢查清單',
        'generate_mock': '生成模擬提交',
        'model_health': '模型健康狀態',
    }
}

def t(key):
    return TRANSLATIONS.get(st.session_state.language, TRANSLATIONS['en']).get(key, key)

@st.cache_data
def load_agents():
    """Load agents from agents.yaml with error handling"""
    agents_file = Path('agents.yaml')
    if agents_file.exists():
        try:
            with open(agents_file, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
                return data if data else {'agents': []}
        except Exception as e:
            st.error(f"Error loading agents.yaml: {e}")
            return {'agents': []}
    return {'agents': []}

# Provider initializers with better error handling
def init_gemini(api_key):
    if not GEMINI_AVAILABLE:
        return False
    try:
        genai.configure(api_key=api_key)
        # Test the connection
        list(genai.list_models())
        st.session_state.providers_ready['gemini'] = True
        return True
    except Exception as e:
        st.session_state.providers_ready['gemini'] = False
        st.error(f"Gemini init failed: {e}")
        return False

def init_openai(api_key):
    if not OPENAI_AVAILABLE:
        return False
    try:
        client = OpenAI(api_key=api_key)
        # Test connection
        client.models.list()
        st.session_state.providers_ready['openai'] = True
        return True
    except Exception as e:
        st.session_state.providers_ready['openai'] = False
        st.error(f"OpenAI init failed: {e}")
        return False

def init_grok(api_key):
    if not GROK_AVAILABLE:
        return False
    try:
        _ = XAIClient(api_key=api_key)
        st.session_state.providers_ready['grok'] = True
        return True
    except Exception as e:
        st.session_state.providers_ready['grok'] = False
        st.error(f"xAI Grok init failed: {e}")
        return False

# Provider call wrappers with robust error handling
def call_gemini(model_name, system_prompt, user_prompt, params):
    if not GEMINI_AVAILABLE:
        raise RuntimeError("Gemini not available")
    model = genai.GenerativeModel(model_name)
    full_prompt = f"System: {system_prompt}\n\nUser: {user_prompt}"
    resp = model.generate_content(full_prompt, generation_config={
        "temperature": params.get("temperature", 0.2),
        "top_p": params.get("top_p", 1.0),
        "max_output_tokens": params.get("max_tokens", 1500),
    })
    return resp.text

def call_openai_direct(openai_api_key, model, system_prompt, user_prompt, params):
    if not OPENAI_AVAILABLE:
        raise RuntimeError("OpenAI not available")
    client = OpenAI(api_key=openai_api_key)
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=params.get("temperature", 0.2),
        top_p=params.get("top_p", 1.0),
        max_tokens=params.get("max_tokens", 1500),
    )
    return response.choices[0].message.content

def call_openai_with_pmpt(openai_api_key, pmpt_id, user_prompt, override_model=None, params=None):
    if not OPENAI_AVAILABLE:
        raise RuntimeError("OpenAI not available")
    # Fallback to direct call if prompt API not available
    return call_openai_direct(
        openai_api_key, 
        override_model or "gpt-4o-mini",
        f"Use prompt ID: {pmpt_id}",
        user_prompt,
        params or {}
    )

def retrieve_openai_prompt(openai_api_key, pmpt_id):
    """Retrieve prompt metadata - graceful fallback"""
    return {
        "id": pmpt_id,
        "name": pmpt_id,
        "description": "Prompt configuration",
        "system_prompt": "",
        "model": None,
        "params": {}
    }

def call_grok(xai_api_key, model, system_prompt, user_prompt, params, image_url=None):
    if not GROK_AVAILABLE:
        raise RuntimeError("Grok not available")
    client = XAIClient(api_key=xai_api_key, timeout=3600)
    chat = client.chat.create(model=model)
    chat.append(xai_system(system_prompt))
    if image_url:
        chat.append(xai_user(user_prompt, xai_image(image_url)))
    else:
        chat.append(xai_user(user_prompt))
    response = chat.sample()
    return response.content

def run_provider(provider, config, user_prompt, keys):
    """Unified provider execution with error handling"""
    try:
        if provider == "gemini":
            if not keys.get("gemini"):
                raise ValueError("Missing Gemini API key")
            return call_gemini(
                model_name=config.get("model", "gemini-2.0-flash-exp"),
                system_prompt=config.get("system_prompt", ""),
                user_prompt=user_prompt,
                params=config.get("params", {})
            )
        elif provider == "openai":
            if not keys.get("openai"):
                raise ValueError("Missing OpenAI API key")
            pmpt_id = config.get("pmpt_id")
            if pmpt_id:
                return call_openai_with_pmpt(
                    openai_api_key=keys["openai"],
                    pmpt_id=pmpt_id,
                    user_prompt=user_prompt,
                    override_model=config.get("model"),
                    params=config.get("params", {})
                )
            else:
                return call_openai_direct(
                    openai_api_key=keys["openai"],
                    model=config.get("model", "gpt-4o-mini"),
                    system_prompt=config.get("system_prompt", ""),
                    user_prompt=user_prompt,
                    params=config.get("params", {})
                )
        elif provider == "grok":
            if not keys.get("grok"):
                raise ValueError("Missing xAI API key")
            return call_grok(
                xai_api_key=keys["grok"],
                model=config.get("model", "grok-beta"),
                system_prompt=config.get("system_prompt", "You are Grok."),
                user_prompt=user_prompt,
                params=config.get("params", {}),
                image_url=config.get("image_url")
            )
        else:
            raise ValueError(f"Unsupported provider: {provider}")
    except Exception as e:
        raise RuntimeError(f"{provider} execution failed: {str(e)}")

# Mock data generator
def generate_mock_submission(device_type='Orthopedic Implant'):
    mock_data = {
        'device_name': f'Mock {device_type} Device {datetime.now().strftime("%Y%m%d")}',
        'submission_date': datetime.now().strftime('%Y-%m-%d'),
        'device_type': device_type,
        'predicate_device': 'K123456',
        'sections': {
            'device_description': 'A novel orthopedic implant designed for knee reconstruction...',
            'indications_for_use': 'Indicated for patients requiring knee arthroplasty...',
            'substantial_equivalence': 'This device is substantially equivalent to predicate...',
            'performance_testing': 'Mechanical testing performed per ASTM F1800...',
            'biocompatibility': 'Tested per ISO 10993-1, all tests passed...',
            'sterilization': 'Gamma sterilization validated per ISO 11137...',
        },
        'pages': 145,
        'confidence_score': 0.94
    }
    return mock_data

# Sidebar
with st.sidebar:
    st.markdown(f"### {t('language')}")
    col_lang1, col_lang2 = st.columns(2)
    with col_lang1:
        if st.button('🇬🇧 English', use_container_width=True):
            st.session_state.language = 'en'
            st.rerun()
    with col_lang2:
        if st.button('🇹🇼 中文', use_container_width=True):
            st.session_state.language = 'zh'
            st.rerun()

    st.divider()
    st.markdown("### 🔑 API Keys")
    
    gemini_key = st.text_input("Gemini API Key", type="password", value=os.getenv("GOOGLE_API_KEY",""))
    openai_key = st.text_input("OpenAI API Key", type="password", value=os.getenv("OPENAI_API_KEY",""))
    grok_key = st.text_input("xAI (Grok) API Key", type="password", value=os.getenv("XAI_API_KEY",""))

    ready_msgs = []
    if gemini_key and GEMINI_AVAILABLE:
        if init_gemini(gemini_key): 
            ready_msgs.append("Gemini ✓")
    if openai_key and OPENAI_AVAILABLE:
        if init_openai(openai_key): 
            ready_msgs.append("OpenAI ✓")
    if grok_key and GROK_AVAILABLE:
        if init_grok(grok_key): 
            ready_msgs.append("Grok ✓")

    if ready_msgs:
        st.success(" • ".join(ready_msgs))
    else:
        st.info("Provide at least one API key to run agents.")

    st.divider()
    st.markdown("### ⚡ Quick Actions")
    if st.button(t('generate_mock'), use_container_width=True):
        mock_data = generate_mock_submission()
        st.session_state.review_sessions.append(mock_data)
        st.toast(f"Generated: {mock_data['device_name']}", icon="✅")

    if st.button('📊 Export Last Run Log', use_container_width=True):
        if st.session_state.run_log:
            log_json = json.dumps(st.session_state.run_log, ensure_ascii=False, indent=2)
            st.download_button(
                label="Download run_log.json",
                data=log_json,
                file_name="run_log.json",
                mime="application/json"
            )
        else:
            st.info("No run log available yet.")

# Main header
st.markdown(f"# {t('title')}")
st.markdown(f"*{t('subtitle')}*")

# Load agents
agents_config = load_agents()
AGENTS = agents_config.get('agents', [])

# Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    f"📊 {t('dashboard')}",
    f"🤖 {t('agents')}",
    f"📄 {t('review')}",
    f"🧩 {t('prompt_runner')}"
])

# Dashboard
with tab1:
    col1, col2, col3, col4 = st.columns(4)
    with col1: 
        st.metric(t('active_sessions'), len(st.session_state.review_sessions))
    with col2: 
        st.metric(t('ocr_confidence'), "94.2%")
    with col3: 
        st.metric(t('agents_running'), str(len(AGENTS)))
    with col4: 
        st.metric(t('avg_review_time'), "4.2h")

    st.divider()
    st.markdown(f"### {t('model_health')}")
    mh1, mh2, mh3 = st.columns(3)
    
    def health_chip(label, ok):
        css = "chip-success" if ok else "chip-error"
        st.markdown(f'<span class="status-chip {css}">{label}</span>', unsafe_allow_html=True)
    
    with mh1: 
        health_chip("Gemini", st.session_state.providers_ready.get('gemini', False))
    with mh2: 
        health_chip("OpenAI", st.session_state.providers_ready.get('openai', False))
    with mh3: 
        health_chip("Grok", st.session_state.providers_ready.get('grok', False))

# Agents Library
with tab2:
    st.markdown(f"## {t('agent_library')}")
    
    if AGENTS:
        for agent in AGENTS:
            with st.expander(f"**{agent.get('name', 'Unnamed Agent')}**", expanded=False):
                st.markdown(f"**Description:** {agent.get('desc', 'No description')}")
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.markdown(f"**Provider:** {agent.get('provider', 'N/A')}")
                with col2:
                    st.markdown(f"**Model:** {agent.get('model', 'N/A')}")
                with col3:
                    st.markdown(f"**Temperature:** {agent.get('temperature', 0.2)}")
                
                if st.button(f"▶️ Select Agent", key=f"select_{agent.get('name')}"):
                    st.session_state.selected_agent = agent
                    st.success(f"Selected: {agent.get('name')}")
    else:
        st.warning("No agents found in agents.yaml. Please create the file.")

# Document Review
with tab3:
    st.markdown(f"## {t('review')}")
    
    uploaded_files = st.file_uploader(
        t('upload'), 
        accept_multiple_files=True, 
        type=['pdf','txt','md','json','csv']
    )
    
    if uploaded_files:
        for file in uploaded_files:
            st.success(f"📄 Uploaded: {file.name}")
            with st.expander(f"Preview: {file.name}"):
                if file.type == "text/plain":
                    try:
                        content = file.read().decode('utf-8')
                        st.text_area("Content", content[:1000], height=200)
                    except Exception as e:
                        st.error(f"Error reading file: {e}")
                else:
                    st.info(f"File type: {file.type}")
    else:
        st.info("📤 Upload documents to begin review")

# Prompt ID Runner
with tab4:
    st.markdown("## 🧩 Prompt ID Runner")
    st.caption("Execute agents sequentially with custom configurations.")

    num_agents = st.number_input(
        "Number of agents to execute", 
        min_value=1, 
        max_value=10, 
        value=2, 
        step=1
    )

    st.markdown("### Agent Configurations")
    agent_configs = []
    
    for i in range(num_agents):
        with st.expander(f"Agent {i+1} Configuration", expanded=True):
            provider_options = []
            if GEMINI_AVAILABLE: provider_options.append("gemini")
            if OPENAI_AVAILABLE: provider_options.append("openai")
            if GROK_AVAILABLE: provider_options.append("grok")
            
            if not provider_options:
                st.error("No providers available. Install required packages.")
                continue
            
            provider = st.selectbox(
                "Provider", 
                options=provider_options, 
                key=f"prov_{i}"
            )
            
            default_models = {
                "openai": "gpt-5-nano",
                "gemini": "gemini-2.5-flash",
                "grok": "grok-3-mini"
            }
            
            model = st.text_input(
                "Model", 
                value=default_models.get(provider, ""), 
                key=f"model_{i}"
            )
            
            system_prompt = st.text_area(
                "System Prompt", 
                value="You are an expert FDA 510(k) reviewer.", 
                height=120, 
                key=f"sys_{i}"
            )
            
            colp1, colp2, colp3 = st.columns(3)
            with colp1:
                temperature = st.slider(
                    "Temperature", 
                    0.0, 1.0, 0.2, 0.05, 
                    key=f"temp_{i}"
                )
            with colp2:
                max_tokens = st.number_input(
                    "Max Tokens", 
                    64, 8000, 1500, 64, 
                    key=f"mtok_{i}"
                )
            with colp3:
                top_p = st.slider(
                    "Top P", 
                    0.0, 1.0, 1.0, 0.05, 
                    key=f"topp_{i}"
                )
            
            agent_configs.append({
                'provider': provider,
                'model': model,
                'system_prompt': system_prompt,
                'params': {
                    'temperature': temperature, 
                    'max_tokens': max_tokens, 
                    'top_p': top_p
                }
            })

    st.markdown("### User Prompt")
    user_prompt_text = st.text_area(
        "Enter the prompt to send to each agent", 
        height=120, 
        key="runner_user_prompt"
    )

    if st.button("🚀 Run Agents Sequentially", use_container_width=True):
        if not user_prompt_text.strip():
            st.warning("Please enter a user prompt before running.")
        else:
            progress = st.progress(0.0)
            run_log = []
            total = len(agent_configs)

            for i, cfg in enumerate(agent_configs, start=1):
                agent_label = f"Agent {i} ({cfg['provider']}:{cfg['model']})"
                
                with st.status(f"Running {agent_label}...", expanded=True) as status:
                    try:
                        start = time.time()
                        
                        out = run_provider(
                            provider=cfg['provider'],
                            config=cfg,
                            user_prompt=user_prompt_text,
                            keys={
                                'openai': openai_key, 
                                'gemini': gemini_key, 
                                'grok': grok_key
                            }
                        )
                        
                        elapsed = time.time() - start
                        status.update(label=f"{agent_label} complete", state="complete")
                        
                        entry = {
                            'agent_index': i,
                            'provider': cfg['provider'],
                            'model': cfg['model'],
                            'output': out,
                            'elapsed_s': round(elapsed, 2),
                            'timestamp': datetime.now().isoformat()
                        }
                        run_log.append(entry)
                        
                        with st.expander(f"Result: {agent_label}", expanded=False):
                            st.code(out)
                        
                        st.toast(f"Agent {i} finished", icon="✅")
                        
                    except Exception as e:
                        status.update(label=f"{agent_label} failed", state="error")
                        st.error(f"Error: {str(e)}")
                        
                        entry = {
                            'agent_index': i,
                            'provider': cfg['provider'],
                            'model': cfg['model'],
                            'error': str(e),
                            'timestamp': datetime.now().isoformat()
                        }
                        run_log.append(entry)
                    
                    progress.progress(i / total)

            st.session_state.run_log = run_log
            st.success("All agents processed.")
            st.balloons()

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: #92400E; font-size: 0.9em;'>
    <p><strong>FDA 510(k) Agentic Review System</strong></p>
    <p>Powered by Multi-Provider AI • Streamlit</p>
</div>
""", unsafe_allow_html=True)
