import yaml
import re

class DetectionEngine:
    def __init__(self, rules_file):
        self.rules = self._load_rules(rules_file)

    def _load_rules(self, rules_file):
        with open(rules_file, 'r') as f:
            return yaml.safe_load(f)

    def check_rule(self, line):
        """Checks a log line against all rules. Returns matched rule or None."""
        for rule in self.rules.get('rules', []):
            if 'keywords' in rule:
                if all(keyword in line for keyword in rule['keywords']):
                    return rule
            
            if 'regex' in rule:
                if re.search(rule['regex'], line):
                    return rule
        return None
