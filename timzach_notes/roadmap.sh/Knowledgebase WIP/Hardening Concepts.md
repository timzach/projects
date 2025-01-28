# MAC-based

**Mandatory Access Control (MAC)** is a security model in which access to resources is governed by predefined policies set by the system or organization, rather than by individual users. In MAC, access decisions are based on security labels or classifications assigned to both users and resources, such as sensitivity levels or clearance levels. Users cannot change these access controls; they are enforced by the system to maintain strict security standards and prevent unauthorized access. MAC is often used in high-security environments, such as government or military systems, to ensure that data and resources are accessed only by individuals with appropriate authorization.

Learn more from the following resources:

- [Mandatory Access Control (MAC) Models](https://www.youtube.com/watch?v=mNN-fEboRAA)
- [What is Mandatory Access Control?](https://nordlayer.com/learn/access-control/mandatory-access-control/)

# NAC-based

Network Access Control (NAC) based hardening is a crucial component in enhancing the security of your network infrastructure. NAC provides organizations with the ability to control and manage access to the network resources, ensuring that only authorized users and devices can connect to the network. It plays a vital role in reducing the attack surface and preventing unauthorized access to sensitive data and resources. By implementing NAC-based hardening in your cybersecurity strategy, you protect your organization from threats and maintain secure access to critical resources.

Learn more from the following resouces:

- [Network Access Control](https://www.youtube.com/watch?v=hXeFJ05J4pQ)
- [What is Network Access Control](https://www.fortinet.com/resources/cyberglossary/what-is-network-access-control)

# Port Blocking

Port blocking is an essential practice in hardening the security of your network and devices. It involves restricting, filtering, or entirely denying access to specific network ports to minimize exposure to potential cyber threats. By limiting access to certain ports, you can effectively safeguard your systems against unauthorized access and reduce the likelihood of security breaches.

Learn more from the following resources:

- [What is port blocking with LAN?](https://www.geeksforgeeks.org/what-is-port-blocking-within-lan/)

# Group Policy

_Group Policy_ is a feature in Windows operating systems that enables administrators to define and manage configurations, settings, and security policies for various aspects of the users and devices in a network. This capability helps you to establish and maintain a consistent and secure environment, which is crucial for organizations of all sizes.

Group Policy works by maintaining a hierarchy of _Group Policy Objects_ (GPOs), which contain multiple policy settings. GPOs can be linked to different levels of the Active Directory (AD) structure, such as domain, site, and organizational unit (OU) levels. By linking GPOs to specific levels, you can create an environment in which different settings are applied to different groups of users and computers, depending on their location in the AD structure.

When a user logs in or a computer starts up, the relevant GPOs from the AD structure get evaluated to determine the final policy settings. GPOs are processed in a specific order — local, site, domain, and OUs, with the latter having the highest priority. This order ensures that you can have a baseline set of policies at the domain level, with more specific policies applied at the OU level, as needed.

Learn more from the following resources:

- [Group Policy overview](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/hh831791(v=ws.11))
- [Learn Windows Group Policy the easy way!](https://www.youtube.com/watch?v=rEhTzP-ScBo)

# Sinkholes

A sinkhole in cybersecurity is a method used to redirect malicious Internet traffic away from its intended destination to a designated server or IP address controlled by a security team or researcher. This technique is often employed to combat botnets, malware, and other cyber threats. By redirecting traffic to a sinkhole, analysts can monitor and analyze malicious activities, prevent further spread of threats, and gather intelligence on attack patterns. Sinkholes are particularly useful in disrupting command and control communications of botnets, effectively neutralizing their ability to receive instructions or exfiltrate data. This approach is a critical tool in large-scale threat mitigation and cyber defense strategies.

Learn more from the following resources:

- [DNS Sinkholes: What is it and how to start using](https://www.threatintelligence.com/blog/dns-sinkhole)

# ACLs

An Access Control List (ACL) is a security mechanism used to define which users or system processes are granted access to objects, such as files, directories, or network resources, and what operations they can perform on those objects. ACLs function by maintaining a list of permissions attached to each object, specifying the access rights of various entities—like users, groups, or network traffic—thereby providing fine-grained control over who can read, write, execute, or modify the resources. This method is essential in enforcing security policies, reducing unauthorized access, and ensuring that only legitimate users can interact with sensitive data or systems.

Learn more from the following resources:

- [Access Control List: Definition, Types & Usages](https://www.okta.com/uk/identity-101/access-control-list/)
- [Access Control Lists](https://www.youtube.com/watch?v=IwLyr0mKK1w)

# Patching

**Patching** refers to the process of updating software or systems with fixes or improvements to address security vulnerabilities, bugs, or performance issues. This involves applying patches—small pieces of code provided by software vendors or developers—to close security gaps, resolve operational problems, and enhance functionality. Regular patching is crucial for maintaining system security and stability, protecting against exploits, and ensuring that systems remain compliant with security standards and best practices.

Learn more from the following resources:

- [What is Patch Management?](https://www.ibm.com/topics/patch-management)
- [What Is Patch Management, and Why Does Your Company Need It?](https://www.youtube.com/watch?v=O5XXlJear0w)

# Jump Server

A **jump server**, also known as a **bastion host** or **jump host**, is a critical security component in many network architectures. It is a dedicated, locked-down, and secure server that sits within a protected network, and provides a controlled access point for users and administrators to access specific components within the system. This intermediate server acts as a bridge between untrusted networks and the internal privileged systems, thereby reducing the attack surface and securing the environment.

Learn more from the following resources:

- [What is a jump server?](https://www.ssh.com/academy/iam/jump-server)
- [What is a bastion host and why is it so important?](https://www.youtube.com/watch?v=pI6glWVEkcY)

# Endpoint Security

Endpoint security focuses on protecting individual devices that connect to a network, such as computers, smartphones, tablets, and IoT devices. It's a critical component of modern cybersecurity strategy, as endpoints often serve as entry points for cyberattacks. This approach involves deploying and managing security software on each device, including antivirus programs, firewalls, and intrusion detection systems. Advanced endpoint protection solutions may incorporate machine learning and behavioral analysis to detect and respond to novel threats. Endpoint security also encompasses patch management, device encryption, and access controls to mitigate risks associated with lost or stolen devices. As remote work and bring-your-own-device (BYOD) policies become more prevalent, endpoint security has evolved to include cloud-based management and zero-trust architectures, ensuring that security extends beyond the traditional network perimeter to protect data and systems regardless of device location or ownership.

Learn more from the following resources:

- [What is Endpoint Security?](https://www.crowdstrike.com/cybersecurity-101/endpoint-security/)
- [Endpoints are the IT frontdoor - Gaurd them!](https://www.youtube.com/watch?v=Njqid_JpqTs)
