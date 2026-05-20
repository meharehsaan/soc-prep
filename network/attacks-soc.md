# Important Cybersecurity Attacks from SOC (Security Operations Center) POV

## Phishing
- Fake emails/messages designed to steal credentials or deliver malware.
- Most common initial access vector in real-world incidents.

## Spear Phishing
- Targeted phishing against specific employees or departments.
- Harder to detect because it looks personalized.

## Business Email Compromise (BEC)
- Attackers impersonate executives/vendors for fraud or data theft.
- Causes major financial losses in organizations.

## Malware
- General malicious software used to damage, spy, or gain access.
- SOC teams constantly monitor malware indicators.

## Ransomware
- Encrypts systems/files and demands payment.
- One of the highest-priority incidents in SOC environments.

## Trojan
- Malware disguised as legitimate software.
- Frequently used for persistence and remote access.

## RAT (Remote Access Trojan)
- Gives attackers remote control over infected machines.
- Common in espionage and persistence attacks.

## Spyware
- Secretly monitors user activity and steals information.
- Often linked with credential theft.

## Keylogger
- Captures keystrokes to steal passwords and sensitive data.
- Common in banking and credential attacks.

## Botnet
- Network of infected devices controlled remotely.
- Used in DDoS and malware distribution.

---

# Credential & Authentication Attacks

## Brute Force Attack
- Repeated password guessing attempts.
- SOC monitors failed login spikes.

## Password Spraying
- Uses common passwords across many accounts.
- Very common against enterprise environments.

## Credential Stuffing
- Uses leaked username/password combinations.
- Major threat after data breaches.

## MFA Fatigue Attack
- Bombards users with MFA requests until approved.
- Increasingly common in modern cloud attacks.

## Pass-the-Hash
- Uses stolen password hashes directly.
- Common in Windows lateral movement.

## Kerberoasting
- Steals Kerberos service ticket hashes for cracking.
- Important Active Directory threat.

## Privilege Escalation
- Gains higher permissions after initial compromise.
- Critical stage in most attacks.

---

# Web & Application Attacks

## XSS (Cross-Site Scripting)
- Injects malicious scripts into websites.
- Important for web app monitoring.

## SQL Injection (SQLi)
- Manipulates backend databases through vulnerable inputs.
- Can lead to full database compromise.

## Command Injection
- Executes system commands on servers.
- Often leads to full server takeover.

## File Inclusion (LFI/RFI)
- Loads malicious/local files through vulnerable applications.
- Frequently abused in PHP applications.

## Directory Traversal
- Accesses restricted files/directories.
- Used for data exposure.

## CSRF
- Tricks authenticated users into unintended actions.
- Impacts web session security.

## SSRF
- Forces servers to make malicious requests internally.
- High-risk in cloud environments.

## Deserialization Attack
- Executes malicious serialized objects.
- Common in enterprise apps and APIs.

## API Abuse
- Exploits insecure APIs for unauthorized access.
- Increasingly important in modern SOCs.

---

# Network Attacks

## Man-in-the-Middle (MITM)
- Intercepts communication between systems.
- Dangerous on insecure networks.

## DNS Tunneling
- Uses DNS traffic for covert communication/data exfiltration.
- Important detection use case for SOC analysts.

## DNS Spoofing
- Redirects users to fake destinations.
- Often used in phishing campaigns.

## ARP Spoofing
- Redirects local network traffic through attacker systems.
- Common in internal attacks.

## Packet Sniffing
- Captures sensitive network traffic.
- SOC monitors suspicious sniffing tools.

## Port Scanning
- Identifies open services before attacks.
- Often first recon stage.

## BGP Hijacking
- Manipulates internet routing.
- Rare but highly impactful.

## SSL Stripping
- Downgrades HTTPS connections to insecure HTTP.
- Used for credential interception.

---

# Denial-of-Service Attacks

## DoS
- Single-source service disruption attack.
- Impacts service availability.

## DDoS
- Large-scale distributed flooding attack.
- Major SOC monitoring priority.

## SYN Flood
- Exhausts server TCP connections.
- Common DDoS technique.

## HTTP Flood
- Overwhelms web applications with requests.
- Harder to distinguish from legitimate traffic.

## Slowloris
- Keeps many connections partially open.
- Effective against poorly configured servers.

---

# Advanced Threats & Persistence

## APT (Advanced Persistent Threat)
- Long-term stealth attacks by skilled groups.
- Often nation-state or highly organized actors.

## Supply Chain Attack
- Compromises trusted vendors/software updates.
- Extremely dangerous due to trusted access.

## Living-off-the-Land (LotL)
- Uses legitimate system tools maliciously.
- Hard to detect because no malware may exist.

## Zero-Day Exploit
- Exploits unknown vulnerabilities before patches exist.
- High-severity SOC incidents.

## Backdoor
- Hidden persistent access mechanism.
- Used after compromise for re-entry.

## Rootkit
- Hides malware and attacker activity deeply in systems.
- Difficult to detect and remove.

---

# Cloud & Identity Attacks

## Cloud Misconfiguration Exploit
- Abuses insecure cloud storage/services.
- Very common in AWS/Azure/GCP incidents.

## Account Takeover (ATO)
- Gains control of user accounts.
- Common via phishing or credential theft.

## OAuth Token Theft
- Steals cloud authentication tokens.
- Important in Microsoft 365/Google Workspace attacks.

## Session Hijacking
- Takes over active authenticated sessions.
- Common in web/cloud attacks.

---

# Reconnaissance & Lateral Movement

## Enumeration
- Collects detailed network/system information.
- Usually happens before exploitation.

## OSINT Gathering
- Uses public information for targeting.
- Common pre-attack activity.

## Lateral Movement
- Moves from one compromised system to another.
- Key SOC detection phase.

## Data Exfiltration
- Steals sensitive company data externally.
- Critical SOC incident category.

---