import csv
data={"name":"anjali","age":22,"course":"MCA"}

with open("student.csv","w",newline='') as f:
    writer = csv.writer(f)
    writer.writerow(data.keys())
    writer.writerow(data.values())

with open("student.csv","r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
