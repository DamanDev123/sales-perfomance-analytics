import pandas as pd
dat = pd.read_csv('Online_retail.csv',encoding ='ISO-8859-1')
print("__Data Set___")
#print(dat.info())
print(dat.head())
#This will show us if there are negative numbers
print(dat[['Quantity', 'UnitPrice']].describe() )
print(dat.isnull().sum())

#to clean this data
#gotta drop the missing customer ID
data_clean = dat.dropna(subset =['CustomerID'].copy())
data_clean = data_clean[(data_clean['Quantity']>0) & (data_clean['UnitPrice']> 0)]
#Add the business logic revenue
data_clean['Total_Sales'] = data_clean['Quantity'] * data_clean['UnitPrice']
#duplicate_count = data_clean.duplicated().sum()
#print(f"Found {duplicate_count}")
data_clean = data_clean.drop_duplicates()

data_clean['Description'] = data_clean['Description'].astype(str).str.strip().str.upper()
data_clean['InvoiceDate'] = pd.to_datetime(data_clean['InvoiceDate'])


#rint(f"Found {duplicate_count}")
data_clean.to_csv('Cleaned_online_retail.csv', index = False)

#How many rows have survived the cut
print(f"Original: {len(dat)}")
print(f"Cleaned rows: : {len(data_clean)}")

