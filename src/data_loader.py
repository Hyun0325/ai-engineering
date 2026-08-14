import pandas as pd

def load_temperature_data():

    print("Loading temperaturedata...")

    data = pd.read_csv("data/temperature.csv")

    return data