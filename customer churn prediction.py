import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Step 1: Simulate Customer Data (Telecom/SaaS Company Scenario)
np.random.seed(100)
n_customers = 300

data = {
    'Customer_ID': range(5001, 5001 + n_customers),
    'Age': np.random.randint(18, 65, n_customers),
    'Tenure_Months': np.random.randint(1, 36, n_customers),
    'Monthly_Charges': np.random.uniform(500, 3000, n_customers).round(2),
    'Support_Tickets': np.random.randint(0, 5, n_customers),
    # Churn: 1 matlab customer gaya, 0 matlab ruka hai
    'Churn': np.random.choice([0, 1], n_customers, p=[0.75, 0.25]),
}

df = pd.DataFrame(data)

# Step 2: Data Analysis & Insights
print('--- Customer Churn Dataset Preview ---')
print(df.head())

print('\n--- Overall Metrics ---')
total_customers = len(df)
churned_customers = df['Churn'].sum()
churn_rate = (churned_customers / total_customers) * 100
print(f'Total Customers: {total_customers}')
print(f'Churned Customers: {churned_customers}')
print(f'Overall Churn Rate: {churn_rate:.2f}%')

print('\n--- Average Monthly Charges by Churn Status ---')
churn_summary = df.groupby('Churn')[['Monthly_Charges', 'Support_Tickets']].mean().round(2)
print(churn_summary)

# Step 3: Visualization (Impact of Support Tickets on Churn)
plt.figure(figsize=(8, 4))
df.groupby('Support_Tickets')['Churn'].mean().plot(kind='bar', color='salmon')
plt.title('Customer Churn Rate vs. Support Tickets Raised')
plt.xlabel('Number of Support Tickets')
plt.ylabel('Churn Rate (Proportion)')
plt.xticks(rotation=0)

plt.tight_layout()
plt.savefig('customer_churn_analysis.png')
print('\n[Success] Analysis complete! Chart saved as "customer_churn_analysis.png".')
