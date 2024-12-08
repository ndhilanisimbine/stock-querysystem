import os
import pandas as pd
from fetch_stock_data import fetch_stock_data

def test_fetch_stock_data():
    # Testing that data is fetched and saved correctly
    fetch_stock_data()
    assert os.path.exists("data/stocks.csv"), "Stock data file was not created."

    df = pd.read_csv("data/stocks.csv")
    assert not df.empty, "Stock data file is empty."
    assert "Symbol" in df.columns, "Missing 'Symbol' column in the data."
    assert "Sector" in df.columns, "Missing 'Sector' column in the data."
