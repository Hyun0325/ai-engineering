# AI Engineering Project

## Goal

기계공학 지식을 기반으로 인공지능(AI)과 소프트웨어 개발 역량을 융합하는 엔지니어로 성장하기 위한 개인 프로젝트.

목표는 Python, 데이터 분석, 머신러닝, 딥러닝 기술을 학습하고 이를 기계 시스템 및 열유체 공학 문제에 적용할 수 있는 기반을 만드는 것이다.

장기적으로는 기계공학의 물리적 지식과 AI/소프트웨어 기술을 결합하여 실제 엔지니어링 데이터를 분석하고 예측하는 역량을 구축하는 것을 목표로 한다.

---

# Development Environment

## Hardware

- MacBook Pro
- Apple M5
- Apple Silicon
- 24 GB RAM

## OS

- macOS

---

# Software Environment

## Package Manager

- Homebrew

## Python Environment

- Miniforge
- Conda
- Environment: `pytorch_env`
- Python: 3.11.15

## Main Python Libraries

- pandas
- NumPy
- PyTorch
- torchvision
- matplotlib
- Pillow
- Jupyter
- scikit-learn
- OpenCV

---

# Deep Learning Framework

## PyTorch

Installed:

- torch
- torchvision
- torchaudio

GPU Acceleration:

- Apple Metal Performance Shaders (MPS)

Status:

- MPS Available = True
- MPS Device = `mps:0`

PyTorch is currently being used to learn:

- Tensor fundamentals
- Tensor data types
- Tensor operations
- CPU vs GPU computation
- MPS-based GPU acceleration

---

# Development Tools

## Editor

- Visual Studio Code

## Version Control

- Git
- GitHub

Completed:

- Git repository initialization
- GitHub remote repository connection
- Commit and push workflow setup
- `.gitignore` configuration

---

# Project Structure

## Current structure:

```text
ai-engineering/
├── main.py
├── README.md
├── PROJECT_CONTEXT.md
├── requirements.txt
├── src/
│   ├── environment.py
│   └── data_loader.py
├── data/
│   ├── temperature.csv
│   └── thermal/
├── models/
├── notebooks/
├── experiments/
└── docs/
```

# Folder and File Purpose

## main.py

Project entry point.

Current responsibilities:

- Print project information
- Check the Python/PyTorch environment
- Load example temperature data
- Load thermal numerical data from a text file
- Load a corresponding PNG thermal image
- Verify the PNG image size


Current data flow:
main.py
   ↓
check_environment()
   ↓
load_temperature_data()
   ↓
load_thermal_txt()
   ↓
PIL.Image.open()

## src/

Contains reusable Python source code.

### src/environment.py

Purpose:

- Check the PyTorch environment
- Display the installed PyTorch version
- Check whether Apple MPS GPU acceleration is available

Current implementation uses:

torch.backends.mps.is_available()
to verify MPS availability.

### src/data_loader.py

Purpose:

- Load CSV data using pandas
- Process temperature data
- Convert pandas data to NumPy arrays
- Convert NumPy arrays to PyTorch tensors
- Move tensors to the MPS device
- Perform basic PyTorch tensor operations
- Load numerical thermal data from text files
- Convert thermal numerical data into NumPy arrays
- Calculate basic statistics
- Verify thermal data dimensions
- Reshape thermal data into a 512 × 640 array

## data/

Contains engineering and AI datasets.
Private research data is not uploaded to GitHub.

### data/temperature.csv

Small example dataset used for learning:

- pandas
- NumPy
- PyTorch
- Tensor operations

The example data contains:

- time
- temperature
- pressure

### data/thermal/
Contains private research laboratory thermal data.
The current thermal dataset contains 

corresponding:

- .txt numerical thermal data
- .png thermal image data
The thermal data is private research data and must not be uploaded to GitHub.

## models/

Contains trained AI model files.
Model files such as:

- .pt
- .pth
are excluded from Git tracking.

## notebooks/

Reserved for:

- Jupyter Notebook experiments
- Data analysis
- Visualization
- Model experiments

## experiments/

Reserved for:

- Experimental results
- Model configurations
- Experiment records
- Performance comparisons

## docs/
Reserved for project documentation.

# Git and GitHub

## Git and GitHub are used for:

- Source code version control
- Project history management
- Learning record management
- Backup of non-sensitive project files

## Completed:

- Git repository initialization
- GitHub remote repository connection
- Commit workflow
- Push workflow
- .gitignore configuration

Private research data is intentionally excluded from GitHub.

## .gitignore

The current .gitignore excludes:

- Python cache files
- .pyc files
- Jupyter checkpoints
- Conda environment folders
- .env
- macOS .DS_Store
- PyTorch model files
- VS Code settings
- Research data under data/

The entire data/ directory is excluded from Git tracking because it contains private research data.

# Current Learning Progress

## Environment Setup

Completed:

- Homebrew installation
- Miniforge installation
- Conda environment creation
- Python 3.11 environment setup
- PyTorch installation
- Apple Silicon MPS verification
- VS Code development environment setup
- Git/GitHub setup

## Python Fundamentals

Currently learned and practiced:

- import
- as
- Python functions using def
- Function scope
- print()
- Python modules
- Basic project structure
- Importing functions from other Python files

The project is being developed using multiple Python modules rather than placing all code in a single file.

## Data Processing Learning

### pandas

pandas is currently being used to:

- Load CSV files
- Represent tabular data using DataFrames
- Inspect columns
- Select specific columns
- Perform basic data processing

Example:

data = pd.read_csv("data/temperature.csv")

The project also uses:

data.columns = data.columns.str.strip()
to remove unnecessary whitespace from column names.

### NumPy

NumPy is currently being used to:

- Convert pandas data into NumPy arrays
- Represent numerical data efficiently
- Perform numerical calculations
- Prepare data for further processing

Example: temperature = data["temperature"].to_numpy()

### PyTorch Tensor

PyTorch tensors are currently being used to:

- Represent numerical data for PyTorch operations
- Perform tensor calculations
- Move numerical data to the MPS device
- Prepare for future machine learning and deep learning models

Current operations practiced:

Tensor + 10
Tensor × 2
Tensor²
Mean
Maximum
Minimum

### CPU and GPU / MPS Learning

The project currently uses Apple's MPS backend for GPU acceleration.
Basic concept learned:

NumPy data
    ↓
PyTorch Tensor
    ↓
MPS device
    ↓
GPU computation
Example device:

mps:0

mps:0 represents the first available MPS device.
The project has successfully verified that PyTorch can perform tensor operations using Apple's MPS backend.

## Thermal Research Data

The project has begun using private thermal data provided by the research laboratory.

The thermal dataset contains numerical measurements and corresponding thermal images.

### Thermal Text Data
The numerical thermal data is stored as comma-separated integer values.

Example: 3339,3328,3306,3303,3299,...

The current tested thermal text file contains:

- Number of values: 327680
- Data type: int64
- Minimum: 3126
- Maximum: 65115
- Mean: approximately 3926.03

The number of values satisfies: 512 × 640 = 327680

Therefore, the data can be reshaped into: 512 × 640

Current processing:

```text
Thermal .txt
     ↓
Read file
     ↓
Split by comma
     ↓
Convert strings to integers
     ↓
Python list
     ↓
NumPy array
     ↓
512 × 640 array
```

### Thermal Image Data

The corresponding thermal image is stored as a PNG file.

The image is currently loaded using Pillow:
from PIL import Image

Example: image = Image.open("data/thermal/...")

The tested PNG image has the size: 640 × 512

The numerical thermal data has been reshaped to: 512 × 640

The relationship between the numerical data and the PNG image still needs to be investigated and verified.

### Important Thermal Data Interpretation

The numerical values in the thermal text file currently range approximately from: 3126

to: 65115

These values must not yet be assumed to represent degrees Celsius.

The exact physical meaning, unit, calibration method, scaling factor, and relationship between the numerical values and actual temperature have not yet been confirmed.

Before using the values as physical temperature measurements, the original research data documentation or measurement specification must be checked.

Current Thermal Data Processing Status

Completed:

- Located a thermal text data file
- Loaded the text file successfully
- Parsed comma-separated numerical values
- Converted values to NumPy
- Verified number of values
- Verified data type
- Calculated minimum value
- Calculated maximum value
- Calculated mean value
- Verified that the data contains 327680 values
- Verified that the data can be reshaped to 512 × 640
- Reshaped the numerical data to 512 × 640
- Loaded the corresponding PNG image
- Verified PNG size as 640 × 512

Not yet completed:

- Visualization of the thermal numerical data
- Comparison between numerical thermal data and 
PNG image
- Verification of pixel-to-data correspondence
- Verification of thermal value calibration
- Physical temperature conversion
- Automated processing of multiple thermal files

## Matplotlib

Matplotlib has been installed and its import/version has been verified.

Current purpose:

- Visualize numerical thermal data
- Display 2D thermal distributions
- Create engineering plots
- Analyze temperature distributions

Next planned use:

```text
512 × 640 thermal NumPy array
        ↓
matplotlib
        ↓
2D thermal visualization
Current Project Architecture
The current learning architecture is:
Research Data
    │
    ├── CSV
    ├── TXT
    └── PNG
          ↓
Data Loading
    │
    ├── pandas
    ├── NumPy
    └── Pillow
          ↓
Data Processing
    │
    ├── NumPy arrays
    └── PyTorch tensors
          ↓
GPU Processing
    │
    └── Apple MPS
          ↓
Visualization
    │
    └── matplotlib
          ↓
Machine Learning
          ↓
Deep Learning
          ↓
Engineering Application
```

# Research Direction

## Long-term interests:

- AI applications in mechanical engineering
- Thermal-fluid engineering
- Engine cooling systems
- Battery thermal management
- Fluid flow analysis
- Engineering simulation and optimization
- Data-driven modeling of physical systems
- Thermal image analysis
- Engineering process quality prediction
- AI-based engineering prediction

## Potential future research topics:

- Thermal image-based analysis
- Thermal anomaly detection
- Thermal field prediction
- CNN-based thermal image analysis
- Multimodal AI using thermal images and numerical data
- AI-based manufacturing process quality prediction
- Data-driven engineering modeling

# Future Development Plan

## Phase 1 — Thermal Data Understanding

1. Visualize the 512 × 640 numerical thermal data using matplotlib
2. Compare the numerical thermal data with the corresponding PNG image
3. Determine whether the numerical data and PNG image have the same spatial orientation
4. Investigate the relationship between numerical values and image pixels
5. Verify the physical meaning and unit of the thermal numerical values

## Phase 2 — Data Preprocessing

1. Build reusable thermal data loading functions
2. Process multiple thermal files automatically
3. Handle missing or invalid data
4. Normalize thermal data when appropriate
5. Convert thermal arrays into PyTorch tensors
6. Build dataset structures for machine learning

## Phase 3 — Machine Learning

1. Learn the basic machine learning workflow
2. Study training, validation, and test datasets
3. Practice scikit-learn models
4. Learn feature engineering
5. Learn evaluation metrics
6. Apply machine learning to engineering data

## Phase 4 — Deep Learning

1. Build basic PyTorch experiments
2. Learn neural network fundamentals
3. Learn loss functions and optimizers
4. Learn training loops
5. Build CNN-based thermal image models
6. Use MPS acceleration for model training

## Phase 5 — Research Application

1. Apply AI techniques to actual thermal engineering data
2. Develop thermal image analysis methods
3. Investigate thermal anomaly detection
4. Explore thermal field prediction
5. Explore multimodal learning using images and numerical data
6. Develop engineering-focused prediction models
7. Evaluate model performance using engineering-relevant metrics

# Dependency Management

The project uses requirements.txt to record Python dependencies.

## Current requirements include:

- numpy
- pandas
- torch
- torchvision
- matplotlib
- jupyter
- scikit-learn
- opencv-python
- Pillow is also currently required by the project because main.py uses:
from PIL import Image
The dependency list should be kept synchronized with libraries actually required by the project.

# Important Notes
- Research laboratory data is private.
- Private research data must not be uploaded to GitHub.
- The data/ directory is excluded from Git tracking.
- Large trained model files are excluded from Git tracking.
- Research data must be handled according to laboratory confidentiality requirements.
- The repository should contain source code, documentation, learning records, and reproducible workflows rather than private research data.
- The physical meaning of research data must be verified from reliable documentation before making engineering interpretations.
- When information about the research dataset is uncertain, do not assume the meaning of the values.
- The project is intended to gradually progress from Python fundamentals to data processing, visualization, machine learning, deep learning, and real mechanical engineering applications.