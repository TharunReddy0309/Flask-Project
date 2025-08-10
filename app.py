'''
Crypto Price Tracker (Flask + CoinGecko API)

Features:

    Live prices of top 20 cryptocurrencies

    Search by coin name or symbol

    Show change over 24h, 7d, 30d

'''

from flask import Flask,render_template,request,redirect,url_for
import requests

app=Flask(__name__)

url = "https://api.coinpaprika.com/v1"
res = requests.get(url)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        coin_name = request.form['name']
        return redirect(url_for('search', results=coin_name))
    
    top_coins_url = "https://api.coinpaprika.com/v1/tickers"
    all_coins = requests.get(top_coins_url).json()
    preview_coins = all_coins[:18]

    return render_template('home.html', top_coins=preview_coins)


@app.route('/top50',methods=['GET','POST'])
def top50():
    url='https://api.coinpaprika.com/v1/tickers'
    res=requests.get(url).json()
    top50=res[:50]
    return render_template('top50.html',results=top50)
@app.route('/search')
def search():
    coin_name = request.args.get('results')
    print("🔍 Received query:", coin_name)

    if not coin_name:
        return redirect(url_for('home'))

    url = f"https://api.coinpaprika.com/v1/search?q={coin_name}"
    res = requests.get(url)
    print("🛰️ API status:", res.status_code)

    data = res.json()
    print("📦 API data keys:", data.keys())

    coins = data.get('currencies', [])
    if not coins:
        return render_template('searched.html', result=None, query=coin_name)
    
    return render_template('searched.html', result=coins, query=coin_name)



@app.route('/<coin_id>')
def coindata(coin_id):
    url=f"https://api.coinpaprika.com/v1/tickers/{coin_id}"
    res=requests.get(url).json()  
    data={
        'id':res['id'],
        'name':res['name'],
        'symbol':res['symbol'],
        'rank':res['rank'],
        'max_supply':res['max_supply'],
        'USD_price':res['quotes']['USD']['price'],
        'percent_change_1hr':res['quotes']['USD']['percent_change_1h'],
        'percent_change_24hr':res['quotes']['USD']['percent_change_24h'],
        'percent_change_7d':res['quotes']['USD']['percent_change_7d'],
        'Total_value':res['quotes']['USD']['market_cap']
    }
    return render_template('show.html',result=data)

if __name__=='__main__':
    app.run(debug=True)

    '''
        res_coindata==>{
            "id": "btc-bitcoin",
            "name": "Bitcoin",
            "symbol": "BTC",
            "rank": 1,
            "circulating_supply": 19647156,
            "max_supply": 21000000,
            "quotes": {
                "USD": {
                "price": 58392.12,
                "volume_24h": 13941032472,
                "volume_24h_change_24h": -8.5,
                "market_cap": 1153521972625,
                "market_cap_change_24h": 1.3,
                "percent_change_1h": -0.1,
                "percent_change_24h": 2.4,
                "percent_change_7d": 5.8
                }
            }
            }
        '''