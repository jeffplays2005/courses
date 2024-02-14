def word_puzzle(horizontal_str, vertical_str):
    individual_vertical_characters = list(vertical_str)
    individual_horizontal_characters = list(horizontal_str)
    
    includes = False
    verti_pos = 1000
    hori_pos = 1000
    char = ""
    
    individual_vertical_characters = ['w', 'o', 'r', 'l', 'd']
    individual_horizontal_characters = ['h', 'e', 'l', 'l', 'o']
    
    print(individual_vertical_characters)
    print(individual_horizontal_characters)
    
    for i, character in enumerate(horizontal_str):
        if character in individual_vertical_characters:
            if (i + individual_vertical_characters.index(character)) / 2 < (verti_pos + hori_pos) / 2:
                hori_pos = individual_horizontal_characters.index(character)
                char = character
                includes = True
        
    for i, character in enumerate(vertical_str):
        if character in individual_horizontal_characters:
            if (i + individual_horizontal_characters.index(character)) / 2 < (verti_pos + hori_pos) / 2:
                verti_pos = individual_vertical_characters.index(character)
                char = character
                includes = True
                
    print(hori_pos)
    print(verti_pos)
    
word_puzzle("hello","world")
