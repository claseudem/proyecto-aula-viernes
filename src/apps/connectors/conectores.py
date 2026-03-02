import yfinance as yf
import datetime

from datetime import datetime, timedelta
import dukascopy_python
from dukascopy_python.instruments import INSTRUMENT_VCCY_DSH_USD, INSTRUMENT_FX_MAJORS_EUR_USD, INSTRUMENT_FX_MAJORS_GBP_USD

import requests
import pandas as pd

def download_from_yfinance(ticker, start_date, end_date):
    return yf.download(ticker, start=start_date, end=end_date)

def download_from_duckascopy(start, end, instrument, interval, offer_side):
    return dukascopy_python.fetch(
        instrument,
        interval,
        offer_side,
        start,
        end,
    )

def download_from_alphavantage(symbol, api_key="demo"):
    # build the request URL, you can replace "demo" with your own key
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}'
    r = requests.get(url)
    data = r.json()
    # return a DataFrame as in the example
    return pd.DataFrame(data.get("Time Series (Daily)", {})).transpose()