# VLAN

A Virtual Local Area Network (VLAN) is a logical segmentation of a physical network, allowing multiple isolated networks to exist on the same physical infrastructure. VLANs group devices together based on function, department, or application, regardless of their physical location. They improve network performance by reducing broadcast traffic, enhance security by isolating sensitive systems, and provide flexibility in network design and management. VLANs are configured on network switches using IEEE 802.1Q standard, which adds tags to Ethernet frames to identify VLAN membership. This technology is crucial for efficient network administration in large enterprises, data centers, and complex network environments.

Learn more from the following resources:

- [What is a VLAN?](https://www.solarwinds.com/resources/it-glossary/vlan)
- [VLAN Explained](https://www.youtube.com/watch?v=jC6MJTh9fRE)

# DMZ

A **DMZ**, also known as a **Demilitarized Zone**, is a specific part of a network that functions as a buffer or separation between an organization's internal, trusted network and the external, untrusted networks like the internet. The primary purpose of a DMZ is to isolate critical systems and data from the potentially hostile external environment and provide an extra layer of security.

Learn more from the following resources:

- [What is a DMZ network?](https://www.fortinet.com/resources/cyberglossary/what-is-dmz)
- [DMZ explained](https://www.youtube.com/watch?v=48QZfBeU4ps)

# ARP

Address Resolution Protocol (ARP) is a crucial mechanism used in networking that allows the Internet Protocol (IP) to map an IP address to a corresponding physical address, commonly known as a Media Access Control (MAC) address. This protocol is essential for enabling devices within a Local Area Network (LAN) to communicate by translating IP addresses into specific hardware addresses.

When one device on a LAN wants to communicate with another, it needs to know the MAC address associated with the target device’s IP address. ARP facilitates this by sending out an ARP request, which broadcasts the target IP to all devices in the network. Each device checks the requested IP against its own. The device that recognizes the IP as its own responds with an ARP reply, which includes its MAC address.

Once the requesting device receives the MAC address, it updates its ARP cache—a table that stores IP-to-MAC address mappings—allowing it to send data directly to the correct hardware address.


Learn more from the following resources: 

- [ARP Explained](https://www.youtube.com/watch?v=cn8Zxh9bPio)
- [What is Address Resolution Protocol?](https://www.fortinet.com/resources/cyberglossary/what-is-arp)

# Dynamic Host Configuration Protocol (DHCP)

The Dynamic Host Configuration Protocol (DHCP) is a network management protocol used to automatically assign IP addresses and other network configuration details, such as subnet masks, default gateways, and DNS servers, to devices on a network. When a device, such as a computer or smartphone, connects to a network, it sends a request to the DHCP server, which then dynamically assigns an available IP address from a defined range and provides the necessary configuration information. This process simplifies network management by eliminating the need for manual IP address assignment and reduces the risk of IP conflicts, ensuring that devices can seamlessly join the network and communicate with other devices and services.

Learn more from the following resources:

- [What is DHCP and how does it work?](https://www.youtube.com/watch?v=ldtUSSZJCGg)
- [Dynamic Host Configuration Protocol (DHCP)](https://learn.microsoft.com/en-us/windows-server/networking/technologies/dhcp/dhcp-top)

# Domain Name System (DNS)

The Domain Name System (DNS) is a fundamental protocol of the internet that translates human-readable domain names, like `www.example.com`, into IP addresses, such as `192.0.2.1`, which are used by computers to locate and communicate with each other. Essentially, DNS acts as the internet's phonebook, enabling users to access websites and services without needing to memorize numerical IP addresses. When a user types a domain name into a browser, a DNS query is sent to a DNS server, which then resolves the domain into its corresponding IP address, allowing the browser to connect to the appropriate server. DNS is crucial for the functionality of the internet, as it underpins virtually all online activities by ensuring that requests are routed to the correct destinations.

Learn more from the following resources:

- [DNS Explained in 100 Seconds](https://www.youtube.com/watch?v=UVR9lhUGAyU)
- [What is DNS?](https://www.youtube.com/watch?v=nyH0nYhMW9M)
- [What is DNS?](https://www.cloudflare.com/en-gb/learning/dns/what-is-dns/)

# NAT

**Network Address Translation (NAT)** is a method used to modify IP address information in packet headers while they are in transit across a network. NAT allows multiple devices on a private network to share a single public IP address for accessing external resources, helping conserve the limited number of available public IP addresses. It also enhances security by hiding internal IP addresses from the public internet. Common types of NAT include **Static NAT** (one-to-one mapping), **Dynamic NAT** (many-to-many mapping), and **Port Address Translation (PAT)** or **NAT overload** (many-to-one mapping, commonly used in home routers).

Learn more from the following resources:

- [How NAT Works](https://www.comptia.org/content/guides/what-is-network-address-translation)
- [NAT explained](https://www.youtube.com/watch?v=FTUV0t6JaDA)

# IP

IP, or Internet Protocol, is a fundamental concept in cybersecurity that refers to the way data is transferred across networks, specifically the internet. It is a core component of the internet's architecture and serves as the primary building block for communication between devices connected to the network. An IP address is a unique identifier assigned to each device connected to a network, like a computer or smartphone. It comprises a series of numbers separated by dots (e.g., 192.168.1.1). IP addresses can be either IPv4 (32-bit) or the newer IPv6 (128-bit) format, which provides more available addresses. They allow devices to send and receive data packets to and from other devices on the internet.

Learn more from the following resources:

- [What is an IP address and what does it mean?](https://www.kaspersky.com/resource-center/definitions/what-is-an-ip-address)
- [Whats an IP address?](https://www.youtube.com/watch?v=6is6Gulh7qE)

# Router

A router is a networking device that directs data packets between different networks, ensuring they reach their destination. It operates at the network layer (Layer 3) of the OSI model and forwards data based on the IP addresses of the source and destination. Routers are essential for connecting devices to the internet or linking multiple networks together. They maintain a routing table to decide the best path for data and can dynamically update routes using protocols like RIP, OSPF, or BGP. Routers also handle Network Address Translation (NAT), allowing multiple devices to share a single public IP address. Many modern routers offer Wi-Fi for wireless connectivity and include basic firewall security to protect the network from threats.

Learn more from the following resources:

- [What is a Router](https://www.cloudflare.com/en-gb/learning/network-layer/what-is-a-router/)
- [What is a router and how does it work?](https://www.youtube.com/watch?v=UIJzHLpG9bM)
- [Everything Routers do](https://youtu.be/AzXys5kxpAM?si=nEsCH6jG2Lj6Ua8N)
- [How Routers forward Packets?](https://youtu.be/Ep-x_6kggKA?si=II5xBPoXjYEjLvWX)

# Switch

A switch is a network device that operates at the data link layer (Layer 2) of the OSI model, connecting multiple devices within a local area network (LAN). It uses MAC addresses to forward data packets between devices, creating separate collision domains for each port. Switches improve network efficiency by sending packets only to their intended destinations, reducing unnecessary traffic. They support full-duplex communication, allowing simultaneous data transmission in both directions. Modern switches often include advanced features like VLANs, port mirroring, and Quality of Service (QoS) management. Switches are fundamental to creating efficient, segmented networks and are crucial components in both small office and large enterprise network infrastructures.

Learn more from the following resources:

- [What is a network switch?](https://www.cloudflare.com/en-gb/learning/network-layer/what-is-a-network-switch/)
- [What is a SWITCH?](https://www.youtube.com/watch?v=9eH16Fxeb9o)

# VPN

A Virtual Private Network (VPN) is a secure connection method used to extend private networks across public networks like the Internet. It creates an encrypted tunnel between the user's device and a remote server, masking the user's IP address and encrypting data in transit. VPNs are used for various purposes, including enhancing online privacy, bypassing geographical restrictions, securing communications over public Wi-Fi, and allowing remote access to corporate networks. They employ protocols like OpenVPN, L2TP/IPsec, or WireGuard to ensure data confidentiality and integrity. While VPNs offer significant privacy and security benefits, their effectiveness can vary based on the provider's policies and the specific implementation.

Visit the following resources to learn more:

- [What is a VPN?](https://azure.microsoft.com/en-us/resources/cloud-computing-dictionary/what-is-vpn)
- [VPN (Virtual Private Network) Explained](https://www.youtube.com/watch?v=R-JUOpCgTZc)
- [Virtual Private Networks - Professor Messer](https://www.youtube.com/watch?v=YFyt8aY8PfI)

# NTP

**Network Time Protocol (NTP)** is a protocol used to synchronize the clocks of computers and network devices over a network. It ensures that all systems maintain accurate and consistent time by coordinating with a hierarchy of time sources, such as atomic clocks or GPS, through network communication. NTP operates over UDP port 123 and uses algorithms to account for network delays and adjust for clock drift, providing millisecond-level accuracy. Proper time synchronization is crucial for applications requiring time-sensitive operations, logging events, and maintaining the integrity of security protocols.

Learn more from the following resources:

- [Network Time Protocol (NTP)](https://www.youtube.com/watch?v=BAo5C2qbLq8)
- [What is NTP?](https://www.pubnub.com/learn/glossary/ntp-protocol/)

# IPAM

IP Address Management (IPAM) is a critical aspect of cyber security, as it helps organizations efficiently manage and track their IP addresses, DNS, and DHCP services. In any network, devices like servers, routers, and switches are assigned unique IP addresses, which enables them to communicate with each other. Efficient and secure management of these IP addresses is vital for maintaining network security and prevent unauthorized access.

Learn more from the following resources:

- [What is IPAM?](https://www.infoblox.com/glossary/ipam-ip-address-management/)
- [IP Address Management](https://learn.microsoft.com/en-us/windows-server/networking/technologies/ipam/ipam-top)

# Types of Networks

## MAN

A **Metropolitan Area Network (MAN)** is a type of network that spans a city or large campus, connecting multiple local area networks (LANs) within that geographic area. MANs are designed to provide high-speed data transfer and communication services to organizations, institutions, or businesses across a city. They support a variety of applications, including internet access, intranet connectivity, and data sharing among multiple locations. Typically, MANs are faster and cover a broader area than LANs but are smaller in scope compared to wide area networks (WANs).

Learn more from the following resources:

- [What is a Metropolitan Area Network?](https://www.cloudflare.com/en-gb/learning/network-layer/what-is-a-metropolitan-area-network/)
- [Network Types: MAN](https://youtu.be/4_zSIXb7tLQ?si=1jTQ5C9PT4WUOztP&t=183)

## LAN

A Local Area Network (LAN) is a computer network that interconnects computers and devices within a limited area, such as a home, office, school, or small group of buildings. LANs typically use Ethernet or Wi-Fi technologies to enable high-speed data communication among connected devices. They allow for resource sharing, including files, printers, and internet connections. LANs are characterized by higher data transfer rates, lower latency, and more direct control over network configuration and security compared to wide area networks (WANs). Common LAN applications include file sharing, collaborative work, local hosting of websites or services, and networked gaming. The advent of software-defined networking and cloud technologies has expanded LAN capabilities, enabling more flexible and scalable local network infrastructures.

Learn more from the following resources:

- [What is a LAN?](https://www.cisco.com/c/en_uk/products/switches/what-is-a-lan-local-area-network.html)
- [LAN vs. WAN: What's the Difference?](https://www.youtube.com/watch?v=5OoX_cRLaNM)

## WAN

A Wide Area Network (WAN) is a telecommunications network that extends over a large geographical area, connecting multiple smaller networks like LANs across cities, countries, or continents. WANs use technologies such as leased lines, satellites, cellular networks, or the internet to facilitate long-distance communication. They enable organizations to share data and resources across dispersed locations, supporting remote offices and global operations. WANs typically involve slower transmission speeds compared to LANs due to longer distances and varied connection types. Key considerations for WANs include bandwidth management, security protocols like VPNs, and optimizing performance across diverse network conditions.

Learn more from the following resources:

- [What is a WAN?](https://www.cloudflare.com/en-gb/learning/network-layer/what-is-a-wan/)
- [WAN...it's not the internet!](https://www.youtube.com/watch?v=xPi4uZu4uF0)

## WLAN

A Wireless Local Area Network (WLAN) is a type of computer network that uses wireless data connections to link devices within a limited area. WLANs typically use Wi-Fi technology, allowing devices like laptops, smartphones, and IoT devices to connect to the internet or communicate with each other without physical cable connections. WLANs operate on radio frequencies, usually in the 2.4 GHz or 5 GHz bands, and are set up using wireless routers or access points. They offer flexibility and mobility within the network's range, but require security measures like encryption (e.g., WPA3) to protect against unauthorized access and data interception.

Visit the following resources to learn more:

- [What Is a Wireless LAN?](https://www.cisco.com/c/en/us/products/wireless/wireless-lan.html)
- [Wireless Networking Explained | Cisco CCNA 200-301](https://www.youtube.com/watch?v=Uz-RTurph3c)
- [Wireless Technologies](https://www.youtube.com/watch?v=_VwpcLiBkAQ)
