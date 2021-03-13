import os
from time import sleep
from PIL import Image
import csv
import sys
import bcrypt
import hashlib

def welcome():
    os.system('clear')
    print("WELCOME!!!")
    c = int(input("Enter 1 to to create a New Account or 2 to Login to an existing Account:"))
    if c == 1:
        acc_create()
    elif c == 2:
        acc_login()
    else:
        print("Wrong input")

def acc_create():
    sleep(1)
    os.system('clear')
    print("Account Creation Page")
    name = input("Enter your Name:")
    pn = input("Enter your Phone Number:")
    k=0
    csv_file = csv.reader(open('users.csv', "r"), delimiter=",")
    while True:
        email = input("Enter your email id:")
        
        for row in csv_file:
            if row == []:
                k=1
                continue
            if email == row[2]:
                k=0
                print("This email id has already been taken. Please enter another email id ")  
                break              
            else:
                k=1
                
                
        if k == 1:
            break
    
      
    sex = input("Enter your sex:")
    add = input("Enter your Address:")

    profile_image(email)
    sleep(1)
    os.system('clear')

    password = input("Set a password for your Account:")
    repass = input("Re-enter your password:")
    if password == repass:
        print("Account Creation Successful!!")
        
        hashed_pass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        with open("users.csv", "a") as dump:
            writer = csv.writer(dump)
            writer.writerow([])
            writer.writerow([name,pn,email,sex,add,hashed_pass.decode('utf-8')])
            dump.close()
    else:
        print("Account Creation Failed ")
        
		

def profile_image(em):
    sleep(1)
    os.system('clear')
    print("Portal to set Profile Picture")
    ic = int(input("Enter 1 to set your image as the Default Image or 2 to enter the path of your preffered image:"))
    if ic == 1:
        path = '/Users/gauravkumar/Documents/DSCT2/default_image.jpg'
        img  = Image.open(path)
        spath = '/Users/gauravkumar/Documents/DSCT2/profile_pictures/'+em+'profileimg.jpg'
        img.save(spath, 'JPEG')
        print("Profile Picture set successfully")
    elif ic == 2:
        path = input("Enter the path of your Preffered Image")
        img  = Image.open(path)
        spath = '/Users/gauravkumar/Documents/DSCT2/profile_pictures/'+em+'profileimg.jpg'
        img.save(spath, 'JPEG')
        print("Profile Picture set successfully")
    else:
        print("Wrong Input")


def acc_login():
    sleep(1)
    os.system('clear')
    print("Account Login Page")
    ui = input("Enter your Unique Identifier i.e Email id:")
    ipass = input("Enter your Password:")
    
    csv_file = csv.reader(open('users.csv', "r"), delimiter=",")
    k = 0
    for row in csv_file:
        if row == []:
            k=0
            continue
        if ui == row[2] and bcrypt.checkpw(ipass.encode('utf-8'), row[5].encode('utf-8')):
            k=1
            break
        else:
            k=0
    if k == 1:
        sleep(1)
        os.system('clear')
        print("Login Successful!!!")
        print("Your Account Information is:")
        print("Name:",row[0])
        print("Phone Number:", row[1])
        print("Email:", row[2])
        print("Sex:", row[3])
        print("Address:", row[4])
        
        sleep(2)
        il = int(input(("Enter 1 to search for Other User's Data or 2 to Logout:")))
        if il == 1:
            iname = input("Enter the Name whose data you want to search:")
            csv_file = csv.reader(open('users.csv', "r"), delimiter=",")
            for row in csv_file:
                if row == []:
                    continue
                if iname == row[0]:
                    print("Name:",row[0])
                    print("Phone Number:",row[1])
                    print("Address:", row[4])
            
        elif il == 2:
            print("You have logged out of your account")
        else:
            print("Wrong Input")

    else:
        print("Incorrect Login Credentials. Login Failed")

welcome()



