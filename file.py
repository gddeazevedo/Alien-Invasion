import json


class File:
    """A class to menage the storage of the high score in a file"""
    
    def __init__(self):
        self.filename = 'high_score.json'
        
    def write_file(self, stats):
        high_score = [stats.high_score]
        try:
            with open(self.filename, 'w') as file:
                json.dump(high_score, file)
        except:
            pass
            
    def read_file(self):
        try:
            with open(self.filename, 'r') as file:
                high_score = json.load(file)
        except:
            pass
        else:
            return high_score[0] or None