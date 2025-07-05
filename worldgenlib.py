# worldgenlib.py
# Cepheus Engine world generation data and rules library
# v1.1, March 31st, 2018
# This is open source code, feel free to use it for any purpose.
# Contact the author at golan2072@gmail.com.

#import modules
import random
import string
import stellagama

def starport_gen():
	"""
	generate starport letter
	"""
	starport="X"
	starport_roll=stellagama.dice(2,6)
	if starport_roll <= 4:
		starport="X"
	if starport_roll in [5, 6]:
		starport="D"
	if starport_roll in [7, 8]:
		starport="C"
	if starport_roll in [9,10]:
		starport="B"
	if starport_roll>=11:
		starport="A"

	return starport #outputs the starport letter

def size_gen(starport):
	"""
	generates the size number
	"""
	worldsize=0
	worldsize=stellagama.dice(2,6)
	##if starport in ['A','B']:
	##	worldsize += 1
	if starport  == 'D':
		worldsize -= 1
	if starport == 'X':
		worldsize -= 2
	if worldsize < 0:
		worldsize = 0
	if worldsize > 12:
		worldsize = 7
	return worldsize #outputs world size number

def atmo_gen(worldsize): #inputs world size number
	"""
	generates the atmosphere number
	"""
	worldatmo=0
	worldatmo=stellagama.dice(2,6)-7 + worldsize
	if worldsize in [0,1,2]: # small worlds havae no atmosphere
		worldatmo = 0
	if worldatmo < 0:
		worldatmo = 0
	if worldatmo > 13:
		worldatmo = 13
	return worldatmo #outputs atmosphere number

def tmpt_gen(worldatmo): #inputs atmos number
	"""
	generates the temperature number
	"""

	worldtemp=0
	worldtemp=stellagama.dice(2,6) - 2
	if worldatmo > 9:
		worldtemp += 3
	if worldtemp < 0:
		worldtemp = 0
	if worldtemp > 10:
		worldtemp = 10
	return worldtemp #outputs temperature number

def hyd_gen(worldatmo,worldtemp): #inputs world size number
	"""
	generates the hydrographics number
	"""
	worldhyd=0
	worldhyd=stellagama.dice(2,6) - 7 + worldatmo
	if worldatmo >= 10: # Hot and weird worlds have less water
		worldhyd -= 4
	if worldatmo in [1,2]: # Atmosphereless worlds have no water
		worldhyd = 0
	if worldhyd < 0:
		worldhyd = 0
	if worldhyd > 10:
		worldhyd = 10

	return worldhyd #outputs hydrographics number

def hab_gen(worldatmo, worldtemp, worldhyd):
	if worldhyd == 0 or worldatmo in [0,1,10,11,12,13]:
		worldhab = "NoHab"
	elif worldhyd in [1,2,3] or worldatmo in [2,3]:
		worldhab = "LoHab"
	elif worldhyd in [4,5,6,7,8,9] and worldatmo in [5,6,7,8]:
		worldhab = "HiHab"
	else:
		worldhab = "MdHab"
	return worldhab

def pop_gen (starport,worldhab): #inputs world size, atmospehere, and hydrographics numbers
	"""
	generates the population number
	"""
	worldpop=0
	worldpop=stellagama.dice(2,6)
	if worldhab == "HiHab" or starport in ['A','B']:
		worldpop += 1
	if worldhab == "NoHab":
		worldpop -= 2
	if starport == 'X':
		worldpop -= 2
	if worldpop < 0:
		worldpop = 0
	if worldpop > 12:
		worldpop = 12
	"""
	if starport == 'X':
		worldpop -= 3

	if worldatmo in [5, 6, 8]:
		worldpop += 1
	if worldatmo <= 2 and worldpop > 5:
		worldpop = 5
	if worldpop < 0:
		worldpop = 0
	if worldpop > 10:
		worldpop = 10
	"""
	return worldpop #outputs population number
	

def gov_gen (worldpop): #inputs the world population number
	"""
	generate government number
	"""
	worldgov=0
	worldgov=stellagama.dice(2,6) - 7 + worldpop
	if worldgov < 0:
		worldgov=0
	if worldgov>15:
		worldgov=15
	if worldpop==0:
		worldgov=0
	return worldgov #outputs the world government number

def law_gen (worldgov): #inputs the world government number
	"""
	generate law level number
	"""
	worldlaw=0
	worldlaw=stellagama.dice(2,6) - 7 + worldgov
	if worldgov == 0:
		worldlaw=0
	if worldlaw>15:
		worldlaw=15
	if worldlaw<0:
		worldlaw=0
	return worldlaw #outputs the world law level number

def tech_gen (starport, worldsize, worldatmo, worldtemp, worldhyd, worldpop, worldgov): #input the world's starport, size, atmosphere, hydrographics, population, and government ratings - 6 parameters
		"""
		generate tech-level number
		"""
		worldtech=0
		worldtech=stellagama.dice(1,6)
		if starport == "A":
			worldtech+=6
		if starport== "B":
			worldtech+=4
		if starport== "C":
			worldtech+=2
		if starport== "X":
			worldtech-=4
		if worldsize in [0, 1]:
			worldtech+=2
		if worldsize in [2, 3, 4]:
			worldtech+=1
		if worldatmo in [0, 1, 2, 3, 10, 11, 12, 13, 14, 15]:
			worldtech+=1
		if worldhyd in [0, 9]:
			worldtech+=1
		if worldhyd == 10:
			worldtech+=2
		if worldpop == 0:
			worldtech=0
		if worldpop in [1, 2, 3, 4, 5, 9]:
			worldtech+=1
		if worldpop==10:
			worldtech+=2
		if worldpop==11:
			worldtech+=3
		if worldpop==12:
			worldtech+=4
		if worldgov in [0, 5]:
			worldtech+=1
		if worldgov==7:
			worldtech+=2
		if worldgov in [13, 14]:
			worldtech-=2
		if worldhyd in [0, 10] and worldpop >= 6 and worldtech < 4:
			worldtech=4
		if worldatmo in [4, 7, 9] and worldtech <5:
			worldtech=5
		if worldatmo < 3 or worldatmo in [10, 11, 12]:
			if worldtech < 7:
				worldtech=7
		if worldatmo in [13, 14] and worldhyd==10 and worldtech<7:
			worldtech=7
		if worldtech<0:
			worldtech=0
		return worldtech #outputs the world tech level number

def uwp_list_gen(starport, worldsize, worldatmo, worldtemp, worldhyd, worldpop, worldgov, worldlaw, worldtech): #input the world's starport, size, atmosphere, hydrographics, population, government, law, and tech-level ratings - 8 parameters
	"""
	convert world variables into a UWP dictionary
	"""
	uwp_list={
		"starport": starport,
		"worldsize": worldsize,
		"worldatmo": worldatmo,
		"worldtemp": worldtemp,
		"worldhyd": worldhyd,
		"worldpop": worldpop,
		"worldgov": worldgov,
		"worldlaw": worldlaw,
		"worldtech": worldtech
	}

	return uwp_list #outputs the UWP dictionary

def trade_gen (uwp_list): #input UWP list
	"""
	determine trade codes from a UWP list
	"""

	trade_list=[]

	popmult=min(stellagama.dice(1,10),stellagama.dice(1,10))
	popadd=stellagama.dice(1,10)
	if popmult == 10:
		popmult = 1
	if popadd == 10:
		popadd = 0
	if uwp_list['worldpop'] == 0:
		trade_list.append("0")
	if uwp_list['worldpop'] == 1:
		trade_list.append(str(random.randint(1, 9)) + "    ")
	if uwp_list['worldpop'] == 2:
		trade_list.append(str(random.randint(10, 99)) + "   ")
	if uwp_list['worldpop'] == 3:
		trade_list.append(str(random.randint(100, 999)) + "  ")
	if uwp_list['worldpop'] == 4:
		trade_list.append(str(popmult) + "000" + "  ")
	if uwp_list['worldpop'] == 5:
		trade_list.append(str(popmult) + str(popadd) + "000" + " ")
	if uwp_list['worldpop'] == 6:
		trade_list.append(str(popmult) + str(popadd) + "0000" + " ")
	if uwp_list['worldpop'] == 7:
		trade_list.append(str(popmult) + "000000" + "  ")
	if uwp_list['worldpop'] == 8:
		trade_list.append(str(popmult) + "000000" + "  ")
	if uwp_list['worldpop'] == 9:
		trade_list.append(str(popmult) + "000000" + " ")
	if uwp_list['worldpop'] == 10:
		trade_list.append(str(popmult) + str(popadd) + "000000" + " ")
	if uwp_list['worldpop'] == 11:
		trade_list.append(str(popmult) + str(popadd) + "000000" + " ")
	if uwp_list['worldpop'] == 12:
		trade_list.append(str(popmult) + str(popadd) + "0000000" + " ")

	if uwp_list['worldpop'] == 0:
		pop = "NoPop"
	if uwp_list['worldpop'] in [1,2,3]:
		pop = "VlPop"
	if uwp_list['worldpop'] in [4,5]:
		pop = "LoPop"
	if uwp_list['worldpop'] in [6,7,8,9]:
		pop = "MdPop"
	if uwp_list['worldpop'] >= 10:
		pop = "HiPop"
	trade_list.append(pop)

	hab = hab_gen(uwp_list['worldatmo'], uwp_list['worldtemp'], uwp_list['worldhyd'])
	trade_list.append(hab)

	if uwp_list['worldatmo'] in [0,1]:
		trade_list.append("Vaccuum")
	if uwp_list['worldatmo'] in [2,3]:
		trade_list.append("VeryThin")
	if uwp_list['worldatmo'] in [4,5]:
		trade_list.append("Thin")
	if uwp_list['worldatmo'] in [6,7]:
		trade_list.append("Standard")
	if uwp_list['worldatmo'] in [8,9]:
		trade_list.append("Dense")
	if uwp_list['worldatmo'] == 10:
		trade_list.append("Exotic")
	if uwp_list['worldatmo'] == 11:
		trade_list.append("Corrosive")
	if uwp_list['worldatmo'] == 12:
		trade_list.append("Insidous")
	if uwp_list['worldatmo'] == 13:
		trade_list.append("Radioactive")

	if uwp_list['worldatmo'] in [4,9]:
		trade_list.append("Tainted")
	else:
		trade_list.append("Untainted")

	if uwp_list['worldtemp'] in [0]:
		trade_list.append("Cold")
	if uwp_list['worldtemp'] in [1]:
		trade_list.append("Cold")
	if uwp_list['worldtemp'] in [2,3]:
		trade_list.append("Cool")
	if uwp_list['worldtemp'] in [4,5,6]:
		trade_list.append("Temperate")
	if uwp_list['worldtemp'] in [7,8]:
		trade_list.append("Warm")
	if uwp_list['worldtemp'] in [9]:
		trade_list.append("Hot")
	if uwp_list['worldtemp'] in [10]:
		trade_list.append("Hot")

	if uwp_list['worldhyd'] == 0:
		trade_list.append("Anhydrous")
	if uwp_list['worldhyd'] in [1,2]:
		trade_list.append("Arid")
	if uwp_list['worldhyd'] in [3]:
		trade_list.append("Lakes")
	if uwp_list['worldhyd'] in [4,5,6,7,8]:
		trade_list.append("Continental")
	if uwp_list['worldhyd'] in [9]:
		trade_list.append("Islands")
	if uwp_list['worldhyd'] in [10]:
		trade_list.append("Pelagic")

	if hab in ["HiHab"] and uwp_list['worldpop'] in [5,6,7,8,9,10]:
		trade_list.append("Agricultural")
	elif hab in ["NoHab","LoHab"]:
		trade_list.append("Non-Agricultural")
	else:
		trade_list.append("Other")

	if hab not in ["HiHab"] and uwp_list['worldpop'] in [9,10,11,12]:
		trade_list.append("Industrial")
	elif uwp_list['worldpop'] in [3,4,5,6]:
		trade_list.append("Non-Industrial")
	else:
		trade_list.append("Other")

	if hab == "NoHab" and uwp_list['worldpop'] in [0,1,2,3]:
		trade_list.append("Outpost")
	elif hab == "HiHab" and pop in [0,1,2,3,4,5,6]:
		trade_list.append("Reserve")
	else:
		trade_list.append("Other")


	trade_list.append(uwp_list['starport'])
	
	return trade_list #output trade code list

def trade_stringer (trade_list): #input trade code list
	"""
	build a Trade Code string suitable for a SEC file
	Note that this is a plain text file formatted by spaces so the trade code string's length must be fixed.
	"""
	trade_string=""
	trade_count=6-len(trade_list)
	if trade_count<=0:
		trade_count=0
	#for i in range (1, trade_count):
		#trade_list.append("  ")
	trade_string= " ".join(trade_list)
	return trade_string #output trade code string	

def pop_mod (worldpop): #inputs the world population number
	"""
	generates the population multiplier
	"""
	popmod=0
	popmod=stellagama.dice(2,6) - 2
	if worldpop==0:
		popmod=0
	if popmod>9:
		popmod=9
	return popmod #outputs the world population multiplier	

def planetoid_gen(worldsize): #input world size
	"""
	determine planetoid presence
	"""
	planetoid=0
	planetoid_presence=0
	planetoid_presence=stellagama.dice(2,6)
	if planetoid_presence >= 4 or worldsize == 0:
		planetoid=stellagama.dice(1, 6) - 3
		if planetoid < 1:
			planetoid = 1
	else:
		planetoid=0
	return planetoid #output planetoid belt number

def gas_gen():
	"""
	determine gas giant presence
	"""
	gas=0
	gas_presence=0
	gas_presence=stellagama.dice(2,6)
	if gas_presence >= 5:
		gas=stellagama.dice(1, 6) - 2
		if gas < 1:
			gas = 1
	else:
		gas=0
	return gas #output gas giant number

def pbg_gen(uwp_list): #inout world UWP list
	"""
	generates a three-digit code of the population multiplier, planetoid belt number, and gas giant number
	"""
	popmod=pop_mod(worldpop)
	planetoid=planetoid_gen(worldsize)
	gas=gas_gen()
	pbg = "%s%s%s" % (popmod, planetoid, gas)
	return pbg #output "PBG" three-digit code
	
def base_gen (starport): #input starship letter
	"""
	determine base presence
	"""
	base=" "
	naval=0
	naval_presence=0
	scout=0
	scout_presence=0
	pirate=0
	pirate_presence=0
	if starport in ["A", "B"]:
		naval_presence=stellagama.dice(2, 6)
		if naval_presence >= 8:
			naval=1
		else:
			naval=0
	if starport in ["A", "B", "C", "D"]:
		scout_presence=stellagama.dice(2, 6)
		if starport == "C":
			scout_presence -= 1
		if starport == "B":
			scout_presence -= 2
		if starport == "A":
			scout_presence -= 3
		if scout_presence >= 7:
			scout=1
	if starport != "A" and naval != 1:
		pirate_presence=stellagama.dice(2, 6)
		if pirate_presence >= 12:
			pirate=1
		else:
			pirate=0
	if naval==1 and scout==1 and pirate!=1:
		base="A"
	if scout==1 and pirate==1 and naval!=1:
		base="G"
	if naval==1 and scout!=1 and pirate!=1:
		base="N"
	if naval!=1 and scout!=1 and pirate==1:
		base="P"
	if naval!=1 and scout==1 and pirate!=1:
		base="S"
	return base #output base letter

def zone_gen(uwp_list): #input UWP list
	"""
	determine Amber Zone presence
	"""
	zone=""
	if worldatmo >= 10 or uwp_list[5] in [0, 7, 10] or uwp_list[6] == 0 or uwp_list[6] >= 9:
		zone=" A "
	else:
		zone="   "
	return zone #output Amber Zone

def uwp_gen():
		"""
		generate world UWP list
		List explanation:
		uwp_list[0] - starport
		worldsize - size
		worldatmo - atmosphere
		worldhyd - hydrographics
		worldpop - population
		uwp_list[5] - government
		uwp_list[6] - law level
		uwp_list[7] - tech-level
		"""
		starport=starport_gen() #generate world starport
		worldsize=size_gen(starport) #generate world size
		worldatmo=atmo_gen(worldsize) #generate world atmosphere
		worldtemp=tmpt_gen(worldatmo) #generate world hydrographics
		worldhyd=hyd_gen(worldatmo, worldtemp) #generate world hydrographics
		worldhab=hab_gen(worldatmo, worldtemp, worldhyd) #generate world habilitability rating
		worldpop=pop_gen(starport,worldhab) #generate world population
		worldgov=gov_gen(worldpop) #generate world government
		worldlaw=law_gen(worldgov) #generate world law level
		worldtech=tech_gen(starport, worldsize, worldatmo, worldtemp, worldhyd, worldpop, worldgov) #generate world tech-level
		#uwp_list=uwp_list_gen(starport, worldsize, worldatmo, worldhyd, worldpop) #convert everything to a list
		uwp_list=uwp_list_gen(starport, worldsize, worldatmo, worldtemp, worldhyd, worldpop, worldgov, worldlaw, worldtech) #convert everything to a list
		return uwp_list #output UWP list

def uwp_hex (uwp_list): #input UWP list
	"""
	convert the UWP list to a pseudo-hex UWP string
	"""
	uwp=[]
	uwp.append(uwp_list['starport'])
	uwp.append(stellagama.pseudo_hex(uwp_list['worldsize']))
	uwp.append(stellagama.pseudo_hex(uwp_list['worldatmo']))
	uwp.append(stellagama.pseudo_hex(uwp_list['worldhyd']))
	uwp.append(stellagama.pseudo_hex(uwp_list['worldpop']))
	uwp.append(stellagama.pseudo_hex(0))
	uwp.append(stellagama.pseudo_hex(0))
	uwp.append(stellagama.pseudo_hex(0))
	uwp_string ="%s%s%s%s%s%s%s-%s " % (uwp[0],uwp[1],uwp[2],uwp[3],uwp[4],uwp[5],uwp[6],uwp[7])
	return uwp_string #output Cepheus-style UWP string

def star_gen(uwp_list): #generates realistic stellar data using Constantine Thomas' rules (version 3.0).
    n_stars=0
    size=""
    star_type=""
    startext1=""
    startext2=""
    startext3=""
    startext4=""
    startext=""
    throw=0
    throw1=0
    x=0
    tag=0
    decimal1=0
    decimal2=0
    decimal3=0
    primary=[]
    secondary=[]
    tretiary=[]
    throw=stellagama.dice(2,6)
    if throw<=7:
        n_stars=1
    if throw>=8 and throw<=11:
        n_stars=2
    if throw==12:
        n_stars=3
    throw=stellagama.dice(2,6) #generate primary star
    if worldatmo>=4 and worldatmo<=9:
        throw=throw+4
        tag=1
    if worldpop>=8 and tag==0:
        throw=throw+4
    if throw<=1:
        star_type="B"
    if throw==2:
        star_type="A"
    if throw>=3 and throw<=8:
        star_type="M"
    if throw==9:
        star_type="K"
    if throw==10:
        star_type="G"
    if throw>=11:
        star_type="F"
    if throw==12:
        star_type="K"
    if throw>=13:
        star_type="G"
    decimal1=stellagama.dice(1,10)-1
    throw1=stellagama.dice(2,6)
    if worldatmo>=4 and worldatmo<=9:
        throw1=throw1+4
        tag=1
    if worldpop>=8 and tag==0:
        throw1=throw1+4
    if throw1<=2:
        throw=stellagama.dice(1,6)
        if throw>=1 and throw<=3:
            size="D"
        if throw>=4 and throw<=5:
            size="III"
        if throw==6:
            size="II"
    if throw1==3:
        size="IV"
    if throw1>=4:
        size="V"
    if star_type=="A" or star_type=="F" or star_type=="G":
        if size=="D" or size=="II" or size=="III":
            size="V"
    if star_type=="M" and size=="IV":
        size="V"
    if star_type=="K" and size=="IV" and decimal1>=2:
        size="V"
    if size=="D" and worldatmo>=1:
        size="V"
    if size=="D":
        star_type=""
        decimal1=""
    primary.append(star_type)
    primary.append(decimal1)
    primary.append(size)
    startext1="%s%s%s " % (primary[0], primary[1], primary[2])
    if n_stars==2 or n_stars==3: #generate secondary star
        decimal2=0
        secondary=[]
        size=""
        star_type=""
        throw=stellagama.dice(2,6)
        if throw<=1:
            star_type="B"
        if throw<=2:
            star_type="A"
        if throw>=3 and throw<=8:
            star_type="M"
        if throw==9:
            star_type="K"
        if throw==10:
            star_type="G"
        if throw>=11:
            star_type="F"
        if throw==12:
            star_type="K"
        if throw>=13:
            star_type="G"
        decimal2=stellagama.dice(1,10)-1
        throw1=stellagama.dice(2,6)
        if throw1==2:
            throw=stellagama.dice(1,6)
        if throw>=1 and throw<=3:
            size="D"
        if throw>=4 and throw<=5:
            size="III"
        if throw==6:
            size="II"
        if throw1==3:
            size="IV"
        if throw1>=4:
            size="V"
        if star_type=="A" or star_type=="F" or star_type=="G":
            if size=="D" or size=="II" or size=="III":
                size="V"
        if star_type=="M" and size=="IV":
            size="V"
        if star_type=="K" and size=="IV" and decimal1>=2:
            size="V"
        if size=="D":
            star_type=""
            decimal2=""
        secondary.append(star_type)
        secondary.append(decimal2)
        secondary.append(size)
        startext2="%s%s%s " % (secondary[0], secondary[1], secondary[2])
    if n_stars==3: #generate tretiary star
        decimal3=0
        secondary=[]
        size=""
        star_type=""
        throw=stellagama.dice(2,6)
        if throw<=1:
            star_type="B"
        if throw==2:
            star_type="A"
        if throw>=3 and throw<=8:
            star_type="M"
        if throw==9:
            star_type="K"
        if throw==10:
            star_type="G"
        if throw>=11:
            star_type="F"
        if throw==12:
            star_type="K"
        if throw>=13:
            star_type="G"
        decimal3=stellagama.dice(1,10)-1
        throw1=stellagama.dice(2,6)
        if throw1==2:
            throw=stellagama.dice(1,6)
            if throw>=1 and throw<=3:
                size="D"
            if throw>=4 and throw<=5:
                size="III"
            if throw==6:
                size="II"
        if throw1==3:
            size="IV"
        if throw1>=4:
            size="V"
        if star_type=="A" or star_type=="F" or star_type=="G":
            if size=="D" or size=="II" or size=="III":
                size="V"
        if star_type=="M" and size=="IV":
            size="V"
        if star_type=="K" and size=="IV" and decimal1>=2:
            size="V"
        if size=="D":
            star_type=""
            decimal3=""
        tretiary.append(star_type)
        tretiary.append(decimal3)
        tretiary.append(size)
        startext3="%s%s%s " % (tretiary[0], tretiary[1], tretiary[2])

    startext4=startext1+startext2+startext3
    startext=str.join('', startext4)
    return startext
	
def name_gen():
	"""
	randomly chooses a world name from a list
	"""
	with open("names.txt") as namefile:
		name_list = namefile.readlines()
	base_name=stellagama.random_choice(name_list)
	base_name=base_name.strip()
	name = base_name
	gap = 14-len(base_name)
	for i in range (1, gap):
		name += " "
	return name #output random name
	
# Testing area

print (name_gen())