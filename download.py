import pyrebase #module (class) for interacting with firebase
import optparse #module (class) for passing arguments to the script in a simpler way
import apikeys #to import firebaseconfig

def get_arguments(): # function for parsing arguments
	parsley=optparse.OptionParser()# create object called parsley which contains whatever OptionParser contains
	parsley.add_option("-u","--email",dest="email",help="Specify email to login")#add option -u the value will be saved to variable email
	parsley.add_option("-p","--password",dest="password",help="You know what this does")#add option -p the value will be saved to variable password
	parsley.add_option("-f","--filename",dest="filename",help="Specify file name")#add option -f the value will be saved to variable filename (path of the file to be downloaded)
	(options,arguments)= parsley.parse_args()#parse the arguments given and save it to email ,password and filename
	return options


def firedown(email,password,filename): #function to download files from firebase
	firebaseConfig=apikeys.firebaseConfig#get firebaseConfig dictionary from apikeys
	firebase=pyrebase.initialize_app(firebaseConfig)#connect to firebase project
	auth=firebase.auth()#create new object called auth
	storage = firebase.storage()# make a new storage object
	user = auth.sign_in_with_email_and_password(email, password) # use sign_in_with_email_and_password function to verify and get JSON 
	uid=user['localId'] #get user id from JSON
	try: # try to download
		if filename=="uploads.txt": # if filename is uploads.txt then 
			storage.child(uid+"/"+filename).download(filename) #call child function to define the path (check folder) then download uploads.txt to current working directory
		else:
			storage.child(uid+"/"+filename).download("Downloads/"+filename) #call child function to define the path (check folder) then download file to Downloads directory

		
		print ("Done")
	except: # if exception occurs then display the message
		print ("Error file does not exist")

	
options= get_arguments() #call the function to get arguments

firedown(options.email,options.password,options.filename) # pass the values options.email,options.password and options.filename to firedown

#eg: download.py -u maver182@gmail.com -p maver182 -f "lorem ipsum.txt.aes"