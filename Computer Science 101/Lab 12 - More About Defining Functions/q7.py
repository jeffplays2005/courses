def print_banner():
    print("""**********************
*A Currency Converter*
**********************""")

def print_menu(currency_list, rate_list):
    print("Select an operation:")
    for i in range(len(currency_list)):
        print(f"Enter {i + 1} to exchange NZ Dollars to {currency_list[i]} (1 NZD = {rate_list[i]} {currency_list[i]})")
    print("Enter 0 to exit the currency converter")

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

def print_exit_message():
    print("""Exiting the currency converter...
Have a good day!""")

def perform_currency_exchange(currency_list, rate_list):
    selection = get_user_selection()
    while selection != 0:
        amount = get_amount()
        exchanged = round(amount * get_exchange_rate(rate_list, selection), 2)
        currency_name = get_currency(currency_list, selection)
        if currency_name == "Japanese Yen": # when its yen
            exchanged = round((amount * get_exchange_rate(, selection)))
        print(f"${amount} NZ dollars = ${exchanged} {currency_name}")
        selection = get_user_selection()

def main():
    currency_list = ["Pound Sterling", "US Dollars", "Euros", "Canadian Dollars",
                     "Australian Dollars", "Singaporean Dollars", "Japanese Yen"]
    rate_list = [0.52, 0.62, 0.58, 0.84, 0.92, 0.84, 84.43]
    
    print_banner()
    print()
    print_menu(currency_list, rate_list)
    print()
    perform_currency_exchange(currency_list, rate_list)
    print()
    print_exit_message()

main()

# better
def print_banner():
    print("""**********************
*A Currency Converter*
**********************""")

def print_menu(currency_list, rate_list):
    print("Select an operation:")
    for i in range(len(currency_list)):
        print(f"Enter {i + 1} to exchange NZ Dollars to {currency_list[i]} (1 NZD = {rate_list[i]} {currency_list[i]})")
    print("Enter 0 to exit the currency converter")

def get_user_selection():
    selection = int(input("Enter your selection: "))
    while selection < 0 or selection > 7:
        print("Invalid selection!")
        selection = int(input("Enter your selection: "))
    return selection

def print_exit_message():
    print("""Exiting the currency converter...
Have a good day!""")

def perform_currency_exchange(currency_list, rate_list):
    selection = get_user_selection()
    while selection != 0:
        amount = float(input("Enter the amount of NZ dollars you want to convert: "))
        exchanged = round(amount * rate_list[selection-1], 2)
        currency_name = currency_list[selection - 1]
        if currency_name == "Japanese Yen": # when its yen
            exchanged = round((amount * get_exchange_rate(rate_list, selection)))
        print(f"${amount} NZ dollars = ${exchanged} {currency_name}")
        selection = get_user_selection()

def main():
    currency_list = ["Pound Sterling", "US Dollars", "Euros", "Canadian Dollars",
                     "Australian Dollars", "Singaporean Dollars", "Japanese Yen"]
    rate_list = [0.52, 0.62, 0.58, 0.84, 0.92, 0.84, 84.43]
    
    print_banner()
    print()
    print_menu(currency_list, rate_list)
    print()
    perform_currency_exchange(currency_list, rate_list)
    print()
    print_exit_message()

main()