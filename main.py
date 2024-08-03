import pandas
df= pandas.read_csv('cats_dataset.csv')
print(df[df['Gender'] == 'Female'][df['Age (Years)']> 5].head(10))