import csv
import os
import io
import re
import pandas as pd


def merge_csv(*files):
    # creating a dataframe using pandas
    df = pd.concat([pd.read_csv(f, header=None) for f in files], ignore_index=True)
    # print(df)
    word_map = {}
    for i in range(len(df)):
        c = df[0][i]  # current character
        num = df[1][i]
        if c in word_map:
            count = word_map.get(c)
            word_map[c] = count + num
        else:
            word_map[c] = num
    # print(word_map)
    # print(word_map['the'])
    # final_file = open('merged_michael.csv', 'w')
    print(len(word_map))
    # for i in

    with open('merged_michael.csv', 'w') as csvfile:
        mike_writer = csv.writer(csvfile)
        mike_writer.writerow(['Words', 'Count'])
        for i, j in word_map.items():
            mike_writer.writerow([i, j])


    return df

if __name__ == '__main__':
    merge_csv(open('Mystic_trees.csv', encoding='utf-8'), open('Poems_of_adoration.csv', encoding='utf-8'),
              open('Dedicated.csv', encoding='utf-8'), open('Long_ago.csv', encoding='utf-8'),
              open('Underneath_the_bough.csv', encoding='utf-8'), open('Wild_honey_from_various_thyme.csv',encoding='utf-8'))
