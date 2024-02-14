def process_transactions(filename):
    input_file = open(filename, "r")
    lines = input_file.read().split('\n')
    input_file.close()
    name = lines.pop(0)
    transactions = 0
    for i in lines:
        split = i.split(":")
        if split[0] == name:
            transactions += int(split[1])
    return (name, transactions)

filename = "Transactions1-FCLE02.txt"
transaction_data = process_transactions(filename)
if transaction_data[1] < 0:
    print(f"The sum of transactions for {transaction_data[0]} = -${transaction_data[1] * -1}")
else:
    print(f"The sum of transactions for {transaction_data[0]} = ${transaction_data[1]}")
