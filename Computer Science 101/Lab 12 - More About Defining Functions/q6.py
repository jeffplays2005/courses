def get_user_selection():
    selection = int(input("Enter your selection: "))
    while selection < 0 or selection > 7:
        print("Invalid selection!")
        selection = int(input("Enter your selection: "))
    return selection

def get_amount():
    return float(input("Enter the amount of NZ dollars you want to convert: "))

def get_exchange_rate(currency_list, selection):
    return currency_list[selection - 1]

def get_currency(currency_name_list, selection):
    return currency_name_list[selection - 1]

def perform_currency_exchange(currency_list, rate_list):
    selection = get_user_selection()
    while selection != 0:
        amount = get_amount()
        exchanged = round(amount * get_exchange_rate(rate_list, selection), 2)
        currency_name = get_currency(currency_list, selection)
        if currency_name == "Japanese Yen": # when its yen
            exchanged = round((amount * get_exchange_rate(rate_list, selection)))
        print(f"${amount} NZ dollars = ${exchanged} {currency_name}")
        selection = get_user_selection()
        
currency_list = ["Pound Sterling", "US Dollars", "Euros", "Canadian Dollars",
                 "Australian Dollars", "Singaporean Dollars", "Japanese Yen"]
rate_list = [0.52, 0.62, 0.58, 0.84, 0.92, 0.84, 84.43]
perform_currency_exchange(currency_list, rate_list)