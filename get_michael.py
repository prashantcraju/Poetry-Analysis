import csv
import os
import io
import re

def makecsv(writer, file):
    curr_file = io.open(file + '.tsv', encoding='utf-8')
    #print(file)
    # with open(file + '.tsv', encoding='utf-8') as actual_file:
    #     print(file)
    tsv_reader = csv.reader(curr_file, delimiter='\t', dialect=csv.excel_tab)

    for line in tsv_reader:
        # testStr = "some string"
        # previous split command
        # line_split = line[0].split('\t')
        line_split = re.split('\t|\n', line[0])

        #print(len(line_split))
        #print(line_split)
        if len(line_split) > 1:
            i = 0
            while i < (len(line_split) - 2):
                # print(line_split[i])

                #print(i)
                writer.writerow([line_split[i], line_split[i + 1]])
                i += 2
        else:
            #print("inside else clause")
            # print(line_split)
            if line[1] != None:
                writer.writerow([line[0], line[1]])


def get_year(year, work_title, file):
    os.chdir("/Users/grandhis/Desktop/Sarah_kersch")
    oneWork = open(work_title, 'w')
    writer = csv.writer(oneWork)
    if year < 1890:
        os.chdir("./poetry_1880-1889/")
        print("1st work: %s" % work_title)
        print('changing to 1889 directory: %s' % os.getcwd())
        makecsv(writer, file)
    elif 1890 <= year <= 1894:
        os.chdir("./poetry_1890-1894/")
        print("2nd work: %s" % work_title)
        print('changing to 1890 directory: %s' % os.getcwd())
        makecsv(writer, file)
    elif 1905 <= year <= 1909:
        os.chdir("./poetry_1905-1909/")
        print("3rd work: %s" % work_title)
        print('changing to 1905 directory: %s' % os.getcwd())
        makecsv(writer, file)
    elif 1910 <= year <= 1914:
        os.chdir("./poetry_1910-1914/")
        print("final work: %s" % work_title)
        print('changing to 1910 directory: %s' % os.getcwd())
        makecsv(writer, file)

if __name__ == '__main__':
    with open('poetry_metadata.csv') as csvfile:
        mikereader = csv.reader(csvfile, delimiter=',')
        for row in mikereader:
            if row[4] == 'Field, Michael,' or row[4] == 'Field, Michael.':
                #print(row)
                file_name = row[0]
                work_title = '_'.join(row[10].split(' ')) + '.csv'
                print(work_title + " " + row[6])
                get_year(int(row[6]), work_title, file_name)


