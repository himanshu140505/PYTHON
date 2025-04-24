from flask import Flask, request, render_template_string, redirect, send_from_directory
import sqlite3, os, subprocess
import uuid

app = Flask(__name__)
UPLOAD_FOLDER = './uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# --- Initial Setup ---
def init_db():
    conn = sqlite3.connect("vulnsite.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS comments (id INTEGER PRIMARY KEY, user TEXT, content TEXT)")
    c.execute("INSERT INTO users (username, password) VALUES ('admin', 'admin')")  # default login
    conn.commit()
    conn.close()

init_db()

# --- Routes ---

@app.route('/')
def home():
    return '''
        <h1>Welcome to VulnApp</h1>
        <ul>
            <li><a href="/login">Login</a></li>
            <li><a href="/comment">Leave a Comment (Stored XSS)</a></li>
            <li><a href="/upload">Upload a File</a></li>
            <li><a href="/ping">Ping Command (CMDi)</a></li>
            <li><a href="/redirect?url=https://google.com">Open Redirect</a></li>
            <li><a href="/idor?id=1">View User Info (IDOR)</a></li>
        </ul>
    '''

# SQL Injection Login Page
@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ""
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        # 🔥 SQLi vulnerable query
        conn = sqlite3.connect("vulnsite.db")
        c = conn.cursor()
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        c.execute(query)
        result = c.fetchone()
        if result:
            return f"<h2>Welcome {username}!</h2><a href='/'>Back</a>"
        else:
            msg = "Login failed."
    return f'''
        <h2>Login</h2>
        <form method="POST">
            Username: <input name="username"><br>
            Password: <input name="password"><br>
            <input type="submit">
        </form>
        <p>{msg}</p>
    '''

# Stored XSS Comment System
@app.route('/comment', methods=['GET', 'POST'])
def comment():
    if request.method == "POST":
        user = request.form['user']
        content = request.form['content']
        conn = sqlite3.connect("vulnsite.db")
        c = conn.cursor()
        # ⚠️ Fix SQL syntax error while still allowing XSS
        c.execute("INSERT INTO comments (user, content) VALUES (?, ?)", (user, content))
        conn.commit()
    conn = sqlite3.connect("vulnsite.db")
    c = conn.cursor()
    c.execute("SELECT * FROM comments")
    comments = c.fetchall()
    comment_list = "".join([f"<p><b>{u}:</b> {c}</p>" for _, u, c in comments])
    return f'''
        <h2>Leave a Comment</h2>
        <form method="POST">
            Name: <input name="user"><br>
            Comment: <textarea name="content"></textarea><br>
            <input type="submit">
        </form>
        <hr>
        <h3>Comments:</h3>
        {comment_list}
    '''

# File Upload Vulnerability
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == "POST":
        f = request.files['file']
        f.save(os.path.join(UPLOAD_FOLDER, f.filename))
        return f"Uploaded {f.filename} successfully! <a href='/uploads/{f.filename}'>View file</a>"
    return '''
        <h2>Upload a File</h2>
        <form method="POST" enctype="multipart/form-data">
            File: <input type="file" name="file"><br>
            <input type="submit">
        </form>
    '''

# Serve uploaded files
@app.route('/uploads/<path:filename>')
def uploaded_file(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

# Command Injection (Ping a Host)
@app.route('/ping', methods=['GET', 'POST'])
def ping():
    output = ""
    if request.method == "POST":
        host = request.form['host']
        # ⚠️ CMD injection vulnerable
        cmd = f"ping -c 1 {host}" if os.name != 'nt' else f"ping {host}"
        try:
            output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, text=True)
        except subprocess.CalledProcessError as e:
            output = e.output
    return f'''
        <h2>Ping a Host</h2>
        <form method="POST">
            Host: <input name="host"><br>
            <input type="submit">
        </form>
        <pre>{output}</pre>
    '''

# Open Redirect (redirect to a specified URL)
@app.route('/redirect')
def open_redirect():
    url = request.args.get("url", "/")
    return redirect(url)

# Insecure Direct Object Reference (IDOR)
@app.route('/idor')
def idor():
    # Simulating an IDOR vulnerable endpoint
    userid = request.args.get("id", "1")
    conn = sqlite3.connect("vulnsite.db")
    c = conn.cursor()
    c.execute(f"SELECT * FROM users WHERE id = {userid}")
    user = c.fetchone()
    if user:
        return f"<h3>User Info:</h3><p>ID: {user[0]}<br>Username: {user[1]}</p>"
    return "User not found."

# --- Run the App ---
if __name__ == '__main__':
    app.run(debug=True)
