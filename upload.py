import pyrebase #module (class) for interacting with firebase
import optparse #module (class) for passing arguments to the script in a simpler way
import apikeys #to import firebaseconfig
import ntpath #for calculating basename

def get_arguments(): # function for parsing arguments
	parsley=optparse.OptionParser() # create object called parsley which contains whatever OptionParser contains
	parsley.add_option("-u","--email",dest="email",help="Specify email to login") #add option -u the value will be saved to variable email
	parsley.add_option("-p","--password",dest="password",help="You know what this does") #add option -p the value will be saved to variable password
	parsley.add_option("-f","--filename",dest="filename",help="Specify file name") #add option -f the value will be saved to variable filename (path of the file to be uploaded)
	(options,arguments)= parsley.parse_args() #parse the arguments given and save it to email ,password and filename
	return options

def writetofile(uploadedfile): #function for writing meta data to uploads.txt
	file=open("uploads.txt","a") #open file uploads.txt and append
	file.write(uploadedfile+"\n") #write value of uploadedfile and add newline
	file.close() # close buffer

def delmetadata (): #function to truncate meta data (uploads.txt)
	try: # try to clean file
		file=open ("uploads.txt","r+") #open file uploads.txt (read and update)
		file.truncate(0) # truncate the file
		file.close() # close buffer
	except: # if exception occurs then display the message
		print ("File Clean") 
		

def firestor(email,password,filename): #function to upload files on firebase
	firebaseConfig=apikeys.firebaseConfig #get firebaseConfig dictionary from apikeys
	firebase=pyrebase.initialize_app(firebaseConfig) #connect to firebase project
	auth=firebase.auth() #create new object called auth
	storage = firebase.storage() # make a new storage object
	user = auth.sign_in_with_email_and_password(email, password) # use sign_in_with_email_and_password function to verify and get JSON 
	filelocal=filename # assign filename to filelocal variable
	uid=user['localId']#get user id from JSON
	print (uid)
	basename=ntpath.basename(filelocal) #get basename of the file path i.e if filelocal=E:\Temp\flowers.png then basename will be flowers.png
	cloudpath=uid+"/"+basename #define cloudpath that is folder path in firebase
	storage.child(cloudpath).put(filelocal, user['idToken']) #call child function to define the path (create folder) then upload the file to the same path 
	print ("Success")
	delmetadata() # truncate uploads.txt
	files = storage.bucket.list_blobs(prefix=uid) #list files according to uid
	for file in files:
		file.name=file.name.replace(uid+"/","") #the format the file names are returned will be uid/filename make it filename only
		if not file.name == "uploads.txt": # if the file name is not uploads.txt (exclude uploads.txt)
			writetofile(file.name) # write to uploads.txt

options= get_arguments() #call the function to get arguments
firestor(options.email,options.password,options.filename) # pass the values options.email,options.password and options.filename to firestor

# eg: upload.py -u maver182@gmail.com -p maver182 -f "E:\Temp\lorem ipsum.txt" 

