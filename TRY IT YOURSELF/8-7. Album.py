def make_album(artist, album):
	"""Build a dictionary describing a music album."""
	album_dict = {
		'artist': artist.title(),
		'album': album.title()
		}
	return album_dict

album = make_album('eminem', 'encore')
print(album)

album = make_album('taylor swift', 'red')
print(album)

album = make_album('ariana grande', 'my everything')
print(album)