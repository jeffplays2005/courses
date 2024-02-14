loan_amount = 650000;
annual_interest_rate = 5;
loan_length_years = 20;
months_per_year = 12;

monthly_interest_rate = annual_interest_rate / months_per_year;
num_payments = loan_length_years * months_per_year;

L = loan_amount;
i = monthly_interest_rate;
n = num_payments;
# formula
p = L*(
(i/100)*((1+i/100)**n)
/
(((1+i/100)**n) - 1)
)
p = round(p)

# print the result
print("You will need to pay $", p, "monthly.")