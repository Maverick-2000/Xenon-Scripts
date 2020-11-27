import pyAesCrypt
import optparse
import apikeys
import os
def get_arguments():
    parsley=optparse.OptionParser()
    parsley.add_option("-f","--filename",dest="filename",help="Specify file name")
    parsley.add_option("-p","--password",dest="password",help="You know what this does")
    parsley.add_option("-e","--encrypt",action="store_true",dest="encrypt",help="Specify to encrypt",default=False)
    parsley.add_option("-d","--decrypt",action="store_true",dest="decrypt",help="Specify to decrypt",default=False)
    (options,arguments)= parsley.parse_args()
    return options

def encrypt(filename,password):
	bufferSize = 64 * 1024
	
	pyAesCrypt.encryptFile(filename, filename+".aes", password, bufferSize)

	print ("Encrypted")
	print (filename+".aes")

def decrypt(filename,password):
	bufferSize = 64 * 1024
	(dirname, basename) = os.path.split(filename)
	defilename=os.path.splitext(basename)[0]
	pyAesCrypt.decryptFile(filename, dirname+"/"+defilename, password, bufferSize)
	print ("Decrypted")

options= get_arguments()
if (options.encrypt):
	encrypt(options.filename,options.password)
else:
	decrypt(options.filename,options.password)

#python AesCrypt.py -f "E:\New folder (2)\lorem ipsum.txt" -p maver0182 -e 