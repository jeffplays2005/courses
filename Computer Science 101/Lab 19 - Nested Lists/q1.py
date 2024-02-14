def get_sum_of_song_lengths_dictionary(songs_dictionary):
    dict = {}
    for i in songs_dictionary.keys():
        total = 0
        for n in songs_dictionary[i]:
            total += n[1]
        dict[i] = total
    return dict
# semi one liner
def get_sum_of_song_lengths_dictionary(songs_dictionary):
    return {artist: sum(length for _, length in songs) for artist, songs in songs_dictionary.items()}


songs_dictionary = {'Wiz Khalifa': [('See You Again', 229), ('We Own It', 227), ('Something New', 200)],'Mark Ronson':[('Uptown Funk', 270), ('Nothing Breaks Like a Heart', 217)]}
print(get_sum_of_song_lengths_dictionary(songs_dictionary))


songs_dictionary = {'Mark Ronson':[('Uptown Funk', 270), ('Nothing Breaks Like a Heart', 217)], 'PSY':[('Gangnam Style', 219)]}
print(get_sum_of_song_lengths_dictionary(songs_dictionary))
