#Single Toned Fascii Function
#Copyright 2011-2012 Steven Richards <sbrichards@mit.edu>

def tonegen(fasciidata):
	loop = 2
	for char in fasciidata:
       		if loop % 2 == 0:
			#tone = device.create_tone((2000 + (ord(char) * 100) + 100)
			loop += 1
			print char
			print ((2000 + (ord(char) * 100) + 100))
		else:
			#tone = device.create_tone((2000 + (ord(char) * 100) - 100)
			loop += 1
			print char
			print ((2000 + (ord(char) * 100) - 100))
               
