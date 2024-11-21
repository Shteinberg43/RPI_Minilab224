from fastapi import APIRouter, Request
import requests


router = APIRouter(prefix='/coins', tags=['coins'])


@router.get('/coin')
async def get_coin(request: Request, coin: str):
	url = "https://api.coingecko.com/api/v3/simple/price"
	params = {
		"ids": coin,
		"vs_currencies": "usd"
	}
	response = requests.get(url, params=params)
	if response.status_code == 200:
		data = response.json()
		return data
	else:
		return {"error": f"Error fetching data. Status code: {response.status_code}"}


@router.get('/derivatives')
async def get_exchanges(request: Request):
	url = "https://api.coingecko.com/api/v3/derivatives"
	response = requests.get(url)
	print(response.text)
	if response.status_code == 200:
		data = response.json()
		return data[0]
	else:
		return {"error": f"Error fetching data. Status code: {response.status_code}"}


@router.get('/platforms')
async def get_volume_tradings(request: Request):
	url = "https://api.coingecko.com/api/v3/asset_platforms"
	headers = {
		"filter": "nft"
	}
	response = requests.get(url, params=headers)
	if response.status_code == 200:
		data = response.json()
		return data
	else:
		return {"error": f"Error fetching data. Status code: {response.status_code}"}
