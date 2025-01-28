# Denial of Service (DoS) vs Distributed Denial of Service (DDoS)

Denial of Service (DoS) and Distributed Denial of Service (DDoS) are both types of cyber attacks aimed at disrupting the normal functioning of a targeted service, typically a website or network. A DoS attack involves a single source overwhelming a system with a flood of requests or malicious data, exhausting its resources and making it unavailable to legitimate users. In contrast, a DDoS attack amplifies this disruption by using multiple compromised devices, often forming a botnet, to launch a coordinated attack from numerous sources simultaneously. This distributed nature makes DDoS attacks more challenging to mitigate, as the traffic comes from many different locations, making it harder to identify and block the malicious traffic. Both types of attacks can cause significant downtime, financial loss, and reputational damage to the targeted organization.

Learn more from the following resources:

- [What is Denial-of-Service attack?](https://www.youtube.com/watch?v=Z7xG3b0aL_I)
- [What is a DDoS attack?](https://www.youtube.com/watch?v=z503nLsfe5s)
- [DoS vs DDoS](https://www.fortinet.com/resources/cyberglossary/dos-vs-ddos)

# Man-in-the-middle attack

A Man-in-the-Middle (MITM) attack occurs when a malicious actor intercepts communication between two parties, such as a user and a website, without their knowledge. The attacker can eavesdrop, alter, or inject false information into the communication, often to steal sensitive data like login credentials or manipulate transactions. MITM attacks are commonly executed through compromised Wi-Fi networks or by exploiting security vulnerabilities in protocols.

Visit the following resources to learn more:

- [Wikipedia - Man-in-the-middle attack](https://en.wikipedia.org/wiki/Man-in-the-middle_attack)

# Cross-Site Request Forgery (CSRF)

Cross-Site Request Forgery (CSRF) is a type of web security vulnerability that allows an attacker to trick a user into performing actions on a web application without their consent. It occurs when a malicious website or link causes a user’s browser to send unauthorized requests to a different site where the user is authenticated, such as submitting a form or changing account settings. Since the requests are coming from the user’s authenticated session, the web application mistakenly trusts them, allowing the attacker to perform actions like transferring funds, changing passwords, or altering user data. CSRF attacks exploit the trust that a web application has in the user's browser, making it critical for developers to implement countermeasures like CSRF tokens, same-site cookie attributes, and user confirmation prompts to prevent unauthorized actions.

Learn more from the following resources:

- [Cross-Site Request Forgery Explained](https://www.youtube.com/watch?v=eWEgUcHPle0)
- [Cross-Site Request Forgery](https://owasp.org/www-community/attacks/csrf)

# Spoofing

Spoofing is a form of deception where someone or something pretends to be another person, device, or entity to mislead or gain an advantage. In technology and cybersecurity, it often involves falsifying information like an IP address, email, or website to trick a user or system into believing it’s interacting with a legitimate source. Spoofing can be used to steal sensitive data, gain unauthorized access, or disrupt communication.

Visit the following resources to learn more:

- [Definition and Explanation of Spoofing](https://www.kaspersky.com/resource-center/definitions/spoofing)
- [What is spoofing?](https://www.youtube.com/watch?v=jIS9XUC4TB4)

# What is SQL Injection?

**SQL Injection** is a type of web application security vulnerability that allows an attacker to inject malicious SQL code into a web application's database, potentially leading to unauthorized data access, modification, or deletion.

Visit the following resources to learn more:

- [PortSwigger - SQL Injection](https://portswigger.net/web-security/sql-injection)
- [SQL Injections are scary](https://www.youtube.com/watch?v=2OPVViV-GQk)

# XSS

Cross-Site Scripting (XSS) is a common web application vulnerability where attackers inject malicious scripts into content from trusted websites. These scripts execute in victims' browsers, potentially stealing sensitive data, hijacking user sessions, or defacing websites. XSS attacks come in three main types: stored (persistent), reflected (non-persistent), and DOM-based. Stored XSS permanently embeds malicious code in a server, while reflected XSS occurs when user input is immediately returned by a web application. DOM-based XSS manipulates the Document Object Model in the browser. Prevention strategies include input validation, output encoding, and implementing Content Security Policy headers to mitigate the risk of XSS vulnerabilities.

Visit the following resources to learn more:

- [Cross Site Scripting (XSS) - OWASP](https://owasp.org/www-community/attacks/xss/)
- [Cross Site Scripting Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- [Cross-site Scripting](https://www.youtube.com/watch?v=PKgw0CLZIhE)

# What is Evil Twin attack

An Evil Twin is a type of wireless network attack where an attacker sets up a rogue Wi-Fi access point that mimics a legitimate Wi-Fi network. The rogue access point has the same SSID (network name) as the legitimate network, making it difficult for users to distinguish between the two. The attacker's goal is to trick users into connecting to the rogue access point, allowing them to intercept sensitive information, inject malware, or launch other types of attacks.

Learn more from the following resources:

- [What is an Evil Twin attack?](https://www.techtarget.com/searchsecurity/definition/evil-twin)
- [How Hackers Can Grab Your Passwords Over Wi-Fi with Evil Twin Attacks](https://www.youtube.com/watch?v=HyxQqDq3qs4)

# VLAN Hopping

VLAN hopping is a network attack where an attacker exploits vulnerabilities in the VLAN (Virtual Local Area Network) configuration to gain unauthorized access to traffic on different VLANs. By manipulating VLAN tagging, the attacker can "hop" from one VLAN to another, bypassing network segmentation. This can be achieved using methods like switch spoofing or double tagging, allowing the attacker to intercept, alter, or reroute traffic within a network that was supposed to be isolated.

Visit the following resources to learn more:

- [What is VLAN Hopping?](https://www.packetlabs.net/posts/what-is-vlan-hopping/)
- [VLAN Hopping](https://www.youtube.com/watch?v=pDumMKDK4Wc)

# DNS(Domain Name System) Poisoning/DNS Spoofing/DNS Cache Poisoning

DNS spoofing or DNS cache poisoning, occurs when fake information is inserted into a DNS server’s cache.This causes DNS queries to return incorrect IP addresses, directing users to the wrong websites. Hackers exploit this to reroute traffic to malicious sites. The issue persists until the cached information is corrected.When the cache is poisoned, it misdirects traffic until the incorrect information is fixed. This technique exploits vulnerabilities in the DNS system and can spread to other servers, causing widespread issues.

Visit the following resources to learn more:

- [What is DNS cache poisoning? | DNS spoofing](https://www.cloudflare.com/learning/dns/dns-cache-poisoning/)
- [What Is DNS Poisoning?](https://www.fortinet.com/resources/cyberglossary/dns-poisoning)
- [DNS Spoofing or DNS Cache poisoning](https://www.geeksforgeeks.org/dns-spoofing-or-dns-cache-poisoning/)
- [DNS Poisoning (DNS Spoofing): Definition, Technique & Defense](https://www.okta.com/identity-101/dns-poisoning/)

# Deauth Attack

A Deauthentication (Deauth) Attack is a type of denial-of-service (DoS) attack specific to wireless networks. It involves sending fake deauthentication frames to a Wi-Fi client or access point, forcing the client to disconnect from the network. The attacker uses this technique to disrupt the communication between the client and the access point, often with the intention of capturing data, launching further attacks, or simply causing disruption.

Visit the following resources to learn more:

- [Wi-Fi Deauthentication Attack](https://medium.com/@balaramapunna123/wi-fi-deauthentication-attack-76cdd91d5fc)
- [Deauthentication Attacks](https://www.baeldung.com/cs/deauthentication-attacks)

# Replay Attack

A Replay Attack is a type of network attack where an attacker intercepts and retransmits legitimate communication data, often with the aim of gaining unauthorized access to a system or performing unauthorized actions. In this attack, the attacker captures a valid data transmission and then "replays" it later, without needing to decrypt or alter the data, to trick the recipient into thinking it's a legitimate request.

Visit the following resources to learn more:

- [What Is a Replay Attack?](https://usa.kaspersky.com/resource-center/definitions/replay-attack)

# Rogue Access Point

A Rogue Access Point (Rogue AP) is an unauthorized wireless access point installed on a secure network without the network administrator's knowledge or consent. These devices can be set up by malicious actors to intercept, steal, or manipulate network traffic, or by employees who unintentionally compromise network security by setting up their own wireless access points.

Visit the following resources to learn more:

- [Rogue access points](https://www.khanacademy.org/computing/computers-and-internet/xcae6f4a7ff015e7d:online-data-security/xcae6f4a7ff015e7d:cyber-attacks/a/rogue-access-points-mitm-attacks)

# Buffer Overflow

A Buffer Overflow is a type of vulnerability that occurs when a program or process attempts to write more data to a buffer—a temporary storage area in memory—than it can hold. This overflow can cause the extra data to overwrite adjacent memory locations, potentially leading to unintended behavior, crashes, or security breaches.

Visit the following resources to learn more:

- [What Is Buffer Overflow?](https://www.fortinet.com/resources/cyberglossary/buffer-overflow)
- [Buffer Overflow Attack](https://www.imperva.com/learn/application-security/buffer-overflow/)

# Memory Leak

A Memory Leak occurs when a computer program consumes memory but fails to release it back to the operating system after it is no longer needed. Over time, this can lead to reduced system performance, increased memory usage, and, in severe cases, the program or system may crash due to the exhaustion of available memory.

- [What are memory leaks?](https://learn.snyk.io/lesson/memory-leaks/)
- [What are memory leaks?](https://www.youtube.com/watch?v=00Kdpgl6fsY)

# Pass the Hash

Pass the Hash (PtH) is a hacking technique that allows an attacker to authenticate to a remote server or service using the hashed value of a user's password, without needing to know the actual plaintext password. This method exploits weaknesses in the way some authentication protocols handle hashed credentials, particularly in Windows-based systems.

Visit the following resources to learn more:

- [What is a pass-the-hash attack?](https://www.crowdstrike.com/cybersecurity-101/pass-the-hash/)
- [Pass the Hash Attack](https://www.netwrix.com/pass_the_hash_attack_explained.html)

# Directory Traversal

Directory Traversal, also known as Path Traversal, is a vulnerability that allows attackers to read files on a system without proper authorization. These attacks typically exploit unsecured paths using "../" (dot-dot-slash) sequences and their variations, or absolute file paths. The attack is also referred to as "dot-dot-slash," "directory climbing," or "backtracking."

While Directory Traversal is sometimes combined with other vulnerabilities like Local File Inclusion (LFI) or Remote File Inclusion (RFI), the key difference is that Directory Traversal doesn't execute code, whereas LFI and RFI usually do.

Visit the following resources to learn more:

- [Portswigger's guide on File Path Traversal](https://portswigger.net/web-security/file-path-traversal)
- [OWASP's article on Path Traversal](https://owasp.org/www-community/attacks/Path_Traversal)
- [TryHackMe's room on Path Traversal & File Inclusion](https://tryhackme.com/r/room/filepathtraversal)
- [Acunetix's article on directory traversal](https://www.acunetix.com/websitesecurity/directory-traversal/)
- [HackTheBox Academy's module on File Inclusion & Path Traversal](https://academy.hackthebox.com/course/preview/file-inclusion)
