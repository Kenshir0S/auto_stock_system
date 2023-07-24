import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import yfinance as yf
from yahoofinancials import YahooFinancials


ticker = yf.Ticker("usmv")
tsd = ticker.history(period="10y")
print(tsd.head())