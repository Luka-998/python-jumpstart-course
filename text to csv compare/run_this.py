import pandas as pd
import numpy as np
import os
import subprocess
# DESIGNED TO RUN LOCALLY!

# Data preparation:
# 1) csv load and txt parsing
# 2) perform merge from right to left, to retain only rows that are present in right, but not in the left table
current_dir = os.getcwd()
# hardcode because it will run locally
path = r'C:\Users\jaske\OneDrive\Desktop\New folder'

def loader(csv,txt):
    #data csv load
    list1=[]
    csv = pd.read_csv(os.path.join((path),'file.csv'))
    # txt file open
    with open((os.path.join(path,'wepnames.txt'))) as f:
        lines = f.readlines()
        txt = ''.join(lines)
    for line in txt.splitlines():
        list1.append(line.strip())
    return csv,list1
    

csv_df, compare_it = loader(csv='file.csv',txt='wepnames.txt')

def cleaner(csv_df,compare_it):
    #EDA
    compare_it_series = pd.Series(compare_it)
    compare_df = pd.DataFrame({'Weapons':compare_it_series})
    sorted_csv_df = csv_df[['Name','Amount']].reset_index(drop=True).sort_values(by='Amount',ascending=True)
    merged_df = pd.merge(sorted_csv_df,compare_df,how='right',left_on='Name',right_on='Weapons').sort_values(by='Amount',ascending=True)
    print(f"Here {merged_df}")
    return merged_df

merged_table = cleaner(csv_df,compare_it)

def results(merged_df):
    in_both_files = merged_df[['Amount','Name']].where(merged_df['Weapons'].notna()).dropna().reset_index(drop=True)
    print(f"Here {in_both_files.head}")
    only_in_txt = merged_df['Weapons'].where(merged_df['Name'].isna()).dropna().reset_index(drop=True)
    merged_df['only_txt'] = only_in_txt
    total_txt = only_in_txt.value_counts().sum()
    return only_in_txt,total_txt,in_both_files
only_in_txt,total_txt,in_both_files = results(merged_table)


if __name__ == "__main__":
    pd.set_option('display.max_rows',None)
    csv_df, compare_it = loader(csv='file.csv', txt='wepnames.txt')
    merged_table = cleaner(csv_df, compare_it)
    only_in_txt, total, in_both_files = results(merged_table)

    with open(os.path.join(path, 'results.txt'), 'w') as f:
        f.write(f'Items that are not in the CSV file. Total: {total_txt} items.\n')
        if total_txt == 0:
            f.write('No matches found!\n')
        f.write(f'\n{only_in_txt}\n')
        f.write(f'--' * 50 + '\n')
        f.write(f'Total overlapping items: {in_both_files.value_counts().sum()}.\nItems that are present in both, CSV and compare list:\n{in_both_files}')
    print("Results written to the results.txt file")
    subprocess.run(['notepad', os.path.join(path, 'results.txt')])














