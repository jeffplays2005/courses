def create_radio_telephone_dictionary(radio_telephone_tuple):
    radio_d = {}
    for i in radio_telephone_tuple:
        radio_d[i[0]] = i
    return radio_d
radio_telephone_alphabet = ('Alpha', 'Foxtrot', 'Kilo', 'Papa',  'Uniform', 'Zulu')
radio_telephone_dict = create_radio_telephone_dictionary(radio_telephone_alphabet)
for key in sorted(radio_telephone_dict ):
    print(key, radio_telephone_dict [key])