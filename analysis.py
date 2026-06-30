import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file
df = pd.read_csv("data.csv")

print("Dataset:")
print(df)

# Basic Analysis
average_marks = df["Marks"].mean()
maximum_marks = df["Marks"].max()
minimum_marks = df["Marks"].min()

print("\nAverage Marks:", average_marks)
print("Maximum Marks:", maximum_marks)
print("Minimum Marks:", minimum_marks)

# Bar Chart
plt.figure(figsize=(8,5))
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("bar_chart.png")
plt.show()

# Scatter Plot
plt.figure(figsize=(8,5))
plt.scatter(df["StudyHours"], df["Marks"])
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.savefig("scatter_plot.png")
plt.show()

# Heatmap
plt.figure(figsize=(6,4))

numeric_df = df[["Age", "Marks", "StudyHours"]]

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")
plt.savefig("heatmap.png")
plt.show()
