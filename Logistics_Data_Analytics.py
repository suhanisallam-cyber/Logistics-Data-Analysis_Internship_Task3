import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Load Logistics Dataset
df = pd.read_csv("logistics_shipments_demo.csv")

print("=== WEEK 3: ADVANCED ANALYSIS & VISUALIZATION ===")

print("\nDataset Preview:")
print(df.head())

# Derive Transport Cost based on weight and mode factor
mode_factor = {
    "Air": 2.5,
    "Road": 1.2,
    "Rail": 0.8,
    "Maritime": 0.5
}

df["transport_cost_usd"] = df.apply(
    lambda x: (
        x["shipment_weight_kg"]
        * 0.4
        * mode_factor.get(x["transport_mode"], 1.0)
    )
    + np.random.normal(0, 5),
    axis=1
)

# On-Time Status
df["on_time_status"] = np.where(
    df["delivery_time_days"] > 6.0,
    "Delayed",
    "On-Time"
)

print("\nTransport Cost and On-Time Status calculated successfully.")

print("\nUpdated Dataset:")
print(df.head())

# Step 2: Visualization
sns.set_theme(style="whitegrid")

# Figure 1: Delivery Time Distribution
plt.figure(figsize=(8, 5))

sns.histplot(
    df["delivery_time_days"],
    bins=10,
    kde=True
)

plt.title("Delivery Time Distribution")
plt.xlabel("Delivery Time (Days)")
plt.ylabel("Number of Shipments")
plt.tight_layout()
plt.savefig("delivery_time_distribution.png", dpi=300, bbox_inches="tight")
plt.show()

#Visualization
sns.set_theme(style="whitegrid")

sns.countplot(
    data=df,
    x="warehouse_origin",
    hue="on_time_status"
)

# Figure 2: Warehouse Performance
plt.title("Shipment Status by Warehouse Origin", fontsize=10, fontweight="bold")
plt.tight_layout()
plt.savefig("shipment_status_by_warehouse.png", dpi=300, bbox_inches="tight")
plt.show()


