
import csv


def gen_csv():
    with open('in/mycsv.csv', 'r', newline="\n") as fr:
        data = csv.reader(fr, delimiter=",")

        for r in data:
            print(r)

        print(type(data))

