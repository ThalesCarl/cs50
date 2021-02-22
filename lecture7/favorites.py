import csv

with open("Favorite TV Shows - Form Responses.csv","r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["title"])
