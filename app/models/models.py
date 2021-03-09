from pathlib import Path
from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Image():
    path: Path
    name: str = field(init = False)
    date: datetime = field(init = False)
    seq: int = field(init = False)
    
    def parse_filename(self, delimiter="_"):
        name = self.path.with_suffix('').name
        nList = name.split(delimiter)
        date = nList[2]
        seq = nList[4]
        return(datetime.strptime(date, '%Y-%m-%d'), int(seq))
    
    def cleanDate(self):
        return self.date.strftime('%Y-%m-%d')
    
    def __post_init__(self):
        self.name = self.path.name
        self.date, self.seq = self.parse_filename()