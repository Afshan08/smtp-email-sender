# 🚀 ISS Overhead Notifier using Python

This Python script notifies you via email when the **International Space Station (ISS)** is passing overhead during **nighttime** at your location.

## 🌌 Features

- Fetches real-time ISS coordinates from an API
- Checks if the ISS is within your visible sky range
- Uses sunrise and sunset data to determine if it's night
- Sends an email notification when both conditions are met

## 📦 Dependencies

- `smtplib` (built-in)
- `datetime` (built-in)
- `time` (built-in)
- `requests`

##  How It Works
- Checks the ISS's current position.

- Determines if it is within ±5 degrees of your location.

- Uses the Sunrise-Sunset API to confirm it's nighttime.

- If both are true, sends an email alert.

## **Configuration**
#### *Update the following constants in the script with your own data:*
MY_LAT = 30.375320       # Your latitude
MY_LONG = 69.345116      # Your longitude
email_1 = "youremail@gmail.com"
email_1_password = "your_app_password"
send_to_email = "recipient@gmail.com"

## Loop
- The script runs for 50 minutes, checking every 60 seconds.


Install `requests` using pip:
```bash
pip install requests


