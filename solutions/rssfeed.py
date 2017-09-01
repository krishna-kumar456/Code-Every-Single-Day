import feedparser

rss_feed_links = ['https://www.reddit.com/.rss', 'https://alvinalexander.com/rss.xml']

for feed_link in rss_feed_links:
    d = feedparser.parse(feed_link)
    print("Total entries: ", len(d.entries))
    print("--------------------------------")
    for entry in d.entries:
        print("--------------------------------")
        print("Title :", entry.title)
        print("Link :", entry.link)
