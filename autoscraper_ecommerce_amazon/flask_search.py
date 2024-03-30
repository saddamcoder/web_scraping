from autoscraper import AutoScraper
from flask import Flask, request, jsonify

amazon_scraper = AutoScraper()
amazon_scraper.load('amazon-search')

app = Flask(__name__)

def get_amazon_result(search_query):
    url = 'https://www.amazon.co.uk/s?k={}'.format(search_query)
    result = amazon_scraper.get_result_similar(url, group_by_alias=True)
    return _aggregate_result(result)

def _aggregate_result(result):
    final_result = []
    for svalue in range(len(list(result.values())[0])):
        try:
            final_result.append({alias: result[alias][svalue] for alias in result})
        except IndexError:
            print("data is not in correct format")
    return final_result


@app.route('/', methods=['GET'])
def home_page():
    return "Home world"
@app.route('/api/', methods=['GET'])
def search_api():
    search_query = request.args.get('q')
    result = get_amazon_result(search_query)
    formatted_result = {f"Title {i + 1}": item['Title'] for i, item in enumerate(result)}
    return jsonify(formatted_result)


if __name__ == '__main__':
    app.run(debug=True)