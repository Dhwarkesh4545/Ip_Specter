# 🔍 IP-SPECTRE // Geolocation Intelligence OSINT Suite

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Status-Active%20Development-green.svg" alt="Status">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
</p>

**IP-SPECTRE** is a lightweight, high-performance command-line OSINT and geolocation intelligence gathering tool built with Python. Designed for rapid infrastructure reconnaissance, it extracts public IPv4/IPv6 telemetry, ASN details, regional data, and automatically generates direct Google Maps investigation links.

---

## 🚀 Features

* **Dual-Stack Support:** Fully parses both IPv4 and IPv6 public target addresses.
* **Rich Terminal UI:** Built using `rich` for clean, high-contrast, professional data presentation.
* **Automated Mapping:** Instantly constructs precise Google Maps search queries based on latitude/longitude coordinates (`loc`).
* **Law Enforcement Context:** Built as part of an investigative suite framework for data triage and reconnaissance workflows.

---

## ⚠️ Legal Disclaimer
*This tool is developed strictly for educational purposes, authorized security assessments, and law enforcement hackathon research. The author is not responsible for any misuse or unauthorized actions conducted using this software.*

---

## 📦 Installation & Setup

Due to modern Kali Linux security policies regarding externally managed environments, it is strongly recommended to install and run this tool inside a Python virtual environment.

### Method 1: Using a Virtual Environment (Recommended)

```bash
# 1. Clone the repository
git clone [https://github.com/Dhwarkesh4545/Ip_Specter.git](https://github.com/Dhwarkesh4545/Ip_Specter.git)
cd Ip_Specter

# 2. Create a virtual environment named 'venv'
python3 -m venv venv

# 3. Activate the virtual environment
source venv/bin/activate

# 4. Install required dependencies inside the environment
pip install -r requirements.txt
