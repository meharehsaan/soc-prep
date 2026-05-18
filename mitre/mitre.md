# MITRE ATT&CK Interview Preparation Guide

## Table of Contents

1. What is MITRE ATT&CK
2. Beginner Questions
3. Intermediate Questions
4. Advanced Questions
5. Scenario-Based Questions
6. ATT&CK Mapping Questions
7. TTP Questions
8. Threat Hunting Questions
9. Detection Engineering Questions
10. SOC Analyst Questions
11. Red Team / Blue Team Questions
12. Common Tools Related to ATT&CK
13. Important ATT&CK Tactics
14. Important Techniques to Memorize
15. Interview Tips
16. Mock Rapid-Fire Questions

---

# 1. What is MITRE ATT&CK?

## Definition

MITRE ATT&CK is a globally accessible knowledge base of adversary tactics, techniques, and procedures (TTPs) based on real-world observations.

It helps:

* SOC analysts
* Threat hunters
* Red teams
* Blue teams
* Detection engineers
* Incident responders

understand attacker behavior.

---

# 2. Basic Interview Questions

## Q1. What is MITRE ATT&CK?

**Answer:**
MITRE ATT&CK is a framework that categorizes cyber adversary behavior into tactics, techniques, and procedures based on real-world attacks.

---

## Q2. What does ATT&CK stand for?

**Answer:**
Adversarial Tactics, Techniques, and Common Knowledge.

---

## Q3. What are TTPs?

**Answer:**

* **Tactics** → attacker goals
* **Techniques** → how attackers achieve goals
* **Procedures** → specific implementations used by attackers

Example:

* Tactic: Persistence
* Technique: Registry Run Keys
* Procedure: Malware adding itself to `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`

---

## Q4. Difference between Tactic and Technique?

| Tactic                     | Technique              |
| -------------------------- | ---------------------- |
| Why attacker acts          | How attacker acts      |
| Goal                       | Method                 |
| Example: Credential Access | Example: LSASS Dumping |

---

## Q5. What are ATT&CK matrices?

**Answer:**
Matrices organize tactics and techniques for different environments:

* Enterprise
* Mobile
* ICS
* Cloud

---

## Q6. What is ATT&CK used for?

**Answer:**

* Threat hunting
* Detection engineering
* Incident response
* Adversary emulation
* Security gap analysis
* Purple teaming

---

# 3. Intermediate Questions

## Q7. What is ATT&CK Mapping?

**Answer:**
ATT&CK mapping is the process of correlating observed attacker activity, alerts, or logs with ATT&CK techniques.

Example:

```text
PowerShell encoded command
→ T1059.001 PowerShell
```

---

## Q8. Explain ATT&CK Tactics

Important tactics:

| Tactic               | Purpose             |
| -------------------- | ------------------- |
| Initial Access       | Entry point         |
| Execution            | Run malicious code  |
| Persistence          | Maintain access     |
| Privilege Escalation | Gain admin rights   |
| Defense Evasion      | Avoid detection     |
| Credential Access    | Steal credentials   |
| Discovery            | Gather info         |
| Lateral Movement     | Move across systems |
| Collection           | Gather data         |
| Exfiltration         | Steal data          |
| Impact               | Disrupt systems     |

---

## Q9. What is ATT&CK Navigator?

**Answer:**
A visualization tool used to:

* Highlight techniques
* Track detections
* Measure coverage
* Build heatmaps

---

## Q10. Difference between ATT&CK and Cyber Kill Chain?

| ATT&CK                | Kill Chain         |
| --------------------- | ------------------ |
| Detailed              | High-level         |
| Behavioral            | Phase-oriented     |
| Real-world techniques | Linear attack flow |

---

## Q11. What is a Sub-technique?

**Answer:**
Detailed breakdown of a technique.

Example:

```text
T1059 → Command and Scripting Interpreter
T1059.001 → PowerShell
```

---

# 4. Advanced Interview Questions

## Q12. How do you use ATT&CK in threat hunting?

**Answer:**

1. Select a tactic/technique
2. Identify relevant logs
3. Build hypotheses
4. Query SIEM/EDR
5. Validate findings
6. Improve detections

---

## Q13. How would you map alerts to ATT&CK?

**Answer Example:**

| Alert                   | ATT&CK Technique |
| ----------------------- | ---------------- |
| Encoded PowerShell      | T1059.001        |
| Mimikatz execution      | T1003            |
| RDP movement            | T1021.001        |
| Scheduled task creation | T1053            |

---

## Q14. How does ATT&CK improve SOC maturity?

**Answer:**

* Standardized detections
* Better threat visibility
* Coverage analysis
* Improved response workflows
* Better reporting

---

## Q15. Explain ATT&CK Coverage Gap Analysis

**Answer:**
Comparing existing detections against ATT&CK techniques to identify blind spots.

---

## Q16. How do adversaries abuse PowerShell?

**Answer:**

* Encoded commands
* Download cradles
* In-memory execution
* AMSI bypass
* Obfuscation

Mapped to:

```text
T1059.001
```

---

## Q17. Explain ATT&CK Data Sources

Examples:

* Process creation logs
* Registry logs
* Network traffic
* Authentication logs
* PowerShell logs
* File activity

---

# 5. Scenario-Based Questions

## Q18. A user opened a phishing email and malware executed. Map the attack.

**Possible Mapping:**

| Activity             | ATT&CK    |
| -------------------- | --------- |
| Phishing email       | T1566     |
| Malicious attachment | T1204     |
| PowerShell execution | T1059.001 |
| Credential dumping   | T1003     |
| Data exfiltration    | T1041     |

---

## Q19. How would you detect lateral movement?

**Answer:**
Monitor:

* SMB
* PsExec
* RDP
* WMI
* Remote service creation

Relevant techniques:

```text
T1021
```

---

## Q20. How do attackers maintain persistence?

**Answer:**

* Scheduled tasks
* Registry Run Keys
* Services
* Startup folders
* WMI subscriptions

---

# 6. ATT&CK Mapping Questions

## Q21. Map these activities

| Activity             | Technique |
| -------------------- | --------- |
| Base64 PowerShell    | T1059.001 |
| LSASS dumping        | T1003.001 |
| RDP login            | T1021.001 |
| Registry persistence | T1547     |
| DNS tunneling        | T1071.004 |

---

## Q22. How do you perform ATT&CK mapping during incident response?

**Answer:**

1. Collect evidence
2. Identify attacker actions
3. Match behavior with ATT&CK techniques
4. Build attack timeline
5. Identify missing detections

---

# 7. TTP Questions

## Q23. Explain TTP lifecycle

| Component  | Description             |
| ---------- | ----------------------- |
| Tactics    | Objective               |
| Techniques | General method          |
| Procedures | Specific implementation |

---

## Q24. Give an example of TTPs

| Tactic            | Technique             | Procedure              |
| ----------------- | --------------------- | ---------------------- |
| Credential Access | OS Credential Dumping | Mimikatz dumping LSASS |

---

## Q25. Why are TTPs important?

**Answer:**
Because attacker infrastructure changes, but behavior patterns often remain consistent.

---

# 8. Threat Hunting Questions

## Q26. How would you hunt for PowerShell abuse?

**Look for:**

* Encoded commands
* Hidden windows
* DownloadString
* IEX
* Suspicious parent-child processes

---

## Q27. What logs are important for ATT&CK hunting?

| Log Type           | Usage                   |
| ------------------ | ----------------------- |
| Sysmon             | Process visibility      |
| Windows Event Logs | Authentication/activity |
| EDR telemetry      | Endpoint behavior       |
| DNS logs           | C2 detection            |
| Proxy logs         | Exfiltration            |

---

## Q28. Explain hypothesis-driven hunting

**Answer:**
Creating assumptions based on attacker techniques and validating them using telemetry.

Example:

```text
Adversaries may abuse PowerShell for execution.
```

---

# 9. Detection Engineering Questions

## Q29. How do you build detections using ATT&CK?

**Answer:**

1. Select technique
2. Identify data sources
3. Define indicators
4. Create SIEM rule
5. Test against attack simulation

---

## Q30. What is detection coverage?

**Answer:**
Measurement of how many ATT&CK techniques your security tools can detect.

---

## Q31. Explain Atomic Red Team

**Answer:**
A tool used to simulate ATT&CK techniques safely for testing detections.

---

# 10. SOC Analyst Questions

## Q32. What ATT&CK techniques are commonly seen in ransomware?

| Stage             | Technique       |
| ----------------- | --------------- |
| Initial access    | Phishing        |
| Execution         | PowerShell      |
| Credential access | LSASS dumping   |
| Lateral movement  | PsExec/RDP      |
| Impact            | Data encryption |

---

## Q33. How would you prioritize ATT&CK techniques?

**Answer:**
Based on:

* Threat intelligence
* Business risk
* Active adversaries
* Detection gaps

---

# 11. Red Team / Blue Team Questions

## Q34. How do red teams use ATT&CK?

**Answer:**
For adversary emulation and attack simulation.

---

## Q35. How do blue teams use ATT&CK?

**Answer:**
For:

* Detection mapping
* Threat hunting
* Coverage assessment
* Incident response

---

# 12. Common Tools Related to ATT&CK

| Tool             | Purpose                       |
| ---------------- | ----------------------------- |
| ATT&CK Navigator | Technique visualization       |
| Atomic Red Team  | Attack simulation             |
| Caldera          | Automated adversary emulation |
| Sigma            | Detection rules               |
| Splunk           | SIEM                          |
| Elastic          | Detection/hunting             |
| Sentinel         | Cloud SIEM                    |

---

# 13. Important ATT&CK Techniques to Memorize

| Technique            | ID        |
| -------------------- | --------- |
| PowerShell           | T1059.001 |
| Command Shell        | T1059.003 |
| Phishing             | T1566     |
| Scheduled Tasks      | T1053     |
| Credential Dumping   | T1003     |
| Remote Services      | T1021     |
| Registry Run Keys    | T1547     |
| Exfiltration Over C2 | T1041     |
| Obfuscated Files     | T1027     |
| Masquerading         | T1036     |

---

# 14. Hard Questions Interviewers Ask

## Q36. How do you validate ATT&CK mapping accuracy?

**Answer:**

* Verify evidence
* Check telemetry
* Correlate multiple logs
* Avoid overmapping
* Use ATT&CK descriptions carefully

---

## Q37. Explain limitations of ATT&CK

**Answer:**

* Not all attacks are covered
* Requires skilled analysts
* Mapping can be subjective
* Detection ≠ prevention

---

## Q38. Difference between IOC and TTP?

| IOC               | TTP                 |
| ----------------- | ------------------- |
| Static indicators | Behavioral patterns |
| IPs, hashes       | Techniques          |
| Easier to change  | Harder to change    |

---

## Q39. How would you detect fileless malware?

**Answer:**
Monitor:

* PowerShell
* WMI
* Memory injection
* LOLBins
* Script interpreters

---

# 15. Behavioral Questions

## Q40. Tell me about a threat hunting case you worked on

Structure:

```text
Situation
Task
Action
Result
```

---

## Q41. Describe a difficult alert investigation

Mention:

* Telemetry
* Correlation
* ATT&CK mapping
* Root cause
* Containment

---

# 16. Rapid-Fire Questions

| Question                  | Answer                 |
| ------------------------- | ---------------------- |
| What is T1003?            | Credential Dumping     |
| What is T1059?            | Command & Scripting    |
| What is persistence?      | Maintaining access     |
| What is lateral movement? | Moving between systems |
| ATT&CK vs IOC?            | Behavior vs indicators |
| ATT&CK used by?           | SOC/IR/Red/Blue teams  |
| What is ATT&CK Navigator? | Visualization tool     |

---

# Common Real-World ATT&CK Examples

| Attack                | ATT&CK Technique    |
| --------------------- | ------------------- |
| Mimikatz              | T1003               |
| PsExec                | T1021.002           |
| Cobalt Strike         | Multiple techniques |
| PowerShell Empire     | T1059.001           |
| Ransomware encryption | T1486               |

---

# Practical Interview Exercise They May Give

## Example:

```text
Alert:
powershell.exe -enc SQBFAFgA...
```

### Expected Response:

* Suspicious encoded PowerShell
* ATT&CK: T1059.001
* Investigate parent process
* Check network connections
* Review user context
* Search for persistence

---

# Best Way to Answer in Interviews

Use this format:

```text
1. Explain the concept
2. Mention ATT&CK technique ID
3. Give real-world example
4. Mention detection strategy
5. Mention mitigation
```

---

# Final Interview Tips

## Memorize These:

* Top 15 ATT&CK techniques
* Common ransomware chains
* PowerShell abuse
* Credential dumping
* Persistence methods
* ATT&CK tactics order

## Practice:

* ATT&CK mapping
* Sigma rules
* Splunk queries
* Threat hunting scenarios

## Be Ready For:

* Log analysis
* Incident timelines
* Detection engineering
* Mapping alerts to ATT&CK

---

# Bonus: Example Full Attack Chain

```text
Phishing Email
→ T1566

Malicious Macro
→ T1204

PowerShell Execution
→ T1059.001

Credential Dumping
→ T1003

Lateral Movement
→ T1021

Data Exfiltration
→ T1041

Ransomware Encryption
→ T1486
```

---

## Complete ATT&CK Tactics With Real Examples

| Order | Tactic               | Goal                             |
| ----- | -------------------- | -------------------------------- |
| 1     | Reconnaissance       | Gather target information        |
| 2     | Resource Development | Prepare infrastructure/resources |
| 3     | Initial Access       | Enter victim environment         |
| 4     | Execution            | Run malicious code               |
| 5     | Persistence          | Maintain access                  |
| 6     | Privilege Escalation | Gain higher privileges           |
| 7     | Stealth              | Hide malicious actions           |
| 8     | Defense Impairment   | Disable/bypass defenses          |
| 9     | Credential Access    | Steal credentials                |
| 10    | Discovery            | Learn environment details        |
| 11    | Lateral Movement     | Move between systems             |
| 12    | Collection           | Gather target data               |
| 13    | Command and Control  | Communicate with attacker        |
| 14    | Exfiltration         | Steal data                       |
| 15    | Impact               | Damage/disrupt systems           |

([MITRE ATT&CK][2])

---

# 1. Reconnaissance (TA0043)

## Goal

Attacker gathers information before attacking.

## Real Examples

* Scanning LinkedIn employees
* Finding company emails
* DNS enumeration
* Port scanning
* WHOIS lookup

## Techniques

| Technique                   | ID    |
| --------------------------- | ----- |
| Active Scanning             | T1595 |
| Gather Victim Identity Info | T1589 |
| Gather Victim Network Info  | T1590 |

## Example Attack

```text id="n7k0k6"
Attacker searches employee emails on LinkedIn
→ crafts phishing campaign
```

---

# 2. Resource Development (TA0042)

## Goal

Prepare infrastructure for attack.

## Examples

* Buying domains
* Setting up VPS servers
* Creating malware
* Registering phishing websites

## Techniques

| Technique              | ID    |
| ---------------------- | ----- |
| Acquire Infrastructure | T1583 |
| Obtain Capabilities    | T1588 |

## Example

```text id="vgn6q6"
evil-microsoft-login.com
```

used for phishing.

---

# 3. Initial Access (TA0001)

## Goal

Get inside victim environment.

## Examples

* Phishing email
* VPN exploit
* Public app exploit
* USB malware

## Techniques

| Technique                 | ID    |
| ------------------------- | ----- |
| Phishing                  | T1566 |
| External Remote Services  | T1133 |
| Exploit Public-Facing App | T1190 |

## Real Example

```text id="1j9t4l"
User opens malicious attachment
→ malware installed
```

---

# 4. Execution (TA0002)

## Goal

Run malicious code.

## How It Happens

Attacker executes:

* PowerShell
* CMD
* Scripts
* Malware
* Macros

## Techniques

| Technique      | ID        |
| -------------- | --------- |
| PowerShell     | T1059.001 |
| Command Shell  | T1059.003 |
| User Execution | T1204     |

## Example

```text id="v58d4x"
powershell -enc SQBFAFgA...
```

## Detection

* Sysmon Event ID 1
* PowerShell logs
* Encoded command detection

---

# 5. Persistence (TA0003)

## Goal

Stay in system after reboot/logout.

## Examples

* Scheduled tasks
* Registry Run Keys
* Startup folder
* Services
* SSH keys

## Techniques

| Technique         | ID    |
| ----------------- | ----- |
| Scheduled Task    | T1053 |
| Registry Run Keys | T1547 |
| Create Account    | T1136 |

## Example

```text id="x4v0nm"
Malware adds itself to startup registry
```

---

# 6. Privilege Escalation (TA0004)

## Goal

Become admin/root.

## Examples

* SUID abuse
* Kernel exploit
* Token impersonation
* UAC bypass

## Techniques

| Technique                 | ID        |
| ------------------------- | --------- |
| Exploitation for Priv Esc | T1068     |
| Access Token Manipulation | T1134     |
| Sudo and Sudo Caching     | T1548.003 |

## Linux Example

```text id="uik7m9"
find / -perm -4000
```

used to find vulnerable SUID binaries.

---

# 7. Stealth (TA0005)

## Goal

Hide malicious activity and blend with normal behavior.

MITRE says Stealth focuses on:

> concealment without disabling defenses. ([MITRE ATT&CK][3])

## Examples

* Obfuscation
* LOLBins
* Renaming malware
* Masquerading
* Process injection

## Techniques

| Technique                 | ID    |
| ------------------------- | ----- |
| Masquerading              | T1036 |
| Obfuscated Files/Info     | T1027 |
| Process Injection         | T1055 |
| Access Token Manipulation | T1134 |

## Real Example

```text id="6s5nmr"
malware.exe renamed to svchost.exe
```

## Another Example

```text id="h5z2ra"
Using PowerShell instead of custom malware
```

because PowerShell is trusted.

---

# 8. Defense Impairment (TA0112)

## Goal

Break or disable security tools.

MITRE introduced this tactic separately in v19. ([MITRE ATT&CK][1])

## Examples

* Disable antivirus
* Stop EDR agent
* Turn off firewall
* Disable logging
* Remove SIEM agents

## Techniques

| Technique               | ID    |
| ----------------------- | ----- |
| Disable or Modify Tools | T1685 |
| Disable Firewall        | T1686 |
| Downgrade Attack        | T1689 |

([MITRE ATT&CK][1])

## Real Example

```text id="4w7n8v"
sc stop WinDefend
```

## Another Example

```text id="4gx2p6"
netsh advfirewall set allprofiles state off
```

---

# 9. Credential Access (TA0006)

## Goal

Steal usernames/passwords/tokens.

## Examples

* LSASS dumping
* Keylogging
* Browser credential theft
* Kerberoasting

## Techniques

| Technique             | ID        |
| --------------------- | --------- |
| OS Credential Dumping | T1003     |
| Keylogging            | T1056.001 |
| Brute Force           | T1110     |

## Example

```text id="wb7d95"
mimikatz sekurlsa::logonpasswords
```

---

# 10. Discovery (TA0007)

## Goal

Understand victim environment.

## Examples

* Network scanning
* User enumeration
* Domain trust discovery
* Process listing

## Techniques

| Technique                | ID    |
| ------------------------ | ----- |
| System Info Discovery    | T1082 |
| Account Discovery        | T1087 |
| Network Service Scanning | T1046 |

## Example

```text id="kq0t2j"
whoami
ipconfig
net user
```

---

# 11. Lateral Movement (TA0008)

## Goal

Move to other systems.

## Examples

* RDP
* SMB
* PsExec
* WMI

## Techniques

| Technique                | ID        |
| ------------------------ | --------- |
| Remote Services          | T1021     |
| SMB/Windows Admin Shares | T1021.002 |

## Example

```text id="l2a1c8"
psexec \\server cmd.exe
```

---

# 12. Collection (TA0009)

## Goal

Gather valuable data.

## Examples

* Screenshot capture
* File collection
* Clipboard capture
* Email collection

## Techniques

| Technique              | ID    |
| ---------------------- | ----- |
| Screen Capture         | T1113 |
| Archive Collected Data | T1560 |

## Example

```text id="66m0vf"
zip confidential files before exfiltration
```

---

# 13. Command and Control (TA0011)

## Goal

Communicate with attacker server.

## Examples

* Reverse shell
* Beaconing
* DNS tunneling
* HTTPS C2

## Techniques

| Technique                  | ID    |
| -------------------------- | ----- |
| Application Layer Protocol | T1071 |
| Ingress Tool Transfer      | T1105 |

## Example

```text id="1woa48"
Beacon every 60 seconds to C2 server
```

---

# 14. Exfiltration (TA0010)

## Goal

Steal data out of environment.

## Examples

* Cloud upload
* FTP
* HTTPS
* DNS tunneling

## Techniques

| Technique                     | ID        |
| ----------------------------- | --------- |
| Exfiltration Over C2          | T1041     |
| Exfiltration to Cloud Storage | T1567.002 |

## Example

```text id="10dz34"
Upload stolen files to Dropbox
```

---

# 15. Impact (TA0040)

## Goal

Damage systems/data/business.

## Examples

* Ransomware
* Data wiping
* Service shutdown
* Encryption

## Techniques

| Technique                 | ID    |
| ------------------------- | ----- |
| Data Encrypted for Impact | T1486 |
| Disk Wipe                 | T1561 |

## Example

```text id="quyv7n"
Ransomware encrypts all files
```

---

# Full Real-World Attack Flow

```text id="p4mjlwm"
Recon
→ find employees

Resource Development
→ setup phishing domain

Initial Access
→ phishing email

Execution
→ PowerShell malware

Persistence
→ scheduled task

Privilege Escalation
→ token impersonation

Stealth
→ obfuscation

Defense Impairment
→ disable Defender

Credential Access
→ dump LSASS

Discovery
→ scan network

Lateral Movement
→ PsExec

Collection
→ gather files

C2
→ HTTPS beacon

Exfiltration
→ upload data

Impact
→ ransomware encryption
```

---

# Most Important Techniques To Memorize For Interviews

| Technique              | ID        |
| ---------------------- | --------- |
| PowerShell             | T1059.001 |
| Credential Dumping     | T1003     |
| Phishing               | T1566     |
| PsExec                 | T1021.002 |
| Process Injection      | T1055     |
| Masquerading           | T1036     |
| Registry Run Keys      | T1547     |
| Exfiltration Over C2   | T1041     |
| Data Encryption        | T1486     |
| Disable Security Tools | T1685     |

---

# Important Interview Question

## Q: Difference between Stealth and Defense Impairment?

| Stealth                    | Defense Impairment          |
| -------------------------- | --------------------------- |
| Hide activity              | Disable defenses            |
| Blend with normal behavior | Break security controls     |
| Uses obfuscation           | Stops AV/EDR                |
| Example: masquerading      | Example: disabling Defender |

([MITRE ATT&CK][1])

[1]: https://attack.mitre.org/tactics/TA0112/?utm_source=chatgpt.com "Defense Impairment, Tactic TA0112 - Enterprise | MITRE ATT&CK®"
[2]: https://attack.mitre.org/tactics/enterprise/?utm_source=chatgpt.com "Tactics - Enterprise | MITRE ATT&CK®"
[3]: https://attack.mitre.org/tactics/TA0005/?utm_source=chatgpt.com "Stealth, Tactic TA0005 - Enterprise | MITRE ATT&CK®"

