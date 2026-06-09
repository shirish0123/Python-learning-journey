import numpy as np
stocks = np.array([
    [100,102,101,105,110,108,115],  # Stock A
    [50,55,53,60,58,62,65],         # Stock B
    [200,198,205,210,215,220,218]   # Stock C
])

print(stocks.shape)
stockA=f"""
-----STOCK MARKET-----
Stock A-----
highest = {stocks[0].max()}
lowest = {stocks[0].min()}
average = {stocks[0].mean().round(2)}
volality = {stocks[0].std().round(2)}
"""

stockB=f"""
Stock B-----
highest = {stocks[1].max()}
lowest = {stocks[1].min()}
average = {stocks[1].mean().round(2)}
volality = {stocks[1].std().round(2)}
"""

stockC=f"""
Stock C -----
highest = {stocks[2].max()}
lowest = {stocks[2].min()}
average = {stocks[2].mean().round(2)}
volality = {stocks[2].std().round(2)}
"""
print(stockA)
print(stockB)
print(stockC)
Stocks=["stockA","stockB","stockC"]
vola= np.std(stocks,axis=1)
max_vola= vola.argmax()

starting=stocks[:,0]
ending=stocks[:,6]
growth = ((ending - starting) / starting) * 100
max_growth=growth.argmax()
min_growth=growth.argmin()

summary=f"""
-----SUMMARY-----
Best performer: {Stocks[max_growth]}
Worst performer: {Stocks[min_growth]}
Most volatile: {Stocks[max_vola]}"""
print(summary)
