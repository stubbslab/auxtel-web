# -*- coding: utf-8 -*-
"""
@author: brodi
"""
import re
from dataclasses import dataclass, field
from datetime import datetime
import os
from pathlib import Path
from flask import Flask,render_template

# from test import test_pages 

app = Flask(__name__)

imageRoot = Path(app.static_folder)/Path("images")

# app.register_blueprint(test_pages)


@app.route('/', defaults={'num':10})
@app.route('/<num>')
def table(num):
    print(num)
    sPaths = [*sorted(imageRoot.iterdir(), key=os.path.getmtime, reverse=True)][-int(num):]
    imgs = [*map(Image, sPaths)]
    return render_template("index.html", imgs = imgs, img_attr = ['date','seq'])


@app.route('/events/<date>/<seq>')
def events(date, seq):
    matchPath = scan(imageRoot, date, seq)
    imgs = [Image(matchPath)]
    return render_template("data.html", imgs = imgs)
    
    

def scan(root: Path, date: str, seq: str) -> Path:
    search = fr'^(.+_){{2}}({date})+(.+_)+({seq}).*$'
    r = re.compile(re.compile(search))
    for fi in root.iterdir():
        match = r.match(fi.name)
        if match:
            return root/Path(match.group())


@dataclass
class Image():
    path: Path
    name: str = field(init=False)
    date: datetime = field(init = False)
    seq: int = field(init = False)
    
    def parse_filename(self, delimiter="_"):
        print(self.path)
        name = self.path.with_suffix('').name
        nList = name.split(delimiter)
        date = nList[2]
        seq = nList[4]
        return(datetime.strptime(date, '%Y-%m-%d'),int(seq))
    
    def cleanDate(self):
        return self.date.strftime('%Y-%m-%d')
    
    def __post_init__(self):
        self.name = self.path.name
        self.date, self.seq = self.parse_filename()
 
if __name__ == '__main__':
    app.run(debug=True)