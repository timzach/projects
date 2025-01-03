import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np

def decode_Message(url):

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table')
    
    x_coordinates = []
    characters = []
    y_coordinates = []
    for row in table.find_all('tr')[1:]:
        cells = row.find_all('td')
        x_coordinates.append(int(cells[0].get_text(strip=True)))
        characters.append(cells[1].get_text(strip=True))
        y_coordinates.append(int(cells[2].get_text(strip=True)))

    width = max(x_coordinates) + 1
    height = max(y_coordinates) + 1

    grid = np.full((height, width), ' ') 

    for x, y, char in zip(x_coordinates,y_coordinates, characters):
        grid[y, x] = char

    fig, ax = plt.subplots(figsize=(10, 1))  
    ax.set_xticks(np.arange(0, width, 1))
    ax.set_yticks(np.arange(0, height, 1))

    for y in range(height):
        for x in range(width):
            ax.text(x, y, grid[y, x], ha='center', va='center', fontsize=8)

    ax.set_xticklabels([])
    ax.set_yticklabels([])
    plt.gca().invert_yaxis()  # invert y axis
    
    plt.axis('off')
    plt.show()


decode_Message('https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub')

