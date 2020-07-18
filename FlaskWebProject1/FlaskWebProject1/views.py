"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template, request
from FlaskWebProject1 import app
from collections import Counter
import requests

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/countme/<input_str>')
def count_me(input_str):
    input_counter = Counter(input_str)
    response = []
    for letter, count in input_counter.most_common():
        response.append('"{}": {}'.format(letter, count))
    return '<br>'.join(response)

@app.route('/ips')
def ips():
    response = []
    browser = requests.session()
    list_of_addresses = ['144.12.97.175', '47.33.190.195', '54.213.136.220', '37.27.54.15', '91.107.252.94', '112.245.28.187', '77.198.208.109', '79.195.246.215', '109.219.196.231', '111.14.43.156', '102.111.174.6', '176.65.253.46', '102.155.114.82']
    for each_ip in list_of_addresses:
        url = f"https://freegeoip.app/json/{each_ip}"
        result = browser.get(url).json()
        print(f"The country for IP Address {result.get('ip')} is {result.get('country_name')}")
        response.append(f"The country for IP Address {result.get('ip')} is {result.get('country_name')}")
    return '<br>'.join(response)


@app.route('/ip')
def my_form():
    return render_template('ip-enter.html')

@app.route('/ip', methods=['POST'])
def my_form_post():
    text = request.form['text']
    address = text.upper()
    response = []
    browser = requests.session()
    url = f"https://freegeoip.app/json/{address}"
    try:
        result = browser.get(url).json()
    except:
        return "ip error"
    print(f"The country for IP Address {result.get('ip')} is {result.get('country_name')}")
    response.append(f"The country for IP Address {result.get('ip')} is {result.get('country_name')}")
    return '<br>'.join(response)
