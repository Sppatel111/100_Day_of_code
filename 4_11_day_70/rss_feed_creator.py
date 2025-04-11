#RSS Feed Creator - Given a link to RSS/Atom Feed, get all posts and display them.
##.rss or .xml files
import feedparser
import requests

def fetch_rss_feed(url):
    try:
        response=requests.get(url)
        response.raise_for_status()
        return feedparser.parse(response.content)
    except Exception as e:
        print(f"Error {e}")
        return None

def display_feed(feed):
    if feed is None:
        print("No feed to display.")
        return

    print(f"Feed Title: {feed.feed.title}\n")

    for entry in feed.entries:
        print(f"Title: {entry.title}")
        print(f"Link: {entry.link}")
        print(f"Published: {entry.published}")
        print(f"Description: {entry.description}\n")


rss_url=input("enter rss url:")
feed=fetch_rss_feed(rss_url)
display_feed(feed)