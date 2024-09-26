import pandas as pd
import numpy as np

diabetes_data = pd.read_csv("diabetes.csv")

print(diabetes_data.columns)
print(len(diabetes_data))

print(diabetes_data.isnull().sum())

print(diabetes_data.describe())

diabetes_data[["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]] = diabetes_data[["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]].replace(0, np.nan)
print(diabetes_data.isnull().sum())

print(diabetes_data[diabetes_data.isnull().any(axis=1)])

print(diabetes_data["Outcome"].unique())


# Replace 'O' with 0 in the Outcome column
diabetes_data['Outcome'] = diabetes_data['Outcome'].replace('O', 0)

# Convert the Outcome column to type int64
diabetes_data['Outcome'] = diabetes_data['Outcome'].astype('int64')

# Print the unique values to verify
print(diabetes_data['Outcome'].unique())