import feedparser
from bs4 import BeautifulSoup
import httpx
import asyncio
from datetime import datetime

async def scrape_website(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        # Basic extraction - customize per site
        title = soup.find('title').text if soup.find('title') else 'No title'
        return {'title': title, 'url': url}

def parse_rss(rss_url):
    feed = feedparser.parse(rss_url)
    articles = []
    for entry in feed.entries[:20]:
        articles.append({
            'title': entry.title,
            'link': entry.link,
            'description': entry.get('summary', ''),
            'pub_date': entry.get('published_parsed')
        })
    return articles