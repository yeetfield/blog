+++
title = 'Music'
date = 2024-03-17T12:06:19-05:00
draft = false
+++
## Deleting Spotify

Spotify has been effective at being my one-stop shop for music discovery, storage, and listening for about a decade now. While convenient, I've been convinced that there are several compelling reasons[^1] to wean myself off it.

### Royalties 
For starters, it doesn't pay small artists as much as I'd like; I end up buying albums directly anyway, so I'd prefer to make use of those purchases rather than just treat these digital album acquisitions as glorified tips. [Bandcamp](https://bandcamp.com/) is the gold standard in making sure money gets to the people who created the music.

### Discovery
I haven't enjoyed Spotify's recommendations either. In general, I'm averse to recommendation systems that operate on nothing other than my consumption patterns. TikTok and YouTube have been pretty effective at discerning what kinds of videos I'm interested in, but my musical tastes are far more capricious, and Spotify understandably sucks at guessing when I'm in the mood for novelty and when I'm not. Even when it works, there's something unpleasant about some other entity deciding unilaterally what I should see or hear, where my own agency is reduced to skipping. 

### Environmental impact
What makes the failure of Spotify's recommendation system even worse is how much compute resources go into failing to predict my interests. Alex Ross's article[^1] goes into some of the economics of datacentres, and the amount of power and water these facilities draw is fascinating. While a lot of these places are built with sustainability and clean energy in mind, that only blunts the profound impact they have. As venture capitalists usher in a new age of power-hungry recommendation technology, consumers should question whether all of its costs are justified.

## My approach

### Discovery
In contrast to the discovery experience of Spotify, I prefer actively exploring
* subreddits[^2], e.g. [/r/indieheads](https://www.reddit.com/r/indieheads/), [/r/letstalkmusic](https://www.reddit.com/r/letstalkmusic/), and [/r/poppunkers](https://www.reddit.com/r/poppunkers/)
* blogs, e.g. [undrcurrents](https://undrcurrents.com/) and some on Bandcamp [itself](https://daily.bandcamp.com/album-of-the-day)
* critical archives, e.g. [RateYourMusic](https://rateyourmusic.com/)
* small record labels, e.g. [The Flenser](https://nowflensing.com/) (dark, experimental) and [Dear Life](https://www.dearliferecs.com/) (brighter, folk-adjacent)
* the music section of mainstream publications, e.g. [The New Yorker](https://www.newyorker.com/culture)[^3]
* [IDAGIO](https://app.idagio.com/discover), a streaming site focusing on classical music, which is necessary because of the fundamentally different metadata that applies to this genre
* anything non-algorithmic[^4] in nature

all of which are curated sources of new music that I can explore on my own. The user experience is more like walking through a museum and less like feeding at the trough. Each destination allows you to choose the genre and range in time from which you'd like to sample, with as much granularity as you like.

You can still "try out" an album by listening to it on YouTube with an adblocker, the use of which I can justify[^5] in this case because of the possibility that I end up paying the artist directly.

### Acquisition
Without streaming platforms like Spotify, it becomes necessary to buy music, which solves the problem of royalties. This alone is a fairly radical decision in an economic milieu that's inured us to renting everything, but I find that it aligns with prioritizing deeply and thoroughly listening to a single work before seeking novelty, which I've always done on Spotify anyway. You might find that it begins to shift you towards looking for secondhand or discounted CDs to rip, as well, which can make for an interesting scavenger hunt. 

My preference for acquiring music is to look for MP3s[^6] first on Bandcamp, and then on other digital stores like iTunes or Amazon. I'm opposed to vinyl, which is very expensive for new releases and incurs a significant environmental cost due to it being a heavy plastic object. Analog storage might have some nostalgic and decorative merit, but it doesn't make sense to build a music collection out of it. CDs are a last resort, if I can't find an album in an intangible digital form. The legality of ripping CDs (which do not have DRM) is not completely decided[^7] in North America, but morally it seems fine[^8], if you've done your due diligence in trying to pay for it, particularly within a context of streaming economics.

### Hosting
It's pleasantly straightforward to make your own collection of music available on a self-hosted platform like [Navidrome](https://www.navidrome.org/), which gives you streaming ergonomics without any of the costs of Spotify that I mention above. Navidrome is a server that takes care of indexing and serving your music collection. While it comes with a decent web UI, it implements the Subsonic API, which makes it possible to use any number of other clients (including mobile phone apps) with it.

I'm personally not interested in (or capable of) doing all the sysadmin work required to completely host it myself, so I gave [PikaPods](https://www.pikapods.com/) a try, but I found myself frustrated at the lack of support for anything beyond FTP, which meant I couldn't use rsync or even scp to move files around. In the long run, the ergonomics of adding music is vital to the whole self-hosting experience. I'm currently on the Oracle Cloud Infrastructure[^9] free tier, which has been decent and not frustrating so far[^10].

My instance is available [here](https://navidrome.yeetfield.com).

### Maintenance
Maintaining your own collection of music means dealing with metadata issues and backups. Bandcamp is great at providing cover art and reliably-named tracks, but you'll find that the heterogeneity of sources of digital music will manifest in a similar heterogeneity of metadata, and that some manual care will be required. This is still less work than maintaining a physical collection (hauling, cleaning, protecting vinyl or CDs). A nominal amount of work will also need to go into maintaining digital backups, where the typical advice applies. You should select a backup strategy suited for your personal risk tolerance. It's worth developing scripts to make this maintenance work easier (again, not possible with physical collections).

### Drawbacks
Doing things this way requires some manual work and more upfront costs, due to having to buy music. The effort is the point, though, as introducing roadblocks to discretionary consumption is better for both life satisfaction (slowing down the hedonic treadmill) and the environment.

[^1]: https://www.newyorker.com/culture/cultural-comment/imagine-a-world-without-spotify
[^2]: Decoupling from reddit has proven to be much harder.
[^3]: I'll always have a soft spot for them because they made me aware of Lankum's *Between the Earth and Sky*.
[^4]: In the colloquial sense of the word.
[^5]: In other scenarios, I use Patreon directly. I also think Nebula is a particularly good idea for the day that YouTube finally clamps down on adblocking.
[^6]: I realized via https://www.npr.org/sections/therecord/2015/06/02/411473508/how-well-can-you-hear-audio-quality that lossless formats didn't make sense for me to have
[^7]: https://en.wikipedia.org/wiki/Ripping#North_America
[^8]: There are of, course, interesting edge cases where an artist intentionally makes it difficult to buy their music, because they're trying to scrub their own work from the digital record entirely. I do think there are cases where one should give up on trying to have a piece of music.
[^9]: The intention of this whole enterprise being to try alternatives to incumbents like Spotify, AWS, and Google Cloud. Reddit also indicated that this product was surprisingly good for an Oracle offering.
[^10]: Even though I had to relive the mild panic I endured a decade ago when I failed spectacularly several times trying to understand what a reverse proxy was, pronouncing nginx wrong in my head, trying to set up a Flask-based blog to pad out my resume. 
