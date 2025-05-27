import requests
import tkinter as tk
from tkinter import messagebox

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    api_key = "3458bd0770f122603831d668945e5ff4"  # Replace with your valid API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200:
        result = f"City: {data['name']}\n"
        result += f"Temperature: {data['main']['temp']}°C\n"
        result += f"Description: {data['weather'][0]['description'].capitalize()}\n"
        result += f"Humidity: {data['main']['humidity']}%\n"
        result += f"Wind Speed: {data['wind']['speed']} m/s"
        result_label.config(text=result)
    else:
        result_label.config(text="City not found or error retrieving data.")

# Create GUI window
root = tk.Tk()
root.title("Weather App")
root.geometry("350x300")
root.configure(bg="#f0f0f0")

# UI Elements
city_label = tk.Label(root, text="Enter City:", font=("Helvetica", 12), bg="#f0f0f0")
city_label.pack(pady=10)

city_entry = tk.Entry(root, font=("Helvetica", 12), width=30)
city_entry.pack(pady=5)

get_button = tk.Button(root, text="Get Weather", font=("Helvetica", 12), command=get_weather)
get_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#f0f0f0", justify="left")
result_label.pack(pady=20)

# Start the GUI loop
root.mainloop()
