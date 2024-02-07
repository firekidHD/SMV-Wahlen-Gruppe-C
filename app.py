from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user data
users = {
    "JohnDoe": {
        "username": "JohnDoe",
        "email": "john@example.com",
        "bio": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio.",
        "skills": ["Python", "Flask", "HTML", "CSS", "JavaScript"]
    },
    # Add more users if needed
}

@app.route("/")
def index():
    return render_template("index.html", user=None)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        if username in users:
            return redirect(url_for('profile', username=username))
    return render_template('login.html')

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/profile/<username>")
def profile(username):
    if username in users:
        return render_template('profile.html', user=users[username])
    else:
        return "User not found."

@app.route("/wahlprozess")
def choose():
        return render_template('choosing.html')
    

if __name__ == "__main__": 
    app.run(debug=True)