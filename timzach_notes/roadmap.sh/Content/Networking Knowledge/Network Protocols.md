# SSH

SSH (Secure Shell) is a cryptographic network protocol used for secure remote login and other secure network services over an unsecured network. It provides a secure channel over an unsecured network by using strong encryption to protect the connection against eavesdropping, tampering, and man-in-the-middle attacks. SSH is commonly used for remote command-line login, remote command execution, and secure file transfers. It typically runs on TCP port 22 and replaces older, less secure protocols like Telnet. SSH uses public-key cryptography for authentication and supports various authentication methods, including passwords and key-based authentication. It's a fundamental tool for system administrators, developers, and anyone requiring secure remote access to systems.

Learn more from the following resources:

- [What is SSH? | Secure Shell (SSH) protocol](https://www.cloudflare.com/en-gb/learning/access-management/what-is-ssh/)
- [How does SSH work](https://www.youtube.com/watch?v=5JvLV2-ngCI)

# RDP

**Remote Desktop Protocol (RDP)** is a Microsoft-developed protocol that enables users to remotely access and control a computer over a network. It allows users to interact with a remote desktop environment as if they were sitting in front of the computer, providing access to applications, files, and network resources. RDP is commonly used for remote administration, technical support, and remote work. It operates over TCP port 3389 and supports encryption for secure data transmission, though proper security measures, like strong passwords and multi-factor authentication, are essential to prevent unauthorized access.

Learn more from the following resources:

- [What is RDP and how to use it?](https://www.youtube.com/watch?v=flPnBSz-lqw)
- [What is the Remote Desktop Protocol (RDP)?](https://www.cloudflare.com/en-gb/learning/access-management/what-is-the-remote-desktop-protocol/)

# File Transfer Protocol (FTP)

FTP is a standard network protocol used to transfer files from one host to another host over a TCP-based network, such as the Internet. Originally developed in the 1970s, it's one of the earliest protocols for transferring files between computers and remains widely used today.

FTP operates on a client-server model, where one computer acts as the client (the sender or requester) and the other acts as the server (the receiver or provider). The client initiates a connection to the server, usually by providing a username and password for authentication, and then requests a file transfer.

Learn more from the following resources:

- [What is FTP?](https://www.youtube.com/watch?v=HI0Oh4NJqcI)
- [FTP meaning and uses](https://www.investopedia.com/terms/f/ftp-file-transfer-protocol.asp)

# SFTP

SFTP (SSH File Transfer Protocol) is a secure file transfer protocol that provides file access, transfer, and management over a reliable data stream. It runs over the SSH protocol, typically on port 22, ensuring encrypted file transfers. SFTP offers stronger security than traditional FTP by encrypting both commands and data in transit, preventing unauthorized interception. It supports features like resuming interrupted transfers, directory listings, and remote file system operations. SFTP is widely used for secure file transfers in various environments, from web hosting to enterprise data management, offering a more secure alternative to FTP while maintaining similar functionality. Its integration with SSH makes it a preferred choice for secure, authenticated file transfers in many network configurations.

Learn more from the following resources:

- [What is SFTP?](https://www.precisely.com/glossary/sftp)
- [How to use SFTP Commands to Copy Files to/from a Server](https://www.youtube.com/watch?v=22lBJIfO9qQ&t=4s)

# HTTP / HTTPS

HTTP (Hypertext Transfer Protocol) and HTTPS (HTTP Secure) are fundamental protocols for web communication. HTTP is the foundation for data exchange on the World Wide Web, allowing browsers to request resources from web servers. However, HTTP transmits data in plain text, making it vulnerable to eavesdropping and man-in-the-middle attacks. HTTPS addresses these security concerns by adding a layer of encryption using SSL/TLS (Secure Sockets Layer/Transport Layer Security). This encryption protects the confidentiality and integrity of data in transit, securing sensitive information such as login credentials and financial transactions. HTTPS also provides authentication, ensuring that users are communicating with the intended website. In recent years, there has been a significant push towards HTTPS adoption across the web, with major browsers marking HTTP sites as "not secure." This shift has greatly enhanced overall web security, though it's important to note that HTTPS secures the connection, not necessarily the content of the website itself.

Learn more from the following resources:

- [An overview of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
- [What is HTTPS?](https://www.cloudflare.com/en-gb/learning/ssl/what-is-https/)

# SSL / TLS

Secure Sockets Layer (SSL) and Transport Layer Security (TLS) are cryptographic protocols used to provide security in internet communications. These protocols encrypt the data that is transmitted over the web, so anyone who tries to intercept packets will not be able to interpret the data. One difference that is important to know is that SSL is now deprecated due to security flaws, and most modern web browsers no longer support it. But TLS is still secure and widely supported, so preferably use TLS.

Learn more from the following resources:

- [What is SSL? | SSL definition](https://www.cloudflare.com/en-gb/learning/ssl/what-is-ssl/)
- [TLS Basics](https://www.internetsociety.org/deploy360/tls/basics/)
- [TLS vs SSL - What's the Difference?](https://www.youtube.com/watch?v=J7fI_jH7L84)

