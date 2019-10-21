import pandas as pd

df = pd.read_json(r'C:\Users\chirag\Documents\Programming\SpringBoard\yelp\data\yelp_academic_dataset_business.json', lines=True)
#print(df.query('stars >= 5'))
#print(df.info())
print(df[df['state']=='NV']['city'].value_counts())