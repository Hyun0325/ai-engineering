import pandas as pd
import numpy as np
import torch

def load_thermal_txt(file_path):
    with open(file_path, "r") as f:
        text = f.read()

    values = [int(value) for value in text.split(",") if value.strip()]

    data = np.array(values)

    print("Thermal data loaded")
    print("Number of values:", len(data))
    print("Data type:", data.dtype)
    print("Minimum:", data.min())
    print("Maximum:", data.max())
    print("Mean:", data.mean())
    print("Can reshape to 512 x 640:", data.size == 512 * 640)

    thermal_image = data.reshape(512, 640)

    print("Thermal image shape:", thermal_image.shape)
    print("First row", thermal_image[0])

    return data

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

    temperature_tensor = torch.tensor(
        temperature, dtype=torch.float32
        )

    temperature_mps = temperature_tensor.to("mps")

    print("MPS Tensor:")
    print(temperature_mps)
    print("Device:", temperature_mps.device)

    temperature_mean = temperature_mps.mean()

    print("MPS Mean:", temperature_mean)
    print("Result Device:", temperature_mean.device)

    print("Tensor + 10:")
    print(temperature_mps + 10)

    print("Tensor * 2:")
    print(temperature_mps *2)

    print("Tensor squared:")
    print(temperature_mps ** 2)
    

    return data