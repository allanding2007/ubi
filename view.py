"""
    File Name: view.py
    Created On: 2017/03/21
"""
from flask import Flask, render_template, make_response, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from template import template_location
from forms.form import LoginForm
from models.model import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost/ubiwifi"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = "ubiwifi belong to winasdaq"
db.init_app(app)
bootstrap = Bootstrap(app)
moment = Moment(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template(template_location['404']), 404


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login/", methods=["GET", "POST"])
def user_login():
    form = LoginForm()
    print form.data
    if form.validate_on_submit():
        user_name = form.name.data
        user = User.query.filter_by(user_name=user_name).first()
        if not user:
            return redirect(url_for('page_not_found'))
        pwd = form.password.data
        if pwd == user.pass_word:
            return redirect(url_for('dashboard'))
        else:
            flash("Invliad username or password!")
    return render_template(template_location['login'], form=form)


@app.route("/user/info/")
def user_info():
    return render_template(template_location['user_info'])


@app.route("/dashboard/")
def dashboard():
    return render_template(template_location['dashboard'])


@app.route("/overview/")
def overview():
    return render_template(template_location['overview'])


@app.route("/assets/devices/")
def devices():
    return render_template(template_location['devices'])


@app.route("/assets/device/edit/")
def edit_device():
    return render_template(template_location['edit_device'])


@app.route("/ssids/ssid/")
def ssid():
    return render_template(template_location['ssid'])


@app.route("/ssids/ssid/edit/")
def edit_ssid():
    return render_template(template_location['edit_ssid'])


@app.route("/statistics/device_statistics/")
def device_statistics():
    return render_template(template_location['device_statistics'])


@app.route("/statistics/device_detail/")
def device_statistic_detail():
    return render_template(template_location['device_statistic_detail'])


if __name__ == "__main__":
    app.run(debug=True)
