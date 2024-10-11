import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import sys

# Add the 'src' directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../data')))

from data_loader import load_data
from logger_setup import info_logger, error_logger

def main():
    file_path = os.path.join(os.getcwd(), 'data', 'telegram_medical_businesses_data.csv')
    print("Current working directory:", os.getcwd())  # Debug line
    
    try:
        if os.path.exists(file_path):
            df = load_data(file_path=file_path)
            info_logger.info(f"Loaded data successfully from {file_path}")
            print(df.head())
            print(df.shape)
            print(df.isnull().sum())
        else:
            error_logger.error(f"File not found: {file_path}")
    except Exception as e:
        error_logger.error(f"Error loading data from {file_path}: {e}")

if __name__ == '__main__':
    main()
