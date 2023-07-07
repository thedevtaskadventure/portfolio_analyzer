import data_prep
import ratio_calc

# TODO implement sorting mechanism
# TODO also give suggestions based on metrics


# This is a sample Python script.
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Function to get the data from a portfolio (upload portfolio in the system)

    # portfolio_data = collect_portfolio(input file)
    stock_data = data_prep.read_input_data()

    print("Welcome to the Portfolio Analyzer by Meeher Kapoor \n")
    print("Please ensure you have uploaded your portfolio in CSV format containing the columns in the following order "
          "\n")

    print("*----------------ANALYZING PORTFOLIO BEEP BOOP----------------------* \n")
    print("Choose what type of result you would like to see related to your p"
          "ortfolio \n")
    print("1. Return On Investment (ROI) \n")
    print("2. Gain/Loss Ratio \n")
    print("3. Break Even Metrics \n")
    print("4. Exit \n")

    print("*--------------------MAKE YOUR CHOICE------------------------------* \n")

    choice = -1
    while choice != 4:
        choice = int(input("Select your option or press 4 to exit :  "))
        if choice == 1:
            roi = ratio_calc.return_on_investment(stock_data)
            print("Here is your Return of Investment in % \n")
            print("*-------------------------------------------------------------------------* \n")
            print(roi)
            continue
        elif choice == 2:
            gain_or_loss = ratio_calc.gain_or_loss(stock_data)
            print("Here is your Gain/Loss Ratios \n")
            print("*-------------------------------------------------------------------------* \n")
            print(gain_or_loss)
            continue
        elif choice == 3:
            roi = ratio_calc.return_on_investment(stock_data)
            break_even = ratio_calc.break_even_price(stock_data, roi)
            print("Here is your Break Even Ratios \n")
            print("*-------------------------------------------------------------------------* \n")
            print(break_even)
            continue
        elif choice == 4:
            exit()
        else:
            print("Invalid Input")
            continue
