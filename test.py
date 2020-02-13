from bs4 import BeautifulSoup
import requests

URL = 'https://www.gameology.com.au/collections/board-game/products/altiplano-board-game-card-game'

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'lxml')
