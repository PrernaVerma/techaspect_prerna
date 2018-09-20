from tkinter import *


def func():
    global namee,agee,addresse,emaile,mobilee,bloodgroupe,gendere
    f=open("BloodDonor.txt","w")
    f.write(namee.get()+","+agee.get()+","+addresse.get()+","+emaile.get()+","+mobilee.get()+","+bloodgroupe.get()+","+gendere.get())
    f.close
    
def list_users():
    root = Tk()
    frame = Frame(root)
    f=open("BloodDonor.txt","r")
    data=f.read().split(",")

    a=data[0]
    
    namel = Label(root, text=a).grid(row=1,column=1)
    
    

def techaspect():
    global namee,agee,addresse,emaile,mobilee,bloodgroupe,gendere
    root = Tk()
    frame = Frame(root)

    namel = Label(root, text="Name").grid(row=1,column=1)
    namee=Entry(root)
    namee.grid(row=1,column=2)


    agel = Label(root, text="Age").grid(row=2,column=1)
    agee=Entry(root)
    agee.grid(row=2,column=2)

    addressl = Label(root, text="Address").grid(row=3,column=1)
    addresse=Entry(root)
    addresse.grid(row=3,column=2)

    emaill = Label(root, text="Email Id").grid(row=4,column=1)
    emaile=Entry(root)
    emaile.grid(row=4,column=2)

    mobilel = Label(root, text="Mobile No.").grid(row=5,column=1)
    mobilee=Entry(root)
    mobilee.grid(row=5,column=2)

    bloodgroupl = Label(root, text="BloodGroup").grid(row=6,column=1)
    bloodgroupe=Entry(root)
    bloodgroupe.grid(row=6,column=2)

    genderl= Label(root, text="Gender").grid(row=7,column=1)
    gendere=Entry(root)
    gendere.grid(row=7,column=2)

    submit=Button(root,text="Submit",height=2,command=func).grid(row=8,columnspan=2,column=2)


root = Tk()
frame = Frame(root)


regsiter=Button(root,text="Register BLood Donor",height=2,command=techaspect).grid(row=1,columnspan=2,column=1)
users=Button(root,text="Existing Donors",height=2,command=list_users).grid(row=2,columnspan=2,column=2)

root.mainloop()
