# Basics of Subnetting

Subnetting is a technique used in computer networking to divide a large network into smaller, more manageable sub-networks, or "subnets." It enhances network performance and security by reducing broadcast traffic and enabling better control over IP address allocation. Each subnet has its own range of IP addresses, which allows network administrators to optimize network traffic and reduce congestion by isolating different sections of a network. In subnetting, an IP address is split into two parts: the network portion and the host portion. The network portion identifies the overall network, while the host portion identifies individual devices within that network. Subnet masks are used to define how much of the IP address belongs to the network and how much is reserved for hosts. By adjusting the subnet mask, administrators can create multiple subnets from a single network, with each subnet having a limited number of devices. Subnetting is particularly useful for large organizations, allowing them to efficiently manage IP addresses, improve security by segmenting different parts of the network, and control traffic flow by minimizing unnecessary data transmissions between segments.

Learn more from the following resources:

- [Networking Basics: What is IPv4 Subnetting?](https://www.cbtnuggets.com/blog/technology/networking/networking-basics-what-is-ipv4-subnetting)
- [Subnetting](https://www.youtube.com/playlist?list=PLIhvC56v63IKrRHh3gvZZBAGvsvOhwrRF)

# Public vs Private IP Addresses

Public addresses are IP addresses assigned to devices directly accessible over the internet, allowing them to communicate with external networks and services. In contrast, private addresses are used within local networks and are not routable over the internet, providing a way for devices within a private network to communicate with each other while conserving public IP address space. Public addresses are unique across the internet, whereas private addresses are reused across different local networks and are typically managed by network address translation (NAT) to interface with public networks.

Learn more from the following resources:

- [Public vs Private IP Addresses](https://www.avast.com/c-ip-address-public-vs-private)
- [What is the difference between public and private ip?](https://www.youtube.com/watch?v=R6Czae6Iow4&t=1s)

# localhost

**Localhost** refers to the standard hostname used to access the local computer on which a network service or application is running. It resolves to the loopback IP address `127.0.0.1` for IPv4 or `::1` for IPv6. When you connect to `localhost`, you're effectively communicating with your own machine, allowing you to test and debug network services or applications locally without accessing external networks.

Learn more from the following resources:

- [What is localhost?](https://www.freecodecamp.org/news/what-is-localhost/)
- [What is localhost? | Explained](https://www.youtube.com/watch?v=m98GX51T5dI)

# loopback

**Loopback** refers to a special network interface used to send traffic back to the same device for testing and diagnostic purposes. The loopback address for IPv4 is `127.0.0.1`, while for IPv6 it is `::1`. When a device sends a request to the loopback address, the network data does not leave the local machine; instead, it is processed internally, allowing developers to test applications or network services without requiring external network access. Loopback is commonly used to simulate network traffic, check local services, or debug issues locally.

Learn more from the following resources:

- [What is a loopback address?](https://www.geeksforgeeks.org/what-is-a-loopback-address/)
- [Understanding the loopback address and loopback interfaces](https://study-ccna.com/loopback-interface-loopback-address/)

# CIDR

CIDR, or Classless Inter-Domain Routing, is a method of allocating IP addresses and routing Internet Protocol packets in a more flexible and efficient way, compared to the older method of Classful IP addressing. Developed in the early 1990s, CIDR helps to slow down the depletion of IPv4 addresses and reduce the size of routing tables, resulting in better performance and scalability of the Internet.

CIDR achieves its goals by replacing the traditional Class A, B, and C addressing schemes with a system that allows for variable-length subnet masking (VLSM). In CIDR, an IP address and its subnet mask are written together as a single entity, referred to as a _CIDR notation_.

A CIDR notation looks like this: `192.168.1.0/24`. Here, `192.168.1.0` is the IP address, and `/24` represents the subnet mask. The number after the slash (/) is called the _prefix length_, which indicates how many bits of the subnet mask should be set to 1 (bitmask). The remaining bits of the subnet mask are set to 0.

Learn more from the following resources:

- [What is CIDR?](https://aws.amazon.com/what-is/cidr/)
- [What is Network CIDR Notation?](https://www.youtube.com/watch?v=tpa9QSiiiUo)

# subnet mask

A subnet mask is a 32-bit number used in IP networking to divide an IP address into network and host portions. It determines which part of an IP address refers to the network and which part refers to the host. Subnet masks enable network administrators to create subnetworks, improving network efficiency and security by controlling traffic flow between subnets. Common subnet masks include 255.255.255.0 (for a /24 network) and 255.255.0.0 (for a /16 network). Subnetting helps in efficient IP address allocation, reduces broadcast traffic, and enhances network performance. Understanding subnet masks is crucial for network configuration, troubleshooting, and implementing effective network segmentation strategies.

Learn more from the following resources:

- [What Is a Subnet Mask?](https://www.spiceworks.com/tech/networking/articles/what-is-subnet-mask/)
- [What is a subnet mask?](https://www.youtube.com/watch?v=s_Ntt6eTn94)

# default gateway

A default gateway is a network node, typically a router or a firewall, that serves as the access point or intermediary between a local network and external networks, such as the internet. When a device on a local network needs to communicate with a device outside its own subnet—such as accessing a website or sending an email—it sends the data to the default gateway, which then routes it to the appropriate external destination. The default gateway acts as a traffic director, ensuring that data packets are correctly forwarded between the internal network and external networks, making it a crucial component for enabling communication beyond the local network's boundaries.

Learn more from the following resources:

- [What is a default gateway?](https://nordvpn.com/blog/what-is-a-default-gateway/?srsltid=AfmBOoosi5g4acnT9Gv_B86FMGr72hWDhk8J-4jr1HvxPCSu96FikCyw)
- [Routers and Default Gateways](https://www.youtube.com/watch?v=JOomC1wFrbU)
