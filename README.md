# 🔐 ReachMCP — CVE Reachability Analysis & VEX Report Generator

ReachMCP is a server and UI tool that performs **CVE-based reachability analysis** on source code and generates a **VEX (Vulnerability Exploitability eXchange)** report.

---

## 🚀 Features

- **SBOM + CVE Analysis** using CVE ID, package, and version
-  **Reachability Check** (mock or static analysis plugin support)
- **VEX Report** Generation in CycloneDX-compatible format
- **Streamlit UI** for interactive CVE submissions and results

---

## Requirements

    Python 3.8+

## Install Dependencies
    pip install -r requirements.txt

## Running the Project

1. Start the MCP Server
        
        uvicorn app.main:app --reload

2. Launch the Streamlit UI
    
        streamlit run reachmcp_ui.py

## Visit
MCP API: http://localhost:8000/docs

UI: http://localhost:8501
