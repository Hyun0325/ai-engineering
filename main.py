from src.environment import check_environment
from src.data_loader import load_temperature_data
from src.data_loader import load_thermal_txt
from PIL import Image

print("AI Engineering Project")

check_environment()

temperature_data = load_temperature_data()

thermal_data = load_thermal_txt(
    "data/thermal/H2032509301621B220012S000 _1.txt"
)

image = Image.open(
    "data/thermal/H2032509301621B220012S000 _1.png"
)

print("PNG size", image.size)
print(temperature_data)