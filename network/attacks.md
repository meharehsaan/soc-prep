# Cybersecurity Attack Types List

## Web & Application Attacks

- **XSS (Cross-Site Scripting)** — Injects malicious scripts into web pages viewed by users.
- **Stored XSS** — Malicious script is permanently stored on the server.
- **Reflected XSS** — Script is reflected from a request into the response instantly.
- **DOM-based XSS** — Client-side JavaScript modifies the page insecurely.

- **SQL Injection (SQLi)** — Injects SQL queries to manipulate databases.
- **NoSQL Injection** — Exploits NoSQL database query handling.
- **Command Injection** — Executes system commands through vulnerable input fields.
- **Code Injection** — Injects executable code into applications.
- **LDAP Injection** — Manipulates LDAP directory queries.
- **XML Injection** — Alters XML data processing behavior.
- **XPath Injection** — Exploits XPath queries in XML systems.
- **CRLF Injection** — Injects carriage return/line feed into HTTP headers.
- **SSTI (Server-Side Template Injection)** — Executes code via template engines.

- **LFI (Local File Inclusion)** — Includes local files from the server.
- **RFI (Remote File Inclusion)** — Includes remote malicious files into execution.
- **Directory Traversal** — Accesses restricted directories using path manipulation.
- **CSRF (Cross-Site Request Forgery)** — Tricks users into unwanted authenticated actions.
- **SSRF (Server-Side Request Forgery)** — Forces server to send unintended requests.
- **HTTP Request Smuggling** — Exploits inconsistent HTTP request parsing.
- **Session Hijacking** — Steals active user sessions.
- **Cookie Poisoning** — Modifies cookies to bypass security.
- **Clickjacking** — Tricks users into clicking hidden elements.
- **Open Redirect** — Redirects users to malicious websites.
- **Buffer Overflow** — Overwrites memory causing crashes or code execution.
- **Heap Overflow** — Corrupts heap memory allocation.
- **Integer Overflow** — Exploits arithmetic overflow conditions.
- **Race Condition Attack** — Exploits timing flaws in execution order.
- **Deserialization Attack** — Executes malicious serialized objects.
- **Privilege Escalation** — Gains higher system permissions.
- **Authentication Bypass** — Circumvents login or verification mechanisms.
- **Business Logic Attack** — Exploits flawed application workflows.
- **API Abuse** — Misuses APIs beyond intended functionality.
- **Zero-Day Exploit** — Exploits unknown/unpatched vulnerabilities.

---

## Network Attacks

- **MITM (Man-in-the-Middle)** — Intercepts communication between two parties.
- **DNS Tunneling** — Transfers hidden data through DNS traffic.
- **DNS Spoofing** — Redirects users to fake websites via forged DNS replies.
- **DNS Cache Poisoning** — Corrupts DNS cache with malicious mappings.
- **ARP Spoofing** — Fakes MAC-IP mappings on local networks.
- **IP Spoofing** — Forges source IP addresses.
- **MAC Spoofing** — Changes device MAC address identity.
- **DHCP Starvation** — Exhausts DHCP IP allocation pool.
- **DHCP Spoofing** — Rogue DHCP server distributes malicious settings.
- **Packet Sniffing** — Captures network packets secretly.
- **Session Replay Attack** — Reuses captured valid session data.
- **TCP SYN Flood** — Floods server with incomplete TCP connections.
- **UDP Flood** — Overwhelms systems with UDP packets.
- **ICMP Flood** — Uses ping traffic to overload targets.
- **Smurf Attack** — Amplified ICMP flood using broadcast addresses.
- **Fraggle Attack** — UDP variant of the Smurf attack.
- **Routing Attack** — Manipulates network routing paths.
- **Evil Twin Attack** — Creates fake Wi-Fi access points.
- **Rogue Access Point** — Unauthorized wireless access point on network.
- **BGP Hijacking** — Redirects internet traffic using fake BGP routes.
- **Port Scanning** — Searches systems for open ports.
- **Traffic Analysis** — Studies communication patterns for intelligence.
- **SSL Stripping** — Downgrades HTTPS connections to HTTP.

---

## Malware Attacks

- **Virus** — Malicious code that infects files and spreads.
- **Worm** — Self-replicating malware spreading automatically.
- **Trojan Horse** — Malware disguised as legitimate software.
- **Ransomware** — Encrypts data and demands payment.
- **Spyware** — Secretly monitors user activity.
- **Adware** — Displays intrusive advertisements.
- **Rootkit** — Hides malware with privileged access.
- **Keylogger** — Records keyboard input secretly.
- **Logic Bomb** — Activates malicious actions under conditions.
- **Backdoor** — Hidden access method bypassing authentication.
- **Botnet Malware** — Turns systems into remotely controlled bots.
- **Cryptojacking** — Steals resources for cryptocurrency mining.
- **Wiper Malware** — Permanently destroys data.
- **Fileless Malware** — Operates mainly in system memory.
- **Polymorphic Malware** — Changes code to evade detection.
- **Metamorphic Malware** — Rewrites itself completely while retaining function.
- **RAT (Remote Access Trojan)** — Gives attackers remote control access.
- **Banking Trojan** — Targets banking credentials and transactions.
- **Dropper Malware** — Installs additional malware payloads.

---

## Social Engineering Attacks

- **Phishing** — Fake messages steal credentials or data.
- **Spear Phishing** — Targeted phishing against specific individuals.
- **Whaling** — Phishing attacks targeting executives.
- **Smishing** — SMS-based phishing attack.
- **Vishing** — Voice-call phishing attack.
- **Clone Phishing** — Copies legitimate emails with malicious modifications.
- **BEC (Business Email Compromise)** — Fraud using compromised business emails.
- **Pretexting** — Creates fake scenarios to obtain information.
- **Baiting** — Uses tempting offers to lure victims.
- **Tailgating** — Unauthorized physical access by following someone.
- **Shoulder Surfing** — Observes confidential information physically.
- **Scareware** — Frightens users into unsafe actions.
- **Impersonation Attack** — Pretends to be trusted individuals.
- **Romance Scam** — Manipulates victims emotionally for money.
- **Tech Support Scam** — Fake support tricks victims into granting access.
- **Deepfake Scam** — Uses AI-generated fake audio/video deception.

---

## Password & Authentication Attacks

- **Brute Force Attack** — Tries every password combination.
- **Dictionary Attack** — Uses common word lists for passwords.
- **Credential Stuffing** — Reuses leaked credentials on multiple sites.
- **Password Spraying** — Uses common passwords against many accounts.
- **Rainbow Table Attack** — Uses precomputed password hash tables.
- **MFA Fatigue Attack** — Bombards users with MFA approval requests.
- **Session Fixation** — Forces users to use attacker-controlled sessions.
- **Pass-the-Hash** — Uses stolen password hashes directly.
- **Kerberoasting** — Extracts service ticket hashes in Active Directory.
- **Golden Ticket Attack** — Forges Kerberos authentication tickets.
- **Silver Ticket Attack** — Forges service-specific Kerberos tickets.

---

## Denial-of-Service Attacks

- **DoS (Denial of Service)** — Disrupts service availability from one source.
- **DDoS (Distributed Denial of Service)** — Uses many systems to overwhelm targets.
- **Amplification Attack** — Magnifies attack traffic using third-party servers.
- **Reflection Attack** — Spoofs victim IP to redirect responses.
- **HTTP Flood** — Floods web servers with HTTP requests.
- **Slowloris** — Keeps many HTTP connections partially open.
- **Ping of Death** — Sends malformed oversized packets.
- **Teardrop Attack** — Sends fragmented overlapping packets.

---

## Wireless & Mobile Attacks

- **Bluejacking** — Sends unsolicited Bluetooth messages.
- **Bluesnarfing** — Steals data over Bluetooth connections.
- **SIM Swapping** — Hijacks phone numbers via carrier fraud.
- **Wi-Fi Eavesdropping** — Intercepts wireless communications.
- **NFC Exploits** — Abuses Near Field Communication features.
- **Mobile Malware** — Malware targeting smartphones/devices.
- **Juice Jacking** — Compromises devices via USB charging stations.
- **IMSI Catcher Attack** — Fake cell tower intercepts mobile traffic.

---

## Cloud & Infrastructure Attacks

- **Cloud Misconfiguration Exploit** — Abuses insecure cloud settings.
- **Container Escape** — Breaks isolation between containers and host.
- **Kubernetes Attack** — Targets Kubernetes cluster vulnerabilities.
- **Supply Chain Attack** — Compromises trusted vendors/software updates.
- **CI/CD Pipeline Attack** — Targets software deployment pipelines.
- **Hypervisor Attack** — Exploits virtualization layer vulnerabilities.
- **Shadow IT Exploit** — Targets unauthorized organizational tools.
- **VM Escape** — Escapes virtual machine into host system.

---

## Cryptography Attacks

- **Birthday Attack** — Exploits hash collision probability.
- **Collision Attack** — Finds two inputs with same hash.
- **Side-Channel Attack** — Exploits physical implementation leakage.
- **Padding Oracle Attack** — Exploits cryptographic padding validation.
- **Replay Attack** — Reuses captured valid communication data.
- **Downgrade Attack** — Forces weaker encryption protocols.
- **Chosen Plaintext Attack** — Analyzes encryption using selected plaintexts.
- **Chosen Ciphertext Attack** — Uses selected ciphertexts to reveal secrets.
- **Timing Attack** — Uses response timing to infer secrets.

---

## Insider & Human Threats

- **Insider Threat** — Malicious or negligent internal actors.
- **Data Exfiltration** — Unauthorized transfer of sensitive data.
- **Sabotage** — Intentional damage to systems or operations.
- **Privilege Misuse** — Abuse of legitimate access rights.
- **USB Drop Attack** — Malware delivery through planted USB devices.

---

## Advanced Persistent & Nation-State Attacks

- **APT (Advanced Persistent Threat)** — Long-term stealthy targeted attack campaign.
- **Watering Hole Attack** — Compromises websites frequented by targets.
- **Drive-by Download** — Malware downloaded by visiting infected websites.
- **Firmware Attack** — Targets low-level device firmware.
- **Hardware Implant Attack** — Installs malicious physical hardware.
- **Cyber Espionage** — Steals sensitive government/corporate intelligence.
- **Living-off-the-Land (LotL)** — Uses legitimate system tools maliciously.

---

## IoT & Embedded Device Attacks

- **IoT Botnet Attack** — Controls smart devices for attacks.
- **Smart Device Hijacking** — Takes control of connected devices.
- **Firmware Exploit** — Exploits vulnerabilities in device firmware.
- **Sensor Spoofing** — Manipulates sensor readings falsely.

---

## Cryptocurrency & Blockchain Attacks

- **51% Attack** — Majority network control manipulates blockchain.
- **Double Spending Attack** — Reuses same cryptocurrency multiple times.
- **Rug Pull** — Developers abandon projects after taking funds.
- **Smart Contract Exploit** — Exploits vulnerable blockchain contract code.
- **Flash Loan Attack** — Manipulates DeFi markets using instant loans.
- **Wallet Draining** — Steals cryptocurrency wallet assets.

---

## AI & Modern Threats

- **Prompt Injection** — Manipulates AI behavior through crafted prompts.
- **Model Poisoning** — Corrupts AI training data/models.
- **Data Poisoning** — Injects malicious training data.
- **Adversarial AI Attack** — Tricks AI models with crafted inputs.
- **AI Jailbreak Attack** — Bypasses AI safety restrictions.

---

## Reconnaissance & Information Gathering

- **Footprinting** — Collects target information before attacking.
- **OSINT Gathering** — Uses publicly available intelligence sources.
- **Banner Grabbing** — Retrieves service/version information from systems.
- **Enumeration** — Extracts detailed system/user/network information.
- **Whois Enumeration** — Collects domain registration details.
- **Subdomain Enumeration** — Finds hidden or related subdomains.

---
