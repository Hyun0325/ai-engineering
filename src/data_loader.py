import csv

def load_data():
    print("Loading data...")

    data = []

    with open("data/temperature.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            data.append(row)
            
    return data