# user input
user_input = input("Enter your text: ")
htmls = ('>'.join(user_input.split('<'))).split('>')
html_tags = []
for i, item in enumerate(htmls):
    if((i % 2) != 0):
        html_tags.append(item)
print(f"List of HTML tags: {html_tags}")
