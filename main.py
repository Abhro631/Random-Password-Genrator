import string

import random

if __name__=="__main__":
    #for taking into consideration the lowercase characters in the passcode
    
    str1=string.ascii_lowercase
    # print(str1)
    
    #for taking into consideration the uppercase characters in the passcode
    
    str2=string.ascii_uppercase
    # print(str2)
    #for taking into consideration the numbers/digits characters in the passcode
    
    str3=string.digits
    # print(str3)
    #for taking into consideration the various special characters i.e. punctuation marks in the passcode
    
    str4=string.punctuation
    # print(str4)
    #to take user definned input for the passcode size
    
    paassize=int(input("Enter the length/size of the password\n"))
    final_pass_code=[]
    
    final_pass_code.extend(str1)
    
    final_pass_code.extend(str2)
    
    final_pass_code.extend(str3)
    
    final_pass_code.extend(str4)
    
    #an empty list is taken and then all the elements are concatenated in that empty string 
    # so as to consider all the possible characters for the pass code
    # print(final_pass_code)
    
    #imported random module and shiffled so as a random and tough to crack passcode is generated
    # random.shuffle(final_pass_code)
    
    #also an alternative technique i.e random .sample to generate random password
    print("The generated passcode is : ")
    
    # random.shuffle will also perform the same function
    
    print("".join(random.sample(final_pass_code,paassize)))
    
    # print("".join(final_pass_code[0:paassize]))



    

