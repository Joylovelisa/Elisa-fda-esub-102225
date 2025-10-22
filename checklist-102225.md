Regulatory-ready re-organization of your submission materials for FDA software review

What you provided
- Source: FDA Guidance “Content of Premarket Submissions for Device Software Functions” (June 14, 2023), complete English text with appendices and figures.

Language handling
- Translation status: Not needed. The provided content is in English. For completeness, a bilingual equivalence table and JSON are included below with “original” and “translated” values identical.

A. Review-ready submission map (Software Documentation Folder index)
Organize the 510(k) submission’s software portion into the following numbered binder to align with FDA’s Table 1 and section VI:

1. Cover and administrative index
   - Device name, model/version
   - Submission type (e.g., 510(k))
   - Contact info; device classification/regulation number; product code(s)

2. Documentation Level evaluation (VI.A; Section V)
   - Declared level: Basic or Enhanced
   - Rationale: hazard analysis summary prior to risk controls (include link to specific hazards in Risk Management File)
   - If Class III, BECS, combination product, or otherwise Enhanced by default, include rationale if proposing Basic

3. Software description (VI.B)
   - Device intended use; software’s role
   - Users and patient population
   - Inputs/outputs; formats; providers/receivers
   - Algorithms/AI-ML details (methods, data, bias mitigation, transparency)
   - OTS components and hosting environment (on-prem, cloud)
   - Interoperability claims and standards
   - Change summary vs. prior cleared/approved version (if applicable)

4. Risk Management File (VI.C)
   4.1 Risk Management Plan (criteria for acceptability and overall residual risk method)
   4.2 Risk Assessment (analysis, evaluation, risk controls, verification of controls, residual risk)
   4.3 Benefit-risk (if any non-acceptable residual risk remains)
   4.4 Risk Management Report (implementation, overall residual risk acceptability, post-production info collection)

5. Software Requirements Specification (SRS) (VI.D)
   - Organized, traceable, testable requirements (system and/or subsystem), including safety-derived requirements
   - Identification/tracking method; highlight requirements critical to safety/effectiveness
   - Differences vs. prior cleared device (if applicable)

6. System and software architecture diagrams (VI.E; Appendix B)
   - Modules, layers, interfaces; data flows; external interfaces/IT/peripherals; “other functions” vs. device function(s)-under-review
   - Legible visuals with legends; references to SRS, SDS, testing

7. Software Design Specification (SDS) (VI.F)
   - Basic: not submitted unless requested (maintain in DHF)
   - Enhanced: submit high- and low-level design; full traceability to SRS; interfaces; prospective design records

8. Software development, configuration management, and maintenance practices (VI.G)
   - Option A: Summaries of lifecycle, coding standards, verification/validation, traceability, CM/change control, maintenance with regression strategy
   - Option B: Declaration of Conformity to FDA-recognized IEC 62304 clauses noted in guidance
   - Enhanced: include CM and maintenance plan documents or DoC breadth per guidance

9. Software testing (Verification and Validation) (VI.H)
   - Basic: Summary of unit, integration, system testing; regression analysis/testing; one complete system-level protocol and report with results and pass/fail
   - Enhanced: All unit and integration level protocols and reports; plus Basic items
   - Explain intentional changes due to failures and re-test results

10. Software version history (VI.I)
   - Line-item table: date, version, change summary since previously tested version; clearly mark final release version; differences between tested and released version; note prior cleared/approved versions and submission numbers

11. Unresolved software anomalies (VI.J)
   - Tabular list: description; discovery method; root cause (if known); impact on safety/effectiveness; outcome; risk rationale for deferral; user mitigations/communications; optional defect taxonomy (e.g., AAMI SW91)

12. Additional information – Regulatory considerations (VII)
   - Statements regarding excluded functions, MDDS, CDS, mobile apps, wellness; references to relevant guidances
   - If proposing a Predetermined Change Control Plan (PCCP), cross-reference Q-Submission discussion

13. Referenced standards and guidances
   - ISO 14971, IEC 62304, AAMI SW91, cybersecurity and human factors guidances, interoperability guidance, OTS guidance, etc.

14. Appendices
   - Traceability matrices (requirements-to-design-to-tests-to-risks)
   - Interoperability conformance reports
   - Cybersecurity architecture and SBOM (if applicable)
   - Human factors linkages (if applicable)

B. Crosswalk (original guidance section to submission section)
- V. Documentation Level -> Section 2
- VI.A Documentation Level Evaluation -> Section 2
- VI.B Software Description -> Section 3
- VI.C Risk Management File -> Section 4
- VI.D SRS -> Section 5
- VI.E Architecture -> Section 6
- VI.F SDS -> Section 7
- VI.G Dev/CM/Maintenance -> Section 8
- VI.H Testing -> Section 9
- VI.I Version History -> Section 10
- VI.J Unresolved Anomalies -> Section 11
- VII Regulatory Considerations -> Section 12
- Appendices -> Section 14

C. Medical device software review checklist (markdown)

- Documentation Level
  - Declared level aligns with risk prior to risk controls
  - Rationale references hazards and intended use
  - If proposing Basic for Class III/BECS/combination: robust justification included

- Software description completeness
  - Intended use and software role clearly described
  - Users and patient population defined
  - Inputs, outputs, and formats specified
  - Algorithm type and methodology explained (incl. AI/ML, datasets, bias, transparency)
  - Platforms and hosting described; OTS use identified
  - Interoperability claims and standards listed
  - Change summary vs. prior cleared version included (if applicable)

- Risk management file
  - Risk Management Plan defines acceptability criteria and overall residual risk evaluation method
  - Risk Assessment covers hazards, sequences of events, hazardous situations, severity, probability approach, initial risk evaluation
  - Risk controls prioritized: design, protective measures, information for safety
  - Verification of risk controls and effectiveness evidenced and traced to SRS/SDS/tests
  - Assessment of new hazards from controls included
  - Residual risk evaluation aligns with plan; benefit-risk provided if needed
  - Risk Management Report confirms implementation, overall acceptability, and post-production data plan

- SRS quality
  - Requirements are complete, consistent, unambiguous, testable, traceable
  - Safety requirements derived from risk analysis included
  - Critical requirements highlighted
  - Differences vs. prior versions identified (if applicable)

- System and software architecture
  - Modules/layers/interfaces and data flows clear and legible
  - External systems/IT/peripherals and “other functions” delineated
  - Diagrams reference SRS/SDS/testing; legend and terminology consistent

- SDS
  - Basic: Available in DHF if requested
  - Enhanced: Submitted; shows how design implements SRS with full traceability; prospective design documentation evident

- Development/CM/maintenance
  - Lifecycle process summary (or IEC 62304 DoC) provided
  - Coding standards, methods, tools listed
  - CM and change management described; baselines and versioning defined
  - Maintenance process includes risk assessment, targeted and regression testing strategy
  - Enhanced: CM and maintenance plan documents provided (or broader DoC)

- Software verification and validation
  - Test coverage at unit, integration, system levels mapped to SRS/design/risks
  - Basic: Full system protocol/report with expected vs. actual results and pass/fail
  - Enhanced: Unit and integration protocols/reports included
  - Failures addressed; re-tests documented; regression analysis/testing adequate
  - Tested version identified; environment and tools specified as needed

- Version history
  - Chronological history with dates, versions, change summaries
  - Final release version identified; differences vs. tested version assessed
  - Prior cleared versions and submission numbers annotated

- Unresolved anomalies
  - Comprehensive table: description, discovery, root cause, impact, outcome, risk rationale
  - Defect taxonomy used (e.g., SW91) or equivalent
  - User mitigations/workarounds and communications referenced

- Regulatory considerations
  - Proper scoping of software functions vs. excluded functions
  - Interoperability, cybersecurity, human factors, OTS, mobile policies observed
  - PCCP status noted (if applicable)

- References and appendices
  - Standards and guidances cited
  - Traceability matrix included
  - Cybersecurity SBOM/architecture provided if applicable

D. Translation equivalence table (English-to-English, as content is already in English)

| Original keyword/information | Translated keyword/information |
|---|---|
| Documentation Level | Documentation Level |
| Basic Documentation Level | Basic Documentation Level |
| Enhanced Documentation Level | Enhanced Documentation Level |
| Device software function | Device software function |
| Hazardous situation | Hazardous situation |
| Serious injury | Serious injury |
| Software Description | Software Description |
| Risk Management File | Risk Management File |
| Risk Management Plan | Risk Management Plan |
| Risk Assessment | Risk Assessment |
| Risk Management Report | Risk Management Report |
| Software Requirements Specification (SRS) | Software Requirements Specification (SRS) |
| System and Software Architecture Diagram | System and Software Architecture Diagram |
| Software Design Specification (SDS) | Software Design Specification (SDS) |
| Verification | Verification |
| Validation | Validation |
| Unit testing | Unit testing |
| Integration testing | Integration testing |
| System testing | System testing |
| Regression testing | Regression testing |
| Software Version History | Software Version History |
| Unresolved Software Anomalies | Unresolved Software Anomalies |
| Off-the-Shelf (OTS) Software | Off-the-Shelf (OTS) Software |
| IEC 62304 | IEC 62304 |
| ISO 14971 | ISO 14971 |
| AAMI SW91 | AAMI SW91 |
| Declaration of Conformity | Declaration of Conformity |
| Intended use | Intended use |
| Interoperability | Interoperability |
| AI/ML-enabled model | AI/ML-enabled model |
| Bias mitigation | Bias mitigation |
| Software Bill of Materials (SBOM) | Software Bill of Materials (SBOM) |
| Cybersecurity | Cybersecurity |
| Design Controls (21 CFR 820.30) | Design Controls (21 CFR 820.30) |
| DHF (Design History File) | DHF (Design History File) |
| QSR (Quality System Regulation) | QSR (Quality System Regulation) |
| Predetermined Change Control Plan (PCCP) | Predetermined Change Control Plan (PCCP) |
| Multiple Function Device Products | Multiple Function Device Products |
| BECS (Blood Establishment Computer Software) | BECS (Blood Establishment Computer Software) |
| 510(k) | 510(k) |
| PMA | PMA |
| De Novo | De Novo |
| IDE | IDE |
| HDE | HDE |
| BLA | BLA |
| CDRH | CDRH |
| CBER | CBER |
| CDER | CDER |
| OCP (Office of Combination Products) | OCP (Office of Combination Products) |
| Hazard | Hazard |
| Harm | Harm |
| Probability (assumed 1 for software failure when needed) | Probability (assumed 1 for software failure when needed) |
| Severity | Severity |
| Risk control: design | Risk control: design |
| Risk control: protective measures | Risk control: protective measures |
| Risk control: information for safety | Risk control: information for safety |
| Benefit-risk analysis | Benefit-risk analysis |
| Traceability | Traceability |
| Architecture modules/layers/interfaces | Architecture modules/layers/interfaces |

E. Translation JSON (same-content English mapping)
{
  "translations": [
    {"original":"Documentation Level","translated":"Documentation Level"},
    {"original":"Basic Documentation Level","translated":"Basic Documentation Level"},
    {"original":"Enhanced Documentation Level","translated":"Enhanced Documentation Level"},
    {"original":"Device software function","translated":"Device software function"},
    {"original":"Hazardous situation","translated":"Hazardous situation"},
    {"original":"Serious injury","translated":"Serious injury"},
    {"original":"Software Description","translated":"Software Description"},
    {"original":"Risk Management File","translated":"Risk Management File"},
    {"original":"Risk Management Plan","translated":"Risk Management Plan"},
    {"original":"Risk Assessment","translated":"Risk Assessment"},
    {"original":"Risk Management Report","translated":"Risk Management Report"},
    {"original":"Software Requirements Specification (SRS)","translated":"Software Requirements Specification (SRS)"},
    {"original":"System and Software Architecture Diagram","translated":"System and Software Architecture Diagram"},
    {"original":"Software Design Specification (SDS)","translated":"Software Design Specification (SDS)"},
    {"original":"Verification","translated":"Verification"},
    {"original":"Validation","translated":"Validation"},
    {"original":"Unit testing","translated":"Unit testing"},
    {"original":"Integration testing","translated":"Integration testing"},
    {"original":"System testing","translated":"System testing"},
    {"original":"Regression testing","translated":"Regression testing"},
    {"original":"Software Version History","translated":"Software Version History"},
    {"original":"Unresolved Software Anomalies","translated":"Unresolved Software Anomalies"},
    {"original":"Off-the-Shelf (OTS) Software","translated":"Off-the-Shelf (OTS) Software"},
    {"original":"IEC 62304","translated":"IEC 62304"},
    {"original":"ISO 14971","translated":"ISO 14971"},
    {"original":"AAMI SW91","translated":"AAMI SW91"},
    {"original":"Declaration of Conformity","translated":"Declaration of Conformity"},
    {"original":"Intended use","translated":"Intended use"},
    {"original":"Interoperability","translated":"Interoperability"},
    {"original":"AI/ML-enabled model","translated":"AI/ML-enabled model"},
    {"original":"Bias mitigation","translated":"Bias mitigation"},
    {"original":"Software Bill of Materials (SBOM)","translated":"Software Bill of Materials (SBOM)"},
    {"original":"Cybersecurity","translated":"Cybersecurity"},
    {"original":"Design Controls (21 CFR 820.30)","translated":"Design Controls (21 CFR 820.30)"},
    {"original":"DHF (Design History File)","translated":"DHF (Design History File)"},
    {"original":"QSR (Quality System Regulation)","translated":"QSR (Quality System Regulation)"},
    {"original":"Predetermined Change Control Plan (PCCP)","translated":"Predetermined Change Control Plan (PCCP)"},
    {"original":"Multiple Function Device Products","translated":"Multiple Function Device Products"},
    {"original":"BECS (Blood Establishment Computer Software)","translated":"BECS (Blood Establishment Computer Software)"},
    {"original":"510(k)","translated":"510(k)"},
    {"original":"PMA","translated":"PMA"},
    {"original":"De Novo","translated":"De Novo"},
    {"original":"IDE","translated":"IDE"},
    {"original":"HDE","translated":"HDE"},
    {"original":"BLA","translated":"BLA"},
    {"original":"CDRH","translated":"CDRH"},
    {"original":"CBER","translated":"CBER"},
    {"original":"CDER","translated":"CDER"},
    {"original":"OCP (Office of Combination Products)","translated":"OCP (Office of Combination Products)"},
    {"original":"Hazard","translated":"Hazard"},
    {"original":"Harm","translated":"Harm"},
    {"original":"Probability (assume 1 when appropriate)","translated":"Probability (assume 1 when appropriate)"},
    {"original":"Severity","translated":"Severity"},
    {"original":"Risk control: design","translated":"Risk control: design"},
    {"original":"Risk control: protective measures","translated":"Risk control: protective measures"},
    {"original":"Risk control: information for safety","translated":"Risk control: information for safety"},
    {"original":"Benefit-risk analysis","translated":"Benefit-risk analysis"},
    {"original":"Traceability","translated":"Traceability"},
    {"original":"Architecture modules/layers/interfaces","translated":"Architecture modules/layers/interfaces"}
  ]
}

F. 100 entities derived from the document (summary JSON with entity, title, context, keywords)
[
  {"entity":"Documentation Level","title":"Risk-based documentation level","context":"Determines Basic vs Enhanced software documentation based on hazard of death/serious injury prior to risk controls.","keywords":["Basic","Enhanced","risk","hazardous situation"]},
  {"entity":"Basic Documentation Level","title":"Lower-risk software documentation","context":"Applies when failures would not present probable risk of death/serious injury before risk controls.","keywords":["risk","software","510k"]},
  {"entity":"Enhanced Documentation Level","title":"Higher-risk software documentation","context":"Applies when failures could present probable risk of death/serious injury before risk controls; includes SDS and detailed tests.","keywords":["high risk","SDS","unit/integration tests"]},
  {"entity":"Device software function","title":"Software that is a medical device","context":"A software function meeting FD&C Act 201(h).","keywords":["function","device","FDCA"]},
  {"entity":"Off-the-Shelf Software","title":"OTS software components","context":"Software for which manufacturer lacks full lifecycle control (OS, libraries).","keywords":["OTS","COTS","libraries"]},
  {"entity":"Serious injury","title":"Reportable harm definition","context":"Life-threatening, permanent impairment, or necessitating intervention to preclude permanence.","keywords":["21 CFR 803.3(w)","harm"]},
  {"entity":"Software verification","title":"Phase-output conformance","context":"Confirms outputs meet inputs; includes code reviews, inspections, testing, traceability.","keywords":["verification","reviews","testing"]},
  {"entity":"Software validation","title":"Meets user needs/intended use","context":"Objective evidence in actual/simulated use; relies on prior verification.","keywords":["validation","use environment"]},
  {"entity":"QSR Design Controls","title":"21 CFR 820.30","context":"Requires software validation and risk analysis; DHF maintenance.","keywords":["QSR","DHF","design inputs"]},
  {"entity":"Risk Management Plan","title":"Plan for risk activities","context":"Sets acceptability criteria and overall residual risk method.","keywords":["ISO 14971","criteria"]},
  {"entity":"Risk Analysis","title":"Identify hazards and causes","context":"Hazards, sequences, hazardous situations, severity, probability approach.","keywords":["hazards","hazardous situations"]},
  {"entity":"Risk Evaluation","title":"Initial acceptability","context":"Assess if risk acceptable and if controls needed per plan.","keywords":["acceptability","criteria"]},
  {"entity":"Risk Control Measures","title":"Controls to reduce risk","context":"Priority: design, protective measures, information for safety; verify implementation and effectiveness.","keywords":["controls","design","alarms","warnings"]},
  {"entity":"Residual Risk Evaluation","title":"Post-control acceptability","context":"Assess residual risk; if not acceptable, provide benefit-risk.","keywords":["residual risk","benefit-risk"]},
  {"entity":"Risk Management Report","title":"Evidence of implementation","context":"Shows plan executed, overall residual risk acceptable, post-market info process.","keywords":["report","post-production"]},
  {"entity":"SRS","title":"Software requirements specification","context":"Inputs/outputs, functions, interfaces, performance, safety, ranges, limits; traceable and testable.","keywords":["requirements","traceability"]},
  {"entity":"SDS","title":"Software design specification","context":"How SRS is implemented; high- and low-level design; prospective documentation.","keywords":["design","architecture","interfaces"]},
  {"entity":"Architecture Diagram","title":"System/software architecture","context":"Modules, layers, interfaces, data flows, external interactions; legible and referenced.","keywords":["diagram","modules","interfaces"]},
  {"entity":"Unit Testing","title":"Module-level tests","context":"Verify individual units/components against design/specs.","keywords":["unit tests","verification"]},
  {"entity":"Integration Testing","title":"Interface-level tests","context":"Verify internal/external interfaces and interactions.","keywords":["integration","interfaces"]},
  {"entity":"System Testing","title":"Functional, end-to-end tests","context":"Execute protocols; expected vs actual results with pass/fail.","keywords":["system tests","protocols"]},
  {"entity":"Regression Analysis","title":"Change impact analysis","context":"Determines needed regression tests for unintended effects.","keywords":["regression","impact"]},
  {"entity":"Regression Testing","title":"Re-run prior tests","context":"Detect unintended effects after changes by comparing results.","keywords":["retest","changes"]},
  {"entity":"Version History","title":"Software changes over time","context":"Dates, versions, change summaries; final release vs tested differences.","keywords":["versioning","history"]},
  {"entity":"Unresolved Anomalies","title":"Deferred defects","context":"Describe, root cause, impact, rationale for not fixing, mitigations.","keywords":["defects","risk-based deferral"]},
  {"entity":"AAMI SW91","title":"Defect classification","context":"Taxonomy for classifying software defects in health software.","keywords":["taxonomy","defect classes"]},
  {"entity":"IEC 62304","title":"Software lifecycle standard","context":"Development, maintenance, configuration management processes; DoC option.","keywords":["62304","DoC"]},
  {"entity":"ISO 14971","title":"Risk management standard","context":"Framework for risk activities and documentation.","keywords":["14971","risk management"]},
  {"entity":"SBOM","title":"Software bill of materials","context":"List of software components (commercial, open source, OTS, in-house).","keywords":["components","supply chain"]},
  {"entity":"Cybersecurity","title":"Security risk management","context":"Lifecycle approach to vulnerabilities; may require additional diagrams and content.","keywords":["security","vulnerabilities"]},
  {"entity":"Interoperability","title":"Electronic interfaces","context":"Device transmits/exchanges/uses info with other products; standards disclosed.","keywords":["interfaces","standards"]},
  {"entity":"AI/ML Methods","title":"Model use in device","context":"Methods, data provenance, bias handling, transparency materials.","keywords":["AI","ML","datasets"]},
  {"entity":"Multiple Function Device","title":"Other functions policy","context":"Assess adverse/positive impact of non-device or other functions.","keywords":["other functions","impact analysis"]},
  {"entity":"PCCP","title":"Predetermined Change Control Plan","context":"Plan for changes without supplemental 510(k)/PMA when cleared/approved.","keywords":["FDORA 515C","changes"]},
  {"entity":"eCopy","title":"Submission media format","context":"Architecture diagrams should align with eCopy guidelines.","keywords":["submission","format"]},
  {"entity":"Q-Submission","title":"Pre-sub feedback","context":"Engage FDA on Documentation Level, PCCP, or approach.","keywords":["pre-sub","feedback"]},
  {"entity":"Human Factors","title":"Usability engineering","context":"Apply HF/UE guidance where relevant; integrate with risk control.","keywords":["usability","HF/UE"]},
  {"entity":"OTS Guidance","title":"Use of OTS software","context":"Provide additional information per OTS guidance if used.","keywords":["OTS","COTS"]},
  {"entity":"Cybersecurity Premarket","title":"Cybersecurity content","context":"Follow security guidance for premarket submissions.","keywords":["security","premarket"]},
  {"entity":"Interoperable Device Guidance","title":"Design and submission for interoperability","context":"Include interface specs and conformance where applicable.","keywords":["interoperability","conformance"]},
  {"entity":"Validation in QSR","title":"820.30(g) software validation","context":"Design validation includes software validation and risk analysis.","keywords":["820.30(g)","validation"]},
  {"entity":"DHF","title":"Design History File","context":"Compilation of design records showing compliance with plan and QSR.","keywords":["DHF","records"]},
  {"entity":"Combination Product","title":"Drug-device/biologic-device","context":"Device constituent part may need Enhanced documentation; OCP engagement.","keywords":["combination","OCP"]},
  {"entity":"BECS","title":"Blood establishment software","context":"Enhanced documentation recommended due to high-risk use.","keywords":["blood","BECS"]},
  {"entity":"Class III Devices","title":"High-risk classification","context":"Generally expect Enhanced documentation; justify if proposing Basic.","keywords":["Class III","PMA"]},
  {"entity":"Hazard","title":"Potential source of harm","context":"Used in risk analysis to identify hazardous situations.","keywords":["hazard","risk"]},
  {"entity":"Hazardous Situation","title":"Exposure to hazard","context":"Sequence/combination of events leading to exposure.","keywords":["exposure","events"]},
  {"entity":"Harm","title":"Injury/damage","context":"Health/property/environment damage definition.","keywords":["injury","damage"]},
  {"entity":"Probability Assumption","title":"Set to 1 where appropriate","context":"For software failure probability when uncertain, worst-case approach.","keywords":["probability","assumption"]},
  {"entity":"Protective Measures","title":"Risk control type","context":"E.g., defensive programming, alarms, automatic interlocks.","keywords":["controls","alarms"]},
  {"entity":"Information for Safety","title":"Risk control type","context":"Warnings, labeling, training; lowest-priority control.","keywords":["warnings","IFU"]},
  {"entity":"Design Controls as Risk Control","title":"Primary risk mitigation","context":"Eliminate hazards via design and architecture.","keywords":["design","architecture"]},
  {"entity":"Traceability Matrix","title":"Linkage across lifecycle","context":"Link hazards -> SRS -> SDS -> tests -> results.","keywords":["traceability","matrix"]},
  {"entity":"System Diagram Legibility","title":"Diagram quality requirement","context":"Readable, consistent notation, scaled appropriately.","keywords":["diagram","quality"]},
  {"entity":"State Diagrams","title":"Dynamic behavior depiction","context":"Optional for clarity of states/transitions.","keywords":["state","behavior"]},
  {"entity":"Data Flow","title":"Information movement","context":"Inputs/outputs and transformations across modules.","keywords":["data flow","IO"]},
  {"entity":"External Interfaces","title":"Connections outside system","context":"Printers, networks, EHRs, mobile devices, cloud.","keywords":["interfaces","external"]},
  {"entity":"Testing Protocol","title":"Formal test procedure","context":"Expected vs actual, pass/fail, objective criteria.","keywords":["protocol","results"]},
  {"entity":"Test Report","title":"Execution evidence","context":"Shows protocol completion and outcomes; anomalies documented.","keywords":["report","evidence"]},
  {"entity":"Change Management","title":"Configuration control","context":"Processes to manage changes, baselines, versioning.","keywords":["CM","change control"]},
  {"entity":"Maintenance Process","title":"Post-release changes","context":"Risk assessment, targeted tests, regression plan.","keywords":["maintenance","postmarket"]},
  {"entity":"Coding Standards","title":"Development norms","context":"Language/style rules, static analysis, code review policies.","keywords":["coding","standards"]},
  {"entity":"Tools and Methods","title":"Dev/test toolchain","context":"Compilers, static analyzers, CI/CD, test frameworks.","keywords":["tools","methods"]},
 {"entity":"User Mitigations","title":"Workarounds for anomalies","context":"Communicated actions to safely operate despite known defects.","keywords":["workaround","communication"]},
  {"entity":"Customer Notification","title":"Communication to users","context":"Labeling or notices about unresolved anomalies/risk.","keywords":["notification","labeling"]},
  {"entity":"Submission Cross-references","title":"Linking sections","context":"References among SRS, SDS, test, risk to speed review.","keywords":["cross-reference","navigation"]},
  {"entity":"510(k) Pathway","title":"Premarket notification","context":"Common pathway for many SaMD and device software.","keywords":["510k","premarket"]},
  {"entity":"De Novo Pathway","title":"Novel low/moderate risk","context":"Alternative for new device types without predicates.","keywords":["De Novo","novel"]},
  {"entity":"PMA Pathway","title":"Class III approval","context":"High-risk devices requiring PMA evidence.","keywords":["PMA","approval"]},
  {"entity":"IDE","title":"Investigational device exemption","context":"Permits clinical investigations of devices.","keywords":["IDE","clinical"]},
  {"entity":"HDE","title":"Humanitarian Device Exemption","context":"For rare conditions; lower evidence threshold.","keywords":["HDE","rare disease"]},
  {"entity":"BLA","title":"Biologics License Application","context":"Certain devices in combination may be reviewed in BLAs.","keywords":["BLA","biologics"]},
  {"entity":"CDRH","title":"Center for Devices and Radiological Health","context":"Primary device review center.","keywords":["CDRH","review"]},
  {"entity":"CBER","title":"Center for Biologics Evaluation and Research","context":"Leads certain combo or IVD reviews.","keywords":["CBER","biologics"]},
  {"entity":"CDER","title":"Center for Drug Evaluation and Research","context":"Leads certain combo products.","keywords":["CDER","drugs"]},
  {"entity":"OCP","title":"Office of Combination Products","context":"Engagement for combination products.","keywords":["OCP","combination"]},
  {"entity":"Wellness Policy","title":"General wellness devices","context":"Low-risk policy for general wellness.","keywords":["wellness","policy"]},
  {"entity":"Mobile Medical Applications","title":"Software function policy","context":"Policy for device software functions and apps.","keywords":["mobile","software policy"]},
  {"entity":"MDDS","title":"Data systems policy","context":"Medical device data systems and image storage/communication.","keywords":["MDDS","imaging"]},
  {"entity":"CDS","title":"Clinical decision support","context":"Policy for certain decision support software.","keywords":["CDS","software"]},
  {"entity":"Multiple Function Impact","title":"Interaction analysis","context":"Assess adverse/positive impact of other functions.","keywords":["impact","analysis"]},
  {"entity":"Worst-case Probability","title":"Conservative assumption","context":"Set probability to 1 when estimation unreliable.","keywords":["probability","conservative"]},
  {"entity":"Protective Interlocks","title":"Automatic safeguards","context":"Halt therapy/results upon fault detection.","keywords":["interlock","safety"]},
  {"entity":"Alarms and Alerts","title":"User notification","context":"Timely warning of abnormal conditions or failures.","keywords":["alarm","alert"]},
  {"entity":"Training Materials","title":"Information for safety","context":"User training as part of risk controls.","keywords":["training","IFU"]},
  {"entity":"Clinical Workflow Mapping","title":"Steps replaced by software","context":"Explain manual actions impacted or automated.","keywords":["workflow","manual steps"]},
  {"entity":"Hosting Environments","title":"Where software runs","context":"Hospital network, cloud, edge; functions mapped.","keywords":["hosting","cloud","on-prem"]},
  {"entity":"External Networking","title":"Connectivity surfaces","context":"Network/wireless interfaces; security implications.","keywords":["network","wireless"]},
  {"entity":"User Roles","title":"Intended users","context":"Patient, caregiver, HCP; permissions/UX implications.","keywords":["users","roles"]},
  {"entity":"Patient Population","title":"Target demographic/condition","context":"Disease, age, comorbidities; scope of use.","keywords":["population","indication"]},
  {"entity":"Inputs","title":"Data ingested","context":"Signals, images, measurements, reports, questionnaires.","keywords":["inputs","data types"]},
  {"entity":"Outputs","title":"Device results/actions","context":"Diagnostics, therapy parameters, alarms, control signals.","keywords":["outputs","results"]},
  {"entity":"Data Provenance","title":"AI/ML training data","context":"Populations, sampling, collection time/place.","keywords":["provenance","dataset"]},
  {"entity":"Model Transparency","title":"Communications on AI/ML","context":"Materials explaining model development/performance/limits.","keywords":["transparency","explainability"]},
  {"entity":"Change Summary","title":"Differences vs prior submission","context":"Pertinent software changes affecting safety/effectiveness.","keywords":["changes","delta"]},
  {"entity":"Diagram Legend","title":"Notation clarity","context":"Defines icons, line types, colors used in diagrams.","keywords":["legend","notation"]},
  {"entity":"Terminology Consistency","title":"Uniform naming","context":"Consistent terms across diagrams and documents.","keywords":["terminology","consistency"]},
  {"entity":"Appendix A Examples","title":"Documentation Level examples","context":"Illustrative devices for Basic vs Enhanced.","keywords":["examples","risk mapping"]},
  {"entity":"Appendix B Diagrams","title":"Architecture examples","context":"Sample diagrams for handheld, implantable, cloud algorithm.","keywords":["examples","architecture"]},
  {"entity":"Modified Device Submission","title":"Change from cleared device","context":"Provide prior submission number and highlight changes.","keywords":["modification","predicate"]},
  {"entity":"Overall Residual Risk","title":"Aggregate acceptability","context":"Method to decide total residual risk vs benefits.","keywords":["overall risk","benefit"]},
  {"entity":"Post-production Info","title":"Production/field data","context":"Collection and assessment processes for new hazards.","keywords":["postmarket","feedback"]},
  {"entity":"Test Environment","title":"Setup for V&V","context":"Hardware, software, versions, data sets used for tests.","keywords":["testbed","environment"]},
  {"entity":"Pass/Fail Criteria","title":"Objective thresholds","context":"Define acceptance criteria for each test case.","keywords":["acceptance criteria","testing"]},
  {"entity":"Intentional Changes After Failures","title":"Fix-and-retest documentation","context":"Record changes made to pass tests and verification evidence.","keywords":["fix","retest"]},
  {"entity":"Release Candidate","title":"Candidate software version","context":"Version under consideration with unresolved anomalies assessed.","keywords":["release","candidate"]},
  {"entity":"User Communications","title":"End-user notices","context":"Labeling or field notices for anomalies and mitigations.","keywords":["communications","users"]},
  {"entity":"EHR Interfacing","title":"Clinical data exchange","context":"If interfacing, state standards and security controls.","keywords":["EHR","HL7","FHIR"]},
  {"entity":"Predicate Device Mapping","title":"510(k) alignment","context":"Software delta vs predicate, impact on risk and testing.","keywords":["predicate","substantial equivalence"]},
  {"entity":"Locked vs Adaptive Models","title":"AI model update behavior","context":"Fixed vs continuously learning models; change control approach.","keywords":["locked","adaptive","updates"]},
  {"entity":"Standards DoC","title":"Declaration of Conformity","context":"Used to streamline review for IEC 62304 clauses.","keywords":["DoC","standard compliance"]},
  {"entity":"Safety-Critical Requirements","title":"High-impact SRS items","context":"Call out requirements with most impact on safety/effectiveness.","keywords":["critical","requirements"]},
  {"entity":"Interface Specifications","title":"External interface details","context":"Protocols, data formats, timing for interoperability.","keywords":["specs","interfaces"]},
  {"entity":"Timing and Performance","title":"SRS performance parameters","context":"Latency, throughput, memory, CPU constraints.","keywords":["timing","performance"]},
  {"entity":"Error Handling","title":"Fault management","context":"Definitions, interrupts, exceptions, recovery behavior.","keywords":["errors","recovery"]},
  {"entity":"Safety Requirements","title":"Risk-derived requirements","context":"SRS items created from risk analysis.","keywords":["safety","requirements"]},
  {"entity":"Architecture-to-SRS Trace","title":"Design traceability","context":"Map modules to requirements and vice versa.","keywords":["trace","mapping"]}
]

G. Notes for assembly
- Keep diagrams readable in the eCopy (no cropping; adequate font).
- Include cross-references at the top of each section to quickly link to related content (e.g., “See Risk HAZ-012 controls in SRS-REQ-045 and tests SYS-TC-077/INT-TC-021.”).
- If proposing PCCP or adaptive AI/ML, pre-engage via Q-Submission; include guardrails, triggers, and verification plans.

H. Deliverables recap
- Reorganized software submission index and crosswalk
- FDA checklist in markdown
- Translation equivalence table in markdown (English-to-English)
- Translation JSON (English-to-English)
- 100-entity JSON summary

10 comprehensive follow-up questions
1) What Documentation Level are you declaring for your device software and what specific pre-control hazards drive that decision? Please cite 3–5 highest-severity hazardous situations. 
2) Which parts of your software are OTS, and do you have an SBOM and OTS risk/maintenance strategy aligned with cybersecurity guidance? 
3) For AI/ML-enabled functions, what are the model types, training/validation datasets, bias analyses, and transparency materials you will include? 
4) How does your SRS highlight safety-critical requirements, and how will you present traceability from those to design and tests? 
5) What interoperability interfaces are claimed, and which standards/specifications (e.g., HL7/FHIR, IEEE, DICOM) and conformance evidence will you provide? 
6) Describe your regression analysis method. How do you determine the scope of regression testing after changes and record objective pass/fail? 
7) For Enhanced submissions, what granularity of SDS and unit/integration test artifacts will you provide to demonstrate complete implementation of SRS? 
8) How will you document unresolved anomalies at release, classify them (e.g., SW91), communicate mitigations to users, and monitor in postmarket? 
9) If you plan a PCCP or anticipate frequent software updates (e.g., cloud, AI), what verification triggers, limits of change, and labeling adaptations will your plan include? 
10) What is your overall residual risk determination method, and how will you justify benefit-risk for any non-acceptable residual risks after controls?
