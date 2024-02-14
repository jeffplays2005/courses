def get_bands_per_genre(band_list):
    genre_list = {}
    for band,genre in band_list:
        if genre in genre_list:
            genre_list[genre].append(band)
        else:
            genre_list[genre] = [band]
    for i in genre_list:
        genre_list[i] = sorted(genre_list[i])
    return genre_list

# testing cases
band_list = [("Faith No More","Alternative"), ("Iron Maiden", "Metal"),
             ("Megadeth", "Metal"), ("Social Distortion", "Punk")]
genre_dict = get_bands_per_genre(band_list)
for key in sorted(genre_dict):
    print(key, genre_dict[key])
# Alternative ['Faith No More']
# Metal ['Iron Maiden', 'Megadeth']
# Punk ['Social Distortion']
band_list = [("The Prodigy","Electronica"), ("Lou Reed", "Rock"),
             ("Queen", "Rock"), ("The Smashing Pumpkins", "Alternative"),
             ("Dinosaur Jr.", "Alternative"), ("Everclear", "Alternative")]
genre_dict = get_bands_per_genre(band_list)
for key in sorted(genre_dict):
    print(key, genre_dict[key])
# Alternative ['Dinosaur Jr.', 'Everclear', 'The Smashing Pumpkins']
# Electronica ['The Prodigy']
# Rock ['Lou Reed', 'Queen']
band_list = [("The Bangles","Pop"), ("Tool", "Metal"),
             ("Pearl Jam", "Alternative"), ("Foo Fighters", "Rock"),
             ("Nirvana", "Alternative"), ("Nas", "Hip-hop"),
             ("Metallica", "Metal"), ("Bob Dylan", "Folk")]
genre_dict = get_bands_per_genre(band_list)
for key in sorted(genre_dict):
    print(key, genre_dict[key])
# Alternative ['Nirvana', 'Pearl Jam']
# Folk ['Bob Dylan']
# Hip-hop ['Nas']
# Metal ['Metallica', 'Tool']
# Pop ['The Bangles']
# Rock ['Foo Fighters']
band_list = [("R.E.M.","Alternative"), ("Bruce Springsteen", "Rock"),
             ("Stone Temple Pilots", "Alternative"), ("Rage Against The Machine", "Metal"),
             ("In Flames", "Metal"), ("Eminem", "Hip-hop"), ("Ghost", "Alternative"),
             ("Arch Enemy", "Metal"), ("Def Leppard", "Rock"), ("Power Trip", "Metal")]
genre_dict = get_bands_per_genre(band_list)
for key in sorted(genre_dict):
    print(key, genre_dict[key])
# Alternative ['Ghost', 'R.E.M.', 'Stone Temple Pilots']
# Hip-hop ['Eminem']
# Metal ['Arch Enemy', 'In Flames', 'Power Trip', 'Rage Against The Machine']
# Rock ['Bruce Springsteen', 'Def Leppard']
