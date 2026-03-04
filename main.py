from src.apps.connectors.conectores import download_from_yfinance, download_from_duckascopy, download_from_alphavantage

print(download_from_yfinance('AAPL', '2020-01-01', '2020-12-31'))