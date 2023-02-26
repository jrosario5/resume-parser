import spacy
import re
import os
from datetime import datetime
from tika import parser
import json
class Parser:
    def __init__(self, document):
        self.document = document
        self.parsed = parser.from_file(self.document)
    def process(self):
        text = self.parsed['content']
        if text is None:
            return 'No extractable text'
        doc = nlp(text)
        data = {"props":[], 'values':[]}
        for val in doc.ents:
            data['props'].append(val.label_)
            data['values'].append(val.text)
        return (json.dumps(data))

if __name__ == '__main__':
    nlp = spacy.load("gp")
    parser = Parser("TaylorFosterResume.pdf")
    resume = parser.process()
    print(resume)
