from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak, KeepTogether
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY

# ── Colour palette ──────────────────────────────────────────────────────────
DARK_BG   = colors.HexColor("#0D1117")
ACCENT    = colors.HexColor("#00C8FF")
ACCENT2   = colors.HexColor("#FF6B35")
SECTION   = colors.HexColor("#161B22")
CARD_BG   = colors.HexColor("#1C2333")
TEXT_MAIN = colors.HexColor("#E6EDF3")
TEXT_SUB  = colors.HexColor("#8B949E")
GREEN     = colors.HexColor("#3FB950")
YELLOW    = colors.HexColor("#D29922")
RED       = colors.HexColor("#F85149")
PURPLE    = colors.HexColor("#A371F7")

W, H = A4

def build_styles():
    """Define all paragraph styles including table cell styles."""
    def S(name, **kw):
        return ParagraphStyle(name, **kw)

    return {
        "cover_title": S("cover_title", fontSize=28, textColor=ACCENT,
                          fontName="Helvetica-Bold", alignment=TA_CENTER, spaceAfter=6),
        "cover_sub":   S("cover_sub",   fontSize=13, textColor=TEXT_MAIN,
                          fontName="Helvetica", alignment=TA_CENTER, spaceAfter=4),
        "cover_meta":  S("cover_meta",  fontSize=10, textColor=TEXT_SUB,
                          fontName="Helvetica", alignment=TA_CENTER, spaceAfter=2),

        "h1": S("h1", fontSize=17, textColor=ACCENT, fontName="Helvetica-Bold",
                 spaceBefore=18, spaceAfter=6),
        "h2": S("h2", fontSize=13, textColor=ACCENT2, fontName="Helvetica-Bold",
                 spaceBefore=12, spaceAfter=4),
        "h3": S("h3", fontSize=11, textColor=GREEN, fontName="Helvetica-Bold",
                 spaceBefore=8, spaceAfter=3),

        "q":  S("q",  fontSize=10, textColor=YELLOW, fontName="Helvetica-Bold",
                 spaceBefore=6, spaceAfter=2, leftIndent=8),
        "a":  S("a",  fontSize=9,  textColor=TEXT_MAIN, fontName="Helvetica",
                 spaceAfter=4, leftIndent=16, leading=14),
        "bullet": S("bullet", fontSize=9, textColor=TEXT_MAIN, fontName="Helvetica",
                     spaceAfter=2, leftIndent=20, bulletIndent=10, leading=13),
        "code": S("code", fontSize=8, textColor=GREEN, fontName="Courier",
                   spaceAfter=4, leftIndent=20, leading=12),
        "note": S("note", fontSize=8, textColor=PURPLE, fontName="Helvetica-Oblique",
                   spaceAfter=3, leftIndent=16),
        "body": S("body", fontSize=9, textColor=TEXT_MAIN, fontName="Helvetica",
                   spaceAfter=5, leading=14, alignment=TA_JUSTIFY),
        "tag":  S("tag",  fontSize=8, textColor=ACCENT, fontName="Helvetica-Bold",
                   spaceAfter=2, leftIndent=8),

        # Table cell styles — Paragraphs wrap text; raw strings do not
        "th": S("th", fontSize=8, textColor=ACCENT, fontName="Helvetica-Bold",
                 leading=11, wordWrap="LTR"),
        "td": S("td", fontSize=8, textColor=TEXT_MAIN, fontName="Helvetica",
                 leading=11, wordWrap="LTR"),
    }

def hr(color=ACCENT, thickness=1):
    return HRFlowable(width="100%", thickness=thickness, color=color, spaceAfter=4, spaceBefore=4)

def qa(q_text, a_text, styles):
    """Return a Q+A block."""
    return [
        Paragraph(f"Q: {q_text}", styles["q"]),
        Paragraph(a_text, styles["a"]),
    ]

def bullet_list(items, styles):
    return [Paragraph(f"• {i}", styles["bullet"]) for i in items]

def section_header(title, styles):
    return [hr(ACCENT, 2), Paragraph(title, styles["h1"]), hr(ACCENT, 0.5)]

def colored_table(data, col_widths, header_bg=SECTION):
    """Build a styled dark table — cells wrapped in Paragraph for proper text wrapping."""
    th_style = ParagraphStyle("_th", fontSize=8, textColor=ACCENT,
                               fontName="Helvetica-Bold", leading=11, wordWrap="LTR")
    td_style = ParagraphStyle("_td", fontSize=8, textColor=TEXT_MAIN,
                               fontName="Helvetica", leading=11, wordWrap="LTR")

    # Wrap every cell in a Paragraph so long text wraps instead of overflowing
    wrapped = []
    for r_idx, row in enumerate(data):
        new_row = [Paragraph(str(cell), th_style if r_idx == 0 else td_style) for cell in row]
        wrapped.append(new_row)

    t = Table(wrapped, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND",    (0, 0), (-1,  0), header_bg),
        ("BACKGROUND",    (0, 1), (-1, -1), DARK_BG),
        ("ROWBACKGROUNDS",(0, 1), (-1, -1), [DARK_BG, CARD_BG]),
        ("GRID",          (0, 0), (-1, -1), 0.5, colors.HexColor("#30363D")),
        ("VALIGN",        (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING",    (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING",   (0, 0), (-1, -1), 6),
        ("RIGHTPADDING",  (0, 0), (-1, -1), 6),
    ]))
    return t

# ═══════════════════════════════════════════════════════════════════════════════
# CONTENT BUILDERS
# ═══════════════════════════════════════════════════════════════════════════════

def cover_page(story, S):
    story.append(Spacer(1, 2*cm))
    story.append(Paragraph("SOC ENGINEER", S["cover_title"]))
    # story.append(Paragraph("Interview Preparation Guide", S["cover_sub"]))
    story.append(Spacer(1, 0.3*cm))
    story.append(hr(ACCENT2, 2))
    story.append(Spacer(1, 0.3*cm))
    story.append(Paragraph("2 YOE | SOC Engineer Interview Preparation", S["cover_sub"]))
    story.append(Spacer(1, 1*cm))

    meta = [
        "Threat Intelligence  •  Detection Engineering  •  SIEM Operations",
        "MITRE ATT&CK  •  Malware Analysis  •  Sigma Rules  •  Python Automation",
        "PCI DSS  •  Network Security  •  OSI Model  •   Threat Landscape",
    ]
    for m in meta:
        story.append(Paragraph(m, S["cover_meta"]))

    story.append(Spacer(1, 1.5*cm))
    sections = [
        ["#", "Section", "Topics"],
        ["1", "SOC Interview Q&A", "Threat Intel, Detection, SIEM, Malware, MITRE, Sigma, Automation"],
        ["2", "Fintech Threat Landscape", "Top Threat Actors, Active Malware, Tools, Attack Vectors"],
        ["3", "PCI DSS v4.0",            "12 Requirements, SOC Responsibilities, Violations"],
        ["4", "OSI Model & Network Attacks","Layer Attacks, Mitigations, Examples"],
        ["5", "SOC & SIEM Deep Dive",    "Architecture, Use Cases, Detection Logic, IR"],
        ["6", "Dilemmas & Dangers",       "Alert Fatigue, False Positives, Insider Threats"],
        ["7", "Quick Cheatsheet","Commands, Tools, IOC Types, TTP Matrix"],
    ]
    story.append(colored_table(sections, [0.6*cm, 5*cm, 9.5*cm]))
    story.append(PageBreak())

def section1_cv_qa(story, S):
    story += section_header("SECTION 1 — CV-BASED INTERVIEW Q&A", S)
    story.append(Paragraph("Questions mapped directly to your experience and role requirements.", S["body"]))

    # --- Threat Intelligence ---
    story.append(Paragraph("1.1  Threat Intelligence", S["h2"]))
    qas = [
        ("Walk me through how you convert a vendor threat report into an actionable detection.",
         "I start by parsing the report for IOCs (IPs, hashes, domains), TTPs mapped to MITRE ATT&CK, "
         "and adversary objectives. I then enrich the IOCs via VirusTotal, Shodan, or AbuseIPDB APIs, "
         "profile the threat actor (motivation, target sector), and build a simulation package (strike) "
         "replicating the kill chain. Finally I write Sigma rules for the key behavioral patterns and "
         "ingest the enriched data into the SIEM as a threat intel feed."),

        ("What intelligence feeds do you use and how do you prioritize them?",
         "Primary: MISP feeds, AlienVault OTX, Mandiant Advantage, CERT advisories (sector-specific). "
         "Secondary: Twitter/X threat intel community, Shodan trending ports, vendor blogs (CrowdStrike, "
         "Recorded Future). Prioritization: relevance to our sector (fintech), recency (&lt;72h for critical), "
         "confidence score, and whether IOCs appear in our telemetry. High-fidelity, sector-specific intel "
         "always takes precedence over bulk commodity feeds."),

        ("How do you track adversary campaign evolution over time?",
         "I maintain a threat actor dossier per group: known aliases, infrastructure patterns, preferred "
         "initial access vectors, and TTP drift across campaigns. I correlate new IOCs against historical "
         "campaigns using diamond model attributes (adversary, infrastructure, capability, victim). "
         "Automated pivoting in tools like Maltego or MISP helps surface infrastructure overlaps "
         "linking new activity to known actors."),

        ("Explain the Diamond Model vs. Kill Chain — which do you prefer for fintech?",
         "Kill Chain (Lockheed Martin) is linear, great for understanding attack phases and where to "
         "interrupt. Diamond Model is relational — it models the relationship between adversary, "
         "infrastructure, capability, and victim, making it superior for attribution and campaign "
         "tracking. For fintech I use both: Kill Chain for detection gap mapping per phase, "
         "Diamond Model for adversary profiling and linking campaigns to known threat groups."),
    ]
    for q, a in qas:
        story += qa(q, a, S)
    story.append(Spacer(1, 0.3*cm))

    # --- Detection Engineering ---
    story.append(Paragraph("1.2  Detection Engineering & Sigma Rules", S["h2"]))
    qas2 = [
        ("Write a Sigma rule detecting a suspicious PowerShell encoded command execution.",
         "Below is a production-quality rule mapped to T1059.001:"),
        ("What is the difference between a signature-based and behavior-based detection?",
         "Signature-based matches exact IOCs (hash, IP, string) — fast, low FP, but bypassed by "
         "obfuscation. Behavior-based detects TTPs (e.g., process hollowing, LSASS access) — "
         "harder to evade but higher FP rate. Best practice is layered: signature catches known-bad "
         "quickly; behavioral catches novel variants. In fintech I prioritize behavioral rules for "
         "credential theft and lateral movement since adversaries rotate IOCs frequently."),
        ("How do you tune a SIEM rule to reduce false positives without losing coverage?",
         "1) Baseline legitimate behavior for the specific environment (e.g., admin scripts that "
         "run encoded PS). 2) Add exclusion conditions (user=svc_deploy, host in IT_WHITELIST). "
         "3) Increase specificity (add parent process, network connection, or file creation context). "
         "4) Use risk scoring — don't alert on the rule alone, correlate with other signals. "
         "5) Track TP/FP ratio weekly and adjust thresholds. Never suppress without documenting why."),
        ("How do you map a new Sigma rule to MITRE ATT&CK?",
         "I identify the primary technique from the behavior being detected (e.g., T1055 for process "
         "injection), then add sub-technique if applicable (T1055.012 for process hollowing). "
         "In the Sigma rule tags I include: 'attack.t1055', 'attack.defense_evasion'. "
         "I cross-reference the ATT&CK navigator to check existing detection coverage and identify "
         "gaps. This feeds back into our detection roadmap to prioritize uncovered techniques."),
    ]
    for i, (q, a) in enumerate(qas2):
        story.append(Paragraph(f"Q: {q}", S["q"]))
        story.append(Paragraph(a, S["a"]))
        if i == 0:
            sigma = (
                "title: Suspicious PowerShell Encoded Command\n"
                "id: a3b2c1d0-1234-5678-abcd-ef0123456789\n"
                "status: production\n"
                "description: Detects encoded PS execution (T1059.001)\n"
                "tags:\n  - attack.execution\n  - attack.t1059.001\n"
                "logsource:\n  category: process_creation\n  product: windows\n"
                "detection:\n"
                "  selection:\n    Image|endswith: '\\\\powershell.exe'\n"
                "    CommandLine|contains|all:\n      - '-EncodedCommand'\n      - '-NonI'\n"
                "  filter_legitimate:\n    ParentImage|endswith:\n"
                "      - '\\\\sccm.exe'\n      - '\\\\msiexec.exe'\n"
                "  condition: selection and not filter_legitimate\n"
                "falsepositives:\n  - Legitimate admin automation\n"
                "level: high"
            )
            story.append(Paragraph(sigma.replace("\n","<br/>"), S["code"]))
    story.append(Spacer(1, 0.3*cm))

    # --- SIEM Operations ---
    story.append(Paragraph("1.3  SIEM Operations", S["h2"]))
    qas3 = [
        ("What log sources are critical for a fintech SIEM and why?",
         "Tier 1 (must-have): EDR telemetry (process, network, file events), AD/LDAP logs "
         "(authentication, group changes), email gateway (phishing, attachments), WAF/proxy logs "
         "(C2 callbacks, data exfil), cloud audit logs (AWS CloudTrail, Azure Activity Log), "
         "payment system logs (transaction anomalies, API abuse). "
         "Tier 2: DNS logs (beaconing detection), DHCP (IP-to-host correlation), "
         "database audit logs (PCI DSS requirement), network flow (NetFlow/IPFIX)."),

        ("Describe a multi-stage SIEM attack scenario you built in your lab.",
         "Example: Phishing simulation. Stage 1 — email gateway log shows attachment delivery "
         "(known malicious hash). Stage 2 — EDR log shows macro execution spawning cmd.exe "
         "(T1566.001 → T1059.003). Stage 3 — network log shows HTTPS beacon to C2 every 60s "
         "(T1071.001 beaconing). Stage 4 — LDAP log shows BloodHound-style enumeration "
         "(T1087.002). Stage 5 — SMB lateral movement to finance server. Each stage "
         "correlates in the SIEM as a chain, triggering escalating severity alerts."),

        ("How do you handle alert fatigue in a high-volume SOC?",
         "1) Risk-based alerting: score events, only page on high-risk chains not individual events. "
         "2) Playbook automation: SOAR handles L1 enrichment automatically, analyst only sees "
         "pre-enriched, pre-triaged cases. 3) Regular rule review: weekly TP/FP analysis, "
         "suppress or retune noisy rules. 4) Tiered escalation: L1 handles volume, L2 handles "
         "complex cases, L3 does deep investigation. 5) Metrics: track MTTD, MTTR, and "
         "analyst case load to identify bottlenecks early."),
    ]
    for q, a in qas3:
        story += qa(q, a, S)

    # --- Malware Analysis ---
    story.append(Paragraph("1.4  Malware Analysis", S["h2"]))
    qas4 = [
        ("What is your malware detonation methodology?",
         "1) Static analysis first: hash lookup (VT/MalwareBazaar), strings extraction, PE header "
         "analysis (section entropy, imports), YARA scanning. 2) Dynamic analysis in isolated VM "
         "(Flare VM/REMnux): detonate in Cuckoo or Any.run sandbox, observe API calls, network "
         "traffic, registry/file changes, injected processes. 3) Behavioral mapping: map observed "
         "behaviors to MITRE ATT&CK techniques. 4) IOC extraction: C2 IPs/domains, mutex names, "
         "registry keys, file paths. 5) Report generation for detection team."),

        ("How do you detect process injection in a SIEM?",
         "Look for: CreateRemoteThread calls from unexpected processes, WriteProcessMemory "
         "followed by CreateThread, VirtualAllocEx with PAGE_EXECUTE_READWRITE, "
         "processes with no parent (orphaned). In SIEM rules: detect svchost.exe with "
         "a non-services.exe parent, or lsass.exe accessed by a non-SYSTEM process. "
         "EDR telemetry is key here — Sysmon EventID 8 (CreateRemoteThread) and "
         "EventID 10 (ProcessAccess) are primary signals."),

        ("Explain the difference between a dropper, loader, and payload.",
         "Dropper: delivers and writes the malware to disk, may self-delete. "
         "Loader: loads the payload into memory (often fileless), may decrypt/unpack it. "
         "Payload: the final malicious code (RAT, ransomware, stealer). "
         "Modern malware chains: email attachment (dropper) → PowerShell (loader) → "
         "Cobalt Strike beacon (payload). Understanding this chain helps map each stage "
         "to a MITRE technique and write targeted detections per stage."),
    ]
    for q, a in qas4:
        story += qa(q, a, S)

    # --- Python Automation ---
    story.append(Paragraph("1.5  Python Automation & LLM Pipelines", S["h2"]))
    qas5 = [
        ("Describe your Python pipeline for IOC enrichment.",
         "Input: raw IOC list (IPs, hashes, domains) from threat report. "
         "Step 1: classify IOC type using regex. "
         "Step 2: async API calls to VirusTotal v3, AbuseIPDB, Shodan, URLhaus. "
         "Step 3: aggregate scores, flag high-confidence malicious IOCs. "
         "Step 4: LLM (via API) summarizes context and suggests MITRE technique mappings. "
         "Step 5: structured JSON output ingested into SIEM threat intel feed or MISP. "
         "Rate limiting, retry logic, and caching (Redis) are implemented to avoid API exhaustion."),

        ("How did you use LLMs in your simulation package generation?",
         "I fed the LLM a structured prompt containing the threat report summary, extracted IOCs, "
         "and target environment profile. The LLM generated: attack narrative, step-by-step "
         "simulation commands mapped to MITRE techniques, and Sigma detection drafts. "
         "A human review step validated accuracy before ingestion. This reduced simulation "
         "package creation time from ~4 hours to ~45 minutes per report."),
    ]
    for q, a in qas5:
        story += qa(q, a, S)
    story.append(PageBreak())

def section2_fintech(story, S):
    story += section_header("SECTION 2 — FINTECH THREAT LANDSCAPE", S)

    story.append(Paragraph("2.1  Top Active Threat Actors Targeting Fintech", S["h2"]))
    actors = [
        ["Threat Actor", "Origin", "Primary TTP", "Notable Targets", "Active"],
        ["Lazarus Group (APT38)", "DPRK", "SWIFT fraud, crypto theft, RATs", "Banks, crypto exchanges", "YES"],
        ["FIN7 / Carbanak", "Russia/UKR", "POS malware, spear-phishing, BEC", "Banks, POS networks", "YES"],
        ["Scattered Spider", "W. English", "SIM swap, MFA fatigue, social eng.", "MGM, Caesars, fintechs", "YES"],
        ["Silence Group", "Russia", "ATM jackpotting, SWIFT attacks", "Banks in Eastern Europe/Asia", "YES"],
        ["TA505", "Russia", "Dridex, FlawedAmmyy, phishing campaigns", "Banks, insurance, fintech", "YES"],
        ["Dragonbridge / APT41", "China", "Supply chain, espionage, fraud", "Crypto, fintech platforms", "YES"],
        ["Evil Corp", "Russia", "Dridex, WastedLocker ransomware", "Financial sector globally", "YES"],
        ["UNC3944 / 0ktapus", "Unknown", "Okta attacks, SMS phishing", "Cloud-hosted fintechs", "YES"],
    ]
    story.append(colored_table(actors, [3.2*cm, 2*cm, 4*cm, 3.5*cm, 1.5*cm]))
    story.append(Spacer(1, 0.4*cm))

    story.append(Paragraph("2.2  Most Active Malware Families in Fintech (2024–2025)", S["h2"]))
    malware = [
        ["Malware", "Type", "Key Behavior", "MITRE Techniques"],
        ["QakBot (Qbot)", "Banking Trojan/Loader", "Email hijack, lateral movement, Cobalt Strike drop", "T1566, T1059, T1071"],
        ["IcedID (BokBot)", "Banking Trojan", "Web inject, form grabbing, proxy", "T1566.001, T1185"],
        ["Emotet (reborn)", "Modular Loader", "Spam botnet, module delivery", "T1547, T1059.005"],
        ["Cobalt Strike", "C2 Framework (abused)", "Beaconing, lateral movement, credential dump", "T1071, T1055, T1003"],
        ["Lumma Stealer", "Info Stealer", "Browser cred theft, crypto wallet drain", "T1555, T1539"],
        ["Gozi / ISFB", "Banking Trojan", "Webinjects, VNC module, HVNC", "T1185, T1021"],
        ["DarkGate", "Loader/RAT", "Multi-stage loader, remote access", "T1059, T1071.001"],
        ["Ransomware (LockBit 3.0, Black Basta)", "Ransomware", "Data exfil + encryption, double extortion", "T1486, T1041"],
        ["AsyncRAT / QuasarRAT", "Remote Access Trojan", "Keylogging, screenshot, file exfil", "T1056, T1113"],
    ]
    story.append(colored_table(malware, [2.8*cm, 2.5*cm, 4.5*cm, 4.2*cm]))
    story.append(Spacer(1, 0.4*cm))

    story.append(Paragraph("2.3  Attack Vectors Common in Fintech", S["h2"]))
    vectors = [
        ("Phishing / Spear-Phishing", "Email with malicious attachments or links targeting finance staff. BEC (Business Email Compromise) targeting CFOs for wire transfer fraud."),
        ("API Abuse", "Exploiting poorly secured REST APIs in payment platforms. Brute-force API keys, parameter tampering, excessive data retrieval."),
        ("Credential Stuffing", "Leaked credential databases used against banking portals. Automated bots test millions of combinations. Defense: MFA, device fingerprinting, rate limiting."),
        ("SIM Swapping", "Social engineering mobile carriers to redirect victim's number. Bypasses SMS-based 2FA. Major threat for crypto and mobile banking."),
        ("Supply Chain Attacks", "Compromise of third-party SDKs or payment processors used by the fintech. E.g., malicious npm package, compromised CI/CD pipeline."),
        ("Insider Threats", "Privileged employees exfiltrating customer PII or transaction data. Common in fintechs due to broad data access for 'move fast' culture."),
        ("ATM / POS Jackpotting", "Malware installed on ATM OS (XFS layer) to dispense cash on command. Black Box attacks physically connect to ATM dispenser."),
    ]
    for name, desc in vectors:
        story.append(Paragraph(f"▸ {name}", S["h3"]))
        story.append(Paragraph(desc, S["a"]))

    story.append(Paragraph("2.4  Key Tools in SOC / Fintech Security", S["h2"]))
    tools = [
        ["Category", "Tools"],
        ["SIEM", "Splunk, Microsoft Sentinel, IBM QRadar, Elastic SIEM, Chronicle"],
        ["EDR / XDR", "CrowdStrike Falcon, SentinelOne, Microsoft Defender XDR, Carbon Black"],
        ["Threat Intel", "MISP, OpenCTI, Recorded Future, Mandiant, ThreatConnect, AlienVault OTX"],
        ["Malware Analysis", "Any.run, Cuckoo Sandbox, Flare VM, REMnux, IDA Pro, Ghidra, x64dbg"],
        ["Detection", "Sigma (rules), YARA (patterns), Snort/Suricata (network IDS)"],
        ["SOAR", "Splunk SOAR (Phantom), Palo Alto XSOAR, IBM Resilient, Tines"],
        ["Network", "Wireshark, Zeek (Bro), NetworkMiner, Suricata, Nmap, Shodan"],
        ["Forensics", "Volatility, Autopsy, FTK, Velociraptor, KAPE, Plaso"],
        ["Vulnerability", "Nessus, OpenVAS, Qualys, Rapid7 InsightVM, Burp Suite"],
        ["Cloud Security", "AWS GuardDuty, Azure Sentinel, Prisma Cloud, Wiz"],
    ]
    story.append(colored_table(tools, [3.5*cm, 10.5*cm]))
    story.append(PageBreak())

def section3_pcidss(story, S):
    story += section_header("SECTION 3 — PCI DSS v4.0 FOR SOC ANALYSTS", S)
    story.append(Paragraph(
        "PCI DSS (Payment Card Industry Data Security Standard) v4.0 released March 2022. "
        "Mandatory for any entity storing, processing, or transmitting cardholder data (CHD). "
        "As a SOC analyst in fintech, you are directly responsible for multiple requirements.",
        S["body"]))

    story.append(Paragraph("3.1  The 12 Requirements — SOC Relevance", S["h2"]))
    reqs = [
        ["Req #", "Requirement", "SOC Relevance"],
        ["1", "Install & maintain network security controls", "Monitor firewall rules, alert on unauthorized changes (T1562)"],
        ["2", "Apply secure configs to all system components", "Detect misconfigurations, CIS benchmark violations"],
        ["3", "Protect stored account data", "Alert on unencrypted PAN in logs, unauthorized DB access"],
        ["4", "Protect cardholder data with strong cryptography in transit", "Detect plain-text transmission (HTTP, FTP with sensitive data)"],
        ["5", "Protect all systems against malware", "EDR telemetry correlation, malware detection use cases in SIEM"],
        ["6", "Develop and maintain secure systems and software", "Alert on patch lag, detect exploitation of known vulns"],
        ["7", "Restrict access to system components by need-to-know", "Detect privilege escalation, unauthorized access attempts"],
        ["8", "Identify users and authenticate access", "Monitor failed logins, MFA bypass attempts, shared accounts"],
        ["9", "Restrict physical access to cardholder data", "Out of SOC scope typically; but badge reader log correlation"],
        ["10", "Log and monitor all access to system components", "CORE SOC FUNCTION — SIEM ingestion, log integrity, retention"],
        ["11", "Test security of systems and networks regularly", "Pentest results feed into detection gaps, vuln scan alerts"],
        ["12", "Support information security with org policies", "Incident response procedures, security awareness"],
    ]
    story.append(colored_table(reqs, [1.2*cm, 5.5*cm, 7.3*cm]))
    story.append(Spacer(1, 0.4*cm))

    story.append(Paragraph("3.2  Requirement 10 Deep Dive — Most Critical for SOC", S["h2"]))
    r10 = [
        "10.2: Audit logs must capture: all access to CHD, admin actions, access to audit trails, invalid access attempts, use of elevated privileges, changes to identification/authentication mechanisms.",
        "10.3: Protect audit logs from destruction/modification — store off-system, use write-once media or SIEM with tamper detection.",
        "10.4: Log review — Req 10.4.1 requires daily review of security events. As SOC analyst this is your primary daily function.",
        "10.5: Retain audit log history for at least 12 months, with 3 months immediately available for analysis.",
        "10.6: Synchronize clocks (NTP) — critical for SIEM correlation. Clock skew breaks event correlation.",
        "10.7: Failures of critical security controls must be detected and reported promptly — map this to your SIEM health monitoring alerts.",
    ]
    for item in r10:
        story.append(Paragraph(f"• {item}", S["bullet"]))

    story.append(Paragraph("3.3  Common PCI DSS Violations Detected in SOC", S["h2"]))
    viols = [
        ["Violation", "Detection Method", "Alert Example"],
        ["Unencrypted PAN in logs", "DLP + regex pattern matching on CHD fields", "Sigma: log line matches PAN regex outside secure zone"],
        ["Unauthorized CHD access", "DB audit logs + privileged access monitoring", "Non-admin user SELECT on card_number table at 2AM"],
        ["Missing log sources", "SIEM health check — expected vs actual log volumes", "Payment gateway logs silent for &gt;15 minutes"],
        ["Shared/default credentials", "Authentication log analysis", "Multiple concurrent sessions same service account"],
        ["Unpatched systems in CDE", "Vuln scan integration + SIEM asset tagging", "CVE exploit attempt against known-unpatched host"],
        ["Excessive access rights", "IAM review + SIEM privilege monitoring", "Contractor account accessing CHD beyond contract end"],
    ]
    story.append(colored_table(viols, [3.5*cm, 4.5*cm, 6*cm]))
    story.append(PageBreak())

def section4_osi_network(story, S):
    story += section_header("SECTION 4 — OSI MODEL & NETWORK ATTACKS", S)

    story.append(Paragraph("4.1  OSI Layer Attack Matrix", S["h2"]))
    osi = [
        ["Layer", "Name", "Key Attacks", "Detection & Mitigation"],
        ["L7", "Application", "SQLi, XSS, CSRF, API abuse, phishing, HTTP floods", "WAF, input validation, rate limiting, OWASP controls"],
        ["L6", "Presentation", "SSL stripping, malformed TLS, data encoding attacks", "TLS 1.2+ enforcement, cert pinning, HSTS"],
        ["L5", "Session", "Session hijacking, cookie theft, replay attacks", "Secure cookies (HttpOnly/Secure), token rotation, MFA"],
        ["L4", "Transport", "SYN flood, TCP RST injection, port scanning, UDP flood", "Stateful firewall, SYN cookies, IDS rate limiting"],
        ["L3", "Network", "IP spoofing, ICMP flood, BGP hijacking, MITM routing", "BCP38 filtering, uRPF, route authentication (RPKI)"],
        ["L2", "Data Link", "ARP spoofing, MAC flooding, VLAN hopping, 802.1X bypass", "Dynamic ARP Inspection, port security, 802.1X"],
        ["L1", "Physical", "Cable tapping, hardware implants, RF jamming", "Physical security, fiber monitoring, tamper detection"],
    ]
    story.append(colored_table(osi, [0.8*cm, 2.2*cm, 4.5*cm, 6.5*cm]))
    story.append(Spacer(1, 0.4*cm))

    story.append(Paragraph("4.2  Critical Network Attacks — Detailed Examples", S["h2"]))

    attacks = [
        ("ARP Spoofing (L2)", 
         "Attacker sends gratuitous ARP replies associating their MAC with the gateway IP. "
         "All traffic meant for the gateway flows through the attacker (MITM). "
         "In fintech, this enables credential interception on internal networks.",
         "Detection: SIEM alert on multiple MACs claiming same IP (ARP table anomaly). "
         "Mitigation: Dynamic ARP Inspection (DAI) on switches, static ARP entries for critical hosts."),

        ("SYN Flood (L4)",
         "Attacker sends thousands of SYN packets with spoofed source IPs. Server allocates "
         "half-open connections exhausting the connection table. Payment API becomes unavailable.",
         "Detection: NetFlow anomaly — abnormal SYN:SYN-ACK ratio. "
         "Mitigation: SYN cookies (kernel-level), upstream scrubbing (Cloudflare, AWS Shield)."),

        ("DNS Hijacking / Tunneling",
         "Hijacking: Attacker modifies DNS responses to redirect users to fake banking site. "
         "Tunneling: C2 communication encoded in DNS queries (low-and-slow exfil). "
         "Particularly dangerous for fintech — redirect banking domain to credential harvesting site.",
         "Detection: Baseline DNS query volume per host, alert on high-entropy domain names "
         "(DGA), alert on DNS queries to newly registered domains (&lt;30 days). "
         "Mitigation: DNSSEC, DNS filtering (Cisco Umbrella, Quad9), monitor DNS over HTTPS."),

        ("Lateral Movement via SMB / Pass-the-Hash",
         "After compromising one workstation, attacker extracts NTLM hashes from memory (Mimikatz). "
         "These hashes are replayed to authenticate to other systems without knowing the plaintext. "
         "In fintech, this enables access to financial databases from a single compromised endpoint.",
         "Detection: Sysmon EventID 3 (network connection) from workstation to SMB port on server, "
         "EventID 4624 logon type 3 with NTLM auth at unusual hours. "
         "Mitigation: Disable NTLM where possible, enforce Kerberos, enable Credential Guard, "
         "network segmentation preventing workstation-to-server SMB."),

        ("Beaconing / C2 Communication",
         "Malware periodically contacts C2 server at regular intervals (e.g., every 60 seconds). "
         "Often uses legitimate protocols (HTTPS, DNS) to blend with normal traffic. "
         "Modern variants use jitter (±20% interval randomization) to evade static detection.",
         "Detection: Zeek/Suricata connection logs — statistical analysis for periodic connection "
         "patterns, low byte count, consistent user agents. SIEM query: connections to same IP "
         "within 5% time variance over 24h. "
         "Mitigation: Proxy with SSL inspection, outbound firewall whitelist, threat intel-fed blocking."),
    ]
    for name, detail, mitigation in attacks:
        story.append(Paragraph(f"▸ {name}", S["h3"]))
        story.append(Paragraph(detail, S["a"]))
        story.append(Paragraph(f"🛡  {mitigation}", S["note"]))
    story.append(PageBreak())

def section5_soc_siem(story, S):
    story += section_header("SECTION 5 — SOC & SIEM DEEP DIVE", S)

    story.append(Paragraph("5.1  SIEM Architecture", S["h2"]))
    arch = [
        "Log Collection: Agents (Beats, NXLog, Universal Forwarder), syslog, API pull, cloud connectors.",
        "Normalization: Parse raw logs into common schema (CEF, ECS, OCSF). Field extraction, timestamp normalization.",
        "Correlation Engine: Rule-based (Sigma), statistical (ML baseline), behavioral (UEBA). Event chains across time windows.",
        "Storage: Hot tier (recent, fast SSD) → Warm tier (90 days, slower) → Cold tier (archive, compliance).",
        "Alerting: Risk scoring, deduplication, suppression windows, integration with SOAR/ticketing.",
        "Investigation: Search, pivot (IP → user → host), timeline reconstruction, threat intel enrichment.",
    ]
    for item in arch:
        story.append(Paragraph(f"• {item}", S["bullet"]))
    story.append(Spacer(1, 0.3*cm))

    story.append(Paragraph("5.2  Key Detection Use Cases for Fintech SIEM", S["h2"]))
    ucases = [
        ["Use Case", "Log Sources", "Detection Logic", "MITRE"],
        ["Credential Stuffing", "Auth logs, WAF", "High failed logins from distributed IPs within short window", "T1110.004"],
        ["Phishing Click", "Email GW + Proxy", "User clicks URL in email then proxy logs suspicious domain GET", "T1566.002"],
        ["LSASS Memory Dump", "EDR/Sysmon", "Process accessing lsass.exe with PROCESS_VM_READ rights", "T1003.001"],
        ["Kerberoasting", "AD Security Logs", "EventID 4769: TGS request for service with RC4 encryption from non-service account", "T1558.003"],
        ["DCSync Attack", "AD Security Logs", "Non-DC machine requesting replication rights (4662 with GUID DS-Replication)", "T1003.006"],
        ["Data Exfiltration", "DLP + Proxy + EDR", "Large outbound POST to external IP + file read spike on finance share", "T1041"],
        ["Ransomware Pre-cursor", "EDR + File Logs", "Rapid file rename + .vssadmin delete shadows command", "T1486, T1490"],
        ["Insider Threat", "DLP + UEBA + Badge", "After-hours DB access + mass download + VPN to non-standard location", "T1078"],
        ["API Key Theft", "Cloud Audit Logs", "API call from new IP/region, then sudden resource creation/deletion", "T1552.005"],
        ["Webshell Deploy", "WAF + Web Server", "POST to .aspx/.php file in web root followed by GET execution", "T1505.003"],
    ]
    story.append(colored_table(ucases, [3*cm, 3*cm, 6*cm, 2*cm]))
    story.append(Spacer(1, 0.4*cm))

    story.append(Paragraph("5.3  SOC Incident Response Workflow", S["h2"]))
    ir_steps = [
        ("1. Detection", "SIEM alert fires. Analyst reviews alert metadata, enriches IOCs, checks threat intel."),
        ("2. Triage", "Confirm TP vs FP. Context: asset criticality, user role, time of day, similar past alerts."),
        ("3. Containment", "Isolate affected host via EDR, block IPs/domains in firewall/proxy, reset credentials."),
        ("4. Investigation", "Timeline reconstruction, lateral movement check, blast radius assessment, root cause."),
        ("5. Eradication", "Remove malware/persistence mechanisms, patch exploited vuln, revoke compromised creds."),
        ("6. Recovery", "Restore from clean backup, validate systems clean, monitor intensively post-recovery."),
        ("7. Post-Incident", "Write detailed IR report, update SIEM rules to catch variant, share IOCs with community."),
    ]
    for step, desc in ir_steps:
        story.append(Paragraph(f"  {step}", S["h3"]))
        story.append(Paragraph(desc, S["a"]))
    story.append(PageBreak())

def section6_dilemmas(story, S):
    story += section_header("SECTION 6 — DANGERS, DILEMMAS & HARD QUESTIONS", S)

    story.append(Paragraph("6.1  Real Interview Scenario Questions", S["h2"]))

    scenarios = [
        ("SCENARIO: You receive an alert at 3AM — a domain controller is running Mimikatz. What do you do?",
         "1) Immediately escalate to L3/IR Lead and notify management — this is a critical incident (T1003). "
         "2) Capture volatile memory on the DC if possible WITHOUT taking it offline (domain disruption risk). "
         "3) Check authentication logs for the past 24h — what accounts were accessed from this DC? "
         "4) Isolate the DC from the rest of the network IF you can keep domain functionality (secondary DC available). "
         "5) Identify initial access vector (phishing, lateral movement path from another host). "
         "6) Assume credential compromise — force password reset for all privileged accounts. "
         "7) Activate IR playbook, preserve evidence, document timeline."),

        ("SCENARIO: A developer pushes code that hardcodes an AWS secret key to a public GitHub repo.",
         "1) Immediately invalidate the exposed key in AWS IAM — this takes priority over investigation. "
         "2) Review CloudTrail logs for the past 24h — was the key used by anyone other than the developer? "
         "3) If used: treat as active compromise — check for resource creation (crypto mining), "
         "data access, or exfiltration of S3 buckets. "
         "4) Notify Security Lead, possibly CISO, potentially data breach team if CHD/PII was accessible. "
         "5) Rotate all credentials that were accessible via the compromised key. "
         "6) Implement preventive controls: pre-commit hooks (git-secrets), AWS Config for exposed key detection."),

        ("DILEMMA: Your SOC is understaffed and you're receiving 10,000 alerts/day. How do you prioritize?",
         "1) Risk-based triage: assets in CDE (cardholder data environment) and Tier-1 systems first. "
         "2) Alert fatigue analysis: identify top 5 noisiest rules, tune or suppress with documentation. "
         "3) SOAR automation: auto-close obvious false positives (known scanner IPs, patch management tools). "
         "4) SLA definition: P1 (active breach) = 15 min, P2 (active threat) = 1h, P3 (suspicious) = 4h. "
         "5) Escalate the staffing issue to management with data: show alert volume vs analyst capacity. "
         "This is a real problem — framing it as a business risk (MTTR too high = breach dwell time) "
         "is how you escalate effectively."),

        ("DILEMMA: Threat intel shows an IOC (IP) is malicious, but it belongs to a CDN used by your payment processor.",
         "1) Do NOT block the IP immediately — this could take down payment processing. "
         "2) Confirm attribution: is the specific IP/path being used for malicious activity against YOU, "
         "or is it just flagged generally in TI feeds? "
         "3) Check your logs: is there actual traffic to this IOC in your environment? What's the context? "
         "4) Coordinate with payment processor to understand if IP is legitimately theirs. "
         "5) If confirmed malicious path: work with network team to block specific endpoint not entire IP. "
         "6) Document decision. This illustrates the difference between threat intelligence and threat relevance."),
    ]
    for q, a in scenarios:
        story.append(Paragraph(f"⚠  {q}", S["q"]))
        story.append(Paragraph(a, S["a"]))
        story.append(Spacer(1, 0.2*cm))

    story.append(Paragraph("6.2  Common Traps & Insider Threat Indicators", S["h2"]))
    traps = [
        "Alert Fatigue: SOC analysts numb to alerts. Solution: quality over quantity — tune mercilessly, use risk scoring.",
        "Over-reliance on signatures: Zero-days bypass all signature detection. Always pair with behavioral baselines.",
        "Log gaps: If you can't see it, you can't detect it. Log coverage mapping is as important as detection rules.",
        "Time synchronization: NTP drift breaks event correlation across sources — critical for PCI DSS compliance.",
        "Privileged account sprawl: Service accounts with admin rights, shared passwords — major insider threat amplifier.",
        "Shadow IT: Finance employees using unauthorized cloud storage to share PAN data — DLP critical in fintech.",
        "False sense of compliance: Passing a PCI audit ≠ being secure. Compliance is a floor, not a ceiling.",
    ]
    for item in traps:
        story.append(Paragraph(f"⚡ {item}", S["bullet"]))
    story.append(PageBreak())

def section7_cheatsheet(story, S):
    story += section_header("SECTION 7 — QUICK-REFERENCE CHEATSHEET", S)

    story.append(Paragraph("7.1  Sysmon Event IDs Every SOC Analyst Must Know", S["h2"]))
    sysmon = [
        ["Event ID", "Event", "Detection Use Case"],
        ["1", "Process Create", "Suspicious child processes (cmd from Word, PS from Excel)"],
        ["3", "Network Connect", "Beaconing, lateral movement, C2 callbacks"],
        ["7", "Image Loaded", "DLL hijacking, unsigned DLL loading"],
        ["8", "CreateRemoteThread", "Process injection (Cobalt Strike shellcode)"],
        ["10", "ProcessAccess", "LSASS access (credential dumping via Mimikatz)"],
        ["11", "FileCreate", "Dropper writing payload to disk, webshell creation"],
        ["12/13/14", "Registry Events", "Persistence via Run keys, COM hijacking"],
        ["15", "FileCreateStreamHash", "Alternate data streams (ADS) — hiding payloads"],
        ["22", "DNS Query", "C2 via DNS, DGA domain queries"],
        ["25", "Process Tampering", "Process hollowing, herpaderping detection"],
    ]
    story.append(colored_table(sysmon, [1.5*cm, 3.5*cm, 9*cm]))
    story.append(Spacer(1, 0.4*cm))

    story.append(Paragraph("7.2  MITRE ATT&CK Tactics (In Kill Chain Order)", S["h2"]))
    mitre = [
        ["Tactic", "ID", "Key Techniques"],
        ["Reconnaissance", "TA0043", "T1595 (active scan), T1598 (phishing for info)"],
        ["Resource Dev", "TA0042", "T1583 (acquire infra), T1588 (obtain capabilities)"],
        ["Initial Access", "TA0001", "T1566 (phishing), T1190 (exploit public app), T1078 (valid accounts)"],
        ["Execution", "TA0002", "T1059 (script exec), T1204 (user execution), T1053 (scheduled task)"],
        ["Persistence", "TA0003", "T1547 (boot autostart), T1505 (server software), T1078 (valid accounts)"],
        ["Privilege Esc", "TA0004", "T1055 (process inject), T1548 (UAC bypass), T1134 (token manip)"],
        ["Defense Evasion", "TA0005", "T1562 (impair defenses), T1027 (obfuscation), T1218 (LOLBins)"],
        ["Cred Access", "TA0006", "T1003 (OS credential dump), T1558 (Kerberos), T1555 (browser creds)"],
        ["Discovery", "TA0007", "T1082 (system info), T1087 (account enum), T1135 (network shares)"],
        ["Lateral Move", "TA0008", "T1021 (remote services), T1563 (remote session hijack)"],
        ["Collection", "TA0009", "T1074 (data staged), T1056 (keylogging), T1113 (screenshot)"],
        ["C2", "TA0011", "T1071 (app layer), T1095 (non-app protocol), T1572 (protocol tunnel)"],
        ["Exfiltration", "TA0010", "T1041 (exfil over C2), T1048 (exfil alt protocol), T1567 (web service)"],
        ["Impact", "TA0040", "T1486 (encrypt data), T1490 (inhibit recovery), T1489 (service stop)"],
    ]
    story.append(colored_table(mitre, [2.5*cm, 1.8*cm, 9.7*cm]))
    story.append(Spacer(1, 0.4*cm))

    story.append(Paragraph("7.3  IOC Types & Enrichment Sources", S["h2"]))
    iocs = [
        ["IOC Type", "Examples", "Enrichment Source"],
        ["IP Address", "C2 server, scanner IP, TOR exit node", "VirusTotal, AbuseIPDB, Shodan, IPInfo"],
        ["Domain / URL", "Phishing domain, DGA domain, C2 domain", "VirusTotal, URLhaus, Threat Fox, PassiveDNS"],
        ["File Hash (MD5/SHA)", "Malware sample identifier", "VirusTotal, MalwareBazaar, Hybrid Analysis"],
        ["Email Address", "Sender in BEC/phishing", "Hunter.io, Have I Been Pwned"],
        ["Registry Key", "Persistence mechanism", "MITRE ATT&CK, vendor KBs"],
        ["Mutex Name", "Malware instance lock", "MalwareBazaar, Malpedia"],
        ["User-Agent String", "Malware HTTP communication", "VirusTotal, Shodan, custom baseline"],
        ["TLS Certificate", "C2 infrastructure fingerprint", "Censys, Shodan, crt.sh"],
        ["JA3/JA3S Hash", "TLS client/server fingerprint", "ja3er.com, Suricata JA3 detection"],
    ]
    story.append(colored_table(iocs, [3*cm, 4*cm, 7*cm]))
    story.append(Spacer(1, 0.4*cm))

    story.append(Paragraph("7.4  Top Interview Questions from Head of SOC/NOC", S["h2"]))
    hq = [
        "What metrics do you use to measure SOC effectiveness? (MTTD, MTTR, TP/FP ratio, alert coverage %)",
        "How do you handle a zero-day with no detection rule yet? (Behavioral baselines, threat hunting, IOC feeds)",
        "What's the difference between a SOC and a CSIRT? (SOC = ongoing monitoring; CSIRT = incident response)",
        "How would you build a detection roadmap for our environment? (Asset inventory → log coverage → MITRE gap analysis → priority detections)",
        "Describe a time a detection you built caught a real threat. (Use STAR format: Situation, Task, Action, Result)",
        "How do you stay current with the threat landscape? (RSS feeds, Twitter/X TI community, vendor reports, ISAC)",
        "What would you do in your first 30/60/90 days? (30: learn env + current detections; 60: identify gaps; 90: deliver improvements)",
        "How do you balance security with business operations? (Risk-based decisions, cost of detection vs cost of breach)",
    ]
    for item in hq:
        story.append(Paragraph(f"★  {item}", S["bullet"]))

    story.append(Spacer(1, 0.5*cm))
    story.append(hr(ACCENT2, 1))
    story.append(Paragraph("Prepared for: Fintech SOC Engineer Interview | 2 YOE Level", S["cover_meta"]))
    story.append(Paragraph("Focus: Demonstrate practical experience + strategic thinking = excellent candidate", S["cover_meta"]))

# ═══════════════════════════════════════════════════════════════════════════════
# MAIN BUILD
# ═══════════════════════════════════════════════════════════════════════════════

def build_pdf(path):
    """Build the full interview prep PDF."""
    doc = SimpleDocTemplate(
        path, pagesize=A4,
        leftMargin=1.8*cm, rightMargin=1.8*cm,
        topMargin=1.5*cm, bottomMargin=1.5*cm,
    )

    def on_page(canvas, doc):
        # Draw background first, then content renders on top
        canvas.saveState()
        canvas.setFillColor(DARK_BG)
        canvas.rect(0, 0, W, H, fill=1, stroke=0)
        canvas.restoreState()
        # Footer drawn after background
        canvas.saveState()
        canvas.setFillColor(TEXT_SUB)
        canvas.setFont("Helvetica", 7)
        canvas.drawString(1.8*cm, 0.8*cm, "https://github.com/meharehsaan")
        canvas.drawRightString(W - 1.8*cm, 0.8*cm, f"Page {doc.page}")
        canvas.restoreState()

    S = build_styles()
    story = []
    cover_page(story, S)
    section1_cv_qa(story, S)
    section2_fintech(story, S)
    section3_pcidss(story, S)
    section4_osi_network(story, S)
    section5_soc_siem(story, S)
    section6_dilemmas(story, S)
    section7_cheatsheet(story, S)

    doc.build(story, onFirstPage=on_page, onLaterPages=on_page)
    print(f"PDF built: {path}")

build_pdf("./SOC_Interview_Prep.pdf")