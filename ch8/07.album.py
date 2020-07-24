def make_album(artist, album, tracks=0):
    """Build an artist album"""
    album = {"artist_name": artist, "album_title": album}
    if tracks:
        album["tracks"] = tracks
    return album


album = make_album("Cacho castaña", "garganta con arena")
print(album)

album = make_album("Metallica", "Ghost in the sky")
print(album)

album = make_album("Queen", "Save the Queen", 23)
print(album)
