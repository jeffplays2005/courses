def get_user_option_input(prompt_message):
    prompt = input(prompt_message)
    while prompt not in [ "0", "1" ]:
        prompt = input(prompt_message)
    return prompt
print(get_user_option_input("Enter a number: ") )