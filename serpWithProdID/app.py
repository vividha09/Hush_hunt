from flask import Flask, request, render_template
from serpapi import GoogleSearch

app = Flask(__name__)

# Display the search form
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Process the search request
@app.route('/search', methods=['POST'])
def search():
    product_id = request.form.get('product_id')
    params = {
        "engine": "google_product",
        "product_id": product_id,
        "gl": "us",
        "hl": "en",
        "api_key": "20225618ef3f167c534b293614c28216f390d049407a225cef2fb73084fa446b"  # Make sure to replace with your actual SerpApi API key
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    product_results = results.get("product_results", {})

    # Redirect to the index page if no product_id is provided or no results are found
    if not product_id or not product_results:
        return render_template('index.html', error="No results found for the provided Product ID.")

    return render_template('results.html', product=product_results)

if __name__ == '__main__':
    app.run(debug=True)
