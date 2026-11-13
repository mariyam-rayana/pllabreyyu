import csv
with open("datas.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['name'], row['mark'])