import yfinance as yf
import pandas as pd
import numpy as np

ticker = "SPY"
data = yf.download(ticker, start="2009-03-01", end="2022-04-22")

data["daily_return"] = data["Adj Close"].pct_change()
data["state"] = np.where(data["daily_return"] >= 0, "up", "down")

print(data)

def count_up_after_downs(data, n):
    conditions = [data["state"] == "up"]
    down_conditions = [data["state"].shift(i) == "down" for i in range(1, n+1)]
    # Check that the day after the sequence is also an "up" day to avoid overlaps
    no_overlap = [data["state"].shift(-n-1) == "up"]
    
    return len(data[np.all(conditions, axis=0) & np.all(down_conditions, axis=0) & np.all(no_overlap, axis=0)])

def count_total_downs(data, n):
    conditions = [data["state"] == "up"]
    down_conditions = [data["state"].shift(i) == "down" for i in range(1, n+1)]
    return len(data[np.all(conditions, axis=0) & np.all(down_conditions, axis=0)])

for n in [1, 2, 3, 4, 5, 6, 7, 8]:
    up_after_downs = count_up_after_downs(data, n)
    total_downs = count_total_downs(data, n)
    odds = up_after_downs / total_downs if total_downs != 0 else 0
    print("\n")
    print(f"Odds for at least one up day after {n} down days: {odds:.5f}")
    print(f"Number of occurrences of {n} consecutive down days followed by at least one up day: {up_after_downs}")
