def create_region_dictionary(records_list): return { i[0]: sum(i[1]) for i in records_list }
    
data = [('Auckland', [73.3, 66.1, 87.3, 99.4, 112.6, 126.4, 145.1, 118.4, 105.1, 100.2, 85.8, 92.8]), ('Hamilton', [76.3, 68.7, 79.4, 80.3, 99.7, 113.2, 118.2, 103.4, 91.5, 91.9, 85.0, 100.7])]
a_dict = create_region_dictionary(data)
for key in sorted(a_dict):
    print(key, a_dict[key])