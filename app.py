from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


@app.route('/')
def display_navigation_links():
    return render_template('index.html')

def scrape_data():
    url = 'https://example.com'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    data = []
    for item in soup.find_all('div', class_='example-class'):
        data.append(item.text)

    return data

class DataResource(Resource):
    def get(self):
        data = [
            {'id': 1, 'name': 'Item 1', 'value': 42},
            {'id': 2, 'name': 'Item 2', 'value': 73},
            {'id': 3, 'name': 'Item 3', 'value': 91},
            {'id': 4, 'name': 'Item 4', 'value': 64},
            {'id': 5, 'name': 'Item 5', 'value': 55},
        ]
        return data

api.add_resource(DataResource, '/api/data')


@app.route('/scrape')
def display_scraped_data():
    scraped_data = scrape_data()
    return render_template('scraped_data.html', data=scraped_data)

def scrape_data():
    url = 'https://www.scrapethissite.com/lessons/sign-up/'
    response = requests.get(url)


    soup = BeautifulSoup(response.text, 'html.parser')

    data = []
    for item in soup.select('blockquote'):
        data.append(item.text.strip())

    print(data)
    return data

@app.route('/visualize')
def display_visualization():
    return render_template('visualization.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)