import csv
import io
import os
import re
import sys
csv.field_size_limit(sys.maxsize)

# def get_year(year, file):

seen = set()
wordsDict = {}
count = 0

def make_csv(parsed_dict):
    final_file = open('1920-1922.csv', 'w')
    writer = csv.writer(final_file)
    for key in parsed_dict:
        newList = []
        newList.append(key)
        newList.append(parsed_dict[key])
        writer.writerow(newList)

if __name__ == '__main__':
    with open('poetry_metadata.csv') as csvfile:
        allReader = csv.reader(csvfile, delimiter=',')
        first_line = next(allReader)
        for row in allReader:
            file_name = row[0]
            year = int(row[6])
            os.chdir("/Users/grandhis/Desktop/Sarah_kersch")
            # print(year)
            if 1920 <= year <= 1922:
                os.chdir("./poetry_1920-1922/")
                curr_file = None
                # print("yolo")
                if os.path.isfile(file_name + '.tsv'):
                    # print('shit')
                    # print("a file exists: " + file_name +'.tsv')
                    curr_file = io.open(file_name + '.tsv', encoding='utf-8')
                else:
                    continue
                #curr_file = io.open(file_name + '.tsv', encoding='utf-8')
                tsv_reader = csv.reader(curr_file, delimiter='\t')
                #print("the fileName: " + row[0] + ".tsv")
                for other_row in tsv_reader:
                    # print('shit')
                    line_split = re.split('\t|\n', other_row[0])
                    print(line_split)
                    # if len(line_split) > 1: print(line_split)
                    if len(line_split) > 1:
                        i = 0
                        while i < (len(line_split) - 2):
                            #print('in line split')
                            if count == 0:
                                wordsDict[line_split[i]] = line_split[i+1]
                                seen.add(line_split[i])

                                count += 1
                            else:
                                if line_split[i] in seen:
                                    wordsDict[line_split[i]] = int(wordsDict[line_split[i]]) + int(line_split[i+1])
                                else:
                                    wordsDict[line_split[i]] = line_split[i+1]
                                    seen.add(curr_word)
                            i+=2
                    else:
                        curr_word = other_row[0]
                        if count == 0:
                            wordsDict[curr_word] = other_row[1]
                            seen.add(curr_word)
                            #print(curr_word)
                            count += 1
                        else:
                            if curr_word in seen:
                                wordsDict[curr_word] = int(wordsDict[curr_word]) + int(other_row[1])
                            else:
                                if any(other_row[1:]):
                                    #print(other_row[1])
                                    wordsDict[curr_word] = other_row[1]
                                    seen.add(curr_word)
        make_csv(wordsDict)


