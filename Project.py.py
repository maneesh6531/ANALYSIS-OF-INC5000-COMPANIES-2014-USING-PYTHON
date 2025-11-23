import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('Data Set- Inc5000 Company List_2014.csv')

# Check basic info
print("Data Overview:")
print(df.info())

# Summary statistics
print("\nSummary Statistics:")
print(df[['growth', 'revenue', 'workers', 'yrs_on_list']].describe())

# Top 10 industries by count
industry_counts = df['industry'].value_counts().head(10)
print("\nTop 10 Industries by Company Count:")
print(industry_counts)

# Average growth rate by industry
avg_growth_by_industry = df.groupby('industry')['growth'].mean().sort_values(ascending=False).head(10)
print("\nTop 10 Industries by Average Growth Rate:")
print(avg_growth_by_industry)

# Visualization
plt.figure(figsize=(12, 6))
sns.barplot(x=industry_counts.values, y=industry_counts.index, palette='viridis')
plt.title('Top 10 Industries in Inc5000 List (2014)')
plt.xlabel('Number of Companies')
plt.ylabel('Industry')
plt.tight_layout()
plt.show()


# Top 10 states with most companies
state_counts = df['state_s'].value_counts().head(10)
print("\nTop 10 States with Most Inc5000 Companies:")
print(state_counts)

# Average growth and revenue by state
state_stats = df.groupby('state_s').agg({'growth': 'mean', 'revenue': 'mean'}).sort_values('growth', ascending=False).head(10)
print("\nTop 10 States by Average Growth Rate:")
print(state_stats)

# Visualization
plt.figure(figsize=(12, 6))
sns.barplot(x=state_counts.values, y=state_counts.index, palette='rocket')
plt.title('Top 10 States with Most Inc5000 Companies (2014)')
plt.xlabel('Number of Companies')
plt.ylabel('State')
plt.tight_layout()
plt.show()




# Scatter plot of growth vs. revenue (log scale)
plt.figure(figsize=(10, 6))
sns.scatterplot(x='growth', y='revenue', data=df, alpha=0.6, hue='industry', palette='tab20', legend=False)
plt.title('Growth Rate vs Revenue by Industry')
plt.xlabel('Growth Rate (%)')
plt.ylabel('Revenue ($)')
plt.yscale('log')  # Log scale for better visualization
plt.tight_layout()
plt.show()

# Correlation between growth and revenue
correlation = df['growth'].corr(df['revenue'])
print(f"\nCorrelation between Growth and Revenue: {correlation:.2f}")
















# Distribution of company sizes
plt.figure(figsize=(10, 6))
sns.histplot(df['workers'], bins=30, kde=True, color='purple')
plt.title('Distribution of Company Sizes (Number of Workers)')
plt.xlabel('Number of Workers')
plt.ylabel('Frequency')
plt.xlim(0, 1000)  # Limit to show majority of companies
plt.tight_layout()
plt.show()

# Does company size affect growth?
small_companies = df[df['workers'] < 100]['growth'].mean()
large_companies = df[df['workers'] >= 100]['growth'].mean()
print(f"\nAverage Growth Rate for Small Companies (<100 workers): {small_companies:.2f}%")
print(f"Average Growth Rate for Large Companies (≥100 workers): {large_companies:.2f}%")




# Growth rate distribution by years on the list
plt.figure(figsize=(10, 6))
sns.boxplot(x='yrs_on_list', y='growth', data=df, palette='Set2')
plt.title('Growth Rate Distribution by Years on Inc5000 List')
plt.xlabel('Years on List')
plt.ylabel('Growth Rate (%)')
plt.tight_layout()
plt.show()

# Do repeat companies have higher revenues?
repeat_companies = df[df['yrs_on_list'] > 1]['revenue'].mean()
new_companies = df[df['yrs_on_list'] == 1]['revenue'].mean()
print(f"\nAverage Revenue for Repeat Inc5000 Companies: ${repeat_companies:,.2f}")
print(f"Average Revenue for New Inc5000 Companies: ${new_companies:,.2f}")





# Top 10 companies by growth rate
top_growth = df.sort_values('growth', ascending=False).head(10)[['company', 'growth', 'revenue', 'industry', 'state_s']]
print("\nTop 10 Companies by Growth Rate:")
print(top_growth)

# Top 10 companies by revenue
top_revenue = df.sort_values('revenue', ascending=False).head(10)[['company', 'revenue', 'growth', 'industry', 'state_s']]
print("\nTop 10 Companies by Revenue:")
print(top_revenue)



# Select numerical columns for pair plot
numerical_cols = ['growth', 'revenue', 'workers', 'yrs_on_list']
pair_plot_data = df[numerical_cols]

# Create pair plot with customization
sns.set(style="ticks", font_scale=0.8)
pair_grid = sns.pairplot(
    pair_plot_data,
    diag_kind='kde',      # Kernel Density Estimate for diagonals
    plot_kws={'alpha': 0.6, 's': 20, 'edgecolor': 'k'},
    corner=True,          # Show only lower triangle for clarity
    height=2
)

# Add title and adjust layout
pair_grid.fig.suptitle("Pair Plot of Numerical Variables (Growth, Revenue, Workers, Years on List)", 
                      y=1.02, fontsize=12)
plt.tight_layout()
plt.show()



# Correlation heatmap for numerical variables
plt.figure(figsize=(8, 6))
numerical_corr = df[numerical_cols].corr()
sns.heatmap(numerical_corr, annot=True, fmt=".2f", cmap='coolwarm', square=True, linewidths=0.5)
plt.title('Correlation Heatmap of Numerical Features')
plt.tight_layout()
plt.show()
















