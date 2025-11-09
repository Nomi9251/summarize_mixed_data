#Data Summary.py
# This scrpts calculate basic statistics for a dataset
# Created by Noman 

import pandas as pd

def summarized_data(file_path):
    """Read a CSV file and print summary statistics."""
    try:
        data = pd.read_csv(file_path)
        print("Dataset loaded Successfully!")
        print(""\n📊 Basic information: ")
        print(data.info())
        print("n📈 Basic Statistics: ")
        print(df.describe())

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main":
    print("This is a data summarization tool for GSoC workflow practice.")


    
