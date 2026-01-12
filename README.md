# 🛡️ Mini SOC Tool (Log-Based IDS)

A lightweight **Security Operations Center (SOC) simulation tool** that analyzes logs and detects suspicious activity using rule-based detection.

## 🔍 Features
- Log parsing and analysis
- Rule-based threat detection
- Alert generation in JSON format
- Simulated attack logs for testing
- Beginner-friendly SOC workflow

## 🧱 Project Structure

```text
mini-soc-tool/
├── src/                 # Core detection logic
├── rules/               # Detection rules
├── generate_logs.py     # Fake log generator
├── alerts.json          # Generated alerts
├── test.log             # Sample logs
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation


---

## ⚙️ How It Works

1.⁠ ⁠The tool reads log data from ⁠ test.log ⁠
2.⁠ ⁠Log entries are parsed line-by-line
3.⁠ ⁠Detection rules from the ⁠ rules/ ⁠ directory are applied
4.⁠ ⁠Suspicious activity (failed SSH logins, SQL injection patterns, privilege escalation) is detected
5.⁠ ⁠Alerts are generated and stored in ⁠ alerts.json ⁠

This simulates a *basic SOC alerting pipeline* used in blue-team environments.

---

## ▶️ How To Run

### 1. Install dependencies
```bash
pip install -r requirements.txt

phython genrate_logs.py

---

## ⚠️ Limitations

•⁠  ⁠This is a rule-based intrusion detection system (no machine learning).
•⁠  ⁠Detection is limited to predefined patterns and rules.
•⁠  ⁠Designed for learning and SOC workflow simulation, not production use.

---

## 🚧 Future Improvements

•⁠  ⁠Add real-time log ingestion
•⁠  ⁠Integrate MITRE ATT&CK technique mapping
•⁠  ⁠Add alert severity levels
•⁠  ⁠Export alerts to SIEM tools (ELK / Splunk)
•⁠  ⁠Introduce behavioral or ML-based detection
