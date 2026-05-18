# Windows, Linux, and macOS Attacks for SOC L2 Interview Prep

# 1. Windows Attacks

## Classic / Famous Windows Attacks

### Pass-the-Hash (PtH)
- Uses NTLM hash instead of plaintext password
- Common in lateral movement
- Tools:
  - Mimikatz
  - CrackMapExec
- Detection:
  - Event ID 4624 Type 3
  - Abnormal NTLM authentication
  - Lateral admin logins

---

### Kerberoasting
- Attackers request Kerberos service tickets and crack them offline
- Targets SPN accounts with weak passwords
- Tools:
  - Rubeus
  - Impacket
- Detection:
  - Event ID 4769 spikes
  - RC4 encryption usage
  - Unusual service ticket requests

---

### Golden Ticket Attack
- Forged Kerberos TGT using KRBTGT hash
- Gives persistent domain admin access
- Tools:
  - Mimikatz
- Detection:
  - Invalid ticket lifetimes
  - Abnormal TGT activity
  - KRBTGT compromise indicators

---

### Pass-the-Ticket (PtT)
- Reuses stolen Kerberos tickets
- Avoids password use
- Detection:
  - Unusual ticket reuse
  - Lateral movement anomalies

---

### DLL Hijacking
- Malicious DLL loaded instead of legitimate one
- Persistence + privilege escalation
- Detection:
  - Sysmon Event ID 7
  - Unsigned DLLs
  - DLLs in temp/user directories

---

### PowerShell Attacks
- Fileless malware
- Encoded commands
- Living-off-the-land
- Detection:
  - Event ID 4104
  - Base64 encoded commands
  - AMSI alerts

---

### LSASS Credential Dumping
- Dumps credentials from LSASS memory
- Tools:
  - Mimikatz
  - ProcDump
- Detection:
  - Sysmon Event ID 10
  - LSASS access attempts
  - Defender alerts

---

### RDP Brute Force
- Password spraying against RDP
- Detection:
  - Event ID 4625
  - Multiple failed logins
  - Geographic anomalies

---

# Emerging Windows Threats

## BYOVD (Bring Your Own Vulnerable Driver)
- Attackers load vulnerable signed drivers
- Disable EDR or gain kernel access
- Used by:
  - BlackByte
  - AvosLocker
- Detection:
  - New driver loads
  - Event ID 6 (Sysmon)
  - Unsigned/vulnerable drivers

---

## LOLBins Abuse
- Legitimate binaries abused maliciously
- Examples:
  - mshta.exe
  - rundll32.exe
  - regsvr32.exe
  - certutil.exe
- Detection:
  - Command-line monitoring
  - Parent-child anomalies

---

## AMSI Bypass
- Evades PowerShell inspection
- Detection:
  - Memory patch indicators
  - AMSI failures
  - Obfuscated scripts

---

## ADCS Abuse (ESC1–ESC8)
- Active Directory Certificate Services abuse
- Used for persistence and privilege escalation
- Tools:
  - Certipy
  - Rubeus
- Detection:
  - Certificate enrollment anomalies
  - CA template abuse

---

# 2. Linux Attacks

## Famous Linux Attacks

### SSH Brute Force
- Most common Linux attack
- Detection:
  - `/var/log/auth.log`
  - Multiple failed logins
  - Geographic anomalies

---

### Dirty COW (CVE-2016-5195)
- Privilege escalation vulnerability
- Race condition exploit
- Detection:
  - Kernel exploit behavior
  - Sudden privilege escalation

---

### Rootkits
- Kernel/userland stealth malware
- Examples:
  - Diamorphine
  - Reptile
- Detection:
  - rkhunter
  - chkrootkit
  - Hidden processes/modules

---

### Cron Job Persistence
- Malicious scheduled jobs
- Detection:
  - Modified crontabs
  - Unknown scripts

---

### Sudo Exploits
- Exploiting sudo vulnerabilities
- Example:
  - Baron Samedit (CVE-2021-3156)
- Detection:
  - Suspicious sudo executions

---

### Web Shells
- PHP/JSP shell upload
- Examples:
  - China Chopper
  - c99 shell
- Detection:
  - Suspicious web requests
  - Outbound callbacks
  - Unexpected PHP files

---

# Emerging Linux Threats

## Cloud Metadata Exploitation
- Abuse cloud instance metadata services
- AWS/GCP/Azure token theft
- Detection:
  - Requests to metadata IP:
    - `169.254.169.254`

---

## eBPF Rootkits
- Advanced stealth malware using eBPF
- Difficult to detect
- Detection:
  - Unexpected eBPF programs
  - Kernel telemetry anomalies

---

## Container Escape Attacks
- Escape Docker/Kubernetes containers
- Examples:
  - CVE-2022-0492
- Detection:
  - Privileged container usage
  - Host namespace access

---

## Cryptojacking
- Resource hijacking for mining
- Detection:
  - High CPU usage
  - Mining pool traffic
  - XMRig processes

---

# 3. macOS Attacks

## Famous macOS Attacks

### XCSSET Malware
- Targets Xcode developers
- Steals credentials and browser data
- Detection:
  - Suspicious Xcode projects
  - Persistence agents

---

### Silver Sparrow
- M1-compatible malware
- Detection:
  - LaunchAgent persistence
  - Suspicious binaries

---

### Shlayer Trojan
- Fake Flash installer malware
- Very common macOS malware
- Detection:
  - Fake installer execution
  - Browser redirects

---

### OSX/KeRanger
- First macOS ransomware
- Detection:
  - File encryption behavior
  - Tor communication

---

### LaunchAgents Persistence
- macOS persistence mechanism
- Detection:
  - New plist files
  - User LaunchAgents changes

---

# Emerging macOS Threats

## Atomic Stealer (AMOS)
- Infostealer targeting macOS
- Steals:
  - Keychain
  - Browser credentials
  - Crypto wallets
- Detection:
  - Credential access
  - Unsigned binaries

---

## notarization Bypass
- Malware bypassing Apple notarization
- Detection:
  - Unsigned applications
  - Gatekeeper bypass events

---

## TCC Bypass Attacks
- Abuse Transparency Consent Control
- Access microphone/camera/files
- Detection:
  - TCC.db modifications
  - Suspicious app permissions

---

# SOC L2 Key Detection Areas

## Important Windows Logs
- Security.evtx
- Sysmon
- PowerShell logs
- Defender logs

### Important Event IDs
| Event ID | Meaning |
|---|---|
| 4624 | Successful login |
| 4625 | Failed login |
| 4688 | Process creation |
| 4768 | Kerberos TGT |
| 4769 | Kerberos service ticket |
| 4104 | PowerShell script block |
| 7045 | Service creation |

---

# Linux Logs

| Log File | Purpose |
|---|---|
| /var/log/auth.log | Authentication |
| /var/log/secure | RHEL auth logs |
| /var/log/syslog | System logs |
| auditd logs | Security auditing |

---

# macOS Logs

| Log | Purpose |
|---|---|
| Unified Logs | System activity |
| LaunchAgents | Persistence |
| system.log | General logs |

---

# MITRE ATT&CK Mapping Examples

| Attack | Technique |
|---|---|
| Pass-the-Hash | T1550.002 |
| Kerberoasting | T1558.003 |
| PowerShell Abuse | T1059.001 |
| SSH Brute Force | T1110 |
| Cron Persistence | T1053.003 |
| LaunchAgents | T1543.001 |

---

# Common SOC L2 Interview Questions

## Detection Engineering
- How would you detect Kerberoasting?
- How do you identify PowerShell obfuscation?
- What logs help detect Pass-the-Hash?

## Incident Response
- Steps after detecting ransomware?
- How do you isolate a compromised host?
- What evidence do you collect first?

## Threat Hunting
- Hunt for LOLBins usage
- Hunt for unusual parent-child processes
- Hunt for rare admin logins

## EDR Concepts
- Behavioral detection
- Memory analysis
- Process injection
- Persistence mechanisms

---

# High-Value SOC L2 Topics to Revise

- Active Directory attacks
- Windows Event IDs
- Sysmon
- Sigma rules
- MITRE ATT&CK
- Splunk queries
- KQL queries
- EDR telemetry
- Lateral movement
- Persistence techniques
- Ransomware behaviors
- Threat hunting methodology

---

# Recommended Tools

## Windows
- Sysmon
- Mimikatz
- Procmon
- Autoruns
- Rubeus

## Linux
- auditd
- rkhunter
- chkrootkit
- osquery

## macOS
- osquery
- Santa
- KnockKnock
- LuLu

---

# Quick Memory Trick

## Windows
- AD attacks + credential theft + LOLBins

## Linux
- SSH + privilege escalation + containers

## macOS
- Persistence + stealers + notarization bypass

---