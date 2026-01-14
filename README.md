# Trader Performance vs Market Sentiment

## Objective
Analyze how Bitcoin market sentiment affects trader profitability and behavior using real historical trade data and the Fear & Greed Index.

## Dataset
- Hyperliquid historical trades
- Bitcoin Fear & Greed Index

## Methodology
1. Clean and align datasets by date
2. Merge trader activity with daily market sentiment
3. Compute profitability and behavioral metrics
4. Visualize results and extract insights

## Key Findings
- Traders achieve highest profitability during Extreme Greed
- Fear regimes offer strong volatility-based opportunities
- Neutral and Extreme Fear periods are the weakest performance regimes

## How to Run
```bash
pip install -r requirements.txt
python sentiment_analysis.py
