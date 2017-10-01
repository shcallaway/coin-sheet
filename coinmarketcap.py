import httplib2, jsonpickle

endpoint = 'https://api.coinmarketcap.com/v1/ticker/'

def get_coin(coin):
  print 'Getting coin data for: ' + coin

  http = httplib2.Http()
  (headers, data) = http.request(endpoint + coin, 'GET')

  return jsonpickle.decode(data)
