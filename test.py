# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 17:50:48 2021

@author: brodi
"""
from dataclasses import dataclass
import os
from pathlib import Path
from flask import Blueprint,render_template

test_pages = Blueprint('test_pages', __name__,
                       url_prefix='/test',
                       template_folder='test/templates',
                       static_folder='test/static')

img_root = Path(test_pages.static_folder)/Path("images")

@test_pages.route('/local')
def local():
    sorted_paths = [*sorted(img_root.iterdir(), key=os.path.getmtime)]
    base = [path.name for path in sorted_paths]
    pics = list(map(str, base))
    return render_template("local.html", pics=pics)

@test_pages.route('/random')
def random():
    rand = 4*["https://source.unsplash.com/random/320x240"]
    return render_template("random.html", pics=rand)

@test_pages.route('/table')
def table():
    colors = [Color("blue", "2020"), Color("green","2021")]
    color_attr = Color.__annotations__.keys()
    return render_template("table.html", colors = colors, color_attr = color_attr)
    

@dataclass
class Color():
    name: str
    created_at: str

