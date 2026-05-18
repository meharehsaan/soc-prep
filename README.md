## **1. Core SOC Fundamentals (Basic to Intermediate)**
### **A. Networking Fundamentals**
- **OSI Model**: Understand all 7 layers, protocols (TCP/IP, UDP, ICMP, DNS, HTTP/HTTPS, SMTP, FTP, SSH, etc.), and their security implications.
- **Subnetting & CIDR**: Calculate subnets, understand VLSM, and CIDR notation.
- **Firewalls & IDS/IPS**: How they work, rule-based vs. signature-based, and their placement in the network.
- **VPNs & Proxies**: How they secure traffic, common vulnerabilities (e.g., misconfigurations, weak encryption).
- **Ports & Services**: Common ports (22, 80, 443, 3389, etc.) and associated services.
- **Network Topologies**: Star, mesh, hybrid, and their security pros/cons.

### **B. Operating Systems**
- **Windows**:
  - Event Logs (Security, System, Application)
  - Windows Defender, Firewall, and Group Policy
  - Command Line (PowerShell, CMD): `netstat`, `ipconfig`, `nslookup`, `tasklist`, `Get-Process`, `Get-Service`
  - Active Directory (AD): Users, Groups, GPOs, Kerberos, LDAP, and common attacks (e.g., Pass-the-Hash, Golden Ticket).
- **Linux**:
  - File system permissions (`chmod`, `chown`)
  - Log files (`/var/log/auth.log`, `/var/log/syslog`, `/var/log/secure`)
  - Command Line: `grep`, `awk`, `sed`, `netstat`, `ss`, `ps`, `top`, `lsof`, `journalctl`, `tail -f`
  - User management (`useradd`, `usermod`, `passwd`)
  - SSH, Cron jobs, and service management (`systemctl`)

### **C. Security Concepts**
- **CIA Triad**: Confidentiality, Integrity, Availability.
- **AAA Model**: Authentication, Authorization, Accounting.
- **Threat vs. Vulnerability vs. Risk**
- **Zero Trust Architecture**
- **Defense in Depth**

---

## **2. SOC-Specific Knowledge (Intermediate)**
### **A. SIEM Tools (Splunk, QRadar, ELK, Microsoft Sentinel, etc.)**
- **Log Sources**: Firewalls, IDS/IPS, EDR, Proxy, DNS, DHCP, VPN, Active Directory.
- **Log Parsing**: Extracting meaningful data from raw logs (e.g., IP addresses, timestamps, user agents).
- **Correlation Rules**: Writing rules to detect anomalies (e.g., brute force attacks, lateral movement).
- **Dashboards & Reports**: Creating visualizations for security metrics (e.g., failed logins, top threat sources).
- **Splunk SPL (Search Processing Language)**:
  - Basic searches: `index=* sourcetype=* | head 10`
  - Filtering: `index=windows EventCode=4625` (failed logins)
  - Stats: `index=firewall | stats count by src_ip, dest_ip`
  - Time-based analysis: `earliest=-24h latest=now`
  - Lookups and joins.

### **B. Incident Response (IR)**
- **NIST IR Lifecycle**: Preparation, Detection & Analysis, Containment, Eradication, Recovery, Lessons Learned.
- **IR Frameworks**: MITRE ATT&CK, Kill Chain, Diamond Model.
- **Common Incidents**:
  - Malware (Ransomware, Trojans, Worms)
  - Phishing & Social Engineering
  - DDoS Attacks
  - Insider Threats
  - Credential Stuffing & Brute Force
  - Lateral Movement & Privilege Escalation
- **IR Tools**:
  - **Forensics**: Volatility, Autopsy, FTK, EnCase.
  - **Memory Analysis**: Volatility, Redline.
  - **Disk Analysis**: `dd`, `testdisk`, `foremost`.
  - **Network Forensics**: Wireshark, TShark, Zeek (Bro), NetworkMiner.
- **Evidence Handling**: Chain of custody, hashing (MD5, SHA-1, SHA-256), legal considerations.

### **C. Threat Intelligence**
- **Types of Threat Intel**: Strategic, Operational, Tactical, Technical.
- **Sources**: Open Source (OSINT), Dark Web, Commercial Feeds (e.g., AlienVault OTX, MISP).
- **IOCs (Indicators of Compromise)**: IP addresses, domains, hashes (MD5, SHA-1), file paths, registry keys.
- **Threat Actor Types**: Nation-state, Hacktivists, Cybercriminals, Insiders.
- **MITRE ATT&CK Framework**:
  - Tactics (e.g., Initial Access, Persistence, Lateral Movement)
  - Techniques (e.g., T1059 - Command and Scripting Interpreter)
  - Mitigations and Detection Methods.

### **D. Endpoint Detection & Response (EDR)**
- **EDR Tools**: CrowdStrike, SentinelOne, Carbon Black, Microsoft Defender for Endpoint.
- **Key Features**:
  - Behavioral Analysis
  - File Integrity Monitoring (FIM)
  - Process Injection Detection
  - Registry Monitoring
- **Common EDR Queries**:
  - Detecting unusual process executions (e.g., `powershell.exe` spawning `cmd.exe`).
  - Identifying persistence mechanisms (e.g., scheduled tasks, startup folders).

## **3. Advanced SOC Topics (Hard)**
### **A. Advanced Threat Hunting**
- **Hypothesis-Driven Hunting**: Formulating hypotheses based on threat intel or anomalies.
- **Anomaly Detection**:
  - Unusual login times/locations.
  - Impossible travel (same user logging in from US and Pakistan within 1 hour).
  - Beaconing (C2 traffic at regular intervals).
- **Tools**:
  - **Splunk**: Advanced SPL (e.g., `eval`, `where`, `join`, `append`).
  - **Elasticsearch**: Kibana queries, Lucene syntax.
  - **Sigma Rules**: Writing YAML-based detection rules for SIEMs.
  - **YARA Rules**: Writing rules to detect malware families.
- **Hunting for**:
  - APTs (Advanced Persistent Threats)
  - Living-off-the-Land Binaries (LOLBins) (e.g., `certutil`, `mshta`, `rundll32`)
  - Fileless Malware
  - DNS Tunneling

### **B. Malware Analysis (Static & Dynamic)**
- **Static Analysis**:
  - File hashing (MD5, SHA-1, SHA-256).
  - Strings extraction (`strings` command).
  - PE headers (for Windows executables).
  - Packing/Obfuscation detection.
- **Dynamic Analysis**:
  - Sandboxing (Cuckoo Sandbox, Any.run, Hybrid Analysis).
  - Monitoring behavior (processes, network connections, registry changes).
- **Malware Types**:
  - Ransomware (e.g., LockBit, Conti)
  - Spyware (e.g., Emotet)
  - Rootkits
  - Cryptominers
- **Tools**:
  - **Static**: PEiD, Detect It Easy (DIE), binwalk.
  - **Dynamic**: Process Monitor, Process Explorer, Wireshark, RegShot.

### **C. Threat Emulation & Red Teaming Basics**
- **Red Team vs. Blue Team**: Understand the adversary’s perspective.
- **Common Attack Techniques**:
  - Phishing (Spear Phishing, Whaling)
  - Credential Harvesting (Mimikatz, Responder)
  - Pass-the-Hash/Token
  - Kerberoasting
  - DLL Hijacking
  - Process Hollowing
- **Tools**:
  - **Reconnaissance**: Nmap, Masscan, Shodan, Maltego.
  - **Exploitation**: Metasploit, Cobalt Strike, Empire.
  - **Post-Exploitation**: PowerSploit, BloodHound, Rubeus.
  - **C2 Frameworks**: Mythic, Sliver, Positron.

### **D. Cloud Security (AWS, Azure, GCP)**
- **Shared Responsibility Model**.
- **Cloud-Specific Threats**:
  - Misconfigured S3 Buckets
  - IAM Policy Exploits
  - Container Escapes (Docker, Kubernetes)
  - Serverless Attacks (Lambda, Azure Functions)
- **Monitoring & Logging**:
  - AWS: CloudTrail, GuardDuty, Security Hub.
  - Azure: Azure Sentinel, Microsoft Defender for Cloud.
  - GCP: Chronicle, Security Command Center.
- **Incident Response in Cloud**:
  - Isolating compromised instances.
  - Analyzing API logs for suspicious activity.

### **E. Compliance & Frameworks**
- **Standards**:
  - **NIST CSF**: Identify, Protect, Detect, Respond, Recover.
  - **ISO 27001**: Information Security Management System (ISMS).
  - **PCI DSS**: Payment Card Industry Data Security Standard.
  - **GDPR**: General Data Protection Regulation (for EU data).
  - **HIPAA**: Healthcare data protection (US).
- **Audit & Compliance Tools**:
  - Nessus, OpenVAS (Vulnerability Scanning)
  - Qualys, Rapid7 InsightVM.

### **F. Scripting & Automation**
- **Python for SOC**:
  - Log parsing (e.g., `pandas`, `re` module).
  - Automating repetitive tasks (e.g., pulling IOCs from threat feeds).
  - Writing custom scripts for threat hunting.
- **Bash/PowerShell Scripting**:
  - Automating log analysis.
  - Creating custom alerts.
- **APIs**:
  - Interacting with SIEMs (e.g., Splunk REST API).
  - Pulling threat intel from APIs (e.g., VirusTotal, AbuseIPDB).

## **4. Soft Skills & Interview Tips**
### **A. Communication**
- **Incident Reporting**: Clear, concise, and actionable reports for stakeholders.
- **Escalation Procedures**: Knowing when and how to escalate incidents.
- **Collaboration**: Working with other teams (IT, DevOps, Legal, PR).

### **B. Analytical Thinking**
- **Root Cause Analysis (RCA)**: Identifying the underlying cause of an incident.
- **Critical Thinking**: Evaluating alerts for false positives/negatives.
- **Prioritization**: Triage based on severity (e.g., CVSS scoring).

### **C. Interview-Specific Tips**
- **Behavioral Questions**:
  - "Describe a time you detected a sophisticated threat."
  - "How do you handle a high-pressure incident?"
  - "Explain a mistake you made and how you fixed it."
- **Technical Questions**:
  - "How would you investigate a suspected ransomware attack?"
  - "Explain how you’d detect a DNS tunneling attack."
  - "Write a Splunk query to find brute force attempts."
- **Scenario-Based Questions**:
  - "A user reports their account is locked out. Walk me through your investigation."
  - "You see a spike in outbound traffic to an unknown IP. What do you do?"
- **Whiteboard/ Hands-on Exercises**:
  - Analyzing a PCAP file in Wireshark.
  - Writing a Sigma rule for a specific attack.
  - Triage a set of logs to identify malicious activity.

## **5. Hands-On Labs & Certifications**
### **A. Recommended Labs**
- **TryHackMe**: SOC Level 1 & 2, Blue Team paths.
- **Hack The Box**: Starting Point machines (e.g., "Blue", "Lame").
- **CyberDefenders**: Blue Team challenges.
- **LetsDefend**: SOC simulation platform.
- **Splunk Attack Range**: Practice Splunk queries on real-world attack data.

### **B. Certifications (Prioritized for SOC Analysts)**
| **Certification**       | **Level**       | **Focus Area**                          |
|-------------------------|-----------------|-----------------------------------------|
| CompTIA Security+       | Beginner        | General security concepts              |
| Certified SOC Analyst (CSA) | Beginner-Intermediate | SOC fundamentals, SIEM, IR          |
| GIAC Security Essentials (GSEC) | Intermediate | Hands-on security skills          |
| Splunk Core Certified User | Intermediate | Splunk for security monitoring     |
| Certified Incident Handler (GCIH) | Intermediate-Advanced | Incident response, forensics       |
| Offensive Security Certified Professional (OSCP) | Advanced | Penetration testing (for red team perspective) |
| Certified Ethical Hacker (CEH) | Intermediate | Ethical hacking (theoretical)      |

---


## **7. Resources to Study**
### **Books**
- **"The Blue Team Handbook"** by Don Murdock
- **"Applied Network Security Monitoring"** by Chris Sanders & Jason Smith
- **"The Practice of Network Security Monitoring"** by Richard Bejtlich
- **"Malware Forensic Field Guide for Windows Systems"** by Harlan Carvey

### **Websites & Blogs**
- [Krebs on Security](https://krebsonsecurity.com/)
- [The Hacker News](https://thehackernews.com/)
- [SANS Internet Storm Center](https://isc.sans.edu/)
- [MITRE ATT&CK](https://attack.mitre.org/)
- [CISA Alerts](https://www.cisa.gov/uscert/ncas/alerts)

### **YouTube Channels**
- [The Cyber Mentor](https://www.youtube.com/c/TheCyberMentor)
- [John Hammond](https://www.youtube.com/c/JohnHammond010)
- [NetworkChuck](https://www.youtube.com/c/NetworkChuck)
- [David Bombal](https://www.youtube.com/c/DavidBombal)

### **Podcasts**
- **Darknet Diaries**
- **Security Now**
- **Risky Business**
- **SANS Institute Podcasts**