import os
import json

class Json():
    def __init__(self, filepath):
        self.json_filepath = filepath
        if not os.path.exists(filepath):
            self.write({})

    # Takes in a dict
    def write(self, data):
        with open(self.json_filepath, 'w') as fil:
            json.dump(data, fil, indent=4)

    # Returns a dict
    def load(self):
        with open(self.json_filepath) as fil:
            data = json.load(fil)
            return data
