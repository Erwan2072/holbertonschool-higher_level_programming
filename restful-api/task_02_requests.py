#!/usr/bin/python3
"""Consuming and processing data from an API"""


import requests
import csv


def fetch_and_print_posts():
    """fetches all post from JSONPlaceholder"""
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)

    # Print the status code
    print(f'Status Code: {response.status_code}')

    if response.status_code == 200:
        posts = response.json()

        # Iterate through the parsed JSON data and print titles
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        # Structure the data into a list of dictionaries
        structured_data = [{'id': post['id'], 'title': post['title'], 'body': post['body']} for post in posts]

        # Write the data into a CSV file
        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for post in structured_data:
                writer.writerow(post)
