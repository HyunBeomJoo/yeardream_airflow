
import requests
# client_id, authorize_code 노출 주의, 실제 값은 임시로만 넣고 Git에 올라가지 않도록 유의

client_id = 'd392e3e8ed5f9de52979b72573202ffa'
redirect_uri = 'https://example.com/oauth'
authorize_code = 'JVto1GTGP6rwUQCkOdRoS7QNZhrbAvW2SEBfdOAlZsBu4E8cd2YY8wAAAAQKPXVcAAABkC3zBRkBl6J2VXah6g'


token_url = 'https://kauth.kakao.com/oauth/token'
data = {
    'grant_type': 'authorization_code',
    'client_id': client_id,
    'redirect_uri': redirect_uri,
    'code': authorize_code,
    }

response = requests.post(token_url, data=data)
tokens = response.json()
print(tokens)
