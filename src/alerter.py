import json
import time

class AlertManager:
    def __init__(self):
        pass

    def alert(self, rule, log_line):
        alert_data = {
            "timestamp": time.time(),
            "alert_name": rule.get('name', 'Unknown Alert'),
            "severity": rule.get('severity', 'info'),
            "description": rule.get('description', ''),
            "raw_log": log_line
        }
        
        # Write to JSON file for dashboard
        with open("alerts.json", "a") as f:
            json.dump(alert_data, f)
            f.write("\n")

        # Console output
        print(f"[{alert_data['severity'].upper()}] {alert_data['alert_name']}: {alert_data['raw_log']}")
