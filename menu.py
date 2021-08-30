import os
import getpass
import speech_recognition as sr

password = getpass.getpass("Password : ")
if password != "akhilesh":
    print("Wrong Password")
    exit()
else:
    while True:
         os.system("tput setaf 2")
         print("\n")
         print("\t\t\t\t\t\t\t\t  WELCOME TO MAIN MENU")
         print("\t\t\t\t\t\t\t\t#########################")
         print("\t\t\t\t\t\t\t\t#########################")
         print("""                                            
                                                               1. To execute Linux Operation
                                                               2. To execute Docker Opearation
                                                               3. To execute AWS service Opearation
                                                               4. To execute Hadoop Operation
                                                               5. To exit
         """)
         os.system("tput setaf 0")
         print("\t\t\t\t\t\t\t\t#########################")
         print("\t\t\t\t\t\t\t\t#########################")
 

         r = sr.Recognizer()
         with sr.Microphone() as source:
             print("Start Speaking")
             audio = r.listen(source)
             print("Audio Recorded")

         ch = r.recognize_google(audio)
         print(ch)
         if ((("linux" in ch) or ("Linux" in ch) or ("linux operation" in ch)) and (("run" in ch) or(('Run' in ch))or ("execute" in ch))):
             os.system("python3 linux-operation.py")

         elif ((("docker" in ch) or ("Docker" in ch) or ("docker operation" in ch)) and (("run" in ch) or ("execute" in ch))):
             os.system("python3 docker.py")

         elif ((("aws" in ch) or ("AWS" in ch) or (" Amazon Web service" in ch)) and (("run" in ch) or ("Amazon Web service" in ch))):
             os.system("python3 aws-operation.py")

         elif ((("hadoop" in ch) or ("Hadoop" in ch) or ("hadoop operation" in ch)) and (("run" in ch) or ("execute" in ch))):
             os.system("python3 hadoop.py")

         elif ((("exit" in ch) or ("return" in ch)) and (("from main menu" in ch) or ("menu" in ch))):
             os.system("exit")
             break

         else:
             print("Invalid Option")
        
    
         input("Enter to run more main menu...")
         os.system("clear")


