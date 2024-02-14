def create_zodiac_dictionary(start_year, end_year):
    years = {2000: "Dragon", 2001: "Snake", 2002: "Horse", 2003: "Goat", 2004: "Monkey", 2005: "Rooster", 2006: "Dog", 2007: "Pig", 2008: "Rat", 2009: "Ox", 2010: "Tiger", 2011: "Rabbit"}
    returns = {}
    for year in years.items():
        matched_years = []
        for number in range(start_year, end_year+1):
            found_year = number - ((number - 2000) // 12) * 12
            if(found_year == year[0]):
                matched_years.append(number)
        returns[f"{year[1]}"] = matched_years
    return returns
# 1 line
def create_zodiac_dictionary(start_year, end_year): return { item[1]: [ i for i in range(start_year, end_year + 1) if({2000: "Dragon", 2001: "Snake", 2002: "Horse", 2003: "Goat", 2004: "Monkey", 2005: "Rooster", 2006: "Dog", 2007: "Pig", 2008: "Rat", 2009: "Ox", 2010: "Tiger", 2011: "Rabbit"}[(i - ((i - 2000) // 12) * 12)] == item[1]) ] for item in ({2000: "Dragon", 2001: "Snake", 2002: "Horse", 2003: "Goat", 2004: "Monkey", 2005: "Rooster", 2006: "Dog", 2007: "Pig", 2008: "Rat", 2009: "Ox", 2010: "Tiger", 2011: "Rabbit"}).items() };
# testing cases
a_dict = create_zodiac_dictionary(2003, 2023)
print(a_dict)
