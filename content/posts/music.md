+++
title = 'Music'
date = 2024-03-17T12:06:19-05:00
draft = false
+++
## Deleting Spotify

Spotify has been effective at being my one-stop shop for music discovery, storage, and listening for about a decade now. While convenient, I've been convinced that there are several compelling reasons[^1] to wean myself off it.

### Royalties 
For starters, it doesn't pay small artists as much as I'd like; I end up buying albums directly anyway, so I'd prefer to make use of those purchases rather than just treat these digital album acquisitions as glorified tips. Bandcamp is the gold standard in making sure money gets to the people who created the music.

### Discovery
I haven't enjoyed Spotify's recommendations either. In general, I'm averse to recommendation systems that operate on nothing other than my consumption patterns. TikTok and YouTube have been pretty effective at discerning what kinds of videos I'm interested in, but my musical tastes are far more capricious, and Spotify understandably sucks at guessing when I'm in the mood for novelty and when I'm not. Even when it works, there's something unpleasant about some other entity deciding unilaterally what I should see or hear, where my own agency is reduced to skipping. 

### Environmental impact
What makes the failure of Spotify's recommendation system even worse is how much compute resources go into failing to predict my interests. Alex Ross's article[^1] goes into some of the economics of datacentres, and the amount of power and water these facilities draw is fascinating. While a lot of these places are built with sustainability and clean energy in mind, that only blunts the profound impact they have. As venture capitalists usher in a new age of power-hungry recommendation technology, consumers should question whether all of its costs are justified.

## My approach

### Discovery
In contrast to the Spotify experience described above, I prefer discovering music by actively exploring the subreddits (e.g. [/r/indieheads](https://www.reddit.com/r/indieheads/), [/r/letstalkmusic](https://www.reddit.com/r/letstalkmusic/), and [/r/poppunkers](https://www.reddit.com/r/poppunkers/)) and publications (e.g. [undrcurrents](https://undrcurrents.com/)) that deal with the kind of music I'm interested in. Bandcamp [itself](https://daily.bandcamp.com/album-of-the-day) and [RateYourMusic](https://rateyourmusic.com/) are also curated sources of new music that I can explore on my own. The user experience is more like walking through a museum and less like feeding at the trough. It's also worth pointing out that RateYourMusic and certain subreddits are good at highlighting music from the past, which helps us avoid being impoverished by recency bias. 

You can still "try out" an album by listening to it on YouTube with an adblocker, the use of which I can justify[^5] in this case because of the possibility that I end up paying the artist directly.

### Acquisition
Without streaming platforms like Spotify, it becomes necessary to buy music. This alone is a fairly radical decision in an economic milieu that's inured us to renting everything, but I find that it aligns with prioritizing deeply and thoroughly listening to a single work before seeking novelty, which I've always done on Spotify anyway. You might find that it begins to shift you towards looking for secondhand or discounted CDs to rip, as well, which can make for an interesting scavenger hunt. 

My preference for acquiring music is to look for MP3s[^2] first on Bandcamp, and then on other digital stores like iTunes or Amazon. I'm opposed to vinyl, which is very expensive for new releases and incurs a significant environmental cost due to it being a heavy plastic object. Analog storage might have some nostalgic and decorative merit, but it doesn't make sense to build a music collection out of it. CDs are a last resort, if I can't find an album in an intangible digital form. The legality of ripping CDs (which do not have DRM) is not completely decided[^3] in North America, but morally it seems fine[^4], if you've done your due diligence in trying to pay for it, particularly within a context of streaming economics.

### Hosting
It's pleasantly straightforward to make your own collection of music available on a self-hosted platform like [Navidrome](https://www.navidrome.org/), which gives you streaming ergonomics without any of the costs of Spotify that I mention above. Navidrome is a server that takes care of indexing and serving your music collection. While it comes with a decent web UI, it implements the Subsonic API, which makes it possible to use any number of other clients (including mobile phone apps) with it.

I'm personally not interested in (or capable of) doing all the sysadmin work required to completely host it myself, so I'm giving [PikaPods](https://www.pikapods.com/) a try, and it's been great so far. My instance is available [here](https://navidrome.yeetfield.com).

### Maintenance
Maintaining your own collection of music means dealing with metadata issues and backups. Bandcamp is great at providing cover art and reliably-named tracks, but you'll find that the heterogeneity of sources of digital music will manifest in a similar heterogeneity of metadata, and that some manual care will be required. This is still less work than maintaining a physical collection (hauling, cleaning, protecting vinyl or CDs). A nominal amount of work will also need to go into maintaining digital backups, where the typical advice applies. You should select a backup strategy suited for your personal risk tolerance. It's worth developing scripts to make this maintenance work easier (again, not possible with physical collections).

### Drawbacks
Doing things this way requires some manual work and more upfront costs, due to having to buy music.

[^1]: https://www.newyorker.com/culture/cultural-comment/imagine-a-world-without-spotify
[^2]: I realized via https://www.npr.org/sections/therecord/2015/06/02/411473508/how-well-can-you-hear-audio-quality that lossless formats didn't make sense for me to have
[^3]: https://en.wikipedia.org/wiki/Ripping#North_America
[^4]: There are of, course, interesting edge cases where an artist intentionally makes it difficult to buy their music, because they're trying to scrub their own work from the digital record entirely. I do think there are cases where one should give up on trying to have a piece of music.
[^5]: In other scenarios, I use Patreon directly. I also think Nebula is a particularly good idea for the day that YouTube finally clamps down on adblocking.