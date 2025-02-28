# aiutocomputerhelp-VLAN-Hopping
https://www.aiutocomputerhelp.it/viaggiare-tra-vlan-e-possibile-fare-hop-il-vlan-hopping/
This software is a Proof-of-Concept (PoC) for a VLAN Hopping attack exploiting DTP (Dynamic Trunking Protocol). It demonstrates how an attacker can craft and send malicious DTP frames to negotiate a switch port into trunk mode, potentially gaining access to multiple VLANs.

# How It Works

Frame Construction: The script generates an Ethernet frame with an LLC/SNAP encapsulation to simulate a DTP message. The destination MAC (01:00:0c:cc:cc:cc) is typical for Cisco proprietary protocols, ensuring the frame is recognized by vulnerable switches.
DTP Packet Crafting:
An Ethernet header is created, using an attacker-controlled source MAC (12:34:56:78:9a:bc).
A LLC/SNAP header is added, identifying the packet as a Cisco DTP message (OUI=0x00000c, protocol=0x2004).
A basic DTP payload is included (though a real attack would require full DTP TLV formatting).
Packet Transmission: The crafted DTP frame is continuously sent via the attacker's network interface (eth0), attempting to persuade the switch to enable trunking on the attacker's port.

Potential Impact: If successful, the attacker’s port becomes a trunk port, allowing it to access all VLANs on the switch, effectively bypassing VLAN security.

Purpose
This PoC highlights the dangers of misconfigured or insecure DTP settings on network switches. It underscores the need for security best practices such as:

Disabling DTP on access ports (switchport mode access & switchport nonegotiate on Cisco devices).
Explicitly defining trunk and access ports instead of relying on DTP auto-negotiation.
Using VLAN access controls to prevent unauthorized cross-VLAN traffic.
By leveraging Scapy, this script provides a valuable tool for network security analysis and testing, demonstrating how VLAN hopping attacks can be executed and mitigated.

⚠️ This software is provided solely for educational and security auditing purposes. It is intended to help network administrators, security professionals, and researchers identify vulnerabilities and improve the security of their own systems.

Unauthorized use of this software on networks or systems without explicit permission from the owner is strictly prohibited. Scanning or probing networks without consent may violate local laws, regulations, and organizational policies. The author and distributor of this software assume no liability for any misuse, legal consequences, or damages resulting from its use.

By using this software, you acknowledge that:

You have obtained explicit authorization to test the target systems.
You take full responsibility for your actions and any consequences arising from them.
You comply with all applicable laws, regulations, and ethical guidelines regarding cybersecurity testing.
If you are unsure about the legality of your actions, do not use this software. Always ensure compliance with ethical hacking standards and responsible disclosure practices.
