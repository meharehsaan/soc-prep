# 🛡️ SOC Interview Questions (Basic → Intermediate)

# 🟢 1. Python (SOC Automation)

## ❓ Basic
- What is Python used for in SOC?
- What are common libraries used in security automation?
- How does Python help in log analysis?

## ❓ Intermediate
- How would you write a Python script to parse SIEM logs?
- How do you use Python to interact with APIs like VirusTotal?
- How can Python help in IOC extraction from logs?

---

# 🟢 2. C / C++ (Malware Understanding)

## ❓ Basic
- Why is C/C++ important in cybersecurity?
- What is compiled code vs interpreted code?

## ❓ Intermediate
- How does buffer overflow happen in C programs?
- Why do attackers prefer C/C++ for malware development?
- How can understanding C help in malware analysis?

---

# 🟢 3. x86-64 Assembly

## ❓ Basic
- What is assembly language?
- Why is assembly important in malware analysis?

## ❓ Intermediate
- What are registers like RAX, RBX, RIP used for?
- How do function calls work in x86-64?
- How can you identify malicious behavior in disassembled code?

---

# 🔐 4. SIEM (Splunk / ELK / Sentinel)

## ❓ Basic
- What is a SIEM system?
- Why is log monitoring important in SOC?

## ❓ Intermediate
- How do you correlate logs in SIEM?
- What is the difference between alert and event?
- How do you reduce false positives in SIEM?

---

# 🧠 5. MITRE ATT&CK

## ❓ Basic
- What is MITRE ATT&CK?
- What are tactics and techniques?

## ❓ Intermediate
- How do you map an incident to MITRE techniques?
- What is the difference between IOC and IOA?
- How does MITRE help in detection engineering?

---

# 🧪 6. Threat Intelligence (VirusTotal, IOC, APTs)

## ❓ Basic
- What is threat intelligence?
- What is an IOC?

## ❓ Intermediate
- How do you validate an IOC using VirusTotal?
- What is the difference between IOC and IOA?
- How is threat intelligence used in SOC alerts?

---

# 🛠️ 7. Wireshark (Network Analysis)

## ❓ Basic
- What is Wireshark used for?
- What is a packet?

## ❓ Intermediate
- How do you detect suspicious traffic in Wireshark?
- What is DNS tunneling?
- How do you identify C2 communication?

---

# 🚨 8. Snort (IDS)

## ❓ Basic
- What is Snort?
- IDS vs IPS difference?

## ❓ Intermediate
- How do Snort rules work?
- How do you detect port scanning using Snort?
- What is signature-based detection?

---

# 🧪 9. YARA (Malware Detection)

## ❓ Basic
- What is YARA used for?
- Why is YARA important in malware analysis?

## ❓ Intermediate
- How do YARA rules detect malware?
- What are strings and conditions in YARA?
- How do you write a basic YARA rule?

---

# 📊 10. Sigma Rules (Detection Engineering)

## ❓ Basic
- What is Sigma?
- Why is Sigma used in SOC?

## ❓ Intermediate
- How does Sigma convert rules into SIEM queries?
- What is the advantage of Sigma over platform-specific rules?

---

# 🌐 11. ELK Stack (Elastic Security)

## ❓ Basic
- What is ELK stack?
- What is Kibana used for?

## ❓ Intermediate
- How does Elasticsearch store logs?
- How do you create dashboards in Kibana?
- How do you search logs in ELK?

---

# 🧩 12. Caldera (Adversary Simulation)

## ❓ Basic
- What is MITRE Caldera used for?
- Why do we simulate attacks?

## ❓ Intermediate
- How does Caldera help in detection testing?
- How is Caldera mapped to MITRE ATT&CK techniques?

---

# 💻 13. Linux / Windows Security

## ❓ Basic
- What is the role of Linux in SOC?
- What are Windows Event Logs?

## ❓ Intermediate
- How do you detect brute force attacks in Linux logs?
- What logs are important in Windows for SOC analysis?
- How do attackers use PowerShell in Windows?

---

# 🔥 BONUS (Mixed Scenario Questions)

- An attacker is using PowerShell and contacting unknowns IPs → what tools do you use?
- How would you investigate a suspicious file hash?
- A system shows high CPU usage and unknown process → what is your approach?
- How do you correlate Wireshark + SIEM logs in an incident?