#https://www.youtube.com/watch?v=M9Itm95JzL0

import numpy as np
import pandas as pd
import json,os
from sklearn.model_selection import train_test_split
positive = "POSITIVE"
negative = "NEGATIVE"
neutral = "NEUTRAL"

class review:
    def __init__(self, text, score):
        self.text = text
        self.score = score
        self.sentiment = self.get_sentiment()

    def get_sentiment(self):
        if self.score == 2:
            return negative
        elif self.score == 3:
            return neutral
        else:
            return positive


data = []

file_name = r".\data_ML\data.json"
if os.path.exists(file_name):
    print (f"Tập tin có tồn tại")
    
with open(file_name,'r',encoding="utf-8") as f:
    for line in f:
        data.append(json.loads(line))

print(f"Data count: {len(data)}")

reviews = [[rv.get("reviewText"),rv.get("overall")] for rv in data]

print (f"Reivew data count: {len(reviews)}")

