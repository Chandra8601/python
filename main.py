from pathlib import Path 
import os 
import shutil
def create_folder():
    name = input("Tell your folder name :-")
    p = Path(name)
    
    if p.exists():
        print("this folder already exists please try again !!")
        create_folder()
    else:
        p.mkdir()
        print("folder created successfully !")
        
def read_folder():
    p = Path("")
    names = list(p.rglob("*")) 
    
    for i in range(len(names)):
        print(f"{i+1} : {names[i]}")
        
def update_folder():
    read_folder()
    name = input("which folder you want to update :-")
    old_p = Path(name)
    
    if old_p.exists():
        new_name = input("tell new folder name :-")
        new_p = Path(new_name)
        old_p.rename(new_p)
        print("folder name changed successfully ")
    else :
        print("no such folder exists please try again")
        update_folder()

def delete_folder():
    name = input("tell your folder name :-")
    p = Path(name)
    
    if p.exists() and p.is_dir():
        # shutil.rmtree deletes the folder and everything inside it
        shutil.rmtree(p) 
        print("folder deleted successfully")
    else:
        print("folder does not exist or is not a directory")
        delete_folder()

def create_file():
    name = input("tell your file name and extensions :-")
    p = Path(name)
    
    if p.exists():
        print("your file already exists try again!!")
        create_file()
    else:
        with open(p,"w") as file:
            data = input("enter what you want to write :- ")
            file.write(data)
            print("successfully created")

def read_file():
    name = input("tell your file name :-")
    p = Path(name)
    if p.exists() and p.is_file():
        with open(p,"r") as file:
            data = file.read()
            print("\n\n\n your file data \n\n\n")
            print(data)

    
def update_file():
    names = read_folder()
    for i in names:
        i = str(i)
        p = Path(i)
        if p.is_file():
            print(i)

    name = input("which file you want to update :- ")
    p = Path(name)

    if p.exists() and p.is_file():
        print("press 1 to change the file name ")
        print("press 2 to overwrite the file ")
        print("press 3 to append something in your file ")

        check = int(input("Tell your output :- "))

        if check == 1:
            new_name = input("Tell the new name :- ")
            new_p = Path(new_name)
            p.rename(new_p)

        elif check == 2:
            with open(p,'w') as file:
                data = input("what do you want to overwrite:- ")
                file.write(data)
                print("overwritten successfully ")

        elif check == 3:
            with open(p,'a') as file:
                data = input("what do you want to append:- ")
                file.write(" "+ data)
                print("appended successfully ")
            

    else:
        print("no such file exists please try again ")
        update_file()

    


    
    
    
    
def delete_file():
    name = input("tell your file name and extension :-")
    p = Path(name)
    
    if p.exists() and p.is_file():
        os.remove(p)
        print("file deleted sucessfully")
    else :
        print("no such file exists please try again !!")
        delete_file()
    
    
        
        
        
    

print("press 1 - for creating a folder ")
print("press 2 - for reading a folder ")
print("press 3 - for updating a folder ")
print("press 4 - for deleting a folder ")
print("press 5 - for creating a file ")
print("press 6 - for reading a file ")
print("press 7 - for updating a file ")
print("press 8 - for deleting a file ")

res = int(input("Tell your response:-"))

if res == 1:
    create_folder()

if res == 2:
    read_folder()
    
if res == 3:
    update_folder()
if res == 4:
    delete_folder()
if res == 5:
    create_file()
if res == 6:
    read_file()
if res == 7:
    update_file()
if res == 8 :
    delete_file()
    