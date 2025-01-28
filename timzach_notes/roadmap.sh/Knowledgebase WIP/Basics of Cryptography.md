## Salting

Salting is a crucial concept within the realm of cryptography. It is a technique employed to enhance the security of passwords or equivalent sensitive data by adding an extra layer of protection to safeguard them against hacking attempts, such as brute-force attacks or dictionary attacks.

Learn more from the following resources:

- [What is salting?](https://www.techtarget.com/searchsecurity/definition/salt)
- [Salted Password Scheme](https://www.youtube.com/watch?v=PsIO0gxJF3g)

## Hashing

Hashing is a cryptographic process that converts input data of any size into a fixed-size string of characters, typically a hexadecimal number. This output, called a hash value or digest, is unique to the input data and serves as a digital fingerprint. Unlike encryption, hashing is a one-way process, meaning it's computationally infeasible to reverse the hash to obtain the original data. In cybersecurity, hashing is widely used for password storage, data integrity verification, and digital signatures. Common hashing algorithms include MD5 (now considered insecure), SHA-256, and bcrypt. Hashing helps detect unauthorized changes to data, as even a small alteration in the input produces a significantly different hash value. However, the strength of a hash function is crucial, as weak algorithms can be vulnerable to collision attacks, where different inputs produce the same hash, potentially compromising security measures relying on the uniqueness of hash values.

Learn more from the following resources:

- [Hashing Explained](https://www.youtube.com/watch?v=EOe1XUykdP4)
- [What is hashing and how does it work?](https://www.techtarget.com/searchdatamanagement/definition/hashing)

## Key Exchange

Key exchange is a cryptographic process through which two parties securely share encryption keys over a potentially insecure communication channel. This process is fundamental in establishing a secure communication session, such as in SSL/TLS protocols used for internet security. The most widely known key exchange method is the Diffie-Hellman key exchange, where both parties generate a shared secret key, which can then be used for encrypting subsequent communications. Another common method is the RSA key exchange, which uses public-key cryptography to securely exchange keys. The goal of key exchange is to ensure that only the communicating parties can access the shared key, which is then used to encrypt and decrypt messages, thereby protecting the confidentiality and integrity of the transmitted data.

Learn more from the following resources:

- [Key Exchange](https://nordvpn.com/cybersecurity/glossary/key-exchange/?srsltid=AfmBOoocoykou-7M3OHUQq7APIsGDVjOR8P6wIcIvNA2fgOt1620RZwG)
- [Secret Key Exchange](https://www.youtube.com/watch?v=NmM9HA2MQGI)

## Pvt Key vs Pub Key

**Public keys** and **private keys** are cryptographic components used in asymmetric encryption. 

- **Public Key:** This key is shared openly and used to encrypt data or verify a digital signature. It can be distributed widely and is used by anyone to send encrypted messages to the key owner or to verify their digital signatures.

- **Private Key:** This key is kept secret by the owner and is used to decrypt data encrypted with the corresponding public key or to create a digital signature. It must be protected rigorously to maintain the security of encrypted communications and authentication.

Together, they enable secure communications and authentication, where the public key encrypts or verifies, and the private key decrypts or signs.

Learn more from the following resources:

- [SSH Keys Explained](https://www.sectigo.com/resource-library/what-is-an-ssh-key)
- [Public Key vs Private Key: How are they Different?](https://venafi.com/blog/what-difference-between-public-key-and-private-key/)

## PKI

**Public Key Infrastructure (PKI)** is a framework that manages digital certificates and public-private key pairs, enabling secure communication, authentication, and data encryption over networks. PKI supports various security services such as confidentiality, integrity, and digital signatures. It includes components like **Certificate Authorities (CAs)**, which issue and revoke digital certificates, **Registration Authorities (RAs)**, which verify the identity of certificate requestors, and **certificates** themselves, which bind public keys to individuals or entities. PKI is essential for secure online transactions, encrypted communications, and identity verification in applications like SSL/TLS, email encryption, and code signing.

Learn more from the following resources:

- [What is PKI?](https://cpl.thalesgroup.com/faq/public-key-infrastructure-pki/what-public-key-infrastructure-pki)
- [Design and build a privately hosted Public Key Infrastructure](Design and build a privately hosted Public Key Infrastructure)

## Obfuscation

**Obfuscation** is the practice of deliberately making data, code, or communications difficult to understand or analyze, often to protect intellectual property or enhance security. In software development, obfuscation involves transforming code into a complex or less readable form to hinder reverse engineering or unauthorized access. This technique can include renaming variables and functions to meaningless labels, or altering code structure while preserving functionality. In security contexts, obfuscation can also involve disguising malicious payloads to evade detection by antivirus or security systems.

Learn more from the following resources:

- [How does Obfuscation work?](https://www.hypr.com/security-encyclopedia/obfuscation)
- [Obfuscation - CompTIA Security+](https://www.youtube.com/watch?v=LfuTMzZke4g)
