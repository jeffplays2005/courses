def binary_search(names_list, target_name):
    left = 0
    right = len(names_list) - 1
    mid = (left + right) // 2
    found = False
    output = ""
    while found == False:
        output += f"left: {left}, mid: {mid}, right: {right}\n"
        if names_list[mid] == target_name:
            output += "True"
            return output
        elif left == mid == right:
            output += "False"
            break
        elif names_list[mid] > target_name:
            right = mid - 1
            mid = (left + right) // 2
        elif names_list[mid] < target_name:
            left = mid + 1
            mid = (left + right) // 2
    return output
# testing
my_list = ['Alexandra', 'Auckland', 'Blenheim', 'Chatham Islands', 'Christchurch', 'Dunedin', 'Gisborne', 'Hamilton', 'Hokitika', 'Invercargill', 'Kaikoura', 'Kaitaia', 'Lake Tekapo', 'Manapouri', 'Masterton', 'Milford Sound', 'Mt Cook', 'Napier', 'Nelson', 'New Plymouth', 'Palmerston North', 'Queenstown', 'Rotorua', 'Taupo', 'Tauranga', 'Timaru', 'Wanganui', 'Wellington', 'Westport', 'Whangarei']
print(binary_search(my_list, "Milford Sound"))
# left: 0, mid: 14, right: 29
# left: 15, mid: 22, right: 29
# left: 15, mid: 18, right: 21
# left: 15, mid: 16, right: 17
# left: 15, mid: 15, right: 15
# True
my_list =  ['Alexandra', 'Auckland', 'Christchurch', 'Dunedin', 'Gisborne', 'Hamilton', 'Invercargill', 'Masterton', 'Queenstown', 'Rotorua', 'Taupo', 'Tauranga', 'Wellington']
print(binary_search(my_list , "Whangarei"))
# left: 0, mid: 6, right: 12
# left: 7, mid: 9, right: 12
# left: 10, mid: 11, right: 12
# left: 12, mid: 12, right: 12
# False
