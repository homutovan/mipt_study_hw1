import json

def filereader(path: str):
    with open(path) as f:
        for item in json.load(f):
            yield item 
