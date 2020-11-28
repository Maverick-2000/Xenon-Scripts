import pyrebase #module (class) for interacting with firebase
import optparse #module (class) for passing arguments to the script in a simpler way
import apikeys #to import firebaseconfig
def get_arguments(): # function for parsing arguments
    parsley=optparse.OptionParser() # create object called parsley which contains whatever OptionParser contains
    parsley.add_option("-u","--email",dest="email",help="Specify email to login") #add option -u the value will be saved to variable email
    parsley.add_option("-p","--password",dest="password",help="You know what this does") #add option -p the value will be saved to variable password
    (options,arguments)= parsley.parse_args() #parse the arguments given and save it to email & password
    return options
def firelogin(email,password): # function for user and password verification
    firebaseConfig=apikeys.firebaseConfig #get firebaseConfig dictionary from apikeys
    firebase=pyrebase.initialize_app(firebaseConfig) #connect to firebase project
    auth=firebase.auth() #create new object called auth
    try: #try to login
        auth.sign_in_with_email_and_password(email,password) # use sign_in_with_email_and_password function to verify and get JSON 
        print ("Login Success")
    except: #exception occurs
        print ("Invalid username or password")

options = get_arguments() #call the function to get arguments
firelogin(options.email,options.password)  # pass the values options.email and options.password to firelogin

# eg: login.py -u maver182@gmail.com -p maver182

