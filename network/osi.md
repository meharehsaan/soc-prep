# OSI = Open Systems Interconnection Model

Purpose:

- Standard framework explaining how data moves across a network.
- Divides networking into 7 layers.

---

| Layer | Layer Name                    | Main Purpose                                            | Core Functions                                                           | Common Protocols / Standards                               | Devices                                    | PDU (Protocol Data Unit)               | Addressing Used       | Security Examples                   | Important Ports / Services                                      | Important Notes / Interview Points                                         | Real-World Example                          |
| ----- | ----------------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------- | ------------------------------------------ | -------------------------------------- | --------------------- | ----------------------------------- | --------------------------------------------------------------- | -------------------------------------------------------------------------- | ------------------------------------------- |
| 7     | Application Layer             | Provides network services directly to user applications | Web browsing, email, file transfer, remote access, name resolution       | HTTP, HTTPS, FTP, SFTP, SMTP, POP3, IMAP, DNS, SSH, Telnet | Proxy Server, Gateway, Application Gateway | Data                                   | Domain names, URLs    | WAF, HTTP filtering, API security   | HTTP (80), HTTPS (443), FTP (21), SSH (22), SMTP (25), DNS (53) | Closest layer to user; browser mainly works here; DNS resolves domain → IP | Opening a website like `https://google.com` |
| 6     | Presentation Layer            | Translates, encrypts, and formats data                  | Encryption, decryption, compression, encoding, translation               | SSL/TLS, JPEG, PNG, ASCII, MPEG, GIF                       | Gateway                                    | Data                                   | Data format encoding  | SSL/TLS encryption                  | HTTPS encryption support                                        | Converts data into readable format between systems                         | HTTPS encrypting browser traffic            |
| 5     | Session Layer                 | Establishes and manages communication sessions          | Session setup, maintenance, synchronization, authentication, termination | NetBIOS, RPC, PPTP                                         | Gateway                                    | Data                                   | Session IDs           | Session control security            | VPN sessions, remote procedure calls                            | Manages communication sessions between devices                             | Video conference session management         |
| 4     | Transport Layer               | End-to-end communication and reliability                | Segmentation, flow control, error recovery, acknowledgment, multiplexing | TCP, UDP                                                   | Firewall, Load Balancer                    | Segment (TCP), Datagram (UDP)          | Port Numbers          | Stateful firewall, port filtering   | TCP/UDP ports                                                   | TCP = reliable; UDP = fast; performs segmentation                          | TCP handshake during HTTPS connection       |
| 4     | Transport Layer (TCP Details) | Reliable communication                                  | Ordered delivery, retransmission, acknowledgment                         | TCP                                                        | Firewall                                   | Segment                                | Port Numbers          | Stateful inspection                 | HTTPS, SSH, FTP                                                 | Connection-oriented; reliable                                              | Downloading a file safely                   |
| 4     | Transport Layer (UDP Details) | Fast communication                                      | Low latency communication                                                | UDP                                                        | Firewall                                   | Datagram                               | Port Numbers          | UDP filtering                       | DNS, VoIP, Streaming, Gaming                                    | Connectionless; no guarantee of delivery                                   | Online gaming voice chat                    |
| 3     | Network Layer                 | Routing and logical addressing                          | Routing, path selection, IP addressing, packet forwarding                | IPv4, IPv6, ICMP, OSPF, RIP, ARP                           | Router, Layer-3 Switch                     | Packet                                 | IP Address            | IP filtering, ACLs                  | ICMP ping/traceroute                                            | Routers operate here; handles logical addressing                           | Packet traveling across the internet        |
| 3     | Network Layer (ICMP)          | Diagnostics and error reporting                         | Connectivity testing, error messaging                                    | ICMP                                                       | Router                                     | Packet                                 | IP Address            | ICMP filtering                      | ping, traceroute                                                | Used for troubleshooting                                                   | Ping command                                |
| 2     | Data Link Layer               | Local network delivery                                  | Framing, MAC addressing, error detection, switching                      | Ethernet, PPP, HDLC, Frame Relay                           | Switch, Bridge                             | Frame                                  | MAC Address           | VLANs, MAC filtering, port security | Ethernet switching                                              | Switches work here; handles local delivery                                 | Switch forwarding Ethernet frames           |
| 2     | Data Link Layer (ARP)         | Resolves MAC addresses                                  | IP → MAC resolution                                                      | ARP                                                        | Switch                                     | Frame                                  | MAC + IP              | ARP inspection                      | `arp -a` command                                                | Used before local delivery                                                 | Device learning gateway MAC address         |
| 1     | Physical Layer                | Physical transmission of signals                        | Signal transmission, voltage standards, cabling, radio communication     | Ethernet physical standards, Fiber optics, Wi-Fi radio     | Hub, Repeater, Cables                      | Bits                                   | None                  | Cable protection, anti-tapping      | Electrical/optical signaling                                    | Concerned with hardware and media                                          | Data traveling through fiber cable          |
| —     | Encapsulation Process         | Wraps data with headers during transmission             | Adds headers layer by layer                                              | TCP/IP Stack                                               | All devices                                | Data → Segment → Packet → Frame → Bits | Multiple              | Layered security controls           | Entire network communication                                    | Sender encapsulates; receiver decapsulates                                 | Sending a webpage request                   |
| —     | Decapsulation Process         | Removes headers at receiver                             | Processes received data upward through layers                            | TCP/IP Stack                                               | All devices                                | Bits → Frame → Packet → Segment → Data | Multiple              | Traffic inspection                  | Entire network communication                                    | Reverse of encapsulation                                                   | Receiving a webpage                         |
| —     | OSI Mnemonic (Top → Bottom)   | Helps remember layer order                              | Memorization                                                             | "All People Seem To Need Data Processing"                  | —                                          | —                                      | —                     | —                                   | —                                                               | Application → Physical                                                     | Networking interviews                       |
| —     | OSI Mnemonic (Bottom → Top)   | Reverse layer memory                                    | Memorization                                                             | "Please Do Not Throw Sausage Pizza Away"                   | —                                          | —                                      | —                     | —                                   | —                                                               | Physical → Application                                                     | Troubleshooting                             |
| —     | TCP/IP Mapping                | Practical internet networking model                     | Simplified networking architecture                                       | TCP/IP                                                     | Internet infrastructure                    | Varies                                 | IP + Ports + MAC      | Internet security stack             | Internet services                                               | 4-layer practical model                                                    | Modern internet communication               |
| —     | Device Mapping Summary        | Maps devices to OSI layers                              | Network hardware categorization                                          | —                                                          | Hub, Switch, Router, Firewall, Gateway     | —                                      | MAC/IP/Ports          | Layer-specific security             | —                                                               | Common interview topic                                                     | Enterprise networks                         |
| —     | Addressing Summary            | Shows addressing by layer                               | Communication identification                                             | MAC, IP, Ports, URLs                                       | NICs, Routers                              | —                                      | MAC, IP, Port, Domain | Filtering and access control        | —                                                               | MAC = Layer 2, IP = Layer 3, Ports = Layer 4                               | Web communication                           |
| —     | Security by Layer             | Security technologies across OSI                        | Filtering, encryption, monitoring                                        | TLS, ACLs, VLANs                                           | Firewall, IDS/IPS, WAF                     | —                                      | Multiple              | WAF, VLAN, ACL, TLS                 | HTTPS, VPN                                                      | Security exists at every layer                                             | Secure enterprise environment               |
| —     | Real-World Packet Journey     | Complete network communication flow                     | DNS resolution, TCP handshake, encryption, routing                       | DNS, TCP, TLS, IP, Ethernet                                | Switches, Routers, Servers                 | All PDUs                               | MAC + IP + Ports      | End-to-end security                 | HTTPS browsing                                                  | Demonstrates all OSI layers together                                       | User opening a website                      |


# OSI Architecture Diagram

+---------------------------------------------------+
| Layer 7 | Application Layer                       |
| Protocols: HTTP, HTTPS, FTP, DNS, SMTP, SSH      |
| Devices: Proxy Servers, Gateways                  |
+---------------------------------------------------+
| Layer 6 | Presentation Layer                      |
| Functions: Encryption, Compression, Translation   |
| Protocols: SSL/TLS, JPEG, ASCII, MPEG             |
+---------------------------------------------------+
| Layer 5 | Session Layer                           |
| Functions: Session Establishment & Management     |
| Protocols: NetBIOS, RPC, PPTP                     |
+---------------------------------------------------+
| Layer 4 | Transport Layer                         |
| Protocols: TCP, UDP                               |
| Devices: Firewalls                                |
| PDU: Segment / Datagram                           |
+---------------------------------------------------+
| Layer 3 | Network Layer                           |
| Protocols: IP, ICMP, ARP, OSPF, RIP               |
| Devices: Routers, Layer-3 Switches                |
| PDU: Packet                                       |
+---------------------------------------------------+
| Layer 2 | Data Link Layer                         |
| Protocols: Ethernet, PPP, Frame Relay, MAC        |
| Devices: Switches, Bridges                        |
| PDU: Frame                                        |
+---------------------------------------------------+
| Layer 1 | Physical Layer                          |
| Devices: Hub, Repeater, Cables                    |
| Signals: Electrical / Optical / Radio             |
| PDU: Bits                                         |
+---------------------------------------------------+

---

# Data Encapsulation Flow

Application Data
    ↓
Transport Layer → Segment
    ↓
Network Layer → Packet
    ↓
Data Link Layer → Frame
    ↓
Physical Layer → Bits

Receiver performs:

- Decapsulation

---

# Detailed Layer Explanation

# Layer 7 — Application Layer

Purpose:

- Closest layer to end user.
- Provides network services to applications.

Functions:

- File transfer
- Email
- Web browsing
- Remote login

Common Protocols:

- HTTP/HTTPS → Web traffic
- FTP/SFTP → File transfer
- SMTP → Sending email
- POP3/IMAP → Receiving email
- DNS → Domain resolution
- SSH → Secure remote access

Important Interview Points:

- Users directly interact here.
- Browser operates mainly here.
- DNS converts domain → IP.

Example:
<www.google.com>

---

# Layer 6 — Presentation Layer

Purpose:

- Data formatting and translation.

Functions:

- Encryption
- Compression
- Character encoding
- Data conversion

Protocols/Formats:

- SSL/TLS
- JPEG
- PNG
- ASCII
- MPEG

Important Interview Points:

- Responsible for encryption/decryption.
- Converts data into machine-readable format.

Example:
HTTPS encryption.

---

# Layer 5 — Session Layer

Purpose:

- Establishes and manages communication sessions.

Functions:

- Session setup
- Authentication
- Synchronization
- Session termination

Protocols:

- NetBIOS
- RPC
- PPTP

Important Interview Questions:
Q: Which layer manages sessions?
A: Session Layer

Example:
Video conferencing session.

---

# Layer 4 — Transport Layer

Purpose:

- End-to-end delivery.

Main Responsibilities:

- Segmentation
- Reliability
- Flow control
- Error checking

Protocols:

- TCP
- UDP

PDU:

- Segment (TCP)
- Datagram (UDP)

---

## TCP Features

Associated with:

- :contentReference[oaicite:1]{index=1}

Features:

- Connection-oriented
- Reliable
- Acknowledgment-based
- Ordered delivery
- Error recovery

Uses:

- HTTPS
- SSH
- FTP

TCP 3-Way Handshake:

1. SYN
2. SYN-ACK
3. ACK

---

## UDP Features

Associated with:

- :contentReference[oaicite:2]{index=2}

Features:

- Connectionless
- Faster
- No reliability guarantee

Uses:

- DNS
- Streaming
- Gaming
- VoIP

---

# Layer 3 — Network Layer

Purpose:

- Logical addressing and routing.

Main Functions:

- Path determination
- Routing
- IP addressing

Protocols:

- IPv4
- IPv6
- ICMP
- OSPF
- RIP

Devices:

- Routers
- Layer-3 switches

PDU:

- Packet

Important Interview Questions:
Q: Which layer uses IP addresses?
A: Network Layer

Q: Which device works at Layer 3?
A: Router

---

## IPv4 Address Example

192.168.1.1

Structure:

- Network Portion
- Host Portion

Private IP Ranges:

- 10.0.0.0/8
- 172.16.0.0 – 172.31.255.255
- 192.168.0.0/16

---

## ICMP

Used for:

- Error reporting
- Diagnostics

Commands:

- ping
- traceroute

---

# Layer 2 — Data Link Layer

Purpose:

- Local network communication.

Functions:

- MAC addressing
- Error detection
- Framing

Protocols:

- Ethernet
- PPP
- HDLC

Devices:

- Switches
- Bridges

PDU:

- Frame

Important Interview Questions:
Q: Which layer uses MAC addresses?
A: Data Link Layer

Q: Which device operates at Layer 2?
A: Switch

---

## MAC Address

Example:
00:1A:2B:3C:4D:5E

Features:

- 48-bit hexadecimal address
- Burned into NIC card

---

## ARP (Address Resolution Protocol)

Purpose:

- Converts IP → MAC address.

Command:
arp -a

---

# Layer 1 — Physical Layer

Purpose:

- Physical transmission of bits.

Functions:

- Signal transmission
- Cable standards
- Voltage levels
- Radio frequencies

Devices:

- Hubs
- Repeaters
- Cables

Transmission Media:

- Fiber optic
- Copper cable
- Wireless signals

PDU:

- Bits

Important Interview Questions:
Q: Which layer deals with cables?
A: Physical Layer

Q: Hub operates at which layer?
A: Layer 1

---

# OSI Device Mapping

| Device   | OSI Layer |
| -------- | --------- |
| Hub      | Layer 1   |
| Repeater | Layer 1   |
| Switch   | Layer 2   |
| Bridge   | Layer 2   |
| Router   | Layer 3   |
| Firewall | Layer 3/4 |
| Gateway  | Layer 7   |

---

# Important Port Numbers

| Protocol | Port  |
| -------- | ----- |
| HTTP     | 80    |
| HTTPS    | 443   |
| FTP      | 21    |
| SSH      | 22    |
| Telnet   | 23    |
| SMTP     | 25    |
| DNS      | 53    |
| DHCP     | 67/68 |
| POP3     | 110   |
| IMAP     | 143   |

---

# TCP vs UDP

| Feature        | TCP                 | UDP            |
| -------------- | ------------------- | -------------- |
| Reliable       | Yes                 | No             |
| Connection     | Connection-oriented | Connectionless |
| Speed          | Slower              | Faster         |
| Error Recovery | Yes                 | No             |
| Ordering       | Yes                 | No             |
| Streaming      | Poor                | Better         |

---

# Encapsulation Example

Suppose user opens:
<https://example.com>

Process:

1. Application Layer creates HTTP request
2. Transport Layer adds TCP header
3. Network Layer adds IP header
4. Data Link adds MAC addresses
5. Physical Layer transmits bits

---

# Common Interview Questions

## Basic

Q: How many layers are in OSI?
A: 7

Q: Which layer does routing?
A: Layer 3

Q: Which layer handles encryption?
A: Layer 6

Q: Which layer uses MAC addresses?
A: Layer 2

Q: Which protocol uses port 443?
A: HTTPS

---

## Intermediate

Q: Difference between hub and switch?

Hub:

- Broadcasts everywhere
- Layer 1

Switch:

- Uses MAC table
- Layer 2

---

Q: Difference between packet and frame?

Packet:

- Layer 3
- Uses IP address

Frame:

- Layer 2
- Uses MAC address

---

Q: What is encapsulation?

Adding headers at each OSI layer during transmission.

---

Q: What is decapsulation?

Removing headers at receiving side.

---

# Mnemonics

Top → Bottom:
"All People Seem To Need Data Processing"

Application
Presentation
Session
Transport
Network
Data Link
Physical

Bottom → Top:
"Please Do Not Throw Sausage Pizza Away"

Physical
Data Link
Network
Transport
Session
Presentation
Application

---

# Real-World Packet Journey

User opens website:

1. DNS resolves domain to IP
2. TCP handshake occurs
3. HTTPS encrypts traffic
4. Router forwards packets
5. Switch delivers frames locally
6. Server responds

---

# Important Security Concepts by Layer

| Layer   | Security Examples        |
| ------- | ------------------------ |
| Layer 7 | WAF, HTTP filtering      |
| Layer 6 | SSL/TLS encryption       |
| Layer 4 | Stateful firewall        |
| Layer 3 | IP filtering             |
| Layer 2 | VLAN, MAC filtering      |
| Layer 1 | Cable tapping prevention |

---

# OSI vs TCP/IP Model

| OSI             | TCP/IP            |
| --------------- | ----------------- |
| 7 Layers        | 4 Layers          |
| Reference Model | Practical Model   |
| ISO Standard    | Internet Standard |

TCP/IP Layers:

1. Application
2. Transport
3. Internet
4. Network Access

---

# Final Quick Revision Table

| Layer | Name         | PDU     | Addressing | Device   |
| ----- | ------------ | ------- | ---------- | -------- |
| 7     | Application  | Data    | -          | Gateway  |
| 6     | Presentation | Data    | -          | Gateway  |
| 5     | Session      | Data    | -          | Gateway  |
| 4     | Transport    | Segment | Port       | Firewall |
| 3     | Network      | Packet  | IP         | Router   |
| 2     | Data Link    | Frame   | MAC        | Switch   |
| 1     | Physical     | Bits    | -          | Hub      |
