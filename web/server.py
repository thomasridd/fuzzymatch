# coding=utf-8
__author__ = 'hadoop'

import os
import logging
from flask import Flask, render_template, request
from fuzzy_controller import fuzzy_match_strings

app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])
def landing_page():
    default_data = {'match_items': [], 'to_items': [], 'results': [], 'line_break': '/n'}

    if request.method == 'POST':
        match_items = request.form['matchItems']
        to_items = request.form['toItems']
        fuzzy_items = fuzzy_match_strings(match_items, to_items)
        calculated_data = {'match_items': match_items,
                           'to_items': to_items,
                           'results': fuzzy_items, 'line_break': '/n'}
        return render_template('index.html', template_data = calculated_data)
    else:
        return render_template("index.html", template_data = default_data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

