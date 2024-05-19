import os
import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from statsmodels.distributions.empirical_distribution import ECDF

def plotmuti(file_paths):
    num_subplots = len(file_paths)

    # Create subplots
    fig, axes = plt.subplots(num_subplots, 1, figsize=(10, 6*num_subplots))

    for i, file_path in enumerate(file_paths):
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # Filter values less than 100
        df_filtered = df[df['0'] < 100]  # Assuming the column containing the values is named '0'
        
        # Plot the filtered data on separate subplot
        axes[i].plot(df_filtered.index, df_filtered.iloc[:, 1], label=file_path)  # Assuming the second column contains the data to plot
        axes[i].set_xlabel('Index')  # Customize the X-axis label
        axes[i].set_ylabel('Y-axis Label')  # Customize the Y-axis label
        axes[i].set_title('Title')  # Customize the subplot title
        axes[i].legend()  # Add legend to subplot
        axes[i].grid(True)  # Add grid to subplot

    plt.tight_layout()  # Adjust subplots layout
    plt.show()
if __name__ == "__main__":
    file = ['csv_data/Test_01/real_Right_Test_01_19.csv',
            'csv_data/Test_02/real_Right_Test_02_8.csv',
            'csv_data/Test_03/real_Right_Test_03_12.csv',
            'csv_data/Test_04/real_Right_Test_04_16.csv']
    
    plotmuti(file)