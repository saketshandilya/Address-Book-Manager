from tkinter import *
import tkinter as tk
import csv
import os
import pandas as pd


#Creating Tkinter object.

obj = tk.Tk()



search_var= tk.StringVar()
name_var= tk.StringVar()
email_var= tk.StringVar()
phone_var= tk.StringVar()
address_var= tk.StringVar()
rel_var= tk.StringVar()

name_list=[]
email_list=[]
phone_list=[]
address_list=[]
rel_list=[]


data_dict={}

#The main page.

def mainloop():

    obj.title("Address Book Manager")

    #The heading of main page.
    l1= tk.Label(obj, text="Welcome To The Address Book!!", pady=5, font=("syne mono", 14))
    l2= tk.Label(obj, text="How Can We Help You Today :)", pady=5, font=("vampiro one", 10))

    #Buttons to either search for a query or create a new one.
    b1 = tk.Button(obj,text='Search for an Entry', command=searchloop, pady=5, font=("syne tactile", 10))
    b2 = tk.Button(obj,text='Create a New Entry', command=createquery, pady=5, font=("syne tactile", 10))
    b3 = tk.Button(obj,text='Self Destruct', command=selfdestruct, pady=5,font=("syne tactile", 10, UNDERLINE), foreground='red', background='grey')

    #Geometrical orientation of widgets.
    obj.geometry("300x200")
    l1.pack()
    l2.pack()
    b1.pack()
    b2.pack()
    b3.pack()
    obj.mainloop()

#Search for a query page.

def searchloop():
    #Launching a new window from the main window
    srchobj = tk.Toplevel(obj)
    srchobj.title("Search for an entry")

    #Widgets
    lab= tk.Label(srchobj, text="Enter The Name To Be Searched", pady=5, font=("syne mono", 14))
    srchquer=tk.Entry(srchobj, textvariable= search_var, bd=3, font=("grandstander",8 ), bg="light blue")
    bt1= tk.Button(srchobj, text="Search", command=searchquery, padx=8, pady=3, font=("syne tactile", 10))

    #Geometrical orientation of widgets.
    lab.pack()
    srchquer.pack()
    bt1.pack()


#Back End of Search page.

def searchquery():
    try:
        query= search_var.get()
        data= pd.read_csv("database.csv" , index_col="Name")
        query_details= data.loc[query]
        print(query_details)
    except KeyError:
        print("No such Record Exists. Please Try again.")

#Create a new query page.

def createquery():
    #Launching a new window from the main window.
    crtobj= tk.Toplevel(obj)
    crtobj.title("Create An Entry")

    #Widgets
    lb= tk.Label(crtobj, text="Enter The Details Below", font=("syne mono", 14))



    namelab=tk.Label(crtobj, text="Name", font=("vampirio one", 12))
    namefield= tk.Entry(crtobj,textvariable=name_var, bg="cyan", bd=3, font=("grandstander",8 ))

    emaillab= tk.Label(crtobj, text="Email Address", font=("vampirio one", 12))
    emailfield= tk.Entry(crtobj,textvariable=email_var, bg="cyan", bd=3, font=("grandstander",8 ))

    phonelab=tk.Label(crtobj, text="Phone Number", font=("vampirio one", 12))
    phonefield= tk.Entry(crtobj, textvariable=phone_var, bg="cyan", bd=3, font=("grandstander",8 ))

    addlab= tk.Label(crtobj, text="Address", font=("vampirio one", 12))
    addfield= tk.Entry(crtobj,textvariable=address_var, bg= "cyan", bd=3, font=("grandstander",8 ))

    rellab= tk.Label(crtobj, text="Relation With The Person", font=("vampirio one", 12))
    relfield= tk.Entry(crtobj,textvariable=rel_var, bg="cyan", bd=3, font=("grandstander",8 ))

    submitbtn= tk.Button(crtobj, text="Submit", command=writefile, padx=5, pady=3, font=("syne tactile", 10))

    #Geometrical orientation of widgets.
    lb.pack()
    namelab.pack()
    namefield.pack()
    phonelab.pack()
    phonefield.pack()
    addlab.pack()
    addfield.pack()
    emaillab.pack()
    emailfield.pack()
    rellab.pack()
    relfield.pack()
    submitbtn.pack()


# Back End Of the Create Entry Page
def writefile():
    name= name_var.get()
    email= email_var.get()
    phone= phone_var.get()
    address= address_var.get()
    relation= rel_var.get()

    #name_list.append(name)
    #email_list.append(email)
    #phone_list.append(phone)
    #address_list.append(address)
    #rel_list.append(relation)

    data_dict['Name']= name
    data_dict['Email Address']= email
    data_dict['Phone Number']= phone
    data_dict['Address']= address
    data_dict['Relation']= relation

    data_list=[]
    data_list.append(data_dict)


    with open("database.csv", 'a+') as csvfile:  
      
        writer = csv.DictWriter(csvfile, fieldnames=['Name', 'Email Address', 'Phone Number', 'Address', 'Relation'])
            
        writer.writerows(data_list)  


def selfdestruct():
    os.remove('database.csv')


#Calling the mainloop function
mainloop()

