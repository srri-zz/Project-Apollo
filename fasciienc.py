#Author: 
#Steven Richards <sbrichards@{mit.edu, gnu.org}>
#'FASCII' Based AES256 Point-to-Point Light Encoding
 
import audiere
import base64
import binascii
import os
from Crypto.Cipher import AES
from time import sleep
from math import sqrt
 
device = audiere.open_device()#Open and assign the audio device

toneup = device.create_tone(10000)

def playing(fasciidata):
	for char in fasciidata:
                  print char
		  toneup.play()
		  sleep(0.03)			
		  toneup.stop()
		  tone = device.create_tone(1000 + (ord(char) * 100))
		  print 1000 + (ord(char) * 100)
		  tone.play()
		  sleep(0.03)
		  tone.stop()

def save(filetext):
        yn = raw_input("Would you like to save your transmission?: y/n\n")
        if yn == "y":
                nameoffile = raw_input("enter a name for the .laze file: \n")
                fileobj = open(nameoffile + ".laze", "w")
                fileobj.write(filetext)
                fileobj.close()
                raw_input("write successful, press enter to close")
                exit()
        if yn != "y":
                raw_input("press enter to close")
                exit()

def message(exist, messageold):
        print "\n\nMessage Entry \n\n"
##      key = raw_input("Enter a key with a length of 16, or 32 Characters: ")
##  mode = AES.MODE_ECB #ECB AES
##  encryptor = AES.new(key, mode)
        if exist == 1:
		raw_input("Press enter to send " + messageold)
                print fasciimessage
                currenttone = 0
                playing(fasciimessage)
        else:
                fasciimessage = raw_input("Enter your message: \n")
        ##        if len(key) == 16:
        ##      file_data += "\n" * (16-len(file_data) % 16)#Make length of file data 16 
        ##  else:
        ##          file_data += "\n" * (32-len(file_data) % 32)#Make length of file data 32
                #header = 'DATA:MESSAGE'
                #messagefix = header + message
                mtime = 0.06 * float(len(fasciimessage))
		print 'Your message will take: ' + str(mtime) + ' seconds to transfer'
                raw_input("Press enter to send: " + fasciimessage)
                playing(fasciimessage)
                save(message)
 
def filetrans(exist, filedata):
        print "\n\nFile Sending\n\n"
##      key = raw_input("Enter a key with a length of 16, or 32 Characters: ")
##      mode = AES.MODE_ECB #ECB AES
##      encryptor = AES.new(key, mode)
        if exist == 1:
                fasciifile = filedata
                raw_input("Press enter to Send")
                mtime = 0.06 * float(len(filedata))
		print 'Your file will take: ' + str(mtime) + ' seconds to transfer'
                playing(fasciifile)
        else:
                openfile = raw_input("Enter path to file: ")#File to encrypt
                f = open(openfile)
                ext = raw_input("Enter file extension as .extension: ")
                header = "DATA:FILE"
                ext = "EXT:" + ext
                file_data = f.read()#Read whole file into memory
                ##        if len(key) == 16:
                ##                file_data += "\n" * (16-len(file_data) % 16)#Make length of file data 16 
                ##        else:
                ##                file_data += "\n" * (32-len(file_data) % 32)#Make length of file data 32
                ##
                #enc_file = base64.b64encode(file_data)#Encrypt
                #print enc_file
                file_data = header + ext + file_data
                mtime = 0.06 * float(len(filedata))
		print 'Your file will take: ' + str(mtime) + ' seconds to transfer'
		raw_input('Press Enter to send')
                playing(filedata)
        	save(file_data)
def openlaze():
        print "\n\nOpening a Laze File\n\n"
        fileloc = raw_input("Enter path to file: ")#File to read
        laze = open(fileloc)
        laze_data = str(laze.read())
        if str(laze_data.find('DATA:MESSAGE')) == '0':
                message(1, laze_data)
        if str(laze_data.find('DATA:FILE')) == '0':
                filetrans(1, laze_data)
 
                 
userin = raw_input("Enter\n 1 to send a message\n 2 to send a file \n 3 to enter path to a .laze file: \n ")
 
if userin == '1':
        message(0, 0)
if userin == '2':
        filetrans(0, 0)
if userin == '3':
        openlaze()
if userin != '1' and userin != '2' and userin != '3':
        exit()
