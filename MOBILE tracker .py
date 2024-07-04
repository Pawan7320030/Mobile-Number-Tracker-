from tkinter import*

import phonenumbers 
from phonenumbers import carrier
from phonenumbers import geocoder
from phonenumbers import timezone
from timezonefinder import TimezoneFinder
from geopy.geocoders import Nominatim
from datetime import datetime

import pytz

root=Tk()
root.title("MOBILE NUMBER TRACKER")
root.geometry("385x584+500+100")
root.resizable(False,False)

def Track():
    enter_number=entry.get()
    number=phonenumbers.parse(enter_number)

    #country
    locate=geocoder.description_for_number(number,'en')
    country.config(text=locate)

    #sim operator like jio,airtel,idea,bsnl
    operator=carrier.name_for_number(number,'en')
    sim.config(text=operator)

    #phone time
    time=timezone.time_zones_for_number(number)
    zone.config(text=time)

    #longitude and latitude
    geolocator= Nominatim(user_agent="geoapiExercises")
    location= geolocator.geocode(locate)

    lng=location.longitude 
    lat=location.latitude 
    longitude.config(text=lng)
    latitude.config(text=lat)

     #time showing in phone
    obj =TimezoneFinder()
    result= obj.timezone_at(lng=location.longitude,lat=location.latitude)
    
    home=pytz.timezone(result)
    local_time=datetime.now(home)
    current_time=local_time.strftime("%I:%M %p")
    clock.config(text=current_time)

#icon image
icon=PhotoImage(file='C:\\mobile tracker\\logoimage.png')
root.iconphoto(False,icon)

#LOGO image
logo=PhotoImage(file='C:\\mobile tracker\\logoimage.png')
Label(root,image=logo).place(x=200,y=70)

Eback=PhotoImage(file='C:\\mobile tracker\\search png.png')
Label(root,image=Eback).place(x=20,y=190)

#heading
Heading=Label(root,text="TRACK NUMBER",font=('arial',15,'bold'))
Heading.place(x=90,y=110)

#bottom box
Box=PhotoImage(file='C:\\mobile tracker\\bottom png.png')
Label(root,image=Box).place(x=7,y=355)

#entry
entry=StringVar()
enter_number=Entry(root,textvariable=entry,width=17,justify="center",bd=0,font=("arial",20))
enter_number.place(x=50,y=220)

#search button
Search_image=PhotoImage(file='C:\\mobile tracker\\search.png')
search=Button(root,image=Search_image,borderwidth=0,cursor="hand2",bd=0,command=Track)
search.place(x=35,y=300)

#label(information)
country=Label(root,text="COUNTRY:",bg="#57adff",fg="black",font=("arial",10,'bold'))
country.place(x=50,y=400)

sim=Label(root,text="SIM:",bg="#57adff",fg="black",font=("arial",10,'bold'))
sim.place(x=200,y=400)

zone=Label(root,text="TimeZone:",bg="#57adff",fg="black",font=("arial",10,'bold'))
zone.place(x=50,y=450)

clock=Label(root,text="Phone Time:",bg="#57adff",fg="black",font=("arial",10,'bold'))
clock.place(x=200,y=450)

longitude=Label(root,text="Longitude:",bg="#57adff",fg="black",font=("arial",10,'bold'))
longitude.place(x=50,y=500)

latitude=Label(root,text="Latitude:",bg="#57adff",fg="black",font=("arial",10,'bold'))
latitude.place(x=200,y=500)







root.mainloop()