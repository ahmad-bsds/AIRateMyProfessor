from flask import Flask, render_template, request, jsonify

# Flast app
app = Flask(__name__)

# Home page.
@app.route('/')
def index():
    return render_template('index.html', messages=[])

# On send request
@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    user_message = data.get('message')

    # Here you can handle the message and generate a response
    # For now, it simply returns a generic response
    bot_response = 'Ohh! hi whats up?'

    return jsonify({'response': bot_response})


if __name__ == '__main__':
    app.run(debug=True)
