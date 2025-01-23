from flask import Flask, request, jsonify

app = Flask(__name__)

# Basic response logic (can be expanded or connected to a dataset)
def get_bot_response(user_input):
    if "hello" in user_input.lower():
        return "Hi there! How can I help you today?"
    elif "how are you" in user_input.lower():
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "movie" in user_input.lower():
        return "I love talking about movies! What's your favorite movie?"
    else:
        return "Sorry, I didn't understand that. Can you try rephrasing?"

@app.route('/get-response', methods=['POST'])
def get_response():
    data = request.get_json()
    user_message = data.get('message', '')
    bot_response = get_bot_response(user_message)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
