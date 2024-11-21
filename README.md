# RPI Minilab224 Shteinberg Georgy 5030102/20202

## Description
This is a simple FastAPI application that fetches cryptocurrency information using the CoinGecko API. The service provides endpoints to get the current price of coins, derivatives data, and asset platforms.
## Installation
### Clone the repository:
git clone https://github.com/Shteinberg43/RPI_Minilab224.git
### Install requirements
pip install fastapi uvicorn requests
### Run application
uvicorn main:app --reload
The server will run on http://127.0.0.1:8000.


## Endpoints
When accessing endpoint in my application, the service accesses the link specified in endpoint and receives information from there.
### endpoint "/coin" 
allows you to get the value of a coin in USD, by its name
### endpoint "/derivatives"
allows you to get information about bitcoin trades in 24 hours
### endpoint "/platforms"
allows you to query all the asset platforms on CoinGecko
## Postman workplace
[link](
https://api.postman.com/collections/39915020-3612fe0f-a47b-4987-abbb-345c93722bfc?access_key=PMAT-01JD82KV4H5S9VDKP0K9NGGW0A)
