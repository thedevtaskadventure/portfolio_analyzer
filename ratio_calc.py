import pandas as pd


# To be implemented
# def return_on_investment(stock_data):
# def gain_or_loss(stock_data):
# def percentage_gain_loss(stock_data):
# def break_even_price(stock_data):

def return_on_investment(stock_data):
    # Get current price and purchase price
    current_price = stock_data["Current Price"]
    purchase_price = stock_data["Purchase Price"]

    # Get the list of ticker symbols
    ticker_list = stock_data["Ticker Symbol"]

    # Create a new dataframe with column "ROI" that shows the Return On Investment based on the formula
    return_data = pd.DataFrame({"ROI": ((current_price - purchase_price) / purchase_price) * 100})

    # Join the ticker list to the result dataframe and return it
    return_data = return_data.join(ticker_list)

    # Make the column order pretty
    column_order = ["Ticker Symbol", "ROI"]
    return_data = return_data[column_order]

    return return_data


def gain_or_loss(stock_data):
    # Get current price and purchase price
    current_price = stock_data["Current Price"]
    purchase_price = stock_data["Purchase Price"]

    # Get the list of ticker symbols
    ticker_list = stock_data["Ticker Symbol"]

    # Create a new dataframe with column "ROI" that shows the Return On Investment based on the formula
    return_data = pd.DataFrame({"Gain/Loss": current_price - purchase_price})

    # Join the ticker list to the result dataframe and return it
    return_data = return_data.join(ticker_list)

    # Make the column order pretty
    column_order = ["Ticker Symbol", "Gain/Loss"]
    return_data = return_data[column_order]

    return return_data


def break_even_price(stock_data, roi):
    # Get current price and purchase price
    purchase_price = stock_data["Purchase Price"]

    # Get the list of ticker symbols
    ticker_list = stock_data["Ticker Symbol"]

    # Create a new dataframe with column "ROI" that shows the Return On Investment based on the formula
    data_comp = (1 + (roi["ROI"] / 100))
    return_data = pd.DataFrame({"Break Even Price": purchase_price / data_comp})

    # Join the ticker list to the result dataframe and return it
    return_data = return_data.join(ticker_list)

    # Make the column order pretty
    column_order = ["Ticker Symbol", "Break Even Price"]
    return_data = return_data[column_order]

    return return_data


