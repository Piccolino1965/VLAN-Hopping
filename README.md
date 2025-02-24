# aiutocomputerhelp-VLAN-Hopping
https://www.aiutocomputerhelp.it/viaggiare-tra-vlan-e-possibile-fare-hop-il-vlan-hopping/

This software is a proof-of-concept (PoC) of a VLAN Hopping attack based on DTP (Dynamic Trunking Protocol). 
Specifically, it attempts to send DTP packets to a Cisco switch to negotiate a trunk connection and potentially gain access to more VLANs than those allowed for a standard user.

What does the code do?
Constructs and sends a DTP (Dynamic Trunking Protocol) packet, a proprietary Cisco protocol used to negotiate the creation of trunks between switches.
Uses the destination MAC address 01:00:0c:cc:cc:cc, which is typical for Cisco protocols.
Embeds an LLC/SNAP header to comply with the DTP packet format.
Includes a raw DTP payload, representing a negotiation request.
Sends the packet on a specific network interface (e.g., eth0), simulating a network device attempting to convince the switch to configure it as a trunk.

⚠️ This software is provided solely for educational and security auditing purposes. It is intended to help network administrators, security professionals, and researchers identify vulnerabilities and improve the security of their own systems.

Unauthorized use of this software on networks or systems without explicit permission from the owner is strictly prohibited. Scanning or probing networks without consent may violate local laws, regulations, and organizational policies. The author and distributor of this software assume no liability for any misuse, legal consequences, or damages resulting from its use.

By using this software, you acknowledge that:

You have obtained explicit authorization to test the target systems.
You take full responsibility for your actions and any consequences arising from them.
You comply with all applicable laws, regulations, and ethical guidelines regarding cybersecurity testing.
If you are unsure about the legality of your actions, do not use this software. Always ensure compliance with ethical hacking standards and responsible disclosure practices.
