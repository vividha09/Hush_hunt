# from flask import Flask, request, jsonify,render_template
# from flask_cors import CORS  # Import the CORS library
# from main import get_xerve_product_details  # Import your existing function

# app = Flask(__name__)
# CORS(app)# Initialize CORS with default parameters to allow all origins

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/search', methods=['GET'])
# def search():
#     search_term = request.args.get('search_term')
#     products = get_xerve_product_details(search_term)
#     print(products)
#     return jsonify(products)

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
# Make sure the functions from main.py and sendtobi.py are properly imported
from main import get_xerve_product_details  # Adjusted to be importable
from sendToBI import scrape_and_send_to_powerbi  # Adjusted to be importable

app = Flask(__name__)
CORS(app)  # Enables cross-origin requests, useful if your frontend is on a different domain

@app.route('/')
def index():
    # Serves a simple HTML form for input if you're testing without a React frontend
    return '''
        <form action="/search" method="get">
            Search term: <input type="text" name="search_term">
            <input type="submit" value="Submit">
        </form>
    '''

@app.route('/search', methods=['GET'])
def search():
    # Extracts the search term from the query parameters
    search_term = request.args.get('search_term')
    if not search_term:
        return jsonify({"error": "Search term is required"}), 400

    # Calls the function from main.py to get product details
    products = get_xerve_product_details(search_term)
    print("Sending product details to frontend...")

    # Optionally, you might want to send data to Power BI
    # Depending on your requirements, consider running this in a separate thread or asynchronously
    # especially if the operation is long-running and you don't want to delay the response to the frontend
    try:
        scrape_and_send_to_powerbi(search_term)
        print(f"Data for '{search_term}' sent to Power BI successfully.")
    except Exception as e:
        print(f"Failed to send data to Power BI for '{search_term}': {e}")

    # Returns the scraped product details to the frontend or API caller
    print(products)
    return jsonify(products)

if __name__ == '__main__':
    app.run(debug=True)



