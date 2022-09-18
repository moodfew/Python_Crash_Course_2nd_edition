def make_album(artist, title, tracks = None):
    album_info = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if tracks:
        album_info['tracks'] = tracks


    return album_info

title_prompt = "What album are you thinking of? "
artist_prompt = "Who made it? "

print("Enter 'quit' to quit")

while True:
    title = input(title_prompt)
    if title == 'quit':
        break
    artist = input(artist_prompt)
    if artist == 'quit':
        break
    album = make_album(artist, title)
    print(album)
