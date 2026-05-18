# SOC / SIEM / EDR / XDR / Threat Hunting

Use this exact structure in interviews for almost every technical security topic:

```text id="4g2zsp"
1. Define concept
2. Explain architecture
3. Give real world example
4. Mention ATT&CK mapping
5. Explain detection
6. Explain mitigation/response
```

---

### 1. EDR (Endpoint Detection and Response)

### 1. Define Concept

EDR is a security solution that continuously monitors endpoint activity, collects telemetry, detects malicious behavior, and enables incident response actions such as isolation and remediation.

---

### 2. Architecture

```text id="4l5h3n"
Endpoint Agent
→ Telemetry Collection
→ Cloud/Server Analysis
→ Detection Engine
→ SOC Dashboard
→ Response Actions
```

### Components

| Component           | Purpose               |
| ------------------- | --------------------- |
| Agent               | Collect endpoint data |
| Detection Engine    | Analyze behavior      |
| Threat Intelligence | IOC/TTP correlation   |
| Console             | Investigation         |
| Response Module     | Isolation/remediation |

---

### 3. Real-World Example

```text id="j6lylx"
powershell.exe -enc ...
```

EDR detects:

* encoded PowerShell
* suspicious parent process
* network beaconing

and generates alert.

---

### 4. ATT&CK Mapping

| Activity          | ATT&CK    |
| ----------------- | --------- |
| PowerShell abuse  | T1059.001 |
| Obfuscation       | T1027     |
| Process Injection | T1055     |

---

### 5. Detection

### Telemetry Used

* Process creation
* Command-line arguments
* Network connections
* Registry changes

### Example Detection

```kql id="5jz59r"
DeviceProcessEvents
| where ProcessCommandLine contains "-enc"
```

---

### 6. Mitigation/Response

* Isolate host
* Kill malicious process
* Remove persistence
* Reset credentials
* Hunt across environment

---

### 2. XDR (Extended Detection and Response)

### 1. Define Concept

XDR integrates security telemetry from:

* endpoints
* email
* identity
* cloud
* network

to detect multi-stage attacks.

---

### 2. Architecture

```text id="yw7r61"
Email
Endpoint
Cloud
Identity
Network
↓
Unified Analytics Engine
↓
Correlated Detection
↓
SOC Dashboard
```

---

### 3. Real-World Example

```text id="9djkhe"
Phishing email
→ user clicks link
→ malware executes
→ unusual Azure login
```

XDR correlates full chain.

---

### 4. ATT&CK Mapping

| Activity       | ATT&CK |
| -------------- | ------ |
| Phishing       | T1566  |
| PowerShell     | T1059  |
| Valid Accounts | T1078  |

---

### 5. Detection

XDR correlates:

* email indicators
* endpoint behavior
* identity anomalies
* cloud telemetry

---

### 6. Mitigation/Response

* Disable account
* Block sender domain
* Isolate device
* Revoke sessions
* Hunt impacted users

---

### 3. SIEM

### 1. Define Concept

SIEM collects, stores, correlates, and analyzes security logs from multiple sources to detect threats and support investigations.

---

### 2. Architecture

```text id="d01pzd"
Log Sources
→ Collector
→ Normalization
→ Correlation Engine
→ Alerting
→ Dashboard
```

---

### 3. Real-World Example

```text id="b3egjz"
Firewall denied traffic
+
failed logins
+
PowerShell execution
```

SIEM correlates events into high-severity alert.

---

### 4. ATT&CK Mapping

| Event       | ATT&CK |
| ----------- | ------ |
| Brute Force | T1110  |
| PowerShell  | T1059  |
| Discovery   | T1087  |

---

### 5. Detection

### Correlation Rule

```text id="hq6bzy"
5 failed logins
+
successful login
+
privileged action
```

---

### 6. Mitigation/Response

* Block IP
* Disable account
* Investigate endpoint
* Update detection rules

---

### 4. Microsoft Sentinel

[Microsoft Sentinel Documentation](https://learn.microsoft.com/en-us/azure/sentinel/overview?utm_source=chatgpt.com)

### 1. Define Concept

Cloud-native SIEM/SOAR platform built on Azure.

---

### 2. Architecture

```text id="3rnv11"
Data Connectors
→ Log Analytics Workspace
→ Analytics Rules
→ Incidents
→ Playbooks
```

---

### 3. Real-World Example

```text id="lz3n0x"
Multiple failed Azure AD logins
→ impossible travel
→ suspicious MFA activity
```

---

### 4. ATT&CK Mapping

| Activity       | ATT&CK |
| -------------- | ------ |
| Brute Force    | T1110  |
| Valid Accounts | T1078  |

---

### 5. Detection

### Example KQL

```kql id="rjlwmz"
SigninLogs
| where ResultType != 0
```

---

### 6. Mitigation/Response

* Trigger playbook
* Disable account
* Notify SOC
* Force password reset

---

### 5. Microsoft Defender for Endpoint (MDE)

[Microsoft Defender for Endpoint](https://www.microsoft.com/en-us/security/business/endpoint-security/microsoft-defender-endpoint?utm_source=chatgpt.com)

### 1. Define Concept

Enterprise EDR/XDR platform for endpoint visibility and response.

---

### 2. Architecture

```text id="s1m33i"
Endpoint Sensor
→ Cloud Analytics
→ Detection Engine
→ Advanced Hunting
→ Automated Response
```

---

### 3. Real-World Example

```text id="x3lcxf"
Mimikatz execution detected
```

MDE identifies:

* LSASS access
* suspicious privilege escalation

---

### 4. ATT&CK Mapping

| Activity           | ATT&CK |
| ------------------ | ------ |
| Credential Dumping | T1003  |
| Token Manipulation | T1134  |

---

### 5. Detection

### Query

```kql id="kgexuw"
DeviceProcessEvents
| where ProcessCommandLine contains "sekurlsa"
```

---

### 6. Mitigation/Response

* Isolate device
* Terminate process
* Revoke credentials
* Investigate lateral movement

---

### 6. Rapid7 InsightIDR

[Rapid7 InsightIDR](https://www.rapid7.com/products/insightidr/?utm_source=chatgpt.com)

### 1. Define Concept

Cloud SIEM with UEBA and threat detection capabilities.

---

### 2. Architecture

```text id="n5cwkh"
Agents/Collectors
→ Cloud SIEM
→ UEBA Engine
→ Alerting
→ Investigation
```

---

### 3. Real-World Example

```text id="mjlwm7"
User logs in from Pakistan
then 5 minutes later from Germany
```

Detected as impossible travel.

---

### 4. ATT&CK Mapping

| Activity       | ATT&CK |
| -------------- | ------ |
| Valid Accounts | T1078  |

---

### 5. Detection

Behavior analytics:

* login anomalies
* abnormal access times
* unusual privilege usage

---

### 6. Mitigation/Response

* Lock account
* Force MFA
* Investigate session activity

---

## 7. Rapid7 InsightVM

[Rapid7 InsightVM](https://www.rapid7.com/products/insightvm/?utm_source=chatgpt.com)

### 1. Define Concept

Vulnerability management platform for identifying and prioritizing vulnerabilities.

---

### 2. Architecture

```text id="jlwmw7"
Asset Discovery
→ Vulnerability Scan
→ Risk Scoring
→ Reporting
```

---

### 3. Real-World Example

```text id="x7xep8"
Unpatched Apache Log4j vulnerability discovered
```

---

### 4. ATT&CK Mapping

| Vulnerability Exploitation | ATT&CK |
| -------------------------- | ------ |
| Exploit Public-Facing App  | T1190  |

---

### 5. Detection

* Vulnerability scans
* CVE matching
* Missing patch analysis

---

### 6. Mitigation/Response

* Patch vulnerable systems
* Segment network
* Monitor exploitation attempts

---

## 8. Wazuh

[Wazuh Documentation](https://documentation.wazuh.com/?utm_source=chatgpt.com)

### 1. Define Concept

Open-source SIEM/XDR platform focused on log analysis, FIM, and endpoint monitoring.

---

### 2. Architecture

```text id="k3vr71"
Wazuh Agent
→ Wazuh Manager
→ Elasticsearch/OpenSearch
→ Dashboard
```

---

### 3. Real-World Example

```text id="mrpf5m"
Critical Linux config file modified
```

Wazuh FIM generates alert.

---

### 4. ATT&CK Mapping

| Activity          | ATT&CK |
| ----------------- | ------ |
| File Modification | T1565  |

---

### 5. Detection

* File hash changes
* Unauthorized config modifications
* Rootkit detection

---

### 6. Mitigation/Response

* Restore file
* Investigate user actions
* Review persistence

---

## 9. ELK Stack

## Elasticsearch

#### 1. Define Concept

Distributed search and analytics engine.

---

#### 2. Architecture

```text id="9hszv7"
Nodes
→ Indices
→ Shards
→ Replicas
```

---

#### 3. Real-World Example

Searching millions of logs for:

```text id="xgfwde"
powershell.exe
```

---

#### 4. ATT&CK Mapping

| Search     | ATT&CK    |
| ---------- | --------- |
| PowerShell | T1059.001 |

---

#### 5. Detection

Query suspicious fields:

```json id="w1o1vg"
process.name: powershell.exe
```

---

#### 6. Mitigation/Response

* Create alerts
* Block indicators
* Investigate timeline

---

## Logstash

### 1. Define Concept

Pipeline tool for collecting and transforming logs.

---

### 2. Architecture

```text id="t5bdtb"
Input
→ Filter
→ Output
```

---

### 3. Real-World Example

```text id="a7f0q9"
Windows logs parsed into JSON
```

---

### 4. ATT&CK Mapping

Indirect support for all ATT&CK detections.

---

### 5. Detection

Normalization enables correlation.

---

### 6. Mitigation/Response

Improves visibility and response automation.

---

## Kibana

### 1. Define Concept

Visualization and dashboard platform for Elasticsearch.

---

### 2. Architecture

```text id="l9ig0l"
Elasticsearch
→ Kibana
→ Dashboards/Visualizations
```

---

### 3. Real-World Example

SOC dashboard showing:

* failed logins
* malware alerts
* beaconing traffic

---

### 4. ATT&CK Mapping

Visualize:

* ATT&CK heatmaps
* detection coverage

---

### 5. Detection

Dashboards identify:

* spikes
* anomalies
* attack chains

---

### 6. Mitigation/Response

Supports:

* investigation
* threat hunting
* reporting

---

### 10. Threat Hunting

### 1. Define Concept

Proactive search for hidden threats.

---

### 2. Architecture

```text id="s5g5gx"
Telemetry
→ Hypothesis
→ Query
→ Investigation
→ Findings
```

---

### 3. Real-World Example

```text id="c4jlwm"
Hunt for encoded PowerShell
```

---

### 4. ATT&CK Mapping

| Activity   | ATT&CK    |
| ---------- | --------- |
| PowerShell | T1059.001 |

---

### 5. Detection

Query:

```kql id="90m92s"
ProcessCommandLine contains "-enc"
```

---

### 6. Mitigation/Response

* Remove malware
* Hunt across hosts
* Improve detections

---

### 11. Incident Response

### 1. Define Concept

Process for handling security incidents.

---

### 2. Architecture

```text id="8mt3qt"
Preparation
→ Identification
→ Containment
→ Eradication
→ Recovery
→ Lessons Learned
```

---

### 3. Real-World Example

```text id="31h2n4"
Ransomware outbreak
```

---

### 4. ATT&CK Mapping

| Activity   | ATT&CK |
| ---------- | ------ |
| Encryption | T1486  |

---

### 5. Detection

* EDR alerts
* File encryption spikes
* SMB anomalies

---

### 6. Mitigation/Response

* Isolate systems
* Disable shares
* Restore backups
* Hunt persistence