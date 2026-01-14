import pandas as pd

# -----------------------------
# 1. Load Datasets

historical = pd.read_csv("historical_data.csv")
sentiment = pd.read_csv("fear_greed_index.csv")

# -----------------------------
# 2. Preprocess & Align Dates

historical['date'] = pd.to_datetime(
    historical['Timestamp IST'], dayfirst=True
).dt.date

sentiment['date'] = pd.to_datetime(sentiment['date']).dt.date

# -----------------------------
# 3. Merge Datasets

data = historical.merge(
    sentiment[['date', 'classification']], 
    on='date', 
    how='left'
)

data.dropna(subset=['classification'], inplace=True)

# -----------------------------
# 4. Core Performance Analysis

performance_summary = (
    data
    .groupby('classification')['Closed PnL']
    .agg(['count', 'sum', 'mean'])
    .reset_index()
    .sort_values('mean', ascending=False)
)

print("\nTrader Performance by Market Sentiment\n")
print(performance_summary)

# -----------------------------
# 5. Additional Behavioral Metrics

behavioral_metrics = (
    data
    .groupby('classification')
    .agg(
        avg_trade_size=('Size USD', 'mean'),
        avg_pnl=('Closed PnL', 'mean'),
        trade_count=('Closed PnL', 'count')
    )
    .reset_index()
)

print("\nBehavioral Metrics\n")
print(behavioral_metrics)

# -----------------------------
# 6. Simple Visualization 

import matplotlib.pyplot as plt

plt.figure()
plt.bar(performance_summary['classification'], performance_summary['mean'])
plt.xticks(rotation=30)
plt.title("Average Profit per Trade by Market Sentiment")
plt.ylabel("Average PnL")
plt.xlabel("Market Sentiment")
plt.tight_layout()
plt.show()
