from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
            # Or
    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)
    

# ---------------------------- SAVE PASSWORD ------------------------------- #
def delete_data():
        password_entry.delete(0,END)
        password_entry.insert(0,"")
        website_entry.delete(0,END)
        website_entry.insert(0,"")
        # email_entry.delete(0,END)
        # email_entry.delete(0,"")
        
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    
    new_data = {
        website:{
            "email":email,
            "password":password
        }
    }
    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops",message="Please dont leave any fields empty!")
    else:
        try:
            with open("Data.json","r") as data_file:
                #read old data
                data = json.load(data_file)  
                
                    
        except FileNotFoundError:
            with open("Data.json","w" ) as data_file:
                json.dump(new_data,data_file,indent=4)
                
                
        else :
              #update old data with new data
            data.update(new_data) 
            
            with open("Data.json","w") as data_file:
                #saving updated data            
                json.dump(data,data_file,indent=4,) 
        finally:
            delete_data() 
            
def search_data():
    try:
        website = website_entry.get()
        with open("Data.json","r") as data_file:
            data = json.load(data_file)
            email = data[website]["email"]
            password  = data[website]["password"]
            
    except KeyError as error:
        messagebox.showinfo(title="Error",message=f"No details for {error} exists.")
    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No Data file found.")
    else:
        messagebox.showinfo(title=website,message=f"Email:\"{email}\" and Password: \"{password}\" this are your \"{website}\" details")
            
        
        # email_entry.delete(0,END)
        # email_entry.insert(END,email )
        # password_entry.insert(END,password)
        
        
    
    
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=40,pady=40)

canvas = Canvas(width=200,height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_img)
canvas.grid(row=0,column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1,column=0)


email_Label = Label(text="Email/Username:")
email_Label.grid(row=2,column=0)

password_Label = Label(text="Password:")
password_Label.grid(row=3,column=0)

#Entries
website_entry = Entry(width=21)
website_entry.grid(row=1,column=1,columnspan=1)
website_entry.focus()

email_entry = Entry(width=40)
email_entry.insert(0,"josephtelang303@gmail.com")
email_entry.grid(row=2,column=1,columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(row=3,column=1)

# button
Generate_button = Button(text="Generate Password",command= password_generator)
Generate_button.grid(row=3,column=2)

add_button = Button(text="Add",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)

search_button = Button(text="Search",width=15,command=search_data)
search_button.grid(row=1,column=2)

window.mainloop()