from flask import Flask, request
import os
# from pml import app

app = Flask(__name__)
port = int(os.getenv('PORT'))

@app.route('/', methods=['GET'])
def get_message():
    query_parameters = request.args
    name = query_parameters.get('name')
    message = query_parameters.get('message')
    if name and message:
        return f'Hello {name}! {message}!'
    else:
        return f'Hello! Please enter your name and your message. '


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
