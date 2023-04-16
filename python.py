from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "super_secret_key"

@app.route("/")
def index():
    if "username" in session:
        return redirect("/secret")
    else:
        return redirect("/login")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        # Check if the credentials are valid (you can use any logic you want here)
        if username == "admin" and password == "password":
            session["username"] = username
            return redirect("/secret")
        else:
            error = "Invalid credentials"
            return render_template("login.html", error=error)
    else:
        return render_template("login.html")

@app.route("/secret")
def secret():
    if "username" in session:
        return render_template("secret.html")
    else:
        return redirect("/login")

@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)
