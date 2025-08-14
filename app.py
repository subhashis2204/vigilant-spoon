from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def parse_query_params():
    # Get all query parameters as a dictionary
    query_params = request.args.to_dict()

    # If no query parameters are provided
    if not query_params:
        return jsonify({"error": "No query parameters provided"}), 400

    return jsonify({
        "message": "Query parameters received",
        "parameters": query_params
    })

if __name__ == '__main__':
    app.run(debug=True)
