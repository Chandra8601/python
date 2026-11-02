# "Folder"
# import os 
# os.mkdir("hello")
# os.rmdir("hello")
# yaha se direct folder bana do 

# mkdir to make a new folder directory
# rmdir to remove a folder and directory

"""
File
x
w
a
r
    
    
"""
# mode 1 : x --> just to create the file 
# open("garbasample.txt","x")
# mode 2 : w --> agar file exist karti hai to data usme save ho jaega aur exist nahi krti hai to create hoke usme push ho jaega jo aap karwana chahte ho 
# if there is any content inside the file so the new one will appear and overwrite the previous one 
# file = open("garba.txt","w")
# file.write("khelo garba khub khelo din rat khelo garba")
# file.write("enjoy karo job hi job hai ")# 2 bar write likha hai to add ho jaeaga piche upar wale ko 
                                         # upar wali line save hai pehle se usko comment out krke chalye 
                                        #  to overwrite ho jaega purana data hatke naya aa jaega  

#mode3. a -- > add the text at the last .
# file = open("garba.txt","a")
# file.write("this message is newly added")
# agar aage add karna hai to /n likh do 
# file.write("\n again add this message")

# mode 4. r --- > read the content inside of the any file 
# file = open("garba.txt","r")
# print(file.read())
# file.close()  jitni bar file ko open kro utni baar close kro warna 
                # kkoi third party will read your file 
                
# with open("sample.txt","w") as file: # ye with command use karke aapko open close krne ki jaroorat nahi 
#     file.write("This is new file")


# CRUD --> create,read, update ,delete
# import os 
# os.remove("sample.txt")
# print("press 1 for creating a new file :")
# print("press 2 for reading any file : ")
# print("press 3 for updating any file :")
# print("press 4 for deleting any file :")
