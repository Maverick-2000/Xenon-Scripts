import pyAesCrypt #module (class) for encyption/decryption
import optparse #module (class) for passing arguments to the script in a simpler way
import apikeys #to import firebaseconfig
import os #for handling os operations
def get_arguments(): # function for parsing arguments
    parsley=optparse.OptionParser() # create object called parsley which contains whatever OptionParser contains
    parsley.add_option("-f","--filename",dest="filename",help="Specify file name") #add option -f the value will be saved to variable filename (path of the file to be encrypted/decrypted)
    parsley.add_option("-p","--password",dest="password",help="You know what this does")#add option -p the value will be saved to variable password
    parsley.add_option("-e","--encrypt",action="store_true",dest="encrypt",help="Specify to encrypt",default=False) #add option -e the value will be saved to variable encrypt (will store value true if specified in args)
    parsley.add_option("-d","--decrypt",action="store_true",dest="decrypt",help="Specify to decrypt",default=False) #add option -d the value will be saved to variable decrypt (will store value true if specified in args)
    (options,arguments)= parsley.parse_args() #parse the arguments given and save it to filename,password,encrypt or decrypt
    return options

def encrypt(filename,password): # function for encrypting files 
	bufferSize = 64 * 1024 # function for encrypting files 
	
	pyAesCrypt.encryptFile(filename, filename+".aes", password, bufferSize) # use function encryptFile to encrypt file with .aes extension

	print ("Encrypted")
	print (filename+".aes") # print path path of encrypted file

def decrypt(filename,password): # function for encrypting files 
	bufferSize = 64 * 1024 # function for encrypting files 
	(dirname, basename) = os.path.split(filename) # split directory name and base name 
	defilename=os.path.splitext(basename)[0] # variable defilename contains basename of file to be decrypted (excluding the extension .aes)
	pyAesCrypt.decryptFile(filename, dirname+"/"+defilename, password, bufferSize)  # use function decryptFile to decrypt file
	print ("Decrypted")

options= get_arguments() #call the function to get arguments
if (options.encrypt): # if -e is specified then encrypt the file
	encrypt(options.filename,options.password)
else: # if -d is specified then decrypt the file
	decrypt(options.filename,options.password)

#eg: AesCrypt.py -f "E:\temp\lorem ipsum.txt" -p maver182 -e 