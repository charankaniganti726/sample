import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create screenshots folder automatically
os.makedirs("screenshots", exist_ok=True)

# Load dataset
df = pd.read_csv("sales_data.csv")

print("\nDataset:")
print(df)

# Style
sns.set_style("whitegrid")

# ==========================
# 1. LINE CHART
# ==========================

plt.figure(figsize=(10, 6))

sns.lineplot(
    x="Month",
    y="Sales",
    data=df,
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("screenshots/line_chart.png")
plt.close()

# ==========================
# 2. BAR CHART
# ==========================

plt.figure(figsize=(10, 6))

sns.barplot(
    x="Month",
    y="Sales",
    data=df
)

plt.title("Monthly Sales Comparison")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("screenshots/bar_chart.png")
plt.close()

# ==========================
# 3. PIE CHART
# ==========================

plt.figure(figsize=(8, 8))

plt.pie(
    df["Sales"],
    labels=df["Month"],
    autopct="%1.1f%%"
)

plt.title("Sales Contribution by Month")

plt.savefig("screenshots/pie_chart.png")
plt.close()

# ==========================
# 4. HISTOGRAM
# ==========================

plt.figure(figsize=(8, 6))

plt.hist(
    df["Sales"],
    bins=6
)

plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.tight_layout()

plt.savefig("screenshots/histogram_chart.png")
plt.close()

print("\nAll charts generated successfully!")
print("Saved in screenshots folder.")