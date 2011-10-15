#Author: 
#Steven Richards <sbrichards@{mit.edu, gnu.org}>
#Binary Based AES256 Point-to-Point Laser Encoding
 
import audiere
import base64
import binascii
import os
from Crypto.Cipher import AES
from time import sleep
from math import sqrt
 
device = audiere.open_device()#Open and assign the audio device
currenttone = 0
base = 5000
up = 100
down = -100

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
                binmessage = bin(int(binascii.hexlify(messageold), 16))
                binmessage = str(binmessage[2:])
                raw_input("Press enter to send " + messageold)
                print binmessage
                currenttone = 0
                for char in binmessage:
                  print char
                  if int(char) == 1:
                        tone = device.create_tone(base + up + currenttone) 
                        tone.play()
                        sleep(0.015)
                        tone.stop()
                        print base + up + currenttone
                        print '1'
                        currenttone += 100
                  if int(char) == 0:
                        tone = device.create_tone(base + down + currenttone)
                        tone.play()
                        sleep(0.015)
                        tone.stop()
                        print base + down + currenttone
                        print '0'
                        currenttone += -100
        else:
                message = raw_input("Enter your message: \n")
        ##        if len(key) == 16:
        ##      file_data += "\n" * (16-len(file_data) % 16)#Make length of file data 16 
        ##  else:
        ##          file_data += "\n" * (32-len(file_data) % 32)#Make length of file data 32
                #header = 'DATA:MESSAGE'
                #messagefix = header + message
                binmessage = bin(int(binascii.hexlify(message), 16))
                binmessage = str(binmessage[2:])
                raw_input("Press enter to send '" + message + "'")
                print binmessage
                currenttone = 0
                for char in binmessage:
                  print char
                  if int(char) == 1:
                        tone = device.create_tone(base + up + currenttone) 
                        tone.play()
                        sleep(0.07)
                        tone.stop()
                        print base + up + currenttone
                        print '1'
                        currenttone += 100
                  if int(char) == 0:
                        tone = device.create_tone(base + down + currenttone)
                        tone.play()
                        sleep(0.07)
                        tone.stop()
                        print base + down + currenttone
                        print '0'
                        currenttone += -100
                #save(message)
 
def filetrans(exist, filedata):
        tone = device.create_tone(1000)
        tone.play()
        sleep(1)
        tone.stop()
        print "\n\nFile Sending\n\n"
##      key = raw_input("Enter a key with a length of 16, or 32 Characters: ")
##      mode = AES.MODE_ECB #ECB AES
##      encryptor = AES.new(key, mode)
        if exist == 1:
                binfile = bin(int(binascii.hexlify(filedata), 16))
                binfile = str(binfile[2:])
                raw_input("Press enter to send the file")
                currenttone = 0
                for char in binmessage:
                  print char
                  if int(char) == 1:
                        tone = device.create_tone(base + up + currenttone) 
                        tone.play()
                        sleep(0.07)
                        tone.stop()
                        print base + up + currenttone
                        print '1'
                        currenttone += 100
                  if int(char) == 0:
                        tone = device.create_tone(base + down + currenttone)
                        tone.play()
                        sleep(0.07)
                        tone.stop()
                        print base + down + currenttone
                        print '0'
                        currenttone += -100
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
                enc_file = bin(int(binascii.hexlify(file_data), 16))
                print enc_file
                enc_file = str(enc_file[2:])
                print enc_file
                currenttone = 0
                for char in binmessage:
                  print char
                  if int(char) == 1:
                        tone = device.create_tone(base + up + currenttone) 
                        tone.play()
                        sleep(0.07)
                        tone.stop()
                        print base + up + currenttone
                        print '1'
                        currenttone += 100
                  if int(char) == 0:
                        tone = device.create_tone(base + down + currenttone)
                        tone.play()
                        sleep(0.07)
                        tone.stop()
                        print base + down + currenttone
                        print '0'
                        currenttone += -100
                f.close()
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
