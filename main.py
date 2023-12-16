import pandas as pd
import matplotlib as plt
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv('Salary.csv')
X = dataset.iloc[:, : 1].values
y = dataset.iloc[:, -1].values
