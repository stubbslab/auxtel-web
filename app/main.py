# -*- coding: utf-8 -*-
"""
@author: brodi
"""
import re
import os
from pathlib import Path
from flask import Flask,render_template
from typing import List

import markdown as md
import markdown.extensions.fenced_code
import markdown.extensions.codehilite
from pygments.formatters import HtmlFormatter

from models.models import Image
from tests.tests import test_pages

app = Flask(__name__)

imageRoot = Path(app.static_folder)/Path("images")
parent = Path(__file__).parent

app.register_blueprint(test_pages)


@app.route('/', defaults={'num':10})
@app.route('/<int:num>')
def table(num):
    imgs = timeSort(imageRoot, num)
    header = prepMd(parent/Path('header.md'))
    return render_template("index.html",
                           imgs = imgs,
                           img_attr = ['date','seq'],
                           header = header
                           )


@app.route('/events/<date>/<seq>')
def events(date, seq):
    matchPath = scan(imageRoot, date, seq)
    imgs = [Image(matchPath)]
    return render_template("data.html", imgs = imgs)
    



def prepMd(file: Path) -> str:
    with open(file, "r") as hdFi:
        mdTemp = md.markdown(
                             hdFi.read(),
                             extensions=["fenced_code",
                                        "codehilite"],
                             fenced_code = True,
                             output_format="html5"
                             )
   
        # Generate css for syntax highlighting
        formatter = HtmlFormatter(style = "emacs",
                                  full = True,
                                  cssclass = "codehilite"
                                  )
        cssString = formatter.get_style_defs()
        mdCSS = "<style>" + cssString + "</style>"
        
        return mdCSS + mdTemp
    
        

def timeSort(root: Path, num: int) -> List[Image]:
    sPaths =  [
                *sorted(
                    root.rglob("./*.png"),
                    key=os.path.getmtime,
                    reverse=True)
                ]

    search = r'^(.+_){2}((\d+[-/]\d+[-/]\d+))+(.+_)+(\d+).*$'
    r = re.compile(search)
    clean_sPaths = [fi for fi in sPaths if r.match(fi.name)][-num:]

    return [*map(Image, clean_sPaths)]
    

def scan(root: Path, date: str, seq: str) -> Path:
    search = fr'^(.+_){{2}}({date})+(.+_)+({seq}).*$'
    r = re.compile(search)
    for fi in root.rglob("./*.png"):
        print(fi)
        match = r.match(fi.name)
        if match:
            return fi




if __name__ == '__main__':
    app.run(debug = False, port = 5001)