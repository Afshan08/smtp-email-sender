import time
import smtplib
import requests
import datetime as dt
MY_LONG = 69.345116
MY_LAT = 30.375320
email_1 = "afridiafshan01@gmail.com"
email_1_password = "mmaa@dvj9j9"
send_to_email = "afridiafshan02@gmail.com"
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()["iss_position"]
    iss_longitude = float(data["longitude"])
    iss_latitude = float(data["latitude"])
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG:
        return True
    else:
        return False



def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    response = response.json()
    times = response['results']
    sunrise = times['sunrise']
    sunset = times['sunset']
    the_final_sunrise_time = int(sunrise.split("T")[1].split(":")[0])
    the_final_sunset_time = int(sunset.split("T")[1].split(":")[0])
    # now time
    time_now = dt.datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
    else:
        return False


g = 0

while g < 50:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(email_1, email_1_password)
        connection.sendmail(
            from_addr=email_1,
            to_addrs=send_to_email,
            msg="Subject: Look up! \n\n experience the iss space station in the night sky")




