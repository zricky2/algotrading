import robin_stocks as rs
import pyotp
import os 

#export robinhood_username="your_username_here"
#os.environ.get("robinhood_username")

USER_NAME = ''
PASSWORD = ''
AUTH = ''


def loginUser(user, psw, auth):
    print("Loggin in .....")
    try:
        totp = pyotp.TOTP(auth).now()
        login = rs.login(user, psw, mfa_code=totp)   
    except:
        print("error logging in")


def getStockPositions():
    positions_data = rs.get_open_stock_positions()
    for item in positions_data:
        item['symbol'] = rs.get_symbol_by_url(item['instrument'])
        print(item['symbols'])


def buyCrypto():
    try:
        rs.order_buy_crypto_by_price('DOGE',1)
    except:
        print("Order did not go through")


def buyStock(ticker, amount):
    try:
        r = rs.order_buy_market(ticker, amount)
        print(r)
    except:
        print('Order did not go through')


loginUser(USER_NAME, PASSWORD, AUTH)
buyStock('EXPR', 1)
#rs.logout()


def makeLimitOrder(symbol, quantity, limitPrice):
    rs.orders.order_buy_limit(symbol,
                          quantity,
                          limitPrice,
                          timeInForce='gtc',
                          extendedHours=False)