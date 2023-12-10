import streamlit as stl
import requests
from datetime import datetime
import pytz 

ist = pytz.timezone('Asia/Kolkata')

stl.set_page_config(page_title="WEATHER_APP ",page_icon='⚡',menu_items={       
        'About': """ Hello User, This is Ronak . This is internship project assigned by :blue[#CodesOnBytes]!
         Github: https://github.com/Ronak-Ronu LinkedIn: www.linkedin.com/in/ronak-suthar-2532a4202 """})

api_key = "8afed96cf88c4e1ad6ca904028772827"

stl.title(':blue[WEATHER] APP 🌥')

col1,col2,col3,col4= stl.columns(4)
sunr,suns=stl.columns(2)
wind_col,date_col = stl.columns(2)
current_date= datetime.now(ist)
def get_weather_data(city_name):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&lang={language}"
    response = requests.get(url)
    data=response.json()
    return data

language= stl.selectbox("Choose your preferable Language 🔠",(

    'ar','bg','da','de','el','en','fr','hi','hu','id','it','ja','kr','nl','pt','sp','th','tr','ua','zh_cn'
   
    ), index=None,
   placeholder="Select Language" )

city_name = stl.text_input('City 🌆',max_chars=30,placeholder="Find Your Location Weather ⚡")

json_data = get_weather_data(city_name)
if city_name:

    sunrise = datetime.utcfromtimestamp(json_data['sys']['sunrise'])
    sunset = datetime.utcfromtimestamp(json_data['sys']['sunset'])
    temp= json_data['main']['temp']
    humidity= json_data['main']['humidity']
    weather = json_data['weather'][0]['main']
    weather_description = json_data['weather'][0]['description']
    wind_speed = json_data['wind']['speed']
    wind_deg = json_data['wind']['deg']

    with stl.container() and col1:
        stl.markdown(f'<div style="background-color: #f5f5f5;padding: 10px;text-align:center;border-radius: 5px;margin: 10px 0;" ><p>Weather 🌈 :<br> <span style="color:#2c82d2;font-weight:bold;">{weather}</span></p></div>', unsafe_allow_html=True)
        # stl.write("Weather 🌈 :",weather)
        # stl.markdown(f'', unsafe_allow_html=True)
        # # stl.markdown(f'<div class="data-element">Weather 🌈 : {weather}</div>', unsafe_allow_html=True)
        # stl.markdown('', unsafe_allow_html=True)

    with stl.container() and col2:
        stl.markdown(f'<div style="background-color: #f5f5f5;padding: 10px;text-align:center;border-radius: 5px;margin: 10px 0;" ><p>Weather Description<br> <span style="color:#2c82d2;font-weight:bold;"> {weather_description}</span></p></div>', unsafe_allow_html=True)
        # stl.write("Weather Description :",weather_description)
    with stl.container() and col3:
        stl.markdown(f'<div style="background-color: #f5f5f5;padding: 10px;text-align:center;border-radius: 5px;margin: 10px 0;" ><p>Humidity :<br> <span style="color:#2c82d2;font-weight:bold;"> {humidity}%</span></p></div>', unsafe_allow_html=True)

        # stl.write(f"Humidity {humidity}%")
    with stl.container() and col4:
        stl.markdown(f'<div style="background-color: #f5f5f5;padding: 10px;text-align:center;border-radius: 5px;margin: 10px 0;" ><p>Temperature 🌡️  :<br> <span style="color:#2c82d2;font-weight:bold;"> {temp}℃</span></p></div>', unsafe_allow_html=True)

        # stl.write(f"Temperature 🌡️ {temp}℃")
    with stl.container() and sunr:
        sunrise_time=sunrise.strftime('%Y-%m-%d %H:%M:%S')
        stl.markdown(f'<div style="background-color: #f5f5f5;padding: 10px;text-align:center;border-radius: 5px;margin: 10px 0;" ><p> Sunrise🌅  :<br> <span style="color:#2c82d2;font-weight:bold;"> {sunrise_time}</span></p></div>', unsafe_allow_html=True)
    with stl.container() and suns:
        sunset_time=sunset.strftime('%Y-%m-%d %H:%M:%S')
        stl.markdown(f'<div style="background-color: #f5f5f5;padding: 10px;text-align:center;border-radius: 5px;margin: 10px 0;" ><p>Sunset 🌇   :<br> <span style="color:#2c82d2;font-weight:bold;"> {sunset_time}</span></p></div>', unsafe_allow_html=True)
        # stl.write(":blue[SUNSET] 🌇 :",sunset.strftime('%Y-%m-%d %H:%M:%S'))
    with stl.container() and wind_col:
        stl.markdown(f'<div style="background-color: #f5f5f5;padding: 10px;text-align:center;border-radius: 5px;margin: 10px 0;" ><p>wind_speed 🌪 :<br> <span style="color:#2c82d2;font-weight:bold;"> {wind_speed}km/h</span></p></div>', unsafe_allow_html=True)
        # stl.write(f"wind_speed 🌪 {wind_speed} km/h")
    with stl.container() and date_col:
        formatted_date=current_date.strftime("%A, %I:%M %p")
        stl.markdown(f'<div style="background-color: #f5f5f5;padding: 10px;text-align:center;border-radius: 5px;margin: 10px 0;" ><p>Today🗓️ :<br> <span style="color:#2c82d2;font-weight:bold;"> {formatted_date}</span></p></div>', unsafe_allow_html=True)
        # stl.write(f"wind_speed 🌪 {wind_speed} km/h")


stl.header(":blue[DEVELOPER] SECTION 👨‍💻")
stl.write("API 📡")
code1 = ''' # GET WEATHER DATA BY CITY_NAME
 https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'''
stl.code(code1,language="python")
code2 = ''' # GET WEATHER DATA BY CITY_NAME WITH PREFERABLE LANGUAGE
 https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&lang={language}'''

stl.code(code2,language="python")

stl.write(":blue[GET/]")
stl.json(json_data)

