import pandas as pd

df_business = pd.read_json(r'C:\Users\chirag\Documents\Programming\SpringBoard\yelp\data\yelp_academic_dataset_business.json', lines=True)
df_tip = pd.read_json(r'C:\Users\chirag\Documents\Programming\SpringBoard\yelp\data\yelp_academic_dataset_tip.json', lines=True)

df_business_tip = pd.merge(df_business, df_tip, on="business_id", how="inner")
print(df_business_tip.nlargest(5,['compliment_count']))