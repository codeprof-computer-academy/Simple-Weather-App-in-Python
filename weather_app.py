from tkinter import *
import requests
import tkinter.messagebox

HEIGHT = 500
WIDTH = 600

def format_response(weather):
    try:
        name=weather['name']
        desc=weather['weather'][0]['description']
        temp=int(weather['main']['temp']-273)

    
        final_str =  'City: %s \nConditions: %s \nTemperature(‎°C): %s ' %(name, desc, temp)
    except:
        final_str =  "Sorry! \n The requested information\n could not be retrieved!"

    return final_str
        
    
    


def get_weather(city):
    weather_key = '72619d9669574fb96d3b6fd9a4b96fdd'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID':weather_key, 'q': city}
    response = requests.get(url, params=params)
    weather = response.json()

    label['text'] = format_response(weather)



def close_app():
    closeapp = tkinter.messagebox.askyesno("Weather Detector", "Do you want to exit App")
    if closeapp>0:
        root.destroy()
        return

root = Tk()
root.title("Thompson Weather Detector")
root.geometry("+300+100")
root.iconbitmap('sun.ico')




canvas = Canvas(root,height=HEIGHT, width=WIDTH)
canvas.pack()

menubar = Menu(root)
root.configure(menu=menubar)
submenu1= Menu(menubar)
submenu2= Menu(menubar)
menubar.add_cascade(label="File", menu=submenu1)
menubar.add_cascade(label="Help", menu=submenu2)

submenu1.add_command(label="Get Weather", command=lambda: get_weather(entry.get()))
submenu1.add_command(label="Exit", command=close_app)
submenu2.add_command(label="Need Help ?")

background_image = PhotoImage(file="landscape4.png")
background_label = Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = Entry(frame, font=('Courier', 15))
entry.place(relwidth=0.65, relheight=1)

button = Button(frame, text="Get Weather",font=('Aria', 12), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n' )


label = Label(lower_frame, background="white", font=('Courier', 18))
label.place(relwidth=1, relheight=1)


root.mainloop()
