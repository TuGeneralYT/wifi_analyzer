#!/usr/bin/env python3
"""
WIFI AUDITOR PRO - Con análisis de canales y seguridad
Copia TODO este código en un nuevo archivo en VSCode
"""
import os
import sys
import platform
import subprocess
from collections import Counter
import matplotlib.pyplot as plt  # Requiere: pip install matplotlib

def check_os():
    """Detecta el sistema operativo"""
    current_os = platform.system().lower()
    if current_os == 'linux':
        return 'linux'
    elif current_os == 'windows':
        return 'windows'
    else:
        print(f"[!] OS no soportado: {currentos}")
        sys.exit(1)

def install_dependencies():
    """Instala dependencias automáticamente"""
    print("\n[+] Verificando dependencias...")
    try:
        if platform.system() == 'Linux':
            subprocess.run(['sudo', 'apt', 'install', '-y', 'wireless-tools', 'matplotlib'], check=True)
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'matplotlib'], check=True)
    except subprocess.CalledProcessError:
        print("[!] Error al instalar dependencias")

def analyze_channels(os_type):
    """Analiza congestión de canales WiFi"""
    print("\n[+] Analizando congestión de canales...")
    
    channels = []
    if os_type == 'linux':
        scan_result = subprocess.getoutput("sudo iwlist scan 2>/dev/null | grep 'Channel:'")
        channels = [int(line.split(":")[1]) for line in scan_result.splitlines()]
    else:
        scan_result = subprocess.getoutput("netsh wlan show networks mode=Bssid")
        for line in scan_result.splitlines():
            if "Channel" in line:
                channels.append(int(line.split(":")[1].strip()))
    
    if not channels:
        print("[-] No se detectaron redes")
        return

    # Estadísticas de canales
    channel_count = Counter(channels)
    most_common = channel_count.most_common(3)
    
    print("\n📊 ESTADÍSTICAS DE CANALES:")
    print(f"- Total redes analizadas: {len(channels)}")
    print(f"- Canales más congestionados: {', '.join(f'{ch} ({count} redes)' for ch, count in most_common)}")
    
    # Generar gráfico (opcional)
    if input("\n¿Mostrar gráfico de congestión? [s/n]: ").lower() == 's':
        plt.figure(figsize=(10, 5))
        plt.hist(channels, bins=range(1, 14), align='left', rwidth=0.8)
        plt.title('Congestión de Canales WiFi')
        plt.xlabel('Canal')
        plt.ylabel('Número de Redes')
        plt.xticks(range(1, 14))
        plt.grid(axis='y')
        plt.show()

def security_analysis(os_type):
    """Analiza seguridad de redes"""
    print("\n[+] Analizando protocolos de seguridad...")
    
    security_types = []
    if os_type == 'linux':
        scan_result = subprocess.getoutput("sudo iwlist scan 2>/dev/null | grep 'IE:'")
        security_types = [
            "WPA3" if "WPA3" in line else
            "WPA2" if "WPA2" in line else
            "WPA" if "WPA" in line else 
            "WEP" if "WEP" in line else 
            "Abierta"
            for line in scan_result.splitlines()
        ]
    else:
        scan_result = subprocess.getoutput("netsh wlan show networks mode=Bssid")
        for line in scan_result.splitlines():
            if "Autenticación" in line:
                security_types.append(line.split(":")[1].strip())
    
    if not security_types:
        print("[-] No se detectaron redes")
        return
    
    security_count = Counter(security_types)
    
    print("\n🛡️ TIPOS DE SEGURIDAD DETECTADOS:")
    for sec_type, count in security_count.most_common():
        print(f"- {sec_type}: {count} redes")

def main():
    """Función principal"""
    print("""
    ██████╗ ██╗███████╗██╗       █████╗ ██╗   ██████╗ ██████╗ 
    ██╔══██╗██║██╔════╝██║      ██╔══██╗██║   ██╔══██╗██╔══██╗
    ██████╔╝██║█████╗  ██║█████╗███████║██║   ██████╔╝██████╔╝
    ██╔═══╝ ██║██╔══╝  ██║╚════╝██╔══██║██║   ██╔═══╝ ██╔═══╝ 
    ██║     ██║██║     ██║      ██║  ██║██║██╗██║     ██║     
    ╚═╝     ╚═╝╚═╝     ╚═╝      ╚═╝  ╚═╝╚═╝╚═╝╚═╝     ╚═╝     
    """)
    
    current_os = check_os()
    print(f"[*] Sistema detectado: {current_os.upper()}")
    
    install_dependencies()
    
    while True:
        print("\n🔍 MENÚ PRINCIPAL:")
        print("1. Analizar congestión de canales")
        print("2. Evaluar seguridad de redes")
        print("3. Recomendación de canal óptimo")
        print("4. Salir")
        
        choice = input("Seleccione una opción: ")
        
        if choice == '1':
            analyze_channels(current_os)
        elif choice == '2':
            security_analysis(current_os)
        elif choice == '3':
            print("\n📡 CANALES RECOMENDADOS:")
            print("- 2.4 GHz: Usa canales 1, 6 u 11 (no solapados)")
            print("- 5 GHz: Usa canales 36, 40, 44, 48 (menos congestionados)")
            print("\n💡 Consejo: Evita canales con más de 3 redes vecinas")
        elif choice == '4':
            print("\n[+] Sesión finalizada")
            break
        else:
            print("[!] Opción no válida")

if __name__ == "__main__":
    main()