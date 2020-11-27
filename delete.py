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

def writetofile(uploadedfile):
	file=open("uploads.txt","a")
	file.write(uploadedfile+"\n")
	file.close()

def delmetadata ():
	try:
		file=open ("uploads.txt","r+")
		file.truncate(0)
		file.close()
	except:
		print ("File Clean")
		

def firedel(email,password,filename):
	firebaseConfig=apikeys.firebaseConfig
	firebase=pyrebase.initialize_app(firebaseConfig)
	auth=firebase.auth()
	storage = firebase.storage()
	user = auth.sign_in_with_email_and_password(email, password)
	uid=user['localId']
	try:
		storage.delete(user['localId']+"/"+filename)
		delmetadata()
		files = storage.bucket.list_blobs(prefix=uid) #list files according to uid
		for file in files:
			
			file.name=file.name.replace(uid+"/","")
			if not file.name == "uploads.txt":
				writetofile(file.name)
		print ("Deleted")	

	except:
		print ("File not found.")
	#print (files.name)
	#for file in files:
		#print (file.name)
		#print(storage.child(file.name).get_url(None))



options= get_arguments()
firedel(options.email,options.password,options.filename)

# python upload.py -u maver0182@gmail.com -p maver0182 -f "E:\New folder (2)\lorem ipsum.txt" 
# python upload.py -u maver0182@gmail.com -p maver0182 -f "E:\New folder (2)\lorem ipsum - Copy.txt" 
