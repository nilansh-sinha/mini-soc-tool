import argparse
import sys
from src.ingestor import LogIngestor
from src.detector import DetectionEngine
from src.alerter import AlertManager

def main():
    parser = argparse.ArgumentParser(description="Mini SOC Tool - Log-based IDS")
    parser.add_argument("--log-file", required=True, help="Path to the log file to monitor")
    parser.add_argument("--rules", required=True, help="Path to the YAML rules file")
    
    args = parser.parse_args()

    print(f"[*] Starting Mini SOC Tool...")
    print(f"[*] Monitoring: {args.log_file}")
    print(f"[*] Rules: {args.rules}")

    ingestor = LogIngestor(args.log_file)
    detector = DetectionEngine(args.rules)
    alerter = AlertManager()

    try:
        for line in ingestor.follow():
            # Define 'matched_rule' here from detector
            matched_rule = detector.check_rule(line)
            if matched_rule:
                alerter.alert(matched_rule, line)
    except KeyboardInterrupt:
        print("\n[*] Stopping Mini SOC Tool.")
        sys.exit(0)

if __name__ == "__main__":
    main()
