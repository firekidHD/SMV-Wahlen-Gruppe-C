from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "dOnEr_EiN_eUrO"

# Dummy user data
database = {'zaricj': '12345',
            'lohwasserd': '123', 
            'kloßm': '123'}

@app.route("/")
def index():
    if "logged_in" in session and session["logged_in"]:
        # If user is logged in, redirect to the dashboard
        return redirect(url_for("home"))
    else:
        # If user is not logged in, render the index page
        return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        if username not in database:
            return render_template("login.html", info="Invalid User!")
        else:
            if database[username] != password:
                return render_template('login.html', info='Invalid Password!')
            else:
                session["logged_in"] = True
                session["username"] = username
                return redirect(url_for("home"))
        
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/home")
def home():
    if "logged_in" in session and session["logged_in"]:
        username = session["username"]
        return render_template("home.html", name=username)
    else:
        return redirect(url_for("login"))
    
@app.route("/wahlprozess")
def wahlprozess():
    return render_template("wahlprozess.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

if __name__ == "__main__": 
    app.run(debug=True)
