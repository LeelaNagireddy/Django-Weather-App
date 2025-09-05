# 🌤 Django Weather App

A simple **Weather App** built with **Django** that lets users enter a city name and fetch real-time weather details like **temperature, humidity, pressure, and weather description** using the [OpenWeatherMap API](https://openweathermap.org/api).

---

## 🚀 Features
- 🌍 Search weather by city name  
- 🌡 Shows temperature, humidity, and pressure  
- 🌤 Displays weather description with icons  
- 📱 Responsive UI built with Bootstrap  
- 🔑 Secure API key storage with `.env`  

---

## 🛠 Tech Stack
- **Backend:** Django (Python)  
- **Frontend:** HTML, CSS, Bootstrap  
- **API:** OpenWeatherMap  
- **Version Control:** Git & GitHub  

---

## ⚙️ Installation & Setup

1. **Clone the repository**
   git clone https://github.com/your-username/Django-Weather-App.git
   cd Django-Weather-App

  
2 . Create and activate virtual environment
python -m venv venv
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate

3.Install dependencies
pip install -r requirements.txt

4.Set up environment variables
Create a .env file in the root directory and add your API key:

OPENWEATHER_API_KEY=your_api_key_here

5.Run the server
python manage.py runserver

6.Open the app in your browser:
👉 http://127.0.0.1:8000/

📁 Project Structure
Django-Weather-App/
├── weather_app/          # Main Django app
│   ├── templates/
│   │   └── weather.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── weather_project/      # Django project settings
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── .env                  # Environment variables (not in version control)
├── .gitignore           # Git ignore rules
├── requirements.txt     # Python dependencies
└── manage.py            # Django management script

