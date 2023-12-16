import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

dataset = pd.read_csv('Salary.csv')
X = dataset.iloc[:, : 1].values
y = dataset.iloc[:, -1].values

regressor = LinearRegression()
regressor.fit(X, y)

plt.scatter(X, y, color='red')
plt.plot(X, regressor.predict(X), color='blue')
plt.title('Salary vs Experience')
plt.xlabel('Experience')
plt.ylabel('Salary')
plt.show()