from app import app
from flask import render_template, request, redirect, url_for, flash, make_response, session
import requests

# @app.errorhandler(404)
def error404(e):
    return render_template('/pages/404.html'), 404

@app.route('/', methods=['GET', 'POST']) 
def index(): 
    # if request.method == 'GET':
    #     if request.args.get('redirect') == 'definite_integral':
    #         print('here')
    #         return redirect(url_for('definite_integral'), code=302) 
    #     elif request.args.get('redirect') == 'differential_equation':
    #         return redirect(url_for('equations'), 302)

    return render_template('/pages/main.html')

@app.route('/definite_integral', methods=['GET', 'POST'])
def integral():
    return render_template('/pages/integral.html')

@app.route('/differential_equation', methods=['GET', 'POST'])
def equations():
    return render_template('/pages/equation.html')
