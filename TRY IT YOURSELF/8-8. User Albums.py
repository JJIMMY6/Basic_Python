def make_album(artist, album):
	"""Build a dictionary describing a music album."""
	album_dict = {
		'artist': artist.title(),
		'album': album.title()
		}
	return album_dict

album_prompt = ("\nWhat album are you think? ")
artist_prompt = ("\nWhat's the artist? ")

print("Enter 'quit' when you want to quit.")

while True:
	album = input(album_prompt)
	if album == 'quit':
		break

	artist = input(artist_prompt)
	if artist == 'quit':
		break

	user_albums = make_album(artist, album)
	print(user_albums)