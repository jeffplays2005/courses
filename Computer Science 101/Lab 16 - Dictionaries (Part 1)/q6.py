def build_english_to_maori(translations_list):
    maori_dictiony = {}
    for i in translations_list:
        translation_parameters = i.split(':')
        maori_dictiony[translation_parameters[0]] = translation_parameters[1]
    return maori_dictiony
translations_list = ['black:mangu', 'hello:kiaora', 'house:whare', 'apple:aporo', 'tree:aroha', 'work:mana', 'red:whero']
translation_dict = build_english_to_maori(translations_list)
print(translation_dict)