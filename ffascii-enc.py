#Early development of new encoding method, single toned fascii
#Copyright 2011-2012 Steven Richards <sbrichards@mit.edu>

def tonegen(fasciidata):
	loop = 1
	for char in fasciidata:
       		if loop == 0:
			#tone = device.create_tone((2000 + (ord(char) * 100) + 100)
			loop = 1
			print char
			print ((2000 + (ord(char) * 100) + 100))
		if loop == 1:
  			#tone = device.create_tone((2000 + (ord(char) * 100) - 100)
			loop = 0
			print char
			print ((2000 + (ord(char) * 100) - 100))
tonegen("hello")

                
