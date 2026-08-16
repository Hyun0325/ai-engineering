import pandas as pd
import torch

def load_temperature_data():
    data = pd.read_csv("data/temperature.csv")

    data.columns = data.columns.str.strip()

    print("Loading temperature data...")
    print(data)
    print(data.columns)
    print(data["temperature"])

    temperature = data["temperature"].to_numpy()

    print("Numpy array:")
    print(temperature)
    print(type(temperature))

    temperature_tensor = torch.tensor(temperature)

    print("PyTorch tensor:")
    print(temperature_tensor)
    print(type(temperature_tensor))


    print("Tensor mean:", temperature_tensor.mean())
    print("Tensor max:", temperature_tensor.max())
    print("Tensor min:", temperature_tensor.min())
    

    return data