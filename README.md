# Anemia Detection using CNN

This project implements a 1D Convolutional Neural Network (CNN) to detect Anemia using pixel features extracted from images.

## Project Structure

- `src/`
  - `data_loader.py`: Handles loading and preprocessing of `Anemia_Dataset.csv`.
  - `model.py`: Defines the 1D CNN architecture.
  - `train.py`: Main script to train and evaluate the model.
- `requirements.txt`: List of Python dependencies.

## Setup Instructions

### 1. Prerequisite: Python Environment
**Important:** Please check the Python environment. If you encounter errors, create a fresh environment:

```bash
# Open Anaconda Prompt or Terminal
conda create -n anemia_env python=3.8
conda activate anemia_env
pip install -r requirements.txt
```

### 2. Run Training
**Do not type `python src/train.py`** (it will fail because python is not in your PATH).

Instead, **double-click** the `run_ml.bat` file in this folder, or run this command in your terminal:

```bash
.\run_ml.bat
```

### 3. Output
The script will:
- Train the model for 50 epochs.
- Save the trained model to `anemia_model.h5`.
- Save the training accuracy/loss plot to `training_history.png`.
