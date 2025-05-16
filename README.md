# 📡 WIFI AUDITOR PRO
Script de análisis de redes WiFi: analiza **congestión de canales** y **seguridad de redes inalámbricas** de forma rápida y visual. Compatible con **Linux** y **Windows**.

![Python](https://img.shields.io/badge/Python-3.6%2B-blue?logo=python) ![License](https://img.shields.io/badge/license-MIT-green)

---

## ⚙️ FUNCIONALIDADES

- 🔍 Escaneo de canales WiFi y detección de congestión
- 📊 Gráfico visual con `matplotlib`
- 🛡️ Análisis de protocolos de seguridad (WEP, WPA, WPA2, WPA3)
- 💡 Recomendaciones de canales óptimos
- 🖥️ Compatible con: **Linux** (iwlist) y **Windows** (netsh)

---

## 📥 DESCARGA DEL SCRIPT

### Linux / WSL:

```bash
wget https://raw.githubusercontent.com/TuGeneralYT/wifi_analyzer/main/wifi_analyzer.py
Windows (PowerShell):
powershell
Copiar
Editar
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/TuGeneralYT/wifi_analyzer/main/wifi_analyzer.py" -OutFile "wifi_analyzer.py"
📦 INSTALACIÓN DE DEPENDENCIAS
Linux:
bash
Copiar
Editar
# Requisitos del sistema
sudo apt update
sudo apt install -y python3 python3-pip wireless-tools

# Instalar matplotlib
pip3 install matplotlib
Windows:
Instala Python desde: https://www.python.org/downloads/

Marca la opción "Add Python to PATH" durante la instalación.

Abre CMD o PowerShell como Administrador y ejecuta:

cmd
Copiar
Editar
pip install matplotlib
🚀 EJECUCIÓN
Linux:
bash
Copiar
Editar
sudo python3 wifi_analyzer.py
Windows:
cmd
Copiar
Editar
python wifi_analyzer.py
📝 MENÚ PRINCIPAL
markdown
Copiar
Editar
1. Analizar congestión de canales
2. Evaluar seguridad de redes
3. Recomendación de canal óptimo
4. Salir
📋 ARCHIVO requirements.txt (opcional)
txt
Copiar
Editar
matplotlib
Instalación rápida:

bash
Copiar
Editar
pip install -r requirements.txt
🛡️ LICENCIA
Este proyecto está licenciado bajo la licencia MIT.

📬 CONTACTO
Desarrollado por @TuGeneralYT (Gh0stL1ne)
