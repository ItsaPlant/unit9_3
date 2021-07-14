from collections import namedtuple
from flask import Flask, request, render_template
from forms import EmailPasswordForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "ni"

###

# User = namedtuple("User", field_names=["username", "password"])
# user = User(username="John", password="black")

# @app.route("/login/", methods=["GET", "POST"])
# def login():
#     form = LoginForm()
#     if request.method == "POST":
#         if (
#             form.username.data == user.username and
#             form.password.data == user.password
#         ):
#             return "Ya're in"
#         else:
#             return "wrong credentials"
#     return render_template("login.html", form=form)

###

User = namedtuple("User", field_names=["email", "password"])
user = User(email="john@black.com", password="black")

@app.route("/login/", methods=["GET", "POST"])
def login():
    form = EmailPasswordForm()
    error=""
    if request.method == "POST":
        if form.validate_on_submit():
            if (
                form.email.data == user.email and
                form.password.data == user.password
            ):
                return "Ya're in"
            else:
                return "wrong credentials"
        else:
            error=form.errors
    return render_template("login.html", form=form, error=error)

###

if __name__ == "__main__":
    app.run(debug=False)

