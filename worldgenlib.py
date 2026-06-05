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
	if starport_roll in [2,3,4]:
		starport="X"
	if starport_roll in [5,6]:
		starport="D"
	if starport_roll in [7,8]:
		starport="C"
	if starport_roll in [9,10]:
		starport="B"
	if starport_roll in [11,12]:
		starport="A"

	return starport #outputs the starport letter

def size_gen(starport):
	"""
	generates the size number
	"""
	worldsize=0
	worldsize=stellagama.dice(2,6)-2

	if starport in ['A','B']: # A & B starbases tend to be around larger worlds.
		worldsize=stellagama.hidice(2,3,6)-2
	if starport in ['X']: # X starbases are remote outposts around smaller worlds.
		worldsize=stellagama.lodice(2,3,6)-2
	if worldsize < 0:
		worldsize = 0

	return worldsize #outputs world size number

def atmo_gen(worldsize): #inputs world size number
	"""
	generates the atmosphere number
	"""
	worldatmo=0
	worldatmo=stellagama.dice(2,6)-7 + worldsize
	if worldsize in [-1]: # small worlds have no atmosphere
		worldatmo = -1
	if worldsize in [0]: # small worlds have no atmosphere
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
	# planets with less than thin atmosphere have extreme temperature variations
	if worldatmo in [0,1]:
		worldtemp = -1
	# planets with hostile atmospheres are hotter
	if worldatmo >= 10:
		worldtemp += 3
	if worldtemp < 0:
		worldtemp = -1
	if worldtemp > 10:
		worldtemp = 10
	return worldtemp #outputs temperature number

def hyd_gen(worldsize,worldatmo): #inputs world size number
	"""
	generates the hydrographics number
	"""
	worldhyd=0
	worldhyd=stellagama.dice(2,6) - 7 + worldatmo
	if worldatmo in [-1,0,1,10,11,12,13]:
		worldhyd -= 6
	if worldhyd < 0:
		worldhyd = 0
	if worldhyd > 10:
		worldhyd = 10

	return worldhyd #outputs hydrographics number


def pop_gen (starport): #inputs world size, atmospehere, and hydrographics numbers
	"""
	generates the population number
	"""
	worldpop=0
	"""
	if starport in ["A","B","C","D"]:
		worldpop=stellagama.hidice(2,3,6)-2
		if starport in ["A","B"] and worldpop < 6:
			worldpop = 6
	if starport in ["X"]:
		worldpop=stellagama.lodice(2,3,6)-2
	"""

	if starport in ["A","B"]:
		worldpop=stellagama.hidice(2,3,6)-2
		if worldpop < 6:
			worldpop = 6
	elif starport in ["C","D"]:
		worldpop=stellagama.dice(2,6)-2
	elif starport in ["X"]:
		worldpop=stellagama.lodice(2,3,6)-2
	if worldpop<0:
		worldpop=0
	if worldpop>12:
		worldpop=12
	return worldpop #outputs population number
	
def gov_gen (worldpop): #inputs the world economy number
	"""
	generate government number
	"""
	worldgov=0
	worldgov=stellagama.dice(2,6) - 7 + worldpop
	if worldgov < 0:
		worldgov=0
	if worldgov>12:
		worldgov=12
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
	if worldlaw>9:
		worldlaw=9
	if worldlaw<0:
		worldlaw=0
	return worldlaw #outputs the world law level number

def tech_gen (starport, worldsize, worldatmo, worldhyd, worldpop, worldgov): #input the world's starport, size, atmosphere, hydrographics, population, and government ratings - 6 parameters
	"""
	generate tech-level number
	"""
	worldtech=0
	worldtech=stellagama.dice(1,6)

	if starport == "A":
		worldtech+=4
	if starport== "B":
		worldtech+=3
	if starport== "C":
		worldtech+=2

	if worldsize in [0, 1]:
			worldtech+=2


	if worldatmo in [2,3,4,7,9]:
		worldtech+=2
	if worldatmo in [0,1] or worldatmo > 9:
		worldtech+=2

	if worldpop in [1, 2, 3, 4]:
		worldtech+=1
	if worldpop == 8:
		worldtech+=2
	if worldpop == 9:
		worldtech+=2
	if worldpop == 10:
		worldtech+=2

	if worldpop == 0:
		worldtech = 0

	"""
	# Ind worlds need min tech of 6
	if worldatmo in [0, 1, 2, 4, 7, 9] and worldpop >= 8 and world_tech < 6:
		worldtech=6

	# Vaccuum words, asteroids and orbitals need a min tech of 8
	if (worldatmo in [0,1,2,3] or worldsize < 1) and world_tech < 6:
		worldtech=8
	"""

	if worldtech<0:
		worldtech=0
	if worldtech>12:
		worldtech=12

	return worldtech #outputs the world tech level number

def uwp_list_gen(starport, worldsize, worldatmo, worldhyd, worldpop, worldgov, worldlaw, worldtech): #input the world's starport, size, atmosphere, hydrographics, population, government, law, and tech-level ratings - 8 parameters
	"""
	convert world variables into a UWP dictionary
	"""
	uwp_list={
		"starport": starport,
		"worldsize": worldsize,
		"worldatmo": worldatmo,
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

	popmult=stellagama.dice(1,10)
	if popmult == 10:
		popmult = 1
	popmult = str(popmult)

	'''
	if uwp_list['worldpop'] == 0:
		trade_list.append("0")
	if uwp_list['worldpop'] == 1:
		trade_list.append(popmult + " ")
	if uwp_list['worldpop'] == 2:
		trade_list.append(popmult + "0")
	if uwp_list['worldpop'] == 3:
		trade_list.append(popmult + "00")
	if uwp_list['worldpop'] == 4:
		trade_list.append(popmult + "000")
	if uwp_list['worldpop'] == 5:
		trade_list.append(popmult + "0000")
	if uwp_list['worldpop'] == 6:
		trade_list.append(popmult + "00000")
	if uwp_list['worldpop'] == 7:
		trade_list.append(popmult + "000000")
	if uwp_list['worldpop'] == 8:
		trade_list.append(popmult + "0000000")
	if uwp_list['worldpop'] == 9:
		trade_list.append(popmult + "00000000")
	if uwp_list['worldpop'] == 10:
		trade_list.append(popmult + "000000000")
	if uwp_list['worldpop'] == 11:
		trade_list.append(popmult + "0000000000")
	if uwp_list['worldpop'] == 12:
		trade_list.append(popmult + "00000000000")
	'''


	if worldhyd in [3,4,5,6,7,8,9] and worldatmo in [5,6,8]	: hab = 3;
	else if worldhyd in [3,4,5,6,7,8,9,10] and worldatmo in [,6,8]: hab =2

	if uwp_list['worldpop'] == 0:
		trade_list.append("0")
	if uwp_list['worldpop'] == 1:
		trade_list.append("10")
	if uwp_list['worldpop'] == 2:
		trade_list.append("100")
	if uwp_list['worldpop'] == 3:
		trade_list.append("1000")
	if uwp_list['worldpop'] == 4:
		trade_list.append("10000")
	if uwp_list['worldpop'] == 5:
		trade_list.append("100000")
	if uwp_list['worldpop'] == 6:
		trade_list.append("1000000")
	if uwp_list['worldpop'] == 7:
		trade_list.append("10000000")
	if uwp_list['worldpop'] == 8:
		trade_list.append("100000000")
	if uwp_list['worldpop'] == 9:
		trade_list.append("1000000000")
	if uwp_list['worldpop'] == 10:
		trade_list.append("10000000000")
	if uwp_list['worldpop'] == 11:
		trade_list.append("100000000000")
	if uwp_list['worldpop'] == 12:
		trade_list.append("1000000000000")

	if uwp_list['worldsize'] <= 0:
		trade_list.append("0")
	elif uwp_list['worldsize'] == 1:
		trade_list.append("0.05")
	elif uwp_list['worldsize'] == 2:
		trade_list.append("0.15")
	elif uwp_list['worldsize'] == 3:
		trade_list.append("0.4")
	elif uwp_list['worldsize'] == 4:
		trade_list.append("0.6")
	elif uwp_list['worldsize'] == 5:
		trade_list.append("0.8")
	elif uwp_list['worldsize'] == 6:
		trade_list.append("1.0")
	elif uwp_list['worldsize'] == 7:
		trade_list.append("1.2")
	elif uwp_list['worldsize'] == 8:
		trade_list.append("1.4")
	elif uwp_list['worldsize'] == 9:
		trade_list.append("1.6")
	elif uwp_list['worldsize'] == 10:
		trade_list.append("1.8")
	elif uwp_list['worldsize'] == 11:
		trade_list.append("2.0")
	elif uwp_list['worldsize'] == 12:
		trade_list.append("2.2")
	else:
		trade_list.append("-")

	if uwp_list['worldatmo'] in [0]:
		trade_list.append("Vaccuum")
	if uwp_list['worldatmo'] in [1]:
		trade_list.append("Trace")
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
		trade_list.append("Radioactive")
	if uwp_list['worldatmo'] == 13:
		trade_list.append("Extreme")

	if uwp_list['worldatmo'] in [2,4,7,9]:
		trade_list.append("Tainted")
	else:
		trade_list.append("-")

	worldtemp = tmpt_gen(uwp_list['worldatmo'])

	if worldtemp in [-1]:
		trade_list.append("ExtremeVariable")
	if worldtemp in [0,1]:
		trade_list.append("Cold")
	if worldtemp in [2,3]:
		trade_list.append("Cool")
	if worldtemp in [4,5,6]:
		trade_list.append("Temperate")
	if worldtemp in [7,8]:
		trade_list.append("Warm")
	if worldtemp in [9,10]:
		trade_list.append("Hot")

	if uwp_list['worldatmo'] in [0,1]:
		trade_list.append("Vaccsuit")
	elif uwp_list['worldatmo'] in [2,3]:
		trade_list.append("Compressor")
	elif uwp_list['worldatmo'] in [4,7,9]:
		trade_list.append("Filter")
	elif uwp_list['worldatmo'] in [5,6,8]:
		trade_list.append("Breathable")
	elif uwp_list['worldatmo'] == 10:
		trade_list.append("Oxygen")
	elif uwp_list['worldatmo'] == 11:
		trade_list.append("Hardsuit")
	elif uwp_list['worldatmo'] == 12:
		trade_list.append("Radsuit")
	elif uwp_list['worldatmo'] == 13:
		trade_list.append("Exocraft")

	if uwp_list['worldpop'] >= 9:
		trade_list.append("HiPop")
	elif uwp_list['worldpop'] in [1,2,3,4]:
		trade_list.append("LoPop")
	elif uwp_list['worldpop'] == 0:
		trade_list.append("NoPop")
	else:
		trade_list.append("-")

	if uwp_list['worldgov'] == 0:
		trade_list.append("NoGovt")
	if uwp_list['worldgov'] == 1:
		trade_list.append("Technocratic")
	if uwp_list['worldgov'] == 2:
		trade_list.append("Communal")
	if uwp_list['worldgov'] == 3:
		trade_list.append("Participative")
	if uwp_list['worldgov'] == 4:
		trade_list.append("Feudal")
	if uwp_list['worldgov'] == 5:
		trade_list.append("Disunited")
	if uwp_list['worldgov'] == 6:
		trade_list.append("Colonial")
	if uwp_list['worldgov'] == 7:
		trade_list.append("Theocratic")
	if uwp_list['worldgov'] == 8:
		trade_list.append("Representative")
	if uwp_list['worldgov'] == 9:
		trade_list.append("Oligarchic")
	if uwp_list['worldgov'] == 10:
		trade_list.append("Bureaucratic")
	if uwp_list['worldgov'] == 11:
		trade_list.append("Corporate")
	if uwp_list['worldgov'] == 12:
		trade_list.append("Dictatorship")

	trade_list.append(str(uwp_list['worldtech']))

	if uwp_list['worldatmo'] in [4, 5, 6, 7, 8, 9] and uwp_list['worldhyd'] in [4, 5, 6, 7, 8, 9] and uwp_list['worldpop'] in [5, 6, 7, 8]:
		trade_list.append("Agri")
	elif uwp_list['worldatmo'] in [0, 1, 2, 3, 10, 11, 12, 13] and uwp_list['worldhyd'] in [0, 1, 2, 10] and uwp_list['worldpop'] > 3:
		trade_list.append("NonAgri")
	else:
		trade_list.append("-")

	if uwp_list['worldatmo'] in [0, 1, 2, 3, 4, 7, 9,10,11,12,13] and uwp_list['worldpop'] >= 7 and uwp_list['worldtech'] > 4:
		trade_list.append("Ind")
	elif uwp_list['worldpop'] in [4,5,6]:
		trade_list.append("NonInd")
	else:
		trade_list.append("-")

	if uwp_list['worldsize'] == -1:
		trade_list.append("Orbital")
	elif uwp_list['worldsize'] == 0:
		trade_list.append("Asteroid")
	else:
		if uwp_list['worldatmo'] in [0,1] and uwp_list['worldhyd'] >= 1:
			trade_list.append("Iceball")
		elif uwp_list['worldatmo'] >= 2 and uwp_list['worldhyd'] == 0:
			trade_list.append("Desert")
		elif uwp_list['worldatmo'] >= 10 and uwp_list['worldhyd'] > 1:
			trade_list.append ("Fluid")
		elif uwp_list['worldatmo'] in [2,3] and uwp_list['worldhyd'] in [1,2,3]:
			trade_list.append("Bleak")
		elif uwp_list['worldatmo'] in [5,6,8] and uwp_list['worldhyd'] in [4,5,6,7,8]:
			trade_list.append("Garden")
		elif uwp_list['worldhyd'] in [10]:
			trade_list.append("Oceanic")
		else:
			trade_list.append("-")

	if uwp_list['worldatmo'] not in [5,6,8] and uwp_list['worldpop'] in [1,2,3,4]:
		trade_list.append("Outpost")
	elif uwp_list['worldatmo'] in [5,6,8] and uwp_list['worldhyd'] in [4,5,6,7,8] and uwp_list['worldpop'] < 6:
		trade_list.append("Reserve")
	elif uwp_list['worldpop'] > 4 and uwp_list['worldtech'] < 7:
		trade_list.append("Poor")
	elif uwp_list['worldpop'] > 5 and uwp_list['worldatmo'] in [5,6,8] and uwp_list['worldhyd'] in [4,5,6,7,8] and uwp_list['worldtech'] > 8:
		trade_list.append("Rich")
	else:
		trade_list.append("-")

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
	popmod=stellagama.lodice(2,3,6)-2
	if popmod==0:
		popmod=1
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

def pbg_gen(uwp_list): #input world UWP list
	"""
	generates a three-digit code of the population multiplier, planetoid belt number, and gas giant number
	"""
	popmod=pop_mod(uwp_list['worldpop'])
	planetoid=planetoid_gen(uwp_list['worldsize'])
	gas=gas_gen()
	pbg = "%s %s %s" % (popmod,planetoid, gas)
	return pbg #output "PBG" three-digit code
	
def base_gen (starport): #input starship letter
	"""
	determine base presence
	"""
	bases=[]
	naval=0
	naval_presence=0
	scout=0
	scout_presence=0
	presense_mod=0

	if starport in ["A"]:
		presense_mod = 2 
	if starport in ["B"]:
		presense_mod = 1 

	naval_presence=stellagama.dice(2, 6) + presense_mod
	scout_presence=stellagama.dice(2, 6) + presense_mod
	force_presence=stellagama.dice(2, 6) + presense_mod
	union_presence=stellagama.dice(2, 6) + presense_mod
	merchant_presence=stellagama.dice(2, 6) + presense_mod
	science_presence=stellagama.dice(2, 6) + presense_mod
	church_presence=stellagama.dice(2, 6) + presense_mod

	'''
	if starport != "X":
		if starport in ["A","B"] and naval_presence >= 10:
			bases.append("Nav")
		if starport in ["C","D"] and scout_presence >= 8:
			bases.append("Sco")
		if force_presence >= 10:
			bases.append("For")
		if union_presence >= 8:
			bases.append("Uni")
		if merchant_presence >= 8:
			bases.append("Mer")
		if science_presence >= 10:
			bases.append("Sci")
		if church_presence >= 10:
			bases.append("Chu")
	'''
	if not bases:
		bases.append("NA")

	bases_string = '+'.join(bases)

	return bases_string #output base letter

def zone_gen(uwp_list): #input UWP list
	"""
	determine Amber Zone presence
	"""
	zone=""
	if uwp_list['worldatmo'] >= 10 or uwp_list['worldpop'] in [0, 7, 10] or uwp_list['worldgov'] == 0 or uwp_list['worldgov'] >= 9:
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
		uwp_list['worldgov'] - government
		uwp_list[6] - law level
		uwp_list['worldtech'] - tech-level
		"""
		starport=starport_gen() #generate world starport
		worldsize=size_gen(starport) #generate world size
		worldatmo=atmo_gen(worldsize) #generate world atmosphere
		worldhyd=hyd_gen(worldsize,worldatmo) #generate world hydrographics
		worldpop=pop_gen(starport) #generate world population
		worldgov=gov_gen(worldpop) #generate world government
		worldlaw=law_gen(worldgov) #generate world government
		worldtech=tech_gen(starport, worldsize, worldatmo, worldhyd, worldpop, worldgov) #generate world tech-level
		uwp_list=uwp_list_gen(starport, worldsize, worldatmo, worldhyd, worldpop, worldgov, worldlaw, worldtech) #convert everything to a list
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
	uwp.append(stellagama.pseudo_hex(uwp_list['worldgov']))
	uwp.append(stellagama.pseudo_hex(uwp_list['worldlaw']))
	uwp.append(stellagama.pseudo_hex(uwp_list['worldtech']))
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
    if uwp_list['worldatmo']>=4 and uwp_list['worldatmo']<=9:
        throw=throw+4
        tag=1
    if uwp_list['worldpop']>=8 and tag==0:
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
    if uwp_list['worldatmo']>=4 and uwp_list['worldatmo']<=9:
        throw1=throw1+4
        tag=1
    if uwp_list['worldpop']>=8 and tag==0:
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