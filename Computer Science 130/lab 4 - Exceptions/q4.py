dictionary = {'yes':'oui','no':'non','hello':'bonjour','thank you':'merci','and':'et','or':'ou','but':'mais'}

def get_french_word(dictionary, word):
    try:
        return dictionary[word]
    except KeyError:
        print(f"ERROR: {word} is not available.")
        return None
    except TypeError:
        print("ERROR: Invalid dictionary!")
        return None

print(get_french_word(dictionary, 'hello'))
# bonjour
print(get_french_word(dictionary, 'orange'))
# ERROR: orange is not available.
# None
print(get_french_word([1, 2, 3], 'yes'))
# ERROR: Invalid dictionary!
# None
print(get_french_word(dictionary, 'yes'))