from tkinter import*
import requests
import json
import tkinter.messagebox as m
main_screen=Tk()
main_screen.geometry('400x400')
main_screen.configure(bg="Brown")
main_screen.title("Weather")
name=Label(main_screen,text="Enter City Name ")
name.place(x=20,y=20)

en=Entry()
en.place(x=120,y=20)

t=Label(main_screen,text="Temperature : ")
t.place(x=100,y=160)

tm=Label(main_screen,text="Temp_max : ")
tm.place(x=100,y=200)

tmin=Label(main_screen,text="Temp_min : ")
tmin.place(x=100,y=240)

th=Label(main_screen,text="Humadity : ")
th.place(x=100,y=280)


def callme():
    c=en.get()
    url=f"http://api.openweathermap.org/data/2.5/weather?q={c}&appid=92472cba1ac44bdf5f88de26f70045da"
    res=requests.get(url)
    python_json=json.loads(res.text)
    # print(python_json)
    if(python_json['cod']=='404'):
     m.showinfo("Weather","Enter valid city")
    else:
     mm=python_json["main"]
     t1=Label(main_screen,text=round(mm['temp']-273,2)) 
     t1.place(x=200,y=160)

     t1=Label(main_screen,text=round(mm['temp_max']-273,2)) 
     t1.place(x=200,y=200)

     t1=Label(main_screen,text=round(mm['temp_min']-273,2))
     t1.place(x=200,y=240)

     t1=Label(main_screen,text=mm['humidity'] ) 
     t1.place(x=200,y=280)
     
btn=Button(main_screen,text="Click",command=callme)
btn.place(x=20,y=60)







mainloop()