import pandas as pd

df = pd.read_json(r'C:\Users\chirag\Documents\Programming\SpringBoard\yelp\data\yelp_academic_dataset_review.json', lines=True)
print(df.head())