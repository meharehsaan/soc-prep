# 🟢 1. Basic Level (Foundation)

These questions test if you understand MITRE ATT&CK fundamentals.

## 🔹 Core Concepts
- What is the MITRE ATT&CK framework?
- What does ATT&CK stand for?
- What is the purpose of MITRE ATT&CK in SOC operations?
- What are Tactics, Techniques, and Procedures (TTPs)?
- Difference between tactics, techniques, and sub-techniques?
- What is the ATT&CK matrix?

## 🔹 SOC Basics
- How do you map a security alert to a MITRE technique?
- What is the difference between detection and mitigation?
- Example of MITRE technique used in phishing attacks?
- What is Initial Access in MITRE ATT&CK?

## 🧠 Expected Answer Level
- Basic definitions
- Awareness of cyber attack lifecycle
- Simple SOC mapping understanding

---

# 🟡 2. Intermediate Level (SOC Analyst Core)

These test real SOC operations and analysis skills.

## 🔹 Detection Mapping
- How do you map Windows Event Logs to MITRE ATT&CK?
- PowerShell execution alert → which MITRE technique?
- Which technique is associated with credential dumping?

👉 Key Knowledge:
- T1059 → Command and Scripting Interpreter  
- T1003 → Credential Dumping  

## 🔹 Scenario-Based Questions
- Multiple failed logins → successful login → lateral movement  
  → Map tactics and techniques
- Which MITRE techniques are common in ransomware attacks?
- How do you detect persistence using MITRE ATT&CK?

## 🔹 SOC Tooling
- How does SIEM use MITRE ATT&CK?
- What is threat hunting using MITRE?
- What is ATT&CK Navigator?

## 🧠 Expected Answer Level
- Log → technique mapping
- Attack chain understanding
- Basic threat hunting logic

---

# 🔴 3. Advanced Level (Threat Hunter / Senior SOC)

This level tests real-world SOC thinking.

## 🔹 Detection Engineering
- How do you detect Living-off-the-Land (LOLBins) attacks?
- How to detect PowerShell obfuscation?
- How to detect lateral movement in enterprise networks?

## 🔹 Attack Chain Mapping
- Map full attack chain:
  - Phishing → Execution → Persistence → Exfiltration
- How does MITRE ATT&CK align with Cyber Kill Chain?

## 🔹 Threat Hunting
- How do you start a threat hunt using MITRE ATT&CK?
- What data sources detect credential dumping or remote execution?

## 🔹 Detection Gaps
- What are detection coverage gaps?
- How do you prioritize MITRE techniques in an organization?

## 🧠 Expected Answer Level
- Detection logic creation
- Threat behavior understanding
- SOC maturity awareness

---

# 🔥 4. Hard / Expert Level (Interview Killer Questions)

These are asked in Tier-2 / SOC Lead / Threat Hunter interviews.

## 🔥 Scenario-Based
- Rundll32.exe unusual execution + beaconing every 60 seconds  
  → Identify MITRE techniques + attacker goal

- Design detection for fileless PowerShell malware

## 🔥 Advanced Detection
- How do you detect:
  - Obfuscated scripts
  - Living-off-the-land binaries (LOLBins)

## 🔥 Threat Group Mapping
- Map ransomware lifecycle using MITRE ATT&CK
- Common MITRE techniques used by:
  - APT29
  - FIN7

## 🔥 SOC Architecture
- How to build MITRE ATT&CK coverage in SIEM?
- How to measure detection maturity using ATT&CK?
- What is ATT&CK-based threat modeling?

## 🔥 Real SOC Challenges
- Detect lateral movement using only firewall + Windows logs
- Attacker uses VPN + valid credentials + scheduled tasks  
  → How do you detect using MITRE?

## 🧠 Expected Answer Level
- Real detection engineering
- Adversary thinking
- SOC architecture design

---

# 💀 5. Trick Questions

Interviewers use these to test deep understanding:

- Is MITRE ATT&CK defensive or offensive?
- Can MITRE automatically detect attacks?
- Can every alert be mapped to MITRE?
- Difference between MITRE ATT&CK vs Cyber Kill Chain?
- Can one technique belong to multiple tactics?

---
## **6. Mock Interview Questions (Basic to Hard)**
### **A. Basic**
1. What is the difference between a firewall and an IDS?
2. Explain the OSI model and its relevance to security.
3. How do you investigate a failed login attempt in Windows Event Logs?
4. What is the purpose of a SIEM, and how does it work?
5. What are the steps in the incident response lifecycle?

### **B. Intermediate**
2. What is lateral movement, and how can you detect it?
3. Explain how MITRE ATT&CK can be used in threat hunting.
4. What are LOLBins, and why are they dangerous?
5. How do you analyze a suspicious email for phishing indicators?

### **C. Hard**
1. A user’s account is sending outbound connections to a known C2 server. Walk me through your investigation.
2. How would you write a YARA rule to detect a specific malware family?
3. Explain how you’d investigate a potential DNS tunneling attack.
4. What steps would you take to contain a ransomware attack in progress?
5. How do you differentiate between a false positive and a true positive in a SIEM alert?

---

# 🔴 1. SIEM (Splunk / Sentinel) – Advanced

## ❓ Q1: How do you tune SIEM alerts to reduce false positives?

**Answer:**
- Add context (user, asset criticality, geo-location)
- Use whitelist/exception rules
- Correlate multiple events instead of single logs
- Apply baseline behavior (UEBA)
- Use MITRE ATT&CK mapping to refine detection logic

---

## ❓ Q2: Difference between correlation rule and detection rule?

**Answer:**
- Correlation rule → links multiple events to detect attack pattern  
- Detection rule → identifies single suspicious activity  
- Correlation = higher confidence, multi-step attack detection

---

## ❓ Q3: How do you detect lateral movement in SIEM?

**Answer:**
- Monitor:
  - Failed login spikes
  - Successful login from new host
  - Remote service execution (SMB, WMI, RDP)
- Correlate logs across endpoints + AD
- MITRE: T1021 (Remote Services)

---

## ❓ Q4: What is data normalization in SIEM?

**Answer:**
- Converting logs into standard format (fields like user, IP, action)
- Helps correlation, detection rules, and reporting consistency

---

# 🔵 2. EDR (Endpoint Detection & Response)

## ❓ Q5: How does EDR detect fileless malware?

**Answer:**
- Monitors memory execution instead of file writes
- Detects PowerShell abuse, WMI, registry-based execution
- Behavior-based detection instead of signature-based

---

## ❓ Q6: What would you check first in an EDR alert?

**Answer:**
- Process tree (parent-child relationship)
- Command line arguments
- Network connections
- File modifications
- User context and privileges

---

## ❓ Q7: How do attackers bypass EDR?

**Answer:**
- Living-off-the-land binaries (LOLBins)
- Process injection
- Obfuscation (PowerShell encoded commands)
- Signed malicious binaries

---

# 🟣 3. XDR (Extended Detection & Response)

## ❓ Q8: Difference between EDR and XDR?

**Answer:**
- EDR → endpoint-level detection  
- XDR → correlates endpoint + network + email + cloud logs  
- XDR = unified threat visibility across systems

---

## ❓ Q9: Why is XDR better for SOC Level 2?

**Answer:**
- Cross-layer correlation (email → endpoint → network)
- Faster detection of multi-stage attacks
- Reduces alert fatigue

---

# 🟠 4. Threat Intelligence (TI)

## ❓ Q10: How do you use threat intelligence in SOC?

**Answer:**
- Enrich alerts with IOC (IP, hash, domain)
- Map threats to known APT groups
- Prioritize alerts based on threat severity
- Create detection rules from TI feeds

---

## ❓ Q11: Difference between IOC and IOA?

**Answer:**
- IOC → Indicator of Compromise (IP, hash, domain)
- IOA → Indicator of Attack (behavior like lateral movement)
- IOA is more advanced and proactive

---

## ❓ Q12: What is STIX and TAXII?

**Answer:**
- STIX → format for threat intel data
- TAXII → transport protocol for sharing TI feeds

---

## ❓ Q13: How do you validate threat intelligence?

**Answer:**
- Cross-check multiple TI sources
- Check freshness (time relevance)
- Correlate with internal logs
- Remove false positives from noisy feeds

---

# 🔥 5. Detection Engineering (VERY IMPORTANT)

## ❓ Q14: How do you build a detection rule from scratch?

**Answer:**
1. Identify attack technique (MITRE ATT&CK)
2. Collect relevant log sources
3. Define detection logic (behavior-based)
4. Write SIEM query
5. Test with real/simulated data
6. Tune false positives

---

## ❓ Q15: What is behavior-based detection?

**Answer:**
- Detects attacker actions instead of signatures
- Example:
  - Instead of detecting malware file → detect abnormal PowerShell usage

---

## ❓ Q16: How do you detect credential dumping?

**Answer:**
- Monitor LSASS access
- Tools like Mimikatz behavior
- Suspicious process injection
- MITRE: T1003

---

## ❓ Q17: How do you reduce alert fatigue in SOC?

**Answer:**
- Deduplication of alerts
- Risk-based prioritization
- Use correlation rules
- Tune noisy rules
- Apply threat intelligence enrichment

---

# ⚫ 6. Incident Response + SOC Scenarios

## ❓ Q18: You detect unusual login from foreign IP. What do you do?

**Answer:**
- Verify user activity
- Check MFA logs
- Analyze login history
- Check geo-impossible travel
- Block session if suspicious
- Escalate incident if confirmed

---

## ❓ Q19: How do you handle ransomware detection?

**Answer:**
- Isolate infected endpoint
- Check encryption process behavior
- Identify entry point (phishing / RDP)
- Collect logs for IOC
- Block C2 communication

---

## ❓ Q20: What is your SOC triage process?

**Answer:**
1. Validate alert
2. Check severity + context
3. Correlate logs (SIEM + EDR)
4. Identify scope
5. Escalate or close case

---

# 🧠 7. Advanced Thinking Questions

## ❓ Q21: How would you detect zero-day attacks?

**Answer:**
- Behavior-based detection (not signature-based)
- Anomaly detection in SIEM/UEBA
- Endpoint behavior monitoring (EDR)
- Threat intelligence correlation

---

## ❓ Q22: What is MITRE ATT&CK used for in SOC engineering?

**Answer:**
- Detection mapping
- Coverage analysis
- Threat modeling
- Incident investigation

---

## ❓ Q23: How do SIEM, EDR, and XDR work together?

**Answer:**
- SIEM → log correlation + analysis
- EDR → endpoint visibility
- XDR → combines all + automated correlation

---

## ❓ Q24: What makes a good SOC Level 2 analyst?

**Answer:**
- Strong investigation skills
- Detection engineering mindset
- Threat intelligence understanding
- Ability to correlate multi-source logs

---

# 🚀 Final Tip for Interview

If interviewer asks open question:

👉 Always answer in this structure:

**1. What is it**  
**2. How it works**  
**3. SOC example**  
**4. MITRE mapping (if possible)**   

---
## **8. Final Checklist Before the Interview**
- [ ] Review **networking fundamentals** (OSI, TCP/IP, ports, protocols).
- [ ] Practice **log analysis** (Windows Event Logs, Linux logs, firewall logs).
- [ ] Brush up on **SIEM queries** (Splunk, ELK, Sentinel).
- [ ] Understand **incident response workflows** (NIST, MITRE ATT&CK).
- [ ] Know **common attack techniques** (phishing, ransomware, lateral movement).
- [ ] Practice **malware analysis basics** (static/dynamic, YARA, sandboxing).
- [ ] Be familiar with **threat intelligence platforms** (MISP, AlienVault OTX).
- [ ] Review **compliance frameworks** (NIST, ISO 27001, PCI DSS).
- [ ] Prepare for **scenario-based questions** (e.g., "How would you handle X?").
- [ ] Mock **whiteboard exercises** (PCAP analysis, log triage).
- [ ] Research the **company’s tech stack** (e.g., do they use Splunk, QRadar, or Sentinel?).

---

