print "Dwse stoixeia xrisimopoiontas to keno metaksi tous!"
lista=raw_input()
newlista=lista.split( )

count=0
for i in range (len(newlista)): 
	if newlista[i]=="0":
		count=count+1
for i in range (len(newlista)):
	if newlista[i]=="0":
		newlista[i]=" "
for i in range (count) :
	newlista.append('0')
print newlista
