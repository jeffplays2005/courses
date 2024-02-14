def print_menu(currency_list, rate_list):
    print("Select an operation:")
    for i in range(len(currency_list)):
        print(f"Enter {i + 1} to exchange NZ Dollars to {currency_list[i]} (1 NZD = {rate_list[i]} {currency_list[i]})")
    print("Enter 0 to exit the currency converter")