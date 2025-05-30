from google_play_scraper import app, reviews
import pandas as pd

# 10 Popular App IDs from Google Play
app_ids = [
    "com.whatsapp",
    "com.instagram.android",
    "com.facebook.katana",
    "com.snapchat.android",
    "com.spotify.music",
    "com.twitter.android",
    "com.tiktok.android",
    "com.netflix.mediaclient",
    "com.google.android.youtube",
    "com.zhiliaoapp.musically"  # TikTok alternative ID (older)
]

all_data = []

for app_id in app_ids:
    try:
        app_info = app(app_id, lang='en', country='us')
        result, _ = reviews(
            app_id,
            lang='en',
            country='us',
            count=5 # You can raise this to 50, 100, etc.
        )

        for r in result:
            all_data.append({
                "App Name": app_info['title'],
                "Rating": app_info['score'],
                "Total Reviews": app_info['reviews'],
                "User Review": r['content'],
                "Review Rating": r['score'],
                "Review Date": r['at']
            })
        print(f"✅ Fetched reviews for {app_info['title']}")

    except Exception as e:
        print(f"❌ Failed to fetch {app_id}: {e}")

# Save to CSV
df = pd.DataFrame(all_data)
df.to_csv("google_play_10_app_reviews.csv", index=False)
print("✅ Scraped reviews for 10 apps. Data saved to 'google_play_10_app_reviews.csv'")
