from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "dOnEr_EiN_eUrO"  
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
    if 'logged_in' in session and session['logged_in']:
        # If user is logged in, redirect to the dashboard
        return redirect(url_for('profile', username=session['username']))
    else:
        # If user is not logged in, render the index page
        return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        if username in users:
            session['logged_in'] = True
            session['username'] = username
            return redirect(url_for('profile', username=username))
    return render_template('login.html')

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/profile/<username>")
def profile(username):
    if 'logged_in' in session and session['logged_in']:
        if username in users:
            return render_template('profile.html', user=users[username])
        else:
            return "User not found."
    else:
        return redirect(url_for('login'))

@app.route("/wahlprozess")
def choose():
        return render_template('choosing.html')
    
@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('index'))


if __name__ == "__main__": 
    app.run(debug=True)