from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1/content', methods=['GET'])
def get_content():
    """
    Endpoint to get content.
    """
    return jsonify({'message': 'Content fetched successfully!'}), 200

if __name__ == '__main__':
    app.run(debug=True)
