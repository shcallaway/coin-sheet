import gsheet
import gauth

from datetime import datetime
from coinmarketcap import get_coin

credentials = gauth.get_credentials()

coins = [
  'bitcoin',
  'ethereum'
]

market_cap = {}
price = {}

for coin in coins:
  data = get_coin(coin)[0]
  market_cap[coin] = data['market_cap_usd']
  price[coin] = data['price_usd']

def ordered_values(my_dict):
  keys = sorted(my_dict.keys())

  values = []
  for key in keys:
    values.append(my_dict[key])

  return values

print 'Updating market cap.'
values = ordered_values(market_cap)
gsheet.append('C:D', [ values ], credentials)

print 'Updating price.'
values = ordered_values(price)
gsheet.append('F:G', [ values ], credentials)

print 'Updating timestamp.'
timestamp = datetime.now().isoformat()
gsheet.append('A:A', [[ timestamp ]], credentials)
