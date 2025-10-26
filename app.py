# PR submission by Satvika

from flask import Flask, request, jsonify

app = Flask(__name__)

comments = []  # in-memory store for comments

@app.route('/')
def home():
    return "Flask backend is running!"

# Create Comment
@app.route('/comments', methods=['POST'])
def add_comment():
    data = request.get_json()
    comment = {
        "id": len(comments) + 1,
        "text": data["text"]
    }
    comments.append(comment)
    return jsonify(comment), 201

# Read Comment
@app.route('/comments/<int:id>', methods=['GET'])
def get_comment(id):
    for comment in comments:
        if comment["id"] == id:
            return jsonify(comment)
    return jsonify({"error": "Comment not found"}), 404

# Update Comment
@app.route('/comments/<int:id>', methods=['PUT'])
def update_comment(id):
    data = request.get_json()
    for comment in comments:
        if comment["id"] == id:
            comment["text"] = data["text"]
            return jsonify(comment)
    return jsonify({"error": "Comment not found"}), 404

# Delete Comment
@app.route('/comments/<int:id>', methods=['DELETE'])
def delete_comment(id):
    for comment in comments:
        if comment["id"] == id:
            comments.remove(comment)
            return jsonify({"message": "Deleted successfully"})
    return jsonify({"error": "Comment not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
