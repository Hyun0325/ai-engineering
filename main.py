from src.environment import check_environment
from src.data_loader import load_temperature_data

print("AI Engineering Project")

check_environment()

temperature_data = load_temperature_data()

print(temperature_data)