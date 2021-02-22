import csv

titles = set()

with open("Favorite TV Shows - Form Responses.csv","r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        titles.add(row["title"])

for title in sorted(titles)
    print(title)
