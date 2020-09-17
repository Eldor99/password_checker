import requests
import hashlib

def request_api_data(query_char):
	url = 'https://api.pwnedpasswords.com/range/' + 'CBFDA'
	res = requests.get(url)
	if res.status_code != 200:
		raise RuntimeError(f'Error and fetching: {res.status_code}, check api and code')
	return res

def pwned_api_check(password):
	sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
	return sha1password