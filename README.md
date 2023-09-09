# Trading Profit Loss Diagram and Simple Trading Probabilities

### Part 1. Trader Performance
Quick and easy calculation for profit loss of your trades over time using Python. Track your performance in trading with these simple charts. 

### Part 2. Stock Market Data
Some basic mean reversion problability calculations to get you started.

## Prerequisites

```
pip3 install pandas
pip3 install matplotlib
pip3 install yfinance
pip3 install numpy
pip3 install pandas
pip3 install scipy
pip3 install seaborn
```
## Part 1. Trader Performance
### The Data
For we use the trader's data the input `report.csv` format is as follows of all the trades made:

```
CloseTime,Instrument,Profit/Loss
DD/MM/YYYY,USA 500, 00000.00
DD/MM/YYYY,USA 500, -00000.00
```


### The Result
Results for  profit_loss.py shows all the trades over time.

<img width="100%" alt="Screenshot 2023-09-08 at 18 38 38" src="https://github.com/ThomasAFink/trading-profit-loss-diagram/assets/53316058/f5a2c1e9-e7ed-49dc-9c5f-1408dd53bdc9">

profit_loss_distributions.py shows a normal bell curve of all the trader's trades. Most of my trades are immediately stopped out just below $0.

<img width="49%" alt="Screenshot 2023-09-09 at 21 24 37" src="https://github.com/ThomasAFink/trading-profit-loss-diagram-and-simple-trading-probabilities/assets/53316058/a1a4e946-e77b-44e7-85a6-582be23aa93d">

<img width="49%" alt="Screenshot 2023-09-09 at 21 24 23" src="https://github.com/ThomasAFink/trading-profit-loss-diagram-and-simple-trading-probabilities/assets/53316058/38687324-a320-476e-9851-43533cb41942">


trader_prob_of_profit.py shows the odds of a trader being profitable on a trade. I am a profitable trader with 143% yoy and yet in stark contrast my odds of profit on a single trade are 30:70. More importantly, I split these odds into six categories. While I am doing significantly better on larger trades, I am significantly underperforming on smaller trades, and that is where I need to improve. This could best be remedied by moving my stop-loss orders just above breakeven, rather than just below.

Prob of profit:  29.411764705882355 Prob of loss:  70.27863777089783

Net of profit/loss:  *******

<img width="1386" alt="Screenshot 2023-09-09 at 21 28 51" src="https://github.com/ThomasAFink/trading-profit-loss-diagram-and-simple-trading-probabilities/assets/53316058/c3c34031-d6c6-40ab-bcff-10cf9b0ca638">





## Part 2. Stock Markert Data


Results for prob_down_day.py

Key Insights:
Probability P(n) gives the odds of observing a "down day" after n consecutive "up days".
This is crucial for traders and analysts to understand potential bearish reversals after bullish runs.

<img width="100%" alt="Screenshot 2023-09-08 at 18 34 51" src="https://github.com/ThomasAFink/trading-profit-loss-diagram/assets/53316058/9e22fb23-daed-4b5f-832d-aa7b8d1f4df8">


```
[*********************100%%**********************]  1 of 1 completed
                  Open        High         Low       Close   Adj Close     Volume  daily_return state
Date
2009-03-02   72.519997   73.919998   70.370003   70.599998   53.453293  426452600           NaN  down
2009-03-03   71.610001   71.699997   69.639999   70.070000   53.052017  443761000     -0.007507  down
2009-03-04   71.230003   72.870003   70.070000   71.730003   54.308846  462753100      0.023690    up
2009-03-05   70.099998   71.730003   68.169998   68.800003   52.090443  485549400     -0.040848  down
2009-03-06   69.400002   70.449997   67.099998   68.919998   52.181305  490470000      0.001744    up
...                ...         ...         ...         ...         ...        ...           ...   ...
2022-04-14  443.549988  444.730011  437.679993  437.790009  428.903107   97869500     -0.012452  down
2022-04-18  436.809998  439.750000  435.609985  437.970001  429.079468   66002500      0.000411    up
2022-04-19  437.859985  445.799988  437.679993  445.040009  436.005951   77821000      0.016143    up
2022-04-20  446.920013  447.570007  443.480011  444.709991  435.682617   65224400     -0.000742  down
2022-04-21  448.540009  450.010010  437.100006  438.059998  429.167633   85417300     -0.014954  down

[3310 rows x 8 columns]


Odds for at least one down day after 1 up days: 0.43489
Number of occurrences of 1 consecutive up days followed by at least one down day: 364


Odds for at least one down day after 2 up days: 0.43137
Number of occurrences of 2 consecutive up days followed by at least one down day: 198


Odds for at least one down day after 3 up days: 0.43173
Number of occurrences of 3 consecutive up days followed by at least one down day: 117


Odds for at least one down day after 4 up days: 0.43750
Number of occurrences of 4 consecutive up days followed by at least one down day: 63


Odds for at least one down day after 5 up days: 0.45070
Number of occurrences of 5 consecutive up days followed by at least one down day: 32


Odds for at least one down day after 6 up days: 0.39474
Number of occurrences of 6 consecutive up days followed by at least one down day: 15


Odds for at least one down day after 7 up days: 0.33333
Number of occurrences of 7 consecutive up days followed by at least one down day: 6


Odds for at least one down day after 8 up days: 0.55556
Number of occurrences of 8 consecutive up days followed by at least one down day: 5


Odds for at least one down day after 9 up days: 0.00000
Number of occurrences of 9 consecutive up days followed by at least one down day: 0


Odds for at least one down day after 10 up days: 0.50000
Number of occurrences of 10 consecutive up days followed by at least one down day: 1


Odds for at least one down day after 11 up days: 0.00000
Number of occurrences of 11 consecutive up days followed by at least one down day: 0


Odds for at least one down day after 12 up days: 1.00000
Number of occurrences of 12 consecutive up days followed by at least one down day: 1

```

Results for prob_up_day.py

Key Insights:
Probability P(n) provides the odds of witnessing an "up day" after n consecutive "down days".
Essential knowledge for those looking to capitalize on potential bullish reversals after bearish sequences.

<img width="100%" alt="Screenshot 2023-09-08 at 18 35 12" src="https://github.com/ThomasAFink/trading-profit-loss-diagram/assets/53316058/0f6ee8ac-d1c2-4246-906c-1f6c3f09e1ef">


```
[*********************100%%**********************]  1 of 1 completed
                  Open        High         Low       Close   Adj Close     Volume  daily_return state
Date
2009-03-02   72.519997   73.919998   70.370003   70.599998   53.453278  426452600           NaN  down
2009-03-03   71.610001   71.699997   69.639999   70.070000   53.051991  443761000     -0.007507  down
2009-03-04   71.230003   72.870003   70.070000   71.730003   54.308830  462753100      0.023691    up
2009-03-05   70.099998   71.730003   68.169998   68.800003   52.090446  485549400     -0.040848  down
2009-03-06   69.400002   70.449997   67.099998   68.919998   52.181293  490470000      0.001744    up
...                ...         ...         ...         ...         ...        ...           ...   ...
2022-04-14  443.549988  444.730011  437.679993  437.790009  428.903076   97869500     -0.012452  down
2022-04-18  436.809998  439.750000  435.609985  437.970001  429.079498   66002500      0.000411    up
2022-04-19  437.859985  445.799988  437.679993  445.040009  436.005951   77821000      0.016143    up
2022-04-20  446.920013  447.570007  443.480011  444.709991  435.682648   65224400     -0.000742  down
2022-04-21  448.540009  450.010010  437.100006  438.059998  429.167664   85417300     -0.014954  down

[3310 rows x 8 columns]


Odds for at least one up day after 1 down days: 0.58662
Number of occurrences of 1 consecutive down days followed by at least one up day: 491


Odds for at least one up day after 2 down days: 0.53521
Number of occurrences of 2 consecutive down days followed by at least one up day: 190


Odds for at least one up day after 3 down days: 0.57792
Number of occurrences of 3 consecutive down days followed by at least one up day: 89 


Odds for at least one up day after 4 down days: 0.50746
Number of occurrences of 4 consecutive down days followed by at least one up day: 34 


Odds for at least one up day after 5 down days: 0.53846
Number of occurrences of 5 consecutive down days followed by at least one up day: 14


Odds for at least one up day after 6 down days: 0.62500
Number of occurrences of 6 consecutive down days followed by at least one up day: 5


Odds for at least one up day after 7 down days: 0.50000
Number of occurrences of 7 consecutive down days followed by at least one up day: 2


Odds for at least one up day after 8 down days: 1.00000
Number of occurrences of 8 consecutive down days followed by at least one up day: 1
```


<b> Note: The aforementioned probabilities are calculated based on historical data and patterns, and while useful, they should be interpreted with caution. Always consider other factors and perform further analysis before making any investment decisions.</b>
