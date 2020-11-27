import pyrebase
import optparse
import apikeys
def get_arguments():
    parsley=optparse.OptionParser()
    parsley.add_option("-u","--email",dest="email",help="Specify email to login")
    (options,arguments)= parsley.parse_args()
    return options

def fireforgot(email):
    firebaseConfig=apikeys.firebaseConfig
    firebase=pyrebase.initialize_app(firebaseConfig)
    auth=firebase.auth()
    #storage = firebase.storage()
    
    try:
        auth.send_password_reset_email(email)
        print ("Password reset link sent")
    except:
        print ("Error")

options = get_arguments()
fireforgot(options.email)