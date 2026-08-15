import pandas as pd

def load_temperature_data():
    data = pd.read_csv("data/temperature.csv")

    data.columns = data.columns.str.strip()

    print("Loading temperature data...")
    print(data)
    print(data.columns)
    print(data["temperature"])
 
    print("Maximum temperature:", data["temperature"].max())
    print("Minimum temperature:", data["temperature"].min())
    print("Average temperature:", data["temperature"].mean())

    return data