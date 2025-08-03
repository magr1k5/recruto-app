from flask import Flask, request

recr = Flask(__name__)

@recr.route('/')
def hello():
    name = request.args.get('name', 'Друг') 
    message = request.args.get('message', '')

    # Создаём ответ
    response = f"Hello {name}! {message}"
    return response

if __name__ == '__main__':
    recr.run(host='0.0.0.0', port=5000)
