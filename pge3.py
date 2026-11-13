import csv
with open("datas.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)