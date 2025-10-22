echnical Specification: Hermes Agentic Review System
1. Software Design Specification (SDS)
1.1. System Overview
The Hermes Agentic Review System is a web-based, single-page application (SPA) designed for intelligent document analysis and compliance verification. It provides a highly interactive and visually appealing "WOW UI" for users to configure and execute complex workflows of AI agents against uploaded documents and user prompts. The system is provider-agnostic, supporting major AI models from Gemini, OpenAI, and Grok, and features a dynamic Directed Acyclic Graph (DAG) for orchestrating agent dependencies.
1.2. Purpose and Scope
Purpose: To provide regulatory officers, compliance analysts, and researchers with a powerful tool to automate and enhance the review of complex documents (e.g., FDA 510(k) submissions).
In Scope:
Client-side PDF document loading, text extraction, and previewing.
Management of a library of pre-configured and user-created AI agents.
Dynamic configuration and execution of agent workflows, including parallel processing based on a dependency graph.
Real-time status monitoring and result visualization.
Flexible API key management (environment variables with session-based fallback).
A highly customizable and themeable user interface.
Out of Scope (Current Version):
User authentication and multi-user collaboration.
Server-side data persistence (all state is session-based).
Batch processing of multiple documents.
Direct integration with external databases or knowledge bases.
1.3. Key Features
Live Dashboard: Real-time metrics and charts on system activity (this is currently a UI prototype and would need live data hooks).
Interactive Agent Library: View, create, and test individual AI agents with modifiable prompts and models.
Advanced Document Review: Upload PDFs, select pages for text extraction, preview pages live, and run configurable agents against the document content.
Prompt Runner with DAG: Define complex agent workflows where agents can run in parallel based on user-defined dependencies. Includes a live visualization of the dependency graph.
Dynamic Theming: Instantly switch between multiple aesthetic themes.
2. System Architecture
The application is a client-side, single-page application built on a modern frontend stack.
2.1. Architectural Style
Component-Based Architecture: The UI is built as a tree of reusable React components. This promotes modularity, maintainability, and a clean separation of concerns. Core UI elements like Card, Metric, and AgentConfigurator are shared across different feature tabs.
Centralized State Management: A global state is managed using React's Context API (AppContext) and a useReducer hook. This provides a single source of truth for shared data like the agent library and run logs, ensuring data consistency across the application without prop-drilling.
Service Layer Abstraction: All external API calls to AI providers are handled within a dedicated service file (services/geminiService.ts). This isolates the business logic from the UI components and makes it easy to update or add new API providers in the future.
2.2. Architecture Diagram (Conceptual)
code
Code
[ User Interface (Browser) ]
│
├── [ React Components (App.tsx) ]
│   │
│   ├── Tabs (Dashboard, Agents, Review, Runner)
│   │   └── Child Components (e.g., DependencyGraph, AgentConfigurator)
│   │
│   └── Shared UI Components (Card, Metric, StatusChip)
│
├── [ Global State (AppContext.tsx) ] <- (Single Source of Truth)
│   │
│   ├── State: { agents, runLog, activityLog }
│   └── Dispatch: Actions to modify state (e.g., ADD_AGENT)
│
├── [ Hooks (usePdfProcessor.ts) ] <- (Encapsulated Logic)
│   └── Handles PDF loading, text extraction, and rendering using `pdf.js`.
│
└── [ Service Layer (geminiService.ts) ] <- (API Abstraction)
    │
    ├── runProvider(config, prompt, apiKeys)
    │
    ├───> [ Google Gemini API ]
    ├───> [ OpenAI API ]
    └───> [ Grok (x.ai) API ]
3. Advanced Prompt Engineering Strategy
The system's effectiveness relies heavily on a structured and detailed prompting strategy. Each agent's system_prompt is engineered to be a comprehensive "meta-prompt" that primes the AI model for a specific expert role.
Key Principles:
Role Priming: The prompt always begins by assigning a specific, expert persona (e.g., "You are an expert FDA 510(k) reviewer for orthopedic device performance testing."). This focuses the model's knowledge and response style.
Task Scoping: The prompt clearly defines the Scope of the agent's task, listing exactly what it should look for and what standards to apply (e.g., "- Applicable standards: ASTM F1717...", "- Test plans: rationale, acceptance criteria...").
Structured Deliverables: The prompt specifies the exact output format under a Deliverables section (e.g., "- Findings in prioritized list (CRITICAL/MAJOR/MINOR)...", "- A concise adequacy conclusion..."). This makes the model's output predictable and easier to parse.
Constraints and Guardrails: The prompt includes negative constraints to prevent speculation and hallucinations (e.g., "Do not speculate; if data are missing or unclear, explicitly flag as a deficiency.").
Example Breakdown (Orthopedic Performance Validator):
code
Yaml
system_prompt: |
  # 1. Role Priming
  You are an expert FDA 510(k) reviewer for orthopedic device performance testing.
  Your task is to critically evaluate the completeness, validity, and sufficiency of bench, wear, and biomechanical testing...

  # 2. Task Scoping (with specific details)
  Scope:
  - Applicable standards: ASTM (e.g., F1717 spinal constructs...), ISO 14242...
  - Test plans: rationale, acceptance criteria, sample size justification...
  - Fatigue and wear: setup fidelity, run-in, lubricant selection...

  # 3. Structured Deliverables (defines output format)
  Deliverables:
  - Findings in prioritized list (CRITICAL/MAJOR/MINOR) with exact page/section references.
  - A concise adequacy conclusion (Adequate / Conditionally adequate / Inadequate)...

  # 4. Constraints (prevents undesirable behavior)
  Do not speculate; if data are missing or unclear, explicitly flag as a deficiency.
When this agent is run, the final prompt sent to the API combines this detailed system prompt with the user-provided context (e.g., extracted document text) to generate a highly specialized and relevant analysis.
4. Environment Settings
To run this application locally for development, you need the following:
Node.js: Version 18.x or later.
Package Manager: npm or yarn.
Environment Variables: The application requires API keys to connect to the AI providers. Create a file named .env in the root directory of the project and add your keys:
code
.env
# Note: The 'VITE_' prefix is required if you are using Vite as the build tool.
# If using Create React App, use 'REACT_APP_'.
# For this project, let's assume a standard setup where these are available under process.env.

OPENAI_API_KEY="sk-..."
GEMINI_API_KEY="..."
XAI_API_KEY="..."
The application is designed to automatically pick up these keys. If they are not set, you can enter them into the UI's sidebar for the current session.
5. Deployment Instructions for Beginners
Here are three simple options to deploy this application and share it with the world.
Option 1: Hugging Face Spaces (Recommended for ML Demos)
Hugging Face Spaces is great for hosting static web apps and managing the necessary API keys securely.
Sign Up/In: Create an account on huggingface.co.
Create a New Space: Click on your profile picture, then "New Space".
Configure the Space:
Space name: Choose a name (e.g., hermes-review-system).
License: Choose a license (e.g., mit).
Space SDK: Select Static.
Click "Create Space".
Upload Files: In your new Space, go to the "Files" tab. You can drag and drop your project's dist (or build) folder contents directly into the file viewer.
Note: First, you need to build the project locally by running npm run build or yarn build. Then upload the contents of the generated dist folder.
Add API Keys (Secrets):
Go to the "Settings" tab in your Space.
Scroll down to "Repository secrets".
Click "New secret".
Add each API key:
Name: OPENAI_API_KEY, Secret value: sk-...
Name: GEMINI_API_KEY, Secret value: ...
Name: XAI_API_KEY, Secret value: ...
These will be available as environment variables when your app runs.
Done! Your application is now live at https://huggingface.co/spaces/YOUR_USERNAME/YOUR_SPACE_NAME.
Option 2: Vercel (Recommended for Frontend Apps)
Vercel offers a seamless deployment experience directly from a Git repository.
Push to GitHub: Make sure your project code is on a GitHub (or GitLab/Bitbucket) repository.
Sign Up/In: Create an account on vercel.com using your GitHub account.
Import Project: On your Vercel dashboard, click "Add New..." -> "Project".
Connect Git: Import your project's repository from GitHub.
Configure Project:
Vercel will automatically detect that it's a React project. The build settings should be correct by default.
Expand the "Environment Variables" section.
Add your API keys one by one (e.g., Name: OPENAI_API_KEY, Value: sk-...).
Deploy: Click the "Deploy" button. Vercel will build and deploy your application.
Done! Vercel will provide you with a live URL. Future pushes to your main branch will automatically trigger new deployments.
Option 3: Netlify
Netlify is another excellent, beginner-friendly platform for deploying static sites.
Push to GitHub: Ensure your project is on a GitHub repository.
Sign Up/In: Create an account on netlify.com using your GitHub account.
Add New Site: On your Netlify dashboard, click "Add new site" -> "Import an existing project".
Connect Git: Connect to your Git provider and choose your project's repository.
Configure Site Settings:
Netlify will detect the build settings. They should be correct by default (npm run build and dist directory).
Before deploying, go to "Site settings" -> "Build & deploy" -> "Environment".
Click "Edit variables" and add your API keys (e.g., Key: OPENAI_API_KEY, Value: sk-...).
Deploy: Go to the "Deploys" tab and trigger a new deploy by clicking "Trigger deploy".
Done! Netlify will build and deploy your site, providing a live URL.
Follow-up Questions
Collaboration & Data Persistence: The current app's state is temporary. What is the priority for adding multi-user support? Should we implement a backend with a database (like Firebase or Supabase) to save agent configurations, document analysis results, and checklists?
Security & Access Control: If we add user accounts, what kind of role-based access control is needed? For example, should there be "Admin," "Reviewer," and "Read-only" roles?
Advanced Document Processing: Currently, we extract plain text. Is there a need to extract more structured data like tables and figures from PDFs? This would require more advanced OCR and layout analysis agents.
Audit Trails: For compliance purposes, is it important to have an immutable audit trail? This would log every agent run, every configuration change, and which user performed the action.
Cost Management & Governance: As API usage grows, would a cost-tracking dashboard and the ability to set budgets or rate limits per user or per project be a valuable feature?
Custom Tools for Agents: The agents.yaml mentions tools (e.g., document_search). Should we build a framework that allows agents to call internal tools, such as a function that searches a specific section of the uploaded document for keywords?
Batch Processing UI: What would be the ideal user interface for uploading a batch of 10-20 documents and applying a single agent workflow to all of them, then viewing a consolidated report?
Offline Functionality: Are there any parts of the application that would benefit from offline capabilities, such as drafting review notes or editing checklists without an internet connection?
