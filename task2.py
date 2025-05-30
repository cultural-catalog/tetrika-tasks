# It is necessary to implement a script that will receive a list of all animals from the Russian-language Wikipedia
# ( https://ru.wikipedia.org/wiki/Category:Animals_in_alphabet ) and write it to a file in the format of beasts.csv the
# number of animals for each letter of the alphabet. The contents of the resulting file:


# А,642
# Б,412
# В,....

# Note: there is no need to analyze the text, any entry from the category is considered
# (it may contain not only the name, but also, for example, the genus)

import requests
from bs4 import BeautifulSoup
import csv
from collections import defaultdict

def fetch_animals():
    url = "https://ru.wikipedia.org/wiki/Category:Животные_по_алфавиту"
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    return response.text

def parse_animals(html):
    soup = BeautifulSoup(html, 'html.parser')
    animals = defaultdict(int)

    # Find all links in the category
    for link in soup.select('.mw-category-group a'):
        animal_name = link.get_text()
        if animal_name:  # Ensure the name is not empty
            print(animal_name)
            first_letter = animal_name[0].upper()  # Get the first letter
            animals[first_letter] += 1  # Increment the count for the letter

    return animals

def write_to_csv(animals_count):
    with open('beasts.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for letter in sorted(animals_count.keys()):
            writer.writerow([letter, animals_count[letter]])

def main():
    html = fetch_animals()
    animals_count = parse_animals(html)
    write_to_csv(animals_count)
    print("Data has been written to beasts.csv")

if __name__ == "__main__":
    main()

# Program Output

"""
MacBook-Air:anish-tetrika-tasks anish$ python task2.py 
Data has been written to beasts.csv
MacBook-Air:anish-tetrika-tasks anish$ cat beasts.csv 
А,200
З,1
П,1
"""
