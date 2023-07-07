import pandas as pd


# Get the data in a dataframe

# Output : Profit between purchase price and current price for all tickers
def read_input_data():
    read_stock_data = pd.read_csv("stock_training.csv")
    # Returns the CSV sheet as a pandas dataframe
    return read_stock_data
