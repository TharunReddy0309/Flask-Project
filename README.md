🪙 Crypto Price Tracker with Flask + CoinPaprika API

A responsive and user-friendly cryptocurrency tracker built using Flask, HTML/CSS, and the CoinPaprika API.  
It allows users to search for live price data of any cryptocurrency in the world and also provides quick access to the top 20 coins, with an extended view for the top 50.

------------------------------------------------------------

🚀 Features

- Search any cryptocurrency by name or symbol
- Top 20 cryptocurrencies displayed on the home page
- Dedicated page for the Top 50 coins
- Coin details include:
  • Current USD price  
  • Price changes (1h, 24h, 7d)  
  • Market rank  
  • Market capitalization  
  • Maximum supply  
- API integration using CoinPaprika API
- Clean and modern UI, fully responsive on all devices
- Flask-based routing and server logic
- Graceful error handling (e.g., coin not found)

------------------------------------------------------------

⚙️ Getting Started

🔧 Prerequisites

- Python 3.x
- pip for package installation

📦 Install Dependencies

```bash
pip install -r requirements.txt
📡 API Reference

We use the CoinPaprika API for real-time cryptocurrency data.

Endpoints used:

/v1/tickers — Get latest data for all coins

/v1/search?q={coin_name} — Search for a coin

/v1/tickers/{coin_id} — Get details for a specific coin



📝 Notes

Make sure your internet is on to access the CoinPaprika API service.

You can customize the number of coins shown in app.py if needed.

All price data is live and updated in real-time.


Author
Tharun Reddy
Open to collaboration and feedback to improve this project further.
Feel free to reach out or contribute!