import openpyxl
import pandas as pd
import numpy as np
import math
import datetime as dt
import pylab as pl


# FUNCTION #

def log_returns(price_t, price_1_t):
    try:
        return np.log(price_t/price_1_t)
    except:
        return None

# RUN #

def main():
    df = pd.read_excel('PythonTrainingStockPrices_Input.xlsx','Table')

    df['Nike_t_1'] = df['Nike'].shift(-1)
    df['Apple_t_1'] = df['Apple'].shift(-1)

    df['Nike_return'] = df.apply(lambda x: log_returns(x.Nike, x.Nike_t_1), axis=1)
    df['Apple_return'] = df.apply(lambda x: log_returns(x.Apple, x.Apple_t_1), axis=1)

    df.to_excel('PythonTrainingStockPrices_Output.xlsx','Table',header=True)

    #Calculate Count of Stock Data Points

    nike_count = df['Nike'].count()
    apple_count = df['Apple'].count()

    #Calculate Sum of Stock Returns

    nike_sum = df['Nike_return'].sum()
    apple_sum = df['Apple_return'].sum()

    #Calculate Variance of Stock Returns

    nike_var = df['Nike_return'][:-1].var()
    apple_var = df['Apple_return'][:-1].var()

    #Calculate Standard Deviation of Stock Returns

    nike_std = df['Nike_return'][:-1].std()
    apple_std = df['Apple_return'][:-1].std()

    #Calculate Covariance of Stocks

    nike_cov = df[['Nike']].cov()
    apple_cov = df[['Apple']].cov()

    #Calculate 99% of Historical Value at Risk

    

    df['Date'] = df['Date'].dt.strftime('%Y-%M-%D')

    # plot the data
    ax = df[-50:-1].plot(figsize=(10, 6),
                               title = 'Returns : Apple and Nike Returns over year 2015.',
                               x = ['Date'],
                               y = ['Nike_return', 'Apple_return'],
                               color = ['blue', 'cyan'],
                               kind = 'bar')

    ax.set_xlabel("Date")
    ax.set_ylabel("Stock Return")

    pl.show()

main()


