# File Transfer Protocol (FTP) vs Secure File Transfer Protol (SFTP)

File Transfer Protocol (FTP) and Secure File Transfer Protocol (SFTP) are both used for transferring files over networks, but they differ significantly in terms of security. FTP is an older protocol that transmits data in plain text, making it vulnerable to interception and unauthorized access. It typically uses separate connections for commands and data transfer, operating on ports 20 and 21. SFTP, on the other hand, is a secure version that runs over the SSH protocol, encrypting both authentication credentials and file transfers. It uses a single connection on port 22, providing better firewall compatibility. SFTP offers stronger authentication methods and integrity checking, making it the preferred choice for secure file transfers in modern networks. While FTP is simpler and may be faster in some scenarios, its lack of built-in encryption makes it unsuitable for transmitting sensitive information, leading many organizations to adopt SFTP or other secure alternatives to protect their data during transit.

Learn more from the following resources:

- [FTP defined and explained](https://www.fortinet.com/resources/cyberglossary/file-transfer-protocol-ftp-meaning)
- [How to use SFTP commands](https://www.youtube.com/watch?v=22lBJIfO9qQ)

# SSL vs TLS

**SSL (Secure Sockets Layer)** is a cryptographic protocol used to secure communications by encrypting data transmitted between clients and servers. SSL establishes a secure connection through a process known as the handshake, during which the client and server agree on cryptographic algorithms, exchange keys, and authenticate the server with a digital certificate. SSL’s security is considered weaker compared to its successor, TLS, due to vulnerabilities in its older encryption methods and lack of modern cryptographic techniques.

**TLS (Transport Layer Security)** improves upon SSL by using stronger encryption algorithms, more secure key exchange mechanisms, and enhanced certificate validation. Like SSL, TLS begins with a handshake where the client and server agree on a protocol version and cipher suite, exchange keys, and verify certificates. However, TLS incorporates additional features like Perfect Forward Secrecy (PFS) and more secure hashing algorithms, making it significantly more secure than SSL for modern communications.

Learn more from the following resources:

- [What’s the Difference Between SSL and TLS?](https://aws.amazon.com/compare/the-difference-between-ssl-and-tls/)
- [TLS vs SSL - What's the Difference?](https://www.youtube.com/watch?v=J7fI_jH7L84)

# IPSec

IPSec, which stands for Internet Protocol Security, is a suite of protocols used to secure Internet communications by encrypting and authenticating IP packets. It is commonly utilized in Virtual Private Networks (VPNs) to ensure that data transmitted over public networks is not accessible to unauthorized individuals. IPSec operates by encrypting data at the source and decrypting it at the destination, maintaining the confidentiality and integrity of the data while in transit. Additionally, it provides authentication, ensuring that the data is being sent and received by the intended parties. This protocol suite is versatile as it can be used with both IPv4 and IPv6 networks, making it a fundamental component for secure online communication.

- [IP Sec VPN Fundamentals](https://www.youtube.com/watch?v=15amNny_kKI)
- [What is IPSec?](https://www.cloudflare.com/en-gb/learning/network-layer/what-is-ipsec/)

# DNS Security Extensions (DNSSEC)

DNS Security Extensions (DNSSEC) is a suite of protocols designed to add a layer of security to the Domain Name System (DNS) by enabling DNS responses to be authenticated. While DNS itself resolves domain names into IP addresses, it does not inherently verify the authenticity of the responses, leaving it vulnerable to attacks like cache poisoning, where an attacker injects malicious data into a DNS resolver’s cache. DNSSEC addresses this by using digital signatures to ensure that the data received is exactly what was intended by the domain owner and has not been tampered with during transit. When a DNS resolver requests information, DNSSEC-enabled servers respond with both the requested data and a corresponding digital signature. The resolver can then verify this signature using a chain of trust, ensuring the integrity and authenticity of the DNS response. By protecting against forged DNS data, DNSSEC plays a critical role in enhancing the security of internet communications.

Learn more from the following resources:

- [How DNSSEC works](https://www.cloudflare.com/en-gb/dns/dnssec/how-dnssec-works/)
- [What is DNSSEC?](https://www.youtube.com/watch?v=Fk2oejzgSVQ)

# Lightweight Directory Access Protocol Secure (LDAPS)

LDAPS (Lightweight Directory Access Protocol Secure) is a secure version of the Lightweight Directory Access Protocol (LDAP), which is used to access and manage directory services over a network. LDAP is commonly employed for user authentication, authorization, and management in environments like Active Directory, where it helps manage access to resources such as applications and systems. LDAPS adds security by encrypting LDAP traffic using SSL/TLS (Secure Sockets Layer/Transport Layer Security) protocols, protecting sensitive information like usernames, passwords, and directory data from being intercepted or tampered with during transmission. This encryption ensures data confidentiality and integrity, making LDAPS a preferred choice for organizations that require secure directory communication.

By using LDAPS, organizations can maintain the benefits of LDAP while ensuring that sensitive directory operations are protected from potential eavesdropping or man-in-the-middle attacks on the network.

Learn more from the following resources:

- [LDAP vs LDAPS - Whats the difference?](https://www.youtube.com/watch?v=J2qtayKzMmA)
- [How to enable LDAPS](https://www.dell.com/support/kbdoc/en-uk/000212661/how-to-enable-secure-lightweight-directory-access-protocol-ldaps-on-an-active-directory-domain-controller)

# SRTP

SRTP (Secure Real-time Transport Protocol) is a security-enhanced version of the Real-time Transport Protocol (RTP) used for voice and video communication over IP networks. It provides encryption, message authentication, and integrity for RTP data in unicast and multicast applications. SRTP is designed to ensure the confidentiality of media streams and protect against eavesdropping, tampering, and replay attacks in Voice over IP (VoIP) and video conferencing systems. It uses AES encryption for confidentiality and HMAC-SHA1 for authentication. SRTP is widely used in secure communication applications, including SIP-based VoIP systems and WebRTC, to protect sensitive audio and video transmissions across potentially untrusted networks.

Learn more from the following resources:

- [SRTP (Secure RTP)](https://developer.mozilla.org/en-US/docs/Glossary/RTP)

# S/MIME

S/MIME (Secure/Multipurpose Internet Mail Extensions) is a protocol for sending digitally signed and encrypted messages. It provides end-to-end encryption and authentication for email communications. S/MIME uses public key cryptography to ensure message confidentiality, integrity, and non-repudiation. It allows users to verify the sender's identity and ensures that the message hasn't been tampered with during transmission. S/MIME is widely supported by major email clients and is commonly used in corporate environments to secure sensitive communications. While it offers strong security, its adoption can be limited by the need for certificate management and the complexity of key exchange processes.

Learn more from the following resources:

- [S/MIME for message signing and encryption in Exchange Online](https://learn.microsoft.com/en-us/exchange/security-and-compliance/smime-exo/smime-exo)
- [S/MIME - Secure MIME protocol - Functions, Services](https://www.youtube.com/watch?v=0hzmoB7yYfw)