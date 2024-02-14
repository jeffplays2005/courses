def binary_search(names_list, target_name):
    left = 0
    right = len(names_list) - 1
    mid = (left + right) // 2
    found = False
    aaaaaaaaaa = 0
    while found == False:
        aaaaaaaaaa += 1
        if names_list[mid] == target_name:
            return (True, aaaaaaaaaa)
        elif left == mid == right:
            return (False, aaaaaaaaaa)
        elif names_list[mid] > target_name:
            right = mid - 1
            mid = (left + right) // 2
        elif names_list[mid] < target_name:
            left = mid + 1
            mid = (left + right) // 2
    return (False, aaaaaaaaaa)
    
my_list = ['Alexandra', 'Auckland', 'Blenheim', 'Chatham Islands', 'Christchurch', 'Dunedin', 'Gisborne', 'Hamilton', 'Hokitika', 'Invercargill', 'Kaikoura', 'Kaitaia', 'Lake Tekapo', 'Manapouri', 'Masterton', 'Milford Sound', 'Mt Cook', 'Napier', 'Nelson', 'New Plymouth', 'Palmerston North', 'Queenstown', 'Rotorua', 'Taupo', 'Tauranga', 'Timaru', 'Wanganui', 'Wellington', 'Westport', 'Whangarei']
print(binary_search(my_list, "Milford Sound"))
# (True, 5)
my_list =  ['Alexandra', 'Auckland', 'Christchurch', 'Dunedin', 'Gisborne', 'Hamilton', 'Invercargill', 'Masterton', 'Queenstown', 'Rotorua', 'Taupo', 'Tauranga', 'Wellington']
print(binary_search(my_list , "Whangarei"))
# (False, 4)
