import yfinance as yf
import pandas as pd
import numpy as np

ticker = "SPY"
data = yf.download(ticker, start="2009-03-01", end="2022-04-22")

data["daily_return"] = data["Adj Close"].pct_change()
data["state"] = np.where(data["daily_return"] >= 0, "up", "down")

print(data)

def count_down_after_ups(data, n):
    conditions = [data["state"] == "down"]
    up_conditions = [data["state"].shift(i) == "up" for i in range(1, n+1)]
    # Check that the day after the sequence is also a "down" day to avoid overlaps
    no_overlap = [data["state"].shift(-n-1) == "down"]
    
    return len(data[np.all(conditions, axis=0) & np.all(up_conditions, axis=0) & np.all(no_overlap, axis=0)])

def count_total_ups(data, n):
    conditions = [data["state"] == "down"]
    up_conditions = [data["state"].shift(i) == "up" for i in range(1, n+1)]
    return len(data[np.all(conditions, axis=0) & np.all(up_conditions, axis=0)])

for n in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
    down_after_ups = count_down_after_ups(data, n)
    total_ups = count_total_ups(data, n)
    odds = down_after_ups / total_ups if total_ups != 0 else 0
    print("\n")
    print(f"Odds for at least one down day after {n} up days: {odds:.5f}")
    print(f"Number of occurrences of {n} consecutive up days followed by at least one down day: {down_after_ups}")
