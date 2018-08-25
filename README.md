# fivestarman
Manages track ratings between local iTunes and Google Play Music

## Requirements

* Python 3.6 (I think? because it's my first-ish time with python)
* A Google Music API: [gmusicapi](https://unofficial-google-music-api.readthedocs.io)
* A passion for rating things. Including a Greasemonkey/Tampermonkey script to restore 1-5 star ratings in Google Music web client: [google-play-music-star-ratings](https://github.com/Velenir/google-play-music-star-ratings)
* iTunes 11.1.3.8 (because that's what I currently have installed, and I don't want to get into iTunes library format specs just yet)

## Use Case

So you like Google Music, but you have a decade of star ratings in iTunes. Let's scan your iTunes music library and synchronize the ratings over to Google Music.

I suppose I could build something that goes the other way too but who wants that.

## Implementation

My first plan for this is going to be super-slow, and involve a single thread doing a search for artist/title/album, then updating the synced results. Some optimization ideas that I may or may not get to are:
* Multi-threading
* Searching by album instead of track (more precise, but higher likelyhood of false negatives)
* Grouping by album to fetch all results for specific albums (will save on additional searches for tracks in the same album)
* Cleverly ignoring suffixes like "(Deluxe edition)" or "(Collectors edition") to do better fuzzy matching
* Incorporating track length (with some tiny fuzzing) to make sure that covers/remixes/extended editions aren't ranked inaccurately

## Options

* **syncStoreRatings**: Default == `false`, meaning only ratings for user uploaded music (to "My Library") will be synced. Change to `true` to also sync "store" tracks not in the library
* **maxResults**: Default == `10`. Set as low as `1` or as high as `100`
* **syncAllFoundResults**: Default == `false`, meaning only the top found track's rating will be synced. Change to `true` to sync all found tracks.
* **considerPlayCount**: Default == `true`, meaning higher play count is considered in sort decision
* **matchOnAlbum**: Default == `true`, meaning only tracks found with the same album will have their ratings synced. Change to `false` to set all results for artist/track (ie compilations, alternate editions, etc)

* **aggressiveMode**: Default == `false`; `true` means set **syncStoreRatings**=`true`, **maxResults**=`10`, **syncAllFoundResults**=`true`, **matchOnAlbum**=`false`
* **cautiousMode**: Default == `false`; `true` means set **syncStoreRatings**=`false`, **maxResults**=`2`, **syncAllFoundResults**=`false`, **matchOnAlbum**=`true`
  * **cautiousMode** will override **aggressiveMode**
