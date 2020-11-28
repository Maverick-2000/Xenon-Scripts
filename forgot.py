import pyrebase #module (class) for interacting with firebase
import optparse #module (class) for passing arguments to the script in a simpler way
import apikeys #to import firebaseconfig
def get_arguments():# function for parsing arguments
    parsley=optparse.OptionParser()# create object called parsley which contains whatever OptionParser contains
    parsley.add_option("-u","--email",dest="email",help="Specify email to login")#add option -u the value will be saved to variable email
    (options,arguments)= parsley.parse_args() #parse the arguments given and save it to email & password
    return options

def fireforgot(email): # function for sending forgot password command to firebase
    firebaseConfig=apikeys.firebaseConfig #get firebaseConfig dictionary from apikeys
    firebase=pyrebase.initialize_app(firebaseConfig) #connect to firebase project
    auth=firebase.auth() #create new object called auth
    
    
    try: # try to send forgot email command to firebase
        auth.send_password_reset_email(email)  # use send_password_reset_email function to send email
        print ("Password reset link sent") 
    except: #exception occurs
        print ("Error")

options = get_arguments() #call the function to get arguments
fireforgot(options.email) # pass the values options.email to fireforgot

#eg: forgot.py -u maver182@gmail.com
