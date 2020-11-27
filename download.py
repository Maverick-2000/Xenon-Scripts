#python download.py -u maver0182@gmail.com -p maver0182 -f Riverdale.txt.aes
import pyrebase
import optparse
import apikeys

def get_arguments():
	parsley=optparse.OptionParser()
	parsley.add_option("-u","--email",dest="email",help="Specify email to login")
	parsley.add_option("-p","--password",dest="password",help="You know what this does")
	parsley.add_option("-f","--filename",dest="filename",help="Specify file name")
	(options,arguments)= parsley.parse_args()
	return options


def firedown(email,password,filename):
	firebaseConfig=apikeys.firebaseConfig
	firebase=pyrebase.initialize_app(firebaseConfig)
	auth=firebase.auth()
	storage = firebase.storage()
	user = auth.sign_in_with_email_and_password(email, password)
	uid=user['localId']
	try:
		if filename=="uploads.txt":
			storage.child(uid+"/"+filename).download(filename)
		else:
			storage.child(uid+"/"+filename).download("Downloads/"+filename)

		
		print ("Done")
	except:
		print ("Error file does not exist")

	
options= get_arguments()

firedown(options.email,options.password,options.filename)