import pandas as pd
import numpy as np
import tensorflow as tf
import seaborn as sns
def data_cleaner(data):
    data=data.drop_duplicates
    data=data.dropna(how='all')
    data["date"] = pd.to_datetime(data["date"], errors='coerce')  # Convert to datetime
    data["Channel Title"] = data["Channel Title"].str.strip().str.lower()  # Normalize channel names
    return data
def data_validation(data):
    # Drop rows where date conversion failed
    data = data[data["date"].notna()] 
    # Validate channels (must contain "@")
    data = data[data["channel"].str.startswith("@")]
    return data