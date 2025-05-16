# 📡 WIFI AUDITOR PRO
Script de análisis de redes WiFi: analiza **congestión de canales** y **seguridad de redes inalámbricas** de forma rápida y visual. Compatible con **Linux** y **Windows**.

![banner](https://img.shields.io/badge/Python-3.6%2B-blue?logo=python) ![License](https://img.shields.io/badge/license-MIT-green)

---

## ⚙️ FUNCIONALIDADES

- 🔍 Escaneo de canales WiFi y detección de congestión
- 📊 Gráfico visual con `matplotlib`
- 🛡️ Análisis de protocolos de seguridad (WEP, WPA, WPA2, WPA3)
- 💡 Recomendaciones de canales óptimos
- 🖥️ Compatible con: **Linux** (iwlist) y **Windows** (netsh)

---

## 🚀 INSTALACIÓN Y USO

### 🔧 Requisitos

- Python 3.6 o superior
- `pip` instalado
- Acceso a terminal como administrador o con `sudo`

---

### 🐧 Linux

```bash
# Instala dependencias
sudo apt update
sudo apt install -y python3 python3-pip wireless-tools
pip3 install matplotlib

# Descarga el script
wget https://raw.githubusercontent.com/TuGeneralYT/wifi_analyzer/main/wifi_analyzer.py

# Ejecuta el script con permisos
sudo python3 wifi_analyzer.py


🪟 Windows

# Instala matplotlib
pip install matplotlib

# Descarga el script (desde navegador o con PowerShell)
Invoke-WebRequest -Uri "https://raw.githubusercontent.com/TuGeneralYT/wifi_analyzer/main/wifi_analyzer.py" -OutFile "wifi_analyzer.py"

# Ejecuta en CMD o PowerShell (como administrador)
python wifi_analyzer.py

📝 Menú Principal
markdown
Copiar
Editar
1. Analizar congestión de canales
2. Evaluar seguridad de redes
3. Recomendación de canal óptimo
4. Salir
📦 Archivo requirements.txt (opcional)
txt
Copiar
Editar
matplotlib
Instalación rápida:

bash
Copiar
Editar
pip install -r requirements.txt
🛡️ Licencia
Este proyecto está licenciado bajo la licencia MIT.

📬 Contacto
Desarrollado por @TuGeneralYT (Gh0stL1ne)

