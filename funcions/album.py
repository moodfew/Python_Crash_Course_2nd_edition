def make_album(artist, title, tracks = None):
    album_info = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if tracks:
        album_info['tracks'] = tracks


    return album_info


album = make_album('eminem', 'slim shady')
print(album)

album = make_album('2pac', 'niggaz')
print(album)

album = make_album('biggie', 'ready to die')
print(album)
