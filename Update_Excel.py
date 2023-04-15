import pandas as pd


# read the xlsx file
manifest_df = pd.read_excel(r'https://1drv.ms/x/s!AgRce2M50rkenXZ3eUpBwG3n7mXe?e=DzpJD4')
# perform arithmentic operation
manifest_df['Name'] = 'Ram'
# write again the excel file
manifest_df.to_excel(r'https://1drv.ms/x/s!AgRce2M50rkenXZ3eUpBwG3n7mXe?e=DzpJD4')