def make_album(artist, title, num_songs = None):
    album = {"artista": artist, "titulo": title}
    if num_songs:  # só adiciona se não for None
        album["num_musicas"] = num_songs
    return album

album_1 = make_album('Rita Lee', 'Caso Sério')
album_2 = make_album("Emicida", "AmarElo")
album_3 = make_album("Arctic Monkeys", "AM", 12)

print(album_1)
print(album_2)
print(album_3)

