import requests

# Cung cấp API key từ OpenWeatherMap
api_key = "YOUR_API_KEY"

# Địa điểm cần lấy thông tin thời tiết
city = "London"

# Gửi yêu cầu GET để lấy thông tin thời tiết từ API
response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")

# Kiểm tra mã trạng thái của yêu cầu
if response.status_code == 200:
    # Chuyển đổi dữ liệu từ JSON sang dict
    data = response.json()

    # In thông tin thời tiết
    print("City:", data['name'])
    print("Temperature:", data['main']['temp'])
    print("Weather:", data['weather'][0]['description'])
else:
    print("Error:", response.status_code)
