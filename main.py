from src.environment import check_environment
from src.data_loader import load_data

def main():
    print("AI Engineering Project")

    check_environment()

    data = load_data()

    print(data)


if __name__ == "__main__":
    main()