from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "<h1>ReconOps Dashboard - Home</h1>"

@main.route('/scan')
def scan():
    return "<h1>Start a new Recon Scan</h1>"

@main.route('/results')
def results():
    return "<h1>Scan Results</h1>"

@main.route('/logs')
def logs():
    return "<h1>Activity Logs</h1>"

@main.route('/settings')
def settings():
    return "<h1>Settings</h1>"

