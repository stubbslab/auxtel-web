# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 17:50:48 2021

@author: brodi
"""
from dataclasses import dataclass
import os
from pathlib import Path
from flask import Flask,render_template

from test import test_pages 

app = Flask(__name__)

root = 'static/images/'

app.register_blueprint(test_pages)



if __name__ == '__main__':
   app.run(debug=True)