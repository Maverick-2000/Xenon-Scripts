import pyrebase
import optparse
import apikeys
def get_arguments():
    parsley=optparse.OptionParser()
    parsley.add_option("-u","--email",dest="email",help="Specify email to login")
    parsley.add_option("-p","--password",dest="password",help="You know what this does")
    (options,arguments)= parsley.parse_args()
    return options
def firelogin(email,password):
    firebaseConfig=apikeys.firebaseConfig
    firebase=pyrebase.initialize_app(firebaseConfig)
    auth=firebase.auth()
    #storage = firebase.storage()
    
    try:
        auth.sign_in_with_email_and_password(email,password)
        print ("Login Success")
    except:
        print ("Invalid username or password")
#user = auth.sign_in_with_email_and_password("stevebobygeorge@gmail.com", "stevebobygeorge")
#filename="updown.txt"
#storage.child("myfiles/updooown.txt").put(filename, user['idToken'])

options = get_arguments()
firelogin(options.email,options.password)



