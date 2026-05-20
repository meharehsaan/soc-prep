# OWASP Top 10

The OWASP Top 10 is a widely recognized list of the most critical web application security risks.

Current major categories (2021 edition):

1. Broken Access Control
2. Cryptographic Failures
3. Injection
4. Insecure Design
5. Security Misconfiguration
6. Vulnerable and Outdated Components
7. Identification and Authentication Failures
8. Software and Data Integrity Failures
9. Security Logging and Monitoring Failures
10. Server-Side Request Forgery (SSRF)

---

# 1. Broken Access Control

## Definition

Occurs when users can access resources or perform actions beyond their permissions.

---

## Common Examples

* Accessing another user’s data
* Admin panel accessible to normal users
* Forced browsing
* IDOR (Insecure Direct Object Reference)

Example:

```http
GET /user/123/profile
```

Attacker changes:

```http
GET /user/124/profile
```

and sees another user’s data.

---

## Impact

* Privilege escalation
* Data leakage
* Account takeover
* Full application compromise

---

## Prevention

* Enforce server-side authorization
* Use role-based access control (RBAC)
* Deny by default
* Validate permissions on every request

---

## Interview Answer

> Broken Access Control happens when authorization checks are improperly implemented, allowing attackers to access unauthorized functionality or data.

---

# 2. Cryptographic Failures

## Definition

Sensitive data is exposed due to weak or incorrect cryptography.

Previously called:

* Sensitive Data Exposure

---

## Common Examples

* HTTP instead of HTTPS
* Weak hashing like MD5/SHA1
* Plaintext passwords
* Weak TLS configuration

---

## Impact

* Password theft
* Credit card leaks
* Session hijacking
* Privacy violations

---

## Prevention

* Use TLS 1.2/1.3
* Encrypt sensitive data
* Use bcrypt/Argon2 for passwords
* Rotate keys securely

---

## Interview Answer

> Cryptographic failures occur when sensitive data is not properly protected through encryption, hashing, or secure transmission mechanisms.

---

# 3. Injection

## Definition

Attacker sends malicious input interpreted as commands or queries.

Most famous:

* SQL Injection

---

## Example

Vulnerable query:

```sql
SELECT * FROM users WHERE username = '$user'
```

Attacker input:

```sql
' OR '1'='1
```

---

## Types

* SQL Injection
* NoSQL Injection
* Command Injection
* LDAP Injection
* XPath Injection

---

## Impact

* Database compromise
* Remote code execution
* Authentication bypass

---

## Prevention

* Parameterized queries
* Prepared statements
* Input validation
* ORM frameworks

---

## Interview Answer

> Injection vulnerabilities occur when untrusted input is interpreted as executable commands or queries by the backend system.

---

# 4. Insecure Design

## Definition

Security weaknesses caused by flawed architecture or missing security controls.

Not just coding mistakes.

---

## Examples

* No rate limiting
* Weak business logic
* Missing fraud protection
* Poor threat modeling

---

## Impact

* System-wide compromise
* Abuse of business workflows
* Logic bypasses

---

## Prevention

* Threat modeling
* Secure SDLC
* Security-by-design
* Abuse case analysis

---

## Interview Answer

> Insecure Design refers to architectural weaknesses where the application lacks proper security controls from the design phase.

---

# 5. Security Misconfiguration

## Definition

Improperly configured servers, frameworks, cloud services, or applications.

---

## Examples

* Default passwords
* Open S3 buckets
* Verbose error messages
* Debug mode enabled
* Unused ports/services

---

## Impact

* Information leakage
* Unauthorized access
* Remote compromise

---

## Prevention

* Harden systems
* Disable unnecessary services
* Secure default configurations
* Automated configuration management

---

## Interview Answer

> Security misconfiguration happens when systems are deployed with insecure settings or unnecessary features enabled.

---

# 6. Vulnerable and Outdated Components

## Definition

Using software with known vulnerabilities.

---

## Examples

* Old libraries
* Unsupported frameworks
* Unpatched servers

Example:

* vulnerable Log4j versions

---

## Impact

* Remote code execution
* Data breaches
* Full server compromise

---

## Prevention

* Patch management
* Dependency scanning
* SBOM tracking
* Remove unused components

---

## Interview Answer

> Applications become vulnerable when they use outdated or unpatched third-party components with known security flaws.

---

# 7. Identification and Authentication Failures

## Definition

Weak authentication/session management mechanisms.

Previously:

* Broken Authentication

---

## Examples

* Weak passwords
* No MFA
* Session fixation
* Predictable session IDs

---

## Impact

* Account takeover
* Credential stuffing success
* Identity compromise

---

## Prevention

* MFA
* Strong password policy
* Secure session management
* Rate limiting

---

## Interview Answer

> Authentication failures occur when identity verification or session handling is improperly implemented.

---

# 8. Software and Data Integrity Failures

## Definition

Trusting software updates, CI/CD pipelines, or serialized data without verification.

---

## Examples

* Unsigned updates
* Insecure deserialization
* Supply-chain attacks

Example:
SolarWinds Supply Chain Attack

---

## Impact

* Remote code execution
* Supply-chain compromise
* System-wide infection

---

## Prevention

* Code signing
* Integrity validation
* Secure CI/CD pipelines
* Verify dependencies

---

## Interview Answer

> Software and Data Integrity Failures occur when applications trust code or data without proper integrity verification.

---

# 9. Security Logging and Monitoring Failures

## Definition

Insufficient logging, alerting, or incident detection.

---

## Examples

* No login monitoring
* Missing audit trails
* Logs not reviewed
* No SIEM integration

---

## Impact

* Delayed breach detection
* Difficult incident response
* Attack persistence

---

## Prevention

* Centralized logging
* SIEM solutions
* Real-time alerts
* Proper audit trails

---

## Interview Answer

> Logging and monitoring failures make it difficult to detect, investigate, and respond to attacks effectively.

---

# 10. Server-Side Request Forgery (SSRF)

## Definition

Server makes attacker-controlled requests to internal or external systems.

---

## Example

Application fetches URLs:

```http
POST /fetch
{
  "url":"http://internal-service/admin"
}
```

Attacker abuses this to access:

* internal APIs
* cloud metadata services
* localhost services

---

## Impact

* Internal network scanning
* Cloud credential theft
* Internal service compromise

---

## Prevention

* URL allowlists
* Block internal IP ranges
* Network segmentation
* Disable unnecessary outbound access

---

## Interview Answer

> SSRF occurs when an attacker tricks the server into making unintended requests to internal or external resources.



