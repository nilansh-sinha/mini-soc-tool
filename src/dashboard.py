from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)
ALERTS_FILE = "alerts.json"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/alerts')
def get_alerts():
    alerts = []
    if os.path.exists(ALERTS_FILE):
        with open(ALERTS_FILE, 'r') as f:
            for line in f:
                if line.strip():
                    try:
                        alerts.append(json.loads(line))
                    except json.JSONDecodeError:
                        pass
    # Return reversed to show newest first
    return jsonify(list(reversed(alerts)))

if __name__ == "__main__":
    port = 5001 # Run on a different port than default usually to avoid conflicts
    print(f"[*] Starting Dashboard on http://localhost:{port}")
    app.run(debug=True, port=port)
