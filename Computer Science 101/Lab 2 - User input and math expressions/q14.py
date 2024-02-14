principal = int(input("Enter the principal: "));
interest_rate = float(input("Enter the interest rate: "));
frequency = int(input("Enter the compound frequency: "));
years = int(input("Enter the number of years: "));

new_principal = principal * ((1 + (interest_rate / (100 * frequency))) ** (frequency * years))

print("$"+str(principal), "invested at an interest rate of", str(interest_rate)+"%", "compounded", str(frequency), "times annually will be worth", "$"+str(round(new_principal, 2)), "after", str(years), "years.")