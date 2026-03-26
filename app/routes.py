from flask import Blueprint, render_template, abort
from flask_login import login_required, current_user

main = Blueprint("main", __name__)


@main.route("/")
def home():
    return render_template("index.html")


@main.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", user=current_user)


@main.route("/admin")
@login_required
def admin():
    if current_user.role != "admin":
        abort(403)
    return render_template("admin.html", user=current_user)

from flask import render_template

@main.app_errorhandler(403)
def forbidden(e):
    return render_template("403.html"), 403