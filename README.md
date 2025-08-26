🪙 Crypto Price Tracker & Data Analysis with Flask + CoinPaprika API

A responsive cryptocurrency tracker built with Flask, HTML/CSS, and the CoinPaprika API — extended with a data analysis module that outputs structured summaries of coins.
Users can search for live prices, explore the top 20–50 coins, and view detailed statistical data like market rank, market cap, and percentage changes.

🚀 Features
🔹 Web App (Flask)

Search any cryptocurrency by name or symbol

Top 20 coins shown on the homepage

Dedicated Top 50 coins page

Coin details include:
• Current USD price
• Price changes (1h, 24h, 7d)
• Market rank
• Market capitalization
• Maximum supply

API integration with CoinPaprika

Fully responsive modern UI

Error handling (e.g., coin not found)

🔹 Data Analysis (Tabular Insights)

Fetch live market data and display formatted coin summaries

Output includes:
• Coin name, symbol, and ID
• Current rank
• Maximum supply
• USD price
• Market capitalization
• Percentage changes (1h, 24h, 7d)

Data presented in a clean, tabular format for readability

Designed for quick comparison between multiple coins

Example Output:

Name of the coin: Tether  
Symbol: USDT | ID: usdt-tether  

Rank: 4  
Max Supply: 0  
USD Price: $1.0002518476212285  
Total Market Price: $148942182708  

Percent change in 1 hr    Percent change in 24 hrs    Percent change in a Week  
0.01%                     -0.06%                      0%  

⚙️ Getting Started
🔧 Prerequisites

Python 3.x

pip for package installation

📦 Install Dependencies
pip install -r requirements.txt

📡 API Reference (CoinPaprika)

Endpoints used:

/v1/tickers → Get latest data for all coins

/v1/search?q={coin_name} → Search for a coin

/v1/tickers/{coin_id} → Get details for a specific coin

📝 Notes

Ensure internet access for live API requests

Number of coins shown can be customized in app.py

All price data is real-time

Analysis module outputs readable summaries instead of graphs

👨‍💻 Author

Tharun Reddy

Open to collaboration & feedback

Contributions welcome (new features, analytics, UI improvements)