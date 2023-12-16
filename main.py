# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Loading the dataset
dataset = pd.read_csv('Salary.csv')

# Extracting the independent variable (Experience) and dependent variable (Salary)
X = dataset.iloc[:, : 1].values  # Assuming 'Experience' is in the first column
y = dataset.iloc[:, -1].values  # Assuming 'Salary' is in the last column

# Creating a linear regression model
regressor = LinearRegression()

# Fitting the linear regression model to the dataset
# This will find the line that best fits the data
regressor.fit(X, y)

# Plotting the actual data points
plt.scatter(X, y, color='red')

# Plotting the regression line
plt.plot(X, regressor.predict(X), color='blue')

# Adding title and labels to the plot
plt.title('Salary vs Experience')
plt.xlabel('Experience')
plt.ylabel('Salary')

# Displaying the plot
plt.show()
