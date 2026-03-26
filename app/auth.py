from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from .models import User
from .extensions import db, bcrypt
from .logger import log_event
from .forms import RegisterForm, LoginForm
import re

auth = Blueprint("auth", __name__)

login_attempts = {}


def is_strong_password(password):
    if (
        len(password) < 8
        or not re.search(r"[A-Z]", password)
        or not re.search(r"[a-z]", password)
        or not re.search(r"[0-9]", password)
        or not re.search(r"[!@#$%^&*]", password)
    ):
        return False
    return True


@auth.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        if not is_strong_password(password):
            log_event(f"Weak password attempt for email: {email}")
            flash("Password must be 8+ chars with upper, lower, number & special char", "danger")
            return redirect(url_for("auth.register"))

        existing_user = User.query.filter(
            (User.email == email) | (User.username == username)
        ).first()

        if existing_user:
            log_event(f"Duplicate registration attempt: username={username}, email={email}")
            flash("Username or email already exists.", "danger")
            return redirect(url_for("auth.register"))

        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
        new_user = User(username=username, email=email, password=hashed_password, role="user")

        db.session.add(new_user)
        db.session.commit()

        log_event(f"New user registered: username={username}, email={email}")
        flash("Registration successful. Please log in.", "success")
        return redirect(url_for("auth.login"))

    return render_template("register.html", form=form)


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        ip = request.remote_addr

        if ip in login_attempts and login_attempts[ip] >= 5:
            log_event(f"Blocked login due to too many failed attempts from IP: {ip}")
            flash("Too many failed attempts. Try again later.", "danger")
            return redirect(url_for("auth.login"))

        user = User.query.filter_by(email=email).first()

        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            login_attempts[ip] = 0
            log_event(f"Login success: email={email}, ip={ip}")
            flash("Login successful.", "success")
            return redirect(url_for("main.dashboard"))
        else:
            login_attempts[ip] = login_attempts.get(ip, 0) + 1
            log_event(f"Failed login: email={email}, ip={ip}, attempts={login_attempts[ip]}")
            flash("Invalid email or password.", "danger")

    return render_template("login.html", form=form)


@auth.route("/logout")
@login_required
def logout():
    log_event("User logged out")
    logout_user()
    flash("Logged out successfully.", "info")
    return redirect(url_for("main.home"))