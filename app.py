from flask import Flask, render_template
import psutil
import datetime

app = Flask(__name__)

@app.route('/')
def dashboard():
    # Get system metrics
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    uptime = datetime.datetime.now()
    
    return render_template('dashboard.html',
        cpu=cpu,
        memory=memory,
        disk=disk,
        time=uptime
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
