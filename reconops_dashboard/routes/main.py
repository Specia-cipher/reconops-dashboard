from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/scan')
def scan():
    return render_template('scan.html')

@main.route('/results')
def results():
    return render_template('results.html')

@main.route('/logs')
def logs():
    return render_template('logs.html')

@main.route('/settings')
def settings():
    return render_template('settings.html')
