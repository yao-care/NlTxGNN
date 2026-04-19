#!/usr/bin/env python3
"""
Netherlands Health News Fetcher

Haalt gezondheidsnieuws op via Google News RSS (Nederlands)
Fetches Dutch health news from Google News RSS
"""

import json
import hashlib
from datetime import datetime, timezone
from pathlib import Path

import feedparser

# Project root directory
PROJECT_ROOT = Path(__file__).parent.parent.parent
DATA_DIR = PROJECT_ROOT / "data" / "news"

# Google News Health RSS (Dutch/Netherlands)
GOOGLE_NEWS_HEALTH_RSS = (
    "https://news.google.com/rss/topics/"
    "CAAqJQgKIh9DQkFTRVFvSUwyMHZNR3QwTlRFU0JXNXNMVTVNS0FBUAE"
    "?hl=nl&gl=NL&ceid=NL:nl"
)

# Dutch health keywords for filtering
HEALTH_KEYWORDS = [
    "gezondheid", "ziekenhuis", "arts", "dokter", "medicijn",
    "kanker", "diabetes", "hart", "longontsteking", "griep",
    "vaccin", "behandeling", "therapie", "onderzoek", "studie",
    "patiënt", "ziekte", "aandoening", "symptomen", "diagnose",
    "operatie", "chirurgie", "revalidatie", "preventie",
    "RIVM", "GGD", "huisarts", "specialist", "apotheek",
    "bijwerking", "medicatie", "dosis", "recept"
]


def generate_id(title: str, link: str) -> str:
    """Generate news ID (hash based on title and link)"""
    content = f"{title}:{link}"
    return hashlib.sha256(content.encode()).hexdigest()[:12]


def parse_source(entry) -> dict:
    """Extract source info from RSS entry"""
    source_name = "Google News NL"
    if hasattr(entry, "source") and hasattr(entry.source, "title"):
        source_name = entry.source.title

    return {
        "name": source_name,
        "link": entry.get("link", "")
    }


def parse_published(entry) -> str:
    """Parse published time, convert to ISO 8601 format"""
    published = entry.get("published_parsed")
    if published:
        try:
            dt = datetime(*published[:6], tzinfo=timezone.utc)
            return dt.isoformat()
        except Exception:
            pass

    return datetime.now(timezone.utc).isoformat()


def clean_summary(summary: str) -> str:
    """Clean summary text (remove HTML tags etc.)"""
    import re
    clean = re.sub(r"<[^>]+>", "", summary)
    clean = re.sub(r"\s+", " ", clean).strip()
    return clean[:500] if len(clean) > 500 else clean


def is_health_related(title: str, summary: str) -> bool:
    """Check if news is health-related based on Dutch keywords"""
    text = (title + " " + summary).lower()
    return any(keyword in text for keyword in HEALTH_KEYWORDS)


def fetch_nl_news() -> list[dict]:
    """Fetch Dutch health news from Google News"""
    print(f"Fetching Google News RSS (Netherlands)...")
    print(f"  URL: {GOOGLE_NEWS_HEALTH_RSS[:80]}...")

    feed = feedparser.parse(GOOGLE_NEWS_HEALTH_RSS)

    if feed.bozo:
        print(f"  Warning: RSS parsing issue - {feed.bozo_exception}")

    news_items = []

    for entry in feed.entries:
        title = entry.get("title", "")
        link = entry.get("link", "")

        if not title or not link:
            continue

        summary = clean_summary(entry.get("summary", ""))

        # Filter for health-related news
        if not is_health_related(title, summary):
            continue

        news_id = generate_id(title, link)
        source = parse_source(entry)
        published = parse_published(entry)

        news_items.append({
            "id": news_id,
            "title": title,
            "published": published,
            "summary": summary,
            "sources": [source]
        })

    print(f"  Fetched {len(news_items)} health news items")
    return news_items


def main():
    # Ensure directory exists
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    # Fetch news
    news_items = fetch_nl_news()

    # Output
    output = {
        "source": "nl_news",
        "fetched_at": datetime.now(timezone.utc).isoformat(),
        "count": len(news_items),
        "news": news_items
    }

    output_path = DATA_DIR / "nl_news.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\nOutput: {output_path}")
    print(f"  - News count: {len(news_items)}")


if __name__ == "__main__":
    main()
