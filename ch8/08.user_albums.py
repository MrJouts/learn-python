def make_album(artist, album, tracks=0):
    album = {"artist_name": artist, "album_title": album}
    if tracks:
        album["tracks"] = tracks
    return album


while True:
    artist_name = input("Artist name: ")
    if artist_name == "q":
        break

    album_title = input("Album title: ")
    if album_title == "q":
        break

    album = make_album(artist_name, album_title)
    print(album)
