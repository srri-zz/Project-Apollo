#Single Toned Fascii Decoding
#Copyright 2011-2012 Steven Richards <sbrichards@mit.edu>

start = 1
if which != len(fftData)-1:
        y0,y1,y2 = np.log(fftData[which-1:which+2:])
        x1 = (y2 - y0) * .5 / (2 * y1 - y2 - y0)
        # find the frequency and output it
        thefreq = (which+x1)*RATE/chunk
        
        if int(round(thefreq, -2)) > 2000:
        	found = 'true'
      		if start == 1:
			start = 0
			currentmode = 2
			juststarted = 1
		currentmode += 1		  	
        if found == 'true' and (int(round(thefreq, -2)) != (lasttone) or juststarted == 1)
                if currentmode % 2 == 0:
			tempvar = (int(round(thefreq, -2)) - 2100) / 100
        	        outputstring += chr(tempvar)
			lasttone = int(round(thefreq, -2))
		else:
			tempvar = (int(round(thefreq, -2)) - 1900) / 100
			outputstring += chr(tempvar)
			lasttone = int(round(thefreq, -2))
		juststarted = 0


