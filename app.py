from flask import Flask, render_template
import os
from collections import Counter

app = Flask(__name__)

def read_log():
    if os.path.exists('honeypot.log'):
        with open('honeypot.log', 'r') as log_file:
            log_data = log_file.readlines()
        return log_data
    else:
        return []

def generate_summary(log_data):
    ip_addresses = []
    for line in log_data:
        try:
            parts = line.split(' - ')
            if len(parts) >= 3:
                ip = parts[1].split(':')[0]
                ip_addresses.append(ip)
        except IndexError:
            print(f"Malformed log entry: {line}")
    
    ip_count = Counter(ip_addresses)
    return {
        'total_attacks': len(log_data),
        'unique_ips': len(ip_count),
        'ip_distribution': ip_count.most_common()
    }

@app.route('/')
def start():
    return render_template('start.html')

@app.route('/log')
def index():
    log_data = read_log()
    return render_template('index.html', log_data=log_data)

@app.route('/summary')
def summary():
    log_data = read_log()
    summary = generate_summary(log_data)
    return render_template('summary.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)
