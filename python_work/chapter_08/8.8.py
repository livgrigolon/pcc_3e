def make_album(artist, title, num_songs = None):
    album = {"artista": artist, "titulo": title}
    if num_songs:  # só adiciona se não for None
        album["num_musicas"] = num_songs
    return album

while True:
    print("\nDigite os dados do álbum (ou 'sair' para encerrar):")
    artista = input("Nome do artista: ")
    if artista.lower() == "sair":
        break

    titulo = input("Título do álbum: ")
    if titulo.lower() == "sair":
        break

    num_musicas = input("Número de músicas (opcional): ")

    if num_musicas.isdigit():  # só adiciona se for um número válido
        album = make_album(artista, titulo, int(num_musicas))
    else:
        album = make_album(artista, titulo)

    print(f'\nÁlbum criado: {album}')
