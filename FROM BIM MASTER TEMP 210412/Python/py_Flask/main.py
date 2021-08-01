from flask import Flask,redirect, url_for, render_template, request, session

app = Flask(__name__)
app.secret_key = "hello"
# @app.route("/")
# def home():
#     return "Hello<h1>HELLO</h1>"

# @app.route("/<name>")
# def user(name):
#     return f"Hello {name}"

# @app.route("/admin")
# def admin():
#     return redirect(url_for("user",name = "Admin !"))

# @app.route("/<name>")
# def home(name):
#     return render_template("index1.html",content = name)
@app.route("/")
def home1():
    return render_template("index.html")
@app.route("/2")
def home2():
    return render_template("index2.html",content = ['Tran','Vo','Phuong','Duy'])    
@app.route("/testBootstrap")
def home3():
    return render_template("index3.html",content = "Testing Content")

@app.route("/login", methods = ['POST','GET'])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user",usr=user))
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

@app.route("/login1", methods = ['POST','GET'])
def login1():
    if request.method == "POST":
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        return render_template("login.html")


@app.route("/user")
def user1():
    if "user" in session:
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))
if __name__ == "__main__":
    app.run(debug=True)