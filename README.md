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
