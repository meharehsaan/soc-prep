# EDR, XDR, SIEM & SOC Tools — Deep Interview Preparation Guide

---

# Table of Contents

1. EDR Basics
2. XDR Basics
3. SIEM Basics
4. Difference: EDR vs XDR vs SIEM
5. Microsoft Sentinel
6. Microsoft Defender for Endpoint
7. Rapid7 InsightIDR
8. Rapid7 InsightVM
9. Wazuh
10. ELK Stack (Elasticsearch, Logstash, Kibana)
11. Detection Engineering Questions
12. Threat Hunting Questions
13. Incident Response Questions
14. Real-World SOC Scenarios
15. ATT&CK Mapping in SIEM/EDR
16. Common Log Sources
17. Correlation Rules
18. Important KQL/Sigma/Elastic Queries
19. Hard Interview Questions
20. Rapid-Fire Questions

---

# 1. What is EDR?

## Definition

EDR (Endpoint Detection and Response) monitors endpoints for:

* malicious activity
* suspicious behavior
* attacks
* persistence
* lateral movement

and enables:

* detection
* investigation
* containment
* response

---

# Core EDR Features

| Feature              | Purpose                     |
| -------------------- | --------------------------- |
| Process Monitoring   | Track executions            |
| File Monitoring      | Detect malware              |
| Behavioral Detection | Identify suspicious actions |
| Isolation            | Disconnect infected host    |
| Threat Hunting       | Search telemetry            |
| Timeline Analysis    | Attack reconstruction       |

---

# Example EDR Workflow

```text id="r3q1j1"
PowerShell executed
→ EDR detects encoded command
→ Alert generated
→ Analyst investigates
→ Host isolated
```

---

# Common EDR Vendors

| Vendor      | Product               |
| ----------- | --------------------- |
| Microsoft   | Defender for Endpoint |
| CrowdStrike | Falcon                |
| SentinelOne | Singularity           |
| VMware      | Carbon Black          |
| Palo Alto   | Cortex XDR            |

---

# EDR Interview Questions

## Q1. What is EDR?

Good answer:

> EDR continuously monitors endpoint activity, detects suspicious behavior, records telemetry, and enables rapid investigation and response.

---

## Q2. What telemetry does EDR collect?

| Telemetry           | Example               |
| ------------------- | --------------------- |
| Process creation    | powershell.exe        |
| Network connections | outbound IP           |
| Registry changes    | Run Keys              |
| File modifications  | ransomware encryption |
| User logins         | authentication        |

---

## Q3. Difference between antivirus and EDR?

| Antivirus          | EDR                  |
| ------------------ | -------------------- |
| Signature-based    | Behavioral           |
| Prevention-focused | Detection + Response |
| Limited visibility | Deep telemetry       |
| Static             | Investigative        |

---

# 2. What is XDR?

## Definition

XDR (Extended Detection and Response) integrates multiple security layers:

* endpoints
* email
* cloud
* network
* identity

into one platform.

---

# Difference: EDR vs XDR

| EDR                | XDR                       |
| ------------------ | ------------------------- |
| Endpoint only      | Multiple domains          |
| Endpoint telemetry | Unified telemetry         |
| Local visibility   | Cross-platform visibility |

---

# Example XDR Detection

```text id="7w7phn"
Phishing email
→ user clicks link
→ endpoint executes malware
→ unusual login detected
→ XDR correlates entire attack chain
```

---

# XDR Interview Questions

## Q1. Why is XDR important?

Because modern attacks involve:

* email
* endpoints
* cloud
* identity

XDR correlates all telemetry.

---

## Q2. What is telemetry correlation?

Combining events from multiple sources to detect attacks.

---

# 3. What is SIEM?

## Definition

SIEM (Security Information and Event Management) collects, stores, correlates, and analyzes logs.

---

# SIEM Functions

| Function       | Purpose         |
| -------------- | --------------- |
| Log Collection | Gather logs     |
| Correlation    | Link events     |
| Alerting       | Notify analysts |
| Dashboards     | Visualization   |
| Threat Hunting | Query logs      |
| Compliance     | Audit/reporting |

---

# SIEM Workflow

```text id="h5l9qx"
Firewall logs
+
EDR alerts
+
Windows logs
→ correlation rule
→ alert
```

---

# SIEM Interview Questions

## Q1. What are SIEM use cases?

* Threat detection
* Compliance
* Log retention
* Hunting
* Incident investigation

---

## Q2. Explain correlation rules

Rules combining multiple suspicious events.

Example:

```text id="8d9s7p"
Failed logins
+
successful login
+
PowerShell execution
=
possible compromise
```

---

# 4. EDR vs XDR vs SIEM

| Feature                | EDR     | XDR      | SIEM      |
| ---------------------- | ------- | -------- | --------- |
| Endpoint monitoring    | Yes     | Yes      | Partial   |
| Multi-source telemetry | Limited | Yes      | Yes       |
| Correlation            | Basic   | Advanced | Advanced  |
| Threat hunting         | Yes     | Yes      | Yes       |
| Log storage            | Limited | Medium   | Extensive |

---

# 5. Microsoft Sentinel

[Microsoft Sentinel Official Site](https://learn.microsoft.com/en-us/azure/sentinel/overview?utm_source=chatgpt.com)

## What is Sentinel?

Cloud-native SIEM/SOAR from Microsoft Azure.

---

# Core Components

| Component       | Purpose            |
| --------------- | ------------------ |
| Data Connectors | Ingest logs        |
| Analytics Rules | Detection logic    |
| Workbooks       | Dashboards         |
| Hunting Queries | Threat hunting     |
| Playbooks       | Automated response |

---

# Important Sentinel Concepts

## KQL (Kusto Query Language)

Used for:

* hunting
* dashboards
* detections

---

# Sample KQL Queries

## Failed Logins

```kql id="jlwm5m"
SecurityEvent
| where EventID == 4625
```

---

## PowerShell Detection

```kql id="jv6b2v"
DeviceProcessEvents
| where FileName == "powershell.exe"
```

---

# Sentinel Interview Questions

## Q1. What is Sentinel?

Cloud-native SIEM and SOAR solution built on Azure.

---

## Q2. What are Sentinel playbooks?

Automated workflows using Logic Apps.

Example:

```text id="0eh4k4"
Alert
→ isolate device
→ notify SOC
→ create ticket
```

---

## Q3. Difference between Analytics Rule and Hunting Query?

| Analytics Rule      | Hunting Query        |
| ------------------- | -------------------- |
| Automated detection | Manual investigation |
| Generates alerts    | Analyst-driven       |

---

# 6. Microsoft Defender for Endpoint (MDE)

[Microsoft Defender for Endpoint](https://www.microsoft.com/en-us/security/business/endpoint-security/microsoft-defender-endpoint?utm_source=chatgpt.com)

## What is MDE?

Microsoft’s EDR/XDR platform.

---

# Key Features

| Feature                  | Purpose            |
| ------------------------ | ------------------ |
| Endpoint telemetry       | Visibility         |
| Automated investigation  | AI response        |
| Threat hunting           | Advanced hunting   |
| Device isolation         | Containment        |
| Vulnerability management | Exposure reduction |

---

# Important MDE Tables

| Table                | Purpose          |
| -------------------- | ---------------- |
| DeviceProcessEvents  | Processes        |
| DeviceNetworkEvents  | Connections      |
| DeviceFileEvents     | File actions     |
| DeviceRegistryEvents | Registry changes |

---

# MDE Hunting Query

## Suspicious PowerShell

```kql id="i6f3lg"
DeviceProcessEvents
| where ProcessCommandLine contains "-enc"
```

---

# MDE Interview Questions

## Q1. What is device isolation?

Disconnect infected endpoint from network while keeping management access.

---

## Q2. Explain Advanced Hunting

KQL-based threat hunting across endpoint telemetry.

---

## Q3. What is ASR?

Attack Surface Reduction rules.

Examples:

* block macros
* block credential stealing
* block executable content

---

# 7. Rapid7 InsightIDR

[Rapid7 InsightIDR](https://www.rapid7.com/products/insightidr/?utm_source=chatgpt.com)

## What is InsightIDR?

Cloud SIEM + UEBA + detection platform.

---

# Features

| Feature       | Purpose                 |
| ------------- | ----------------------- |
| SIEM          | Log analysis            |
| UEBA          | User behavior analytics |
| Detection     | Threat alerts           |
| Investigation | Attack timelines        |

---

# Important Concepts

## UEBA

Detects abnormal behavior:

* impossible travel
* unusual logins
* privilege abuse

---

# InsightIDR Interview Questions

## Q1. What is UEBA?

Behavioral analytics detecting anomalies in user/entity behavior.

---

## Q2. What are LEQL queries?

Log Entry Query Language used in Rapid7.

---

# 8. Rapid7 InsightVM

[Rapid7 InsightVM](https://www.rapid7.com/products/insightvm/?utm_source=chatgpt.com)

## What is InsightVM?

Vulnerability management platform.

---

# Features

| Feature                | Purpose           |
| ---------------------- | ----------------- |
| Vulnerability scanning | Find CVEs         |
| Risk scoring           | Prioritize issues |
| Asset discovery        | Inventory         |
| Reporting              | Compliance        |

---

# Important Terms

| Term        | Meaning           |
| ----------- | ----------------- |
| CVE         | Vulnerability ID  |
| CVSS        | Severity score    |
| Remediation | Fix vulnerability |

---

# Interview Questions

## Q1. Difference between InsightIDR and InsightVM?

| InsightIDR | InsightVM                |
| ---------- | ------------------------ |
| SIEM/XDR   | Vulnerability Management |
| Detection  | Scanning                 |
| Monitoring | Risk assessment          |

---

# 9. Wazuh

[Wazuh Official Site](https://wazuh.com/?utm_source=chatgpt.com)

## What is Wazuh?

Open-source SIEM/XDR platform.

---

# Components

| Component                | Purpose             |
| ------------------------ | ------------------- |
| Agent                    | Endpoint collection |
| Manager                  | Rule processing     |
| Elasticsearch/OpenSearch | Storage             |
| Dashboard                | Visualization       |

---

# Wazuh Capabilities

| Capability              | Example                   |
| ----------------------- | ------------------------- |
| FIM                     | File Integrity Monitoring |
| Rootkit detection       | Malware checks            |
| Log analysis            | Security logs             |
| Vulnerability detection | CVE monitoring            |

---

# Wazuh Interview Questions

## Q1. What is FIM?

Detecting unauthorized file changes.

---

## Q2. Explain Wazuh architecture

```text id="zhxdrh"
Agent
→ Manager
→ Indexer
→ Dashboard
```

---

# 10. ELK Stack

## Components

| Component     | Purpose        |
| ------------- | -------------- |
| Elasticsearch | Search/storage |
| Logstash      | Log processing |
| Kibana        | Visualization  |

---

# ELK Flow

```text id="e1z1gh"
Logs
→ Logstash
→ Elasticsearch
→ Kibana
```

---

# Elasticsearch

## Purpose

Distributed search and analytics engine.

---

# Important Concepts

| Concept  | Meaning                 |
| -------- | ----------------------- |
| Index    | Database-like structure |
| Document | JSON log entry          |
| Shard    | Data partition          |

---

# Logstash

## Purpose

Log ingestion and transformation.

---

# Pipeline Example

```text id="8hlvgs"
input
→ filter
→ output
```

---

# Kibana

## Purpose

Visualization/dashboarding.

---

# ELK Interview Questions

## Q1. What is Elasticsearch?

Distributed search and analytics engine storing indexed data.

---

## Q2. What are shards?

Partitions of Elasticsearch indices.

---

## Q3. Why use Logstash?

To parse, enrich, and forward logs.

---

# 11. Detection Engineering Questions

## Q1. How do you build a detection?

1. Identify technique
2. Define telemetry
3. Create logic
4. Test
5. Tune false positives

---

## Q2. Explain false positives

Benign events triggering alerts incorrectly.

---

## Q3. Explain false negatives

Malicious activity missed by detection.

---

# 12. Threat Hunting Questions

## Q1. How do you hunt PowerShell abuse?

Look for:

* encoded commands
* hidden windows
* IEX
* download cradle

---

## Q2. What logs help hunting?

| Log    | Purpose             |
| ------ | ------------------- |
| Sysmon | Endpoint visibility |
| DNS    | C2 detection        |
| EDR    | Behavior            |
| Proxy  | Exfiltration        |

---

# 13. Incident Response Questions

## Q1. IR Lifecycle

| Phase           | Purpose          |
| --------------- | ---------------- |
| Preparation     | Readiness        |
| Identification  | Detect incident  |
| Containment     | Stop spread      |
| Eradication     | Remove threat    |
| Recovery        | Restore systems  |
| Lessons Learned | Improve controls |

---

# 14. Real SOC Scenario Questions

## Scenario 1

```text id="2fd2f9"
Encoded PowerShell detected
```

Expected answer:

* investigate parent process
* map ATT&CK
* check persistence
* isolate endpoint
* review network connections

---

## Scenario 2

```text id="bhff1g"
Multiple failed logins then success
```

Possible:

* brute force
* credential stuffing
* compromised account

---

# 15. ATT&CK Mapping Examples

| Activity             | ATT&CK    |
| -------------------- | --------- |
| Encoded PowerShell   | T1059.001 |
| Mimikatz             | T1003     |
| PsExec               | T1021.002 |
| Obfuscation          | T1027     |
| Registry Persistence | T1547     |

---

# 16. Common Windows Event IDs

| Event ID | Meaning                 |
| -------- | ----------------------- |
| 4624     | Successful login        |
| 4625     | Failed login            |
| 4688     | Process creation        |
| 7045     | Service creation        |
| 4104     | PowerShell script block |

---

# 17. Correlation Rule Example

```text id="6a0pc0"
Failed logins
+
successful login
+
privilege escalation
=
high severity alert
```

---

# 18. Important Elastic Query Example

## Search PowerShell

```json id="5wodj4"
{
  "query": {
    "match": {
      "process.name": "powershell.exe"
    }
  }
}
```

---

# 19. Hard Interview Questions

## Q1. Difference between SIEM and SOAR?

| SIEM            | SOAR                   |
| --------------- | ---------------------- |
| Detects threats | Automates response     |
| Log analysis    | Workflow orchestration |

---

## Q2. Explain telemetry normalization

Converting logs into standardized format.

---

## Q3. Why is context important in alerts?

Because:

* raw alerts lack meaning
* context reduces false positives
* helps prioritization

---

# 20. Rapid-Fire Questions

| Question                 | Answer                   |
| ------------------------ | ------------------------ |
| EDR purpose?             | Endpoint monitoring      |
| XDR purpose?             | Unified detection        |
| SIEM purpose?            | Log correlation          |
| Sentinel query language? | KQL                      |
| Wazuh FIM?               | File monitoring          |
| Elasticsearch stores?    | Indexed documents        |
| Logstash role?           | Parsing                  |
| Kibana role?             | Visualization            |
| InsightVM purpose?       | Vulnerability management |
| UEBA?                    | Behavioral analytics     |

---

# Final High-Value Interview Topics

Focus deeply on:

* KQL
* ATT&CK Mapping
* Detection Engineering
* Threat Hunting
* PowerShell abuse
* Sysmon logs
* Windows Event IDs
* EDR telemetry
* Incident response workflow
* Correlation rules
* SIEM architecture
* False positives tuning

---

# Golden Interview Answer Structure

```text id="5v0lf8"
1. Define concept
2. Explain architecture
3. Give real-world example
4. Mention ATT&CK mapping
5. Explain detection
6. Explain mitigation/response
