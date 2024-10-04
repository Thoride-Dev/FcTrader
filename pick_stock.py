import pandas as pd

#pick a stock from the s&p 500 where a higher score = better stock
def make_pick(score):
    #get symbol column from stock markets
    df = pd.read_csv('tickers100324.csv')
    symbols = df['Symbol'].tolist()

    #lerp score between 0 and 10
    low = 10 
    high = 3
    lerp_score = (score - low) / (high - low)
    lerp_score = lerp_score * len(symbols)
    lerp_score = round(lerp_score)

    #pick stock
    print("Stock position: " + str(lerp_score))
    stock = symbols[lerp_score]
    return stock

#testing
#print(pick_stock(627))
