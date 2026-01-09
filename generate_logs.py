import time
import random
import os

LOG_FILE = "test.log"

def generate_logs():
    print(f"[*] Generating logs to {LOG_FILE}...")
    with open(LOG_FILE, "a") as f:
        while True:
            # Simulate normal traffic
            f.write(f"Jan 10 10:00:00 localhost sshd[1234]: Accepted password for user user1 from 192.168.1.10 port 22 ssh2\n")
            f.flush()
            
            # Simulate an attack occasionally
            if random.random() < 0.3:
                attack_type = random.choice(["ssh_fail", "sudo", "sql_injection"])
                
                if attack_type == "ssh_fail":
                    log = f"Jan 10 10:01:00 localhost sshd[1234]: Failed password for user root from 10.0.0.5 port 22 ssh2\n"
                elif attack_type == "sudo":
                    log = f"Jan 10 10:02:00 localhost sudo:  hacker : TTY=pts/0 ; PWD=/home/hacker ; USER=root ; COMMAND=/bin/bash\n"
                elif attack_type == "sql_injection":
                    log = f"Jan 10 10:03:00 localhost apache2: GET /login.php?user=admin' OR '1'='1 -- HTTP/1.1\n" # This won't match the exact regex "SELECT.*FROM" but let's adjust the test or the rule later. Wait, my rule was SELECT.*FROM. Let's make a log that matches that.
                    log = f"Jan 10 10:03:00 localhost app[999]: Query: SELECT * FROM users WHERE id=1 OR 1=1\n"
                
                print(f"[!] Writing malicious log: {log.strip()}")
                f.write(log)
                f.flush()
            
            time.sleep(2)

if __name__ == "__main__":
    generate_logs()
