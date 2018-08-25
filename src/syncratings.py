import configparser
import json
from gmusicapi import Mobileclient

CREDENTIALS_FILE='../google_music.creds'
CONFIG_FILE='../fivestarman.config'

config = configparser.ConfigParser()
config.read(CONFIG_FILE)

gmusic = Mobileclient()

print("we're live")

def login():
	creds = configparser.ConfigParser()
	creds.read(CREDENTIALS_FILE)
	login = creds.get("GOOGLE_MUSIC", "GOOGLE_MUSIC_LOGIN")
	password = creds.get("GOOGLE_MUSIC", "GOOGLE_MUSIC_APP_PASSWORD")

	logged_in = gmusic.login(login, password, Mobileclient.FROM_MAC_ADDRESS)
	print("logged-in = " + str(logged_in))
	return logged_in

def searchSong(artist, album, title):
	search_str = artist + " " + album + " " + title
	print(search_str)
	results = gmusic.search(search_str, 10)
	print(json.dumps(results, indent=4, sort_keys=True))
	song_hits = results["song_hits"]
	print("Found " + str(len(song_hits)) + " results")
	if (not song_hits):
		print("Unable to find ANY search results :(")
		return
	for song in song_hits:
		track = song["track"]
		if (track["title"].lower() == title and \
			track["artist"].lower() == artist and \
			track["album"].lower() == album):
			print("Found!: " + track)
			return track
	print("No matches found for title/artist/album!")

if (not login()):
	exit

track = searchSong("led zeppelin", "houses of holy", "the song remains the same")

if (track):
	songs = [{'nid':track["nid"], 'trackType': track["trackType"]}]
	gmusic.rate_songs(songs, 5)