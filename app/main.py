from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html",
                           title='Início')


@app.route('/admin')
def admin():
    return render_template("admin.html",
                            title='Menu do Admin')
