from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, DesignerForm
from app.models import Designer
from app import db

@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Max"}
    folds = [
        {
            "designer": "Jason Schneider",
            "design": "Toad",
            "paper_type": "Kami",
            "paper_size": "6x6",
            "date_folded": "3/23/24"
        },
        {
            "designer": "Akira Yoshizawa",
            "design": "Pinwheel",
            "paper_type": "Kami",
            "paper_size": "6x6",
            "date_folded": "3/22/24"
        }
    ]
    return render_template(
        "index.html",
        title="Keep Folding!",
        user=user,
        folds=folds
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login requested for user {}, remember_me={}".format(
              form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template("login.html", title="Sign In", form=form)


@app.route("/add_designer", methods=["GET", "POST"])
def add_designer():
    form = DesignerForm()
    if form.validate_on_submit():
        designer = Designer(first_name=form.first_name.data, last_name=form.last_name.data)
        db.session.add(designer)
        db.session.commit()

        flash("Designer {} added".format(
            form.last_name.data))
        return redirect("/index")
    return render_template(
        "add_designer.html", title="Add Designer", form=form
    )
