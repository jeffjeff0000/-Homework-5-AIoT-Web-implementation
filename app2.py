# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 00:45:30 2022

@author: user
"""

from flask import Flask, render_template, jsonify
import pandas as pd
from six.moves import urllib
import json
from myAPI import index2
app = Flask(__name__)
 
@app.route("/")
def index2():
   index2()

if __name__ == '__main__':
    app.run(port=5000)

