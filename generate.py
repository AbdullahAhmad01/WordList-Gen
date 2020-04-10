print("")

class KbGen:
	def __init__(self):
		self.files = []
		self.keys=[]
		
		try:
			kb_basic_file=open("./kb_basic", "r")
		except:
			kb_basic_file=False

		if(kb_basic_file):
			print("Message : 'kb_basic' accessed")
			self.files.append("kb_basic")
			kw=kb_basic_file.readline()
			while(kw):
				self.keys.append(kw)
				kw=kb_basic_file.readline()
			print("Message : basic keys readed from 'kb_basic' file")
		else:
			print("Problem : 'kb_basic' not found or permission denied. \nSolution : Continue without basic keys\n")
		if(kb_basic_file):
			kb_basic_file.close()
		print("Help : Enter 'm' for Menu")
		KbGen.menu(self)

	def sep(str_val):
		res = []
		thisval="";
		for c in str_val:
			if(c!="" and c!=" " and c!="\n" and c!="\t" and c!="\x0b" and c!= "\x0c"):
				thisval+=str(c)
			else :
				if(res.count(thisval)==0):
					res.append(thisval)
				thisval=""		
		if(res.count(thisval)==0):
			res.append(thisval)
		return res
	
	def rev(str_val):
		res=""
		i=int(len(str_val))-1
		while(i>=0):
			res+=str(str_val[i])
		return res
	
	def menu(self):
		command = input("\nCommand : ")
		if(command=="m"):
			print("\n\n\t\tMenu\n\t p - print keys\n\t r - remove all keys\n\t n - add name\n\t v - add vehicle \n\t i - import  \n\t e - export \n\t q - quit\n\n")
			KbGen.menu(self)

		elif(command=="p"):
			KbGen.print_keys(self)
			KbGen.menu(self)

		elif(command=="r"):
			print("Message : removing "+str(len(self.keys))+" keys. ", end="")
			self.keys=[]
			print("OK.")
			KbGen.menu(self)

		elif(command=="n"):
			KbGen.add_name(self)
			KbGen.menu(self)

		elif(command=="v"):
			KbGen.add_vehicle(self)
			KbGen.menu(self)

		elif(command=="i"):
			KbGen.import_from_file(self)
			KbGen.menu(self)

		elif(command=="e"):
			KbGen.export_to_file(self)
			KbGen.menu(self)

		elif(command=="q"):
			exit()

		else :
			print ("Illegal command")
			KbGen.menu(self)

	def print_keys(self):
		i=1;
		print("\n\t[Total : "+str(len(self.keys))+"]")
		for key in self.keys:
			print(str(i)+" - "+key, end="")
			if(i%20==0):
				if(input("\t\t\t\t\t\t\t\t\t\tEnter to continue or s to stop : ")=="s"):
					break
			i+=1
		print("--END--")
	
	def add_name(self):
		nm = input("\nEnter Name : ")
		if(input("Manual config (y/n) : ")=="y"):
			config=True
		else :
			config=False
		
		nospace=True
		duplicate=True
		space=True
		minus=False
		underscore=False
		capital=True
		lower=True
		upper=False
		#reverse=False
		verbous=False

		if(config):
			val=input("Joined words (y/n) : ")
			if(val=="y"):
				nospec=True
			elif(val=="n"):
				nospec=False
			else :
				print("Massage : Using default joining (True)");

			val=input("Duplicate words (y/n) : ")
			if(val=="y"):
				duplicate=True
			elif(val=="n"):
				duplicate=False
			else :
				print("Massage : Using default duplication (True)");
			
			val=input("Spaced words (y/n) : ")
			if(val=="y"):
				space=True
			elif(val=="n"):
				space=False
			else :
				print("Massage : Using default spacing (True)");
			
			val=input("Minus (-) between words (y/n) : ")
			if(val=="y"):
				minus=True
			elif(val=="n"):
				minus=False
			else :
				print("Massage : Using default minus (False)");
			
			val=input("Underscore (_) between words (y/n) : ")
			if(val=="y"):
				underscore=True
			elif(val=="n"):
				underscore=False
			else :
				print("Massage : Using default underscore (False)");
			
			val=input("Capitalize words (y/n) : ")
			if(val=="y"):
				capital=True
			elif(val=="n"):
				capital=False
			else :
				print("Massage : Using default capitilization (True)");
			
			val=input("Lowercase words (y/n) : ")
			if(val=="y"):
				lower=True
			elif(val=="n"):
				lower=False
			else :
				print("Massage : Using default for lower words (True)");
			
			val=input("Uppercase words (y/n) : ")
			if(val=="y"):
				upper=True
			elif(val=="n"):
				upper=False
			else :
				print("Massage : Using default for upper words (False)");

			#val=input("Reverse all (y/n) : ")
			#if(val=="y"):
			#	reverse=True
			#elif(val=="n"):
			#	reverse=False
			#else :
			#	print("Using default reverse (False)");

			val=input("Verbous (y/n) : ")
			if(val=="y"):
				verbous=True
			elif(val=="n"):
				verbous=False
			else :
				print("Massage : Using default verbouse (False)");
		
		nm_word=KbGen.sep(nm)
		out = []


		if(len(nm_word)>0):
			for w in nm_word:
				out.append(w)
			if(capital and out.count(w.capitalize())==0):
				out.append(w.capitalize())

			if(verbous):
				print("Message : level 1 completed.")
		else :
			print("No name specified. ")

		if(len(nm_word)>1):
			for w1 in nm_word:
				for w2 in nm_word:
					if(w1==w2 and duplicate==False):
						continue
					if(nospace and out.count(w1+w2)==0):
						out.append(w1+w2)
					if(space and out.count(w1+" "+w2)==0):
						out.append(w1+" "+w2)
					if(minus and out.count(w1+"-"+w2)):
						out.append(w1+"-"+w2)
					if(underscore and out.count(w1+"_"+w2)):
						out.append(w1+"_"+w2)
			if(capital):
				for w1 in nm_word:
					w1=w1.capitalize()
					for w2 in nm_word:
						w2=w2.capitalize()
						if(w1==w2 and duplicate==False):
							continue
						if(nospace and out.count(w1+w2)==0):
							out.append(w1+w2)
						if(space and out.count(w1+" "+w2)==0):
							out.append(w1+" "+w2)
						if(minus and out.count(w1+"-"+w2)==0):
							out.append(w1+"-"+w2)
						if(underscore and out.count(w1+"_"+w2)==0):
							out.append(w1+"_"+w2)
			if(verbous):
				print("Message : level 2 completed.")

		if(len(nm_word)>2):
			for w1 in nm_word:
				for w2 in nm_word:
					for w3 in nm_word:
						if((w1==w2 or w2==w3 or w1==w3) and duplicate==False):
							continue
						if(nospace and out.count(w1+w2+w3)==0):
							out.append(w1+w2+w3)
						if(space and out.count(w1+" "+w2+" "+w3)==0):
							out.append(w1+" "+w2+" "+w3)
						if(minus and out.count(w1+"-"+w2+"-"+w3)==0):
							out.append(w1+"-"+w2+"-"+w3)
						if(underscore and out.count(w1+"_"+w2+"_"+w3)==0):
							out.append(w1+"_"+w2+"_"+w3)
			if(capital):
				for w1 in nm_word:
					w1=w1.capitalize()
					for w2 in nm_word:
						w2=w2.capitalize()
						for w3 in nm_word:
							w3=w3.capitalize()
							if((w1==w2 or w2==w3 or w1==w3) and duplicate==False):
								continue
							if(nospace and out.count(w1+w2+w3)==0):
								out.append(w1+w2+w3)
							if(space and out.count(w1+" "+w2+" "+w3)==0):
								out.append(w1+" "+w2+" "+w3)
							if(minus and out.count(w1+"-"+w2+"-"+w3)==0):
								out.append(w1+"-"+w2+"-"+w3)
							if(underscore and out.count(w1+"_"+w2+"_"+w3)==0):
								out.append(w1+"_"+w2+"_"+w3)
			if(verbous):
				print("Message : level 3 completed.")
		
		if(len(nm_word)>3):
			for w1 in nm_word:
				for w2 in nm_word:
					for w3 in nm_word:
						for w4 in nm_word:
							if((w1==w2 or w1==w3 or w1==w4 or w2==w3 or w2==w4 or w3==w4) and duplicate==False):
								continue
							if(nospace and out.count(w1+w2+w3+w4)==0):
								out.append(w1+w2+w3+w4)
							if(space and out.count(w1+" "+w2+" "+w3+" "+w4)==0):
								out.append(w1+" "+w2+" "+w3+" "+w4)
							if(minus and out.count(w1+"-"+w2+"-"+w3+"-"+w4)==0):
								out.append(w1+"-"+w2+"-"+w3+"-"+w4)
							if(underscore and out.count(w1+"_"+w2+"_"+w3+"_"+w4)==0):
								out.append(w1+"_"+w2+"_"+w3+"_"+w4)
			if(capital):
				for w1 in nm_word:
					w1=w1.capitalize()
					for w2 in nm_word:
						w2=w2.capitalize()
						for w3 in nm_word:
							w3=w3.capitalize()
							for w4 in nm_word:
								w4=w4.capitalize()
								if((w1==w2 or w1==w3 or w1==w4 or w2==w3 or w2==w4 or w3==w4) and duplicate==False):
									continue
								if(nospace and out.count(w1+w2+w3+w4)==0):
									out.append(w1+w2+w3+w4)
								if(space and out.count(w1+" "+w2+" "+w3+" "+w4)==0):
									out.append(w1+" "+w2+" "+w3+" "+w4)
								if(minus and out.count(w1+"-"+w2+"-"+w3+"-"+w4)==0):
									out.append(w1+"-"+w2+"-"+w3+"-"+w4)
								if(underscore and out.count(w1+"_"+w2+"_"+w3+"_"+w4)==0):
									out.append(w1+"_"+w2+"_"+w3+"_"+w4)
			if(verbous):
				print("Message : level 4 completed.")

		if(lower):
			for k in out:
				nk=k.lower()
				if(nk==k or out.count(nk)>0):
					continue
				else:
					out.append(nk)
			if(verbous):
				print("Message : lowercase process completed.")

		if(upper):
			for k in out:
				nk=k.upper()
				if(nk==k or out.count(nk)>0):
					continue
				else:
					out.append(nk)
			if(verbous):
				print("Message : uppercase process completed.")
		
		print("Message : Adding "+str(len(out))+" keys. ", end="")
		i=0
		for k in out:
			k=str(k)+"\n"
			if(self.keys.count(k)==0):
				i+=1
				self.keys.append(k)
		print("OK.")
		print("Message : Added "+str(i)+" keys")
	
	def add_vehicle(self):
		no = input("\nEnter Number : ")
		if(input("Manual config (y/n)")=="y"):
			config=True
		else:
			config=False
		
		nospace=True
		duplicate=True
		space=True
		minus=False
		underscore=False
		capital=False
		lower=True
		upper=False
		verbous=False

		
		if(config):
			val=input("Joining (y/n) : ")
			if(val=="y"):
				nospec=True
			elif(val=="n"):
				nospec=False
			else :
				print("Massage : Using default joining (True)");

			val=input("Duplication (y/n) : ")
			if(val=="y"):
				duplicate=True
			elif(val=="n"):
				duplicate=False
			else :
				print("Massage : Using default duplication (True)");
			
			val=input("Spacing (y/n) : ")
			if(val=="y"):
				space=True
			elif(val=="n"):
				space=False
			else :
				print("Massage : Using default spacing (True)");
			
			val=input("Minus (-) sign (y/n) : ")
			if(val=="y"):
				minus=True
			elif(val=="n"):
				minus=False
			else :
				print("Massage : Using default minus (False)");
			
			val=input("Underscore (_) sign (y/n) : ")
			if(val=="y"):
				underscore=True
			elif(val=="n"):
				underscore=False
			else :
				print("Massage : Using default underscore (False)");
			
			val=input("Capitalization (y/n) : ")
			if(val=="y"):
				capital=True
			elif(val=="n"):
				capital=False
			else :
				print("Massage : Using default capitilization (False)");
			
			val=input("Transform Lowercase (y/n) : ")
			if(val=="y"):
				lower=True
			elif(val=="n"):
				lower=False
			else :
				print("Massage : Using default for lower words (True)");
			
			val=input("Transform Uppercase (y/n) : ")
			if(val=="y"):
				upper=True
			elif(val=="n"):
				upper=False
			else :
				print("Massage : Using default for upper words (False)");

			#val=input("Reverse all (y/n) : ")
			#if(val=="y"):
			#	reverse=True
			#elif(val=="n"):
			#	reverse=False
			#else :
			#	print("Massage : Using default reverse (False)");

			val=input("Verbous (y/n) : ")
			if(val=="y"):
				verbous=True
			elif(val=="n"):
				verbous=False
			else :
				print("Massage : Using default verbouse (False)");
		
		no_parts=KbGen.sep(no)
		out = []

		if(len(no_parts)>0):
			for w in no_parts:
				out.append(w)
			if(capital and out.count(w.capitalize())==0):
				out.append(w.capitalize())

			if(verbous):
				print("Message : level 1 completed.")
		else :
			print("No name specified. ")

		if(len(no_parts)>1):
			for w1 in no_parts:
				for w2 in no_parts:
					if(w1==w2 and duplicate==False):
						continue
					if(nospace and out.count(w1+w2)==0):
						out.append(w1+w2)
					if(space and out.count(w1+" "+w2)==0):
						out.append(w1+" "+w2)
					if(minus and out.count(w1+"-"+w2)):
						out.append(w1+"-"+w2)
					if(underscore and out.count(w1+"_"+w2)):
						out.append(w1+"_"+w2)
			if(capital):
				for w1 in no_parts:
					w1=w1.capitalize()
					for w2 in no_parts:
						w2=w2.capitalize()
						if(w1==w2 and duplicate==False):
							continue
						if(nospace and out.count(w1+w2)==0):
							out.append(w1+w2)
						if(space and out.count(w1+" "+w2)==0):
							out.append(w1+" "+w2)
						if(minus and out.count(w1+"-"+w2)==0):
							out.append(w1+"-"+w2)
						if(underscore and out.count(w1+"_"+w2)==0):
							out.append(w1+"_"+w2)
			if(verbous):
				print("Message : level 2 completed.")

		if(len(no_parts)>2):
			for w1 in no_parts:
				for w2 in no_parts:
					for w3 in no_parts:
						if((w1==w2 or w2==w3 or w1==w3) and duplicate==False):
							continue
						if(nospace and out.count(w1+w2+w3)==0):
							out.append(w1+w2+w3)
						if(space and out.count(w1+" "+w2+" "+w3)==0):
							out.append(w1+" "+w2+" "+w3)
						if(minus and out.count(w1+"-"+w2+"-"+w3)==0):
							out.append(w1+"-"+w2+"-"+w3)
						if(underscore and out.count(w1+"_"+w2+"_"+w3)==0):
							out.append(w1+"_"+w2+"_"+w3)
			if(capital):
				for w1 in no_parts:
					w1=w1.capitalize()
					for w2 in no_parts:
						w2=w2.capitalize()
						for w3 in no_parts:
							w3=w3.capitalize()
							if((w1==w2 or w2==w3 or w1==w3) and duplicate==False):
								continue
							if(nospace and out.count(w1+w2+w3)==0):
								out.append(w1+w2+w3)
							if(space and out.count(w1+" "+w2+" "+w3)==0):
								out.append(w1+" "+w2+" "+w3)
							if(minus and out.count(w1+"-"+w2+"-"+w3)==0):
								out.append(w1+"-"+w2+"-"+w3)
							if(underscore and out.count(w1+"_"+w2+"_"+w3)==0):
								out.append(w1+"_"+w2+"_"+w3)
			if(verbous):
				print("Message : level 3 completed.")
		
		if(len(no_parts)>3):
			for w1 in no_parts:
				for w2 in no_parts:
					for w3 in no_parts:
						for w4 in no_parts:
							if((w1==w2 or w1==w3 or w1==w4 or w2==w3 or w2==w4 or w3==w4) and duplicate==False):
								continue
							if(nospace and out.count(w1+w2+w3+w4)==0):
								out.append(w1+w2+w3+w4)
							if(space and out.count(w1+" "+w2+" "+w3+" "+w4)==0):
								out.append(w1+" "+w2+" "+w3+" "+w4)
							if(minus and out.count(w1+"-"+w2+"-"+w3+"-"+w4)==0):
								out.append(w1+"-"+w2+"-"+w3+"-"+w4)
							if(underscore and out.count(w1+"_"+w2+"_"+w3+"_"+w4)==0):
								out.append(w1+"_"+w2+"_"+w3+"_"+w4)
			if(capital):
				for w1 in no_parts:
					w1=w1.capitalize()
					for w2 in no_parts:
						w2=w2.capitalize()
						for w3 in no_parts:
							w3=w3.capitalize()
							for w4 in no_parts:
								w4=w4.capitalize()
								if((w1==w2 or w1==w3 or w1==w4 or w2==w3 or w2==w4 or w3==w4) and duplicate==False):
									continue
								if(nospace and out.count(w1+w2+w3+w4)==0):
									out.append(w1+w2+w3+w4)
								if(space and out.count(w1+" "+w2+" "+w3+" "+w4)==0):
									out.append(w1+" "+w2+" "+w3+" "+w4)
								if(minus and out.count(w1+"-"+w2+"-"+w3+"-"+w4)==0):
									out.append(w1+"-"+w2+"-"+w3+"-"+w4)
								if(underscore and out.count(w1+"_"+w2+"_"+w3+"_"+w4)==0):
									out.append(w1+"_"+w2+"_"+w3+"_"+w4)
			if(verbous):
				print("Message : level 4 completed.")

		if(lower):
			for k in out:
				nk=k.lower()
				if(nk==k or out.count(nk)>0):
					continue
				else:
					out.append(nk)
			if(verbous):
				print("Message : lowercase process completed.")

		if(upper):
			for k in out:
				nk=k.upper()
				if(nk==k or out.count(nk)>0):
					continue
				else:
					out.append(nk)
			if(verbous):
				print("Message : uppercase process completed.")
		
		print("Message : Adding "+str(len(out))+" keys. ", end="")
		i=0
		for k in out:
			k=str(k)+"\n"
			if(self.keys.count(k)==0):
				i+=1
				self.keys.append(k)
		print("OK.")
		print("Message : Added "+str(i)+" keys.")

	def import_from_file(self):
		flnm=input("\nFilename (including path) : ")
		if(input("Verbous (y/n) : ")=="y"):
			verbouse=True
		else :
			verbous=False
			print("Message : Using default (False)")

		out=[]
		try:
			fl = open(flnm, "r")
		except:
			fl = False
		if(not fl):
			print("Problem : File not exists or permission denied.")
		else :
			if(verbouse):
				print("Message : file accessed. \nMessage : Reading lines. ", end="")
			i=1
			kw=fl.readline()
			while(kw):
				out.append(kw)
				i+=1
				kw=fl.readline()
			print(" OK..")
			fl.close()
			print("Message : Readed "+str(i)+" lines")

				
			print("Message : Adding "+str(len(out))+" keys. ", end="")
			i=0
			for k in out:
				if(self.keys.count(k)==0):
					i+=1
					self.keys.append(k)
			print("OK.")
			print("Message : Added "+str(i)+" keys")

	def export_to_file(self):
		flnm=input("\nFilename (including path) : ")
		try:
			fl = open(flnm, "w")
		except:
			fl = False
		
		if(fl):
			duplicate=True
			pass_on=False

			inp_val=input("What to do with < 8s (d - duplicate, e - eliminate, p - pass on) : ")
			if(inp_val=="d"):
				duplicate=True
			elif(inp_val=="e"):
				duplicate=False
			elif(inp_val=="p"):
				passon=True
			else :
				print("Message : Using default (duplicate).")
			
			print("Message : Writing on file. ", end="")
			i=0
			for k in self.keys:
				if(not pass_on):
					if (len(k)<9 and duplicate):
						k=KbGen.sep(k)[0]
						tk=""
						while (len(tk)<9):
							tk+=k
						k=str(tk)+"\n"
					if (len(k)>8):
						i+=1
						fl.write(k)
				else:
					fl.write(k)
			print("OK.")
			print("Message : Written "+str(i)+" lines")
		else :
			print("Problem : File could not created")


KbGen()
