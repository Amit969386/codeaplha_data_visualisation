import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("titanic.csv")

# Gender Distribution
df["Sex"].value_counts().plot(kind="bar")
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.show()
# Survival Count
df["Survived"].value_counts().plot(kind="bar")
plt.title("Survival Count")
plt.show()
# Passenger Class
df["Pclass"].value_counts().plot(kind="pie")
plt.title("Passenger Class Distribution")
plt.show()
# Age Distribution
df["Age"].hist()
plt.title("Age Distribution")
plt.show()