def count_bands_per_genre(band_list):
    dict = {}
    for i in band_list:
        dict[i[1]] = 0
    for i in band_list:
        dict[i[1]] += 1
    return dict
band_list = [("Faith No More","Alternative"), ("Iron Maiden", "Metal"),
             ("Megadeth", "Metal"), ("Social Distortion", "Punk")]
genre_dict = count_bands_per_genre(band_list)
for key in sorted(genre_dict):
    print(key, genre_dict[key])