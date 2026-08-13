import torch

def check_environment():
    print("AI Engineering Environment Check")

    print(f"PyTorch Version: {torch.__version__}")

    if torch.backends.mps.is_available():
        print("MPS GPU Acceleration: Available")
    else:
        print("MPS GPU Acceleration: Not Available")


if __name__=="__main__":
    check_environment()