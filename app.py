from flask import Flask, render_template, request,jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return 'Chào mừng đến v vời trang chủ của ứng dụng Flask!'

@app.route('/hello')
def hello():
    name = request.args.get('name')
    if name:
        return f'Xin chào, {name}!'
    else:
        return 'Xin chào, khách vãng lai!'

@app.route('/submit')
def submit():
    # data = request.get_json()
    # name = data.get('name')
    # price = data.get('price')
    # ready = data.get('ready')

    return 'Dữ liệu đã được gửi thành công!'
@app.route('/api', methods=['POST'])
def process_json_data():
    api_key = "YOUR_API_KEY"
    city = "London"


    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")

    if response.status_code == 200:

        data = response.json()

        print("City:", data['name'])
        print("Temperature:", data['main']['temp'])
        print("Weather:", data['weather'][0]['description'])
    else:
        print("Error:", response.status_code)


if __name__ == '__main__':
    app.run()
