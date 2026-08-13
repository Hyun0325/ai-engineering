import torch

def check_enviroment():
    print("AI Engineering Enviroment Check")

    print(f"PyTorch Version: {torch.__version__}")

    if torch.backends.mps.is_available():
        print("MPS GPU Acceleration: Available")
    else:
        print("MPS GPU Acceleration: Not Available")


if __name__=="__main__":
    check_enviroment()