# -*- coding: utf-8 -*-
"""
    File Name: view.py
    Created On: 2017/03/21
"""
from flask import Flask, render_template, make_response, redirect, url_for, flash, abort
from flask import jsonify
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from flask_moment import Moment
from template import template_location
from forms.form import LoginForm, DeviceForm, SsidForm, ProfileForm
from models.model import db, User, Device, SSidConfig, UsageRecord
from settings import app_config


bootstrap = Bootstrap()
moment = Moment()
login_manager = LoginManager()
login_manager.session_protection = "strong"


def create_app(app_config):
    app = Flask(__name__)
    app.config.from_object(app_config['develop'])
    db.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)
    login_manager.init_app(app)
    return app


app = create_app(app_config)


@app.errorhandler(404)
def page_not_found(e):
    return render_template(template_location['404']), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template(template_location['500']), 500


def get_or_404(model, indent):
    obj = model.query.get(indent)
    if not obj:
        abort(404)
    return obj


@login_manager.user_loader
def load_user(user_id):
    return get_or_404(User, int(user_id))


@app.route("/")
@login_required
def index():
    return render_template("index.html")


@app.route("/auth/login/", methods=["GET", "POST"])
def user_login():
    form = LoginForm()
    print form.data
    if form.validate_on_submit():
        user_name = form.name.data
        user = User.query.filter_by(user_name=user_name).first()
        pwd = form.password.data
        if user and user.verify_password(pwd):
            login_user(user, form.remember_me)
            return redirect(url_for('dashboard'))
        else:
            flash("Invliad username or password!")
    return render_template(template_location['login'], form=form)


@app.route("/auth/logout/")
@login_required
def user_logout():
    logout_user()
    flash("You had been logged out!")
    return redirect(url_for("user_login"))


@app.route("/user/profile/")
@login_required
def profile():
    user = current_user
    form = ProfileForm(user_name=user.user_name, email=user.email, join_date=user.join_date)
    print form.data
    return render_template(template_location['profile'], form=form)


@app.route("/dashboard/")
@login_required
def dashboard():
    return render_template(template_location['dashboard'])


@app.route("/overview/")
@login_required
def overview():
    return render_template(template_location['overview'])


@app.route("/assets/devices/")
@login_required
def devices():
    return render_template(template_location['devices'])


@app.route("/assets/device/edit/<int:id>", methods=["GET", "POST"])
@login_required
def edit_device(id):
    device = Device.query.filter_by(id=id).first()
    if not device:
        abort(404)
    form = DeviceForm(mac_address=device.mac_address, manufacturer=device.manufacturer,
                      is_activated=device.is_activated, join_date=device.join_date,
                      description=device.description)

    print form.data
    if form.validate_on_submit():
        device.mac_address = form.mac_address.data
        device.manufacturer = form.manufacturer.data
        device.is_activated = form.is_activated.data
        device.join_date = form.join_date.data
        device.description = form.description.data
        try:
            db.session.commit()
            print "updating device: {0}".format(device.mac_address)
        except Exception as e:
            print "Error: {0}".format(e)
    return render_template(template_location['edit_device'], form=form)


@app.route("/ssids/ssid/")
@login_required
def ssid():
    return render_template(template_location['ssid'])


@app.route("/ssids/ssid/edit/<int:id>", methods=["GET", "POST"])
@login_required
def edit_ssid(id):
    ssid = SSidConfig.query.filter_by(id=id).first()
    form = SsidForm(name=ssid.name, pass_word=ssid.pass_word, is_activated=ssid.is_activated)
    print form.data
    if form.validate_on_submit():
        ssid.name = form.name.data
        ssid.pass_word = form.pass_word.data
        ssid.is_activated = form.is_activated.data
        try:
            db.session.commit()
            print "Updating ssid: {0}".format(ssid.name)
        except Exception as e:
            print "Update ssid error: {0}".format(e)
    return render_template(template_location['edit_ssid'], ssid=ssid, form=form)


@app.route("/statistics/device_statistics/")
@login_required
def device_statistics():
    return render_template(template_location['device_statistics'])


@app.route("/statistics/device_detail/<int:device_id>")
@login_required
def device_statistic_detail(device_id):
    return render_template(template_location['device_statistic_detail'], device_id=device_id)


@app.route("/assets/devices/ajax/")
@login_required
def devices_ajax():
    devices = Device.query.all()
    return jsonify(map(lambda device: device.to_json(), devices))


@app.route("/ssids/ajax/")
@login_required
def ssids_ajax():
    ssids = SSidConfig.query.all()
    return jsonify(map(lambda ssid: ssid.to_json(), ssids))


@app.route("/statistics/devices/ajax/")
@login_required
def device_statistics_ajax():
    devices = UsageRecord.query.all()
    result = db.session.query(UsageRecord.device_id, db.func.count(UsageRecord.id),
                              db.func.sum(UsageRecord.data_usage)).group_by(UsageRecord.device_id).all()
    try:
        data = {
            "data": map(lambda r: {"device_id": r[0],
                                   "count": r[1],
                                   "usage": r[2],
                                   "mac_address": Device.query.get(r[0]).mac_address},
                        result),
            "code": "1"
        }
    except Exception as e:
        msg = "Get statistics msg error: {0}".format(e)
        print msg
        data = {
            "code": "0",
            "msg": msg
        }

    return jsonify(data)


@app.route("/statistic/per/device/ajax/<int:device_id>")
@login_required
def per_device_statistic_ajax(device_id):
    records = UsageRecord.query.filter_by(device_id=device_id).all()
    if not records:
        data = {
            "code": "0",
            "msg": "No records"
        }
    else:
        data = {
            "code": "1",
            "data": map(lambda r: r.to_json(), records)
        }

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)

