#Earnings Call Sentiment Analyzer

## Overview
This project analyzes the sentiment of Apple earnings call transcripts and compares it with the actual stock price movement the following day.

## Tools & Technologies
- Python
- NLTK (VADER Sentiment Analysis)
- Pandas
- Matplotlib
- yfinance (real Apple stock data)

## What it does
1. Takes real excerpts from Apple quarter earnings calls
2. Analyzes the sentiment of each excerpt (positive, negative, neutral)
3. Fetches real Apple stock price changes from Yahoo Finance
4. Visualizes the relationship between sentiment and stock movement

## Key Finding
Positive sentiment in earnings calls does not always predict stock gains. In Q3 2023, despite high sentiment score (0.69) , the stock decline. this suggest that market expectations and broader context matter beyond CEO language alone

## Limitation
VADER does not always capture financial jargon accurately. Words like "Headwinds" are not scored as negative despite their meaning in a financial context.

## How to run
```bash
pip install nltk pandas matplotlib yfinance
python3 analyzer.py
```
