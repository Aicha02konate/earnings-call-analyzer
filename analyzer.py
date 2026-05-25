import ssl
import pandas as pd
import matplotlib.pyplot as plt
import nltk
import yfinance as yf
from nltk.sentiment import SentimentIntensityAnalyzer

ssl._create_default_https_context = ssl._create_unverified_context
nltk.download('vader_lexicon',quiet=True)

sia=SentimentIntensityAnalyzer()

data=[
    {"quarter": "Q1 2024", "date": "2024-02-01", "text": "We are thrilled to report an all-time revenue record of 119.6 billion dollars."},
    {"quarter": "Q4 2023", "date": "2023-11-02", "text": "We faced significant headwinds in Chima with revenue declining 13 percent."},
    {"quarter": "Q3 2023", "date": "2023-08-03", "text": "We are very confident in our pipeline and long-term groeth prospects."},
    {"quarter": "Q2 2023", "date": "2023-05-04", "text": "Services revenue reached an all-time high of 23.1 billon dollars."},
    {"quarter": "Q1 2023", "date": "2023-02-02", "text": "We returned over 27 billion dollar to shareholders during the quarter."}
]

apple = yf.Ticker("AAPL")

quarters=[ ]
sentiments=[ ]
stock_changes=[ ]

for item in data:
    score = sia.polarity_scores(item["text"])
    sentiments.append(score["compound"])
    quarters.append(item["quarter"])
    hist = apple.history(start=item["date"], period="2d") 
    if len(hist)>=2:
        change= ((hist['Close'].iloc[1] - hist['Close'].iloc[0]) / hist['Close'].iloc[0])*100
        stock_changes.append(round(change, 2))
    else:
        stock_changes.append(0)


df=pd.DataFrame({
    "Quarter": quarters,
    "Sentiment": sentiments,
    "Stock Change %": stock_changes
})

print(df)

fig,(ax1, ax2) = plt.subplots(2,1,figsize=(10, 8))

ax1.bar(quarters, sentiments, color='steelblue')
ax1.set_title('Apple Earnings Call - Sentiment Score')
ax1.set_ylabel('Sentiment Score')

ax2.bar(quarters, stock_changes,color=['green' if x>0 else 'red' for x in stock_changes])
ax2.set_title('Apple Stock Change % apres Earnings Call')
ax2.set_ylabel('Stock Change %')
ax2.axhline(y=0, color='black',linewidth=0.8)

plt.tight_layout()
plt.savefig('sentiment_chart.png')
print("Graphique saved")