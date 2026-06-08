import pandas as pd

# ==============================================================================
# STEP 1: LOAD THE DATASETS FROM EXCEL
# ==============================================================================
# We use read_excel to open the workbook and sheet_name to grab specific tabs
orders_df = pd.read_excel("Aesthetics_Project.xlsx", sheet_name="Orders")
artisan_df = pd.read_excel("Aesthetics_Project.xlsx", sheet_name="Artisan_Operations")

# ==============================================================================
# STEP 2: BUSINESS QUESTION 1 - TOP REVENUE-GENERATING CATEGORY
# ==============================================================================
product_revenue = orders_df.groupby("product_category")["revenue_usd"].sum()
product_revenue_sorted = product_revenue.sort_values(ascending=False)

top_product = product_revenue_sorted.index[0]
top_product_revenue = product_revenue_sorted.iloc[0]

event_revenue = orders_df.groupby("event_type")["revenue_usd"].sum().sort_values(ascending=False)
top_event = event_revenue.index[0]
top_event_revenue = event_revenue.iloc[0]

# ==============================================================================
# STEP 3: BUSINESS QUESTION 2 - CALCULATE DELAYED ORDERS
# ==============================================================================
delayed_count = (orders_df["delivery_status"] == "Delayed").sum()
total_orders = len(orders_df)
delay_rate = (delayed_count / total_orders) * 100

# ==============================================================================
# STEP 4: BUSINESS QUESTION 3 - ARTISAN UTILIZATION ANALYSIS
# ==============================================================================
craft_groups = artisan_df.groupby("craft_type").agg({
    "active_orders": "sum",
    "weekly_capacity": "sum"
})

craft_groups["utilization_pct"] = (craft_groups["active_orders"] / craft_groups["weekly_capacity"]) * 100
craft_groups_sorted = craft_groups.sort_values(by="utilization_pct", ascending=False)

top_utilized_craft = craft_groups_sorted.index[0]
top_utilization_val = craft_groups_sorted.iloc[0]["utilization_pct"]

# ==============================================================================
# STEP 5: GENERATE LEADERSHIP REPORT SUMMARY
# ==============================================================================
print("\n" + "="*60)
print("             AESTHETICS WEEKLY OPERATIONS REPORT          ")
print("                    LEADERSHIP REVIEW                     ")
print("="*60)

print(f"\n[+] REVENUE & DEMAND INSIGHTS:")
print(f"  - Top Product Category: {top_product} (${top_product_revenue:,.2f})")
print(f"  - Top Event Driver:     {top_event} (${top_event_revenue:,.2f})")

print(f"\n[+] FULFILLMENT & LOGISTICS RISK:")
print(f"  - Total Delayed Orders: {delayed_count} out of {total_orders} total orders")
print(f"  - Current Delay Rate:   {delay_rate:.1f}%")

print(f"\n[+] CAPACITY & UTILIZATION METRICS:")
print(f"  - Most Strained Artisan Group: {top_utilized_craft} Artisans")
print(f"  - Group Current Utilization:   {top_utilization_val:.1f}%")

print("\n" + "="*60)
print("             STRATEGIC BUSINESS RECOMMENDATIONS           ")
print("="*60)
print("1. PRODUCT FOCUS: Capitalize on High-Value Demand")
print(f"   Double-down on sales efforts for '{top_product}' items tailored to '{top_event}' settings.")

print("\n2. RISK MITIGATION: Introduce Milestone Tracking to Lower Delays")
print(f"   With a {delay_rate:.1f}% operational delay rate, implement regional checkpoints.")

print("\n3. SUPPLY MANAGEMENT: Balance Capacity & Expand Training")
print(f"   The '{top_utilized_craft}' artisan cohort is operating at a high strain level ({top_utilization_val:.1f}%).")
print("   Transition incoming orders to under-utilized craft groups to scale capacity.")
print("="*60)