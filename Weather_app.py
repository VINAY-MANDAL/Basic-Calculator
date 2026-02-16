import requests
import tkinter as tk
from tkinter import messagebox

API_KEY = "4ffd9faadf229176a2b9fc55ef9ea1e2"

def get_weather():
    city = city_entry.get()
    
    if not city:
        messagebox.showwarning("Warning", "Please enter a city name")
        return
    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] == 200:
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            description = data["weather"][0]["description"]

            result_label.config(
                text=f"City: {city}\n"
                     f"Temperature: {temp} °C\n"
                     f"Humidity: {humidity}%\n"
                     f"Condition: {description}"
            )
        else:
            messagebox.showerror("Error", "City not found")

    except Exception as e:
        messagebox.showerror("Error", "Something went wrong")

# GUI WINDOW
root = tk.Tk()
root.title("Weather App")
root.geometry("300x250")

title = tk.Label(root, text="Weather App", font=("Arial", 16))
title.pack(pady=10)

city_entry = tk.Entry(root, width=25)
city_entry.pack(pady=5)

search_btn = tk.Button(root, text="Get Weather", command=get_weather)
search_btn.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 10))
result_label.pack(pady=10)

root.mainloop()
