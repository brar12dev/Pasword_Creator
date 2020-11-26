# for more information about string module you can check out documentation
import string
import random
import os
import getpass

class pasword_Generator:
    if __name__ == "__main__":

        stringUpperCase = string.ascii_uppercase    # these are in ascending order and in same order by default
        stringLowerCase = string.ascii_lowercase     # these are in ascending order and in same order by ydefault
        stringDigits = string.digits    # these are in ascending order and in same order by default
        stringPunctuation = string.punctuation   # these are in ascending order and in same order by default
        stringHexDigits = string.hexdigits  # these are in ascending order and in same order by default
        stringOctiDigits = string.octdigits # these are in ascending order and in same order by default

    # taking pasword length from user as string then type casting it to integer
        user_name = input("please give your user name \n")
        pasword_length = input("Enter paswords length \n")

        try:
            pasword_length = int(pasword_length)
        except Exception as E:
            print("------- ERROR : Your input should be a Whole number only")


    # making a list of all above string
        s = []
        s.extend(stringPunctuation)
        s.extend(stringLowerCase)
        s.extend(stringPunctuation)
        s.extend(stringOctiDigits)
        s.extend(stringOctiDigits)
        s.extend(stringPunctuation)
        s.extend(stringHexDigits)
        s.extend(stringDigits)
        s.extend(stringPunctuation)
        s.extend(stringDigits)
        s.extend(stringPunctuation)
        s.extend(stringHexDigits)
        s.extend(stringUpperCase)
        s.extend(stringPunctuation)
        s.extend(stringHexDigits)
        s.extend(stringPunctuation)
        s.extend(stringPunctuation)
        s.extend(stringHexDigits)
        s.extend(stringHexDigits)
        s.extend(stringPunctuation)


        print(s)
    # random shufling the element list
        random.shuffle(s)
        
    # generating a password of users_provided length
        users_pasword = "".join(s[0:pasword_length])

    
        user_greeting = "Hello " + user_name + " Your Paswords is "

        
        root_location = "D://Pasword_Creator//Test_Folder"
        print(root_location)




        
class Generate_pasword_file:

    my_path = "D:/Pasword_Creator/Test_Folder"
    is_dir = os.path.isdir(my_path)
    if(is_dir == False):     
        os.makedirs(pasword_Generator.root_location)
        print("folder created")
    else:
        print("folder already present")
        pass

    file_location = my_path+"/Paswords.txt"





    try:
        create_pasword_files = open(file_location,"x")
        create_pasword_files.close()
    except Exception as e:
        print(e , "file already exits , but don't worry")
        
    


    try:
        paswords_files = open(file_location,"a+")
        paswords_files.write(pasword_Generator.user_greeting)
        paswords_files.write(" : ")
        paswords_files.write(pasword_Generator.users_pasword)
        paswords_files.write("\n")
        paswords_files.close()

        p2 = open(file_location,"r")
        print(p2.read(),"users: password")
        p2.close()

    except Exception as e:
        print("sorry")



    
