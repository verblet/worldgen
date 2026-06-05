# worldgenlib.py
# Cepheus Engine world generation data and rules library
# v1.1, March 31st, 2018
# This is open source code, feel free to use it for any purpose.
# Contact the author at golan2072@gmail.com.

#import modules
import random
import string
import stellagama

def size_gen():
  """
  generates the size number
  """
  worldsize=0
  worldsize=stellagama.dice(2,6) - 2
  return worldsize #outputs world size number

def atmo_gen(uwp): #inputs world size number
  """
  generates the atmosphere number
  """
  worldatmo=0
  worldatmo=stellagama.dice(2,6)-7 + uwp['worldsize']
  if uwp['worldsize'] in [0,1]:
    worldatmo = 0
  if worldatmo < 0:
    worldatmo = 0
  if worldatmo > 12:
    worldatmo = 6
  return worldatmo #outputs atmosphere number

def hyd_gen(uwp): #inputs world size number
  """
  generates the hydrographics number
  """
  worldhyd=0
  worldhyd=stellagama.dice(2,6) - 7 + uwp['worldatmo']
  if uwp['worldatmo'] in [0,1]:
    worldhyd-=2
  if uwp['worldatmo'] in [10,11,12]:
    worldhyd-=4
  if uwp['worldsize'] in [0,1]:
    worldhyd=0
  if worldhyd < 0:
    worldhyd = 0
  if worldhyd > 10:
    worldhyd = 5
  return worldhyd #outputs hydrographics number

def pop_gen (uwp): #inputs world size, atmospehere, and hydrographics numbers
  """
  generates the population number
  """
  worldpop=0
  worldpop=stellagama.dice(2,6)-2
  if uwp['worldatmo'] < 3 or uwp['worldatmo']>9:
    worldpop-=2
  if uwp['worldatmo'] in [4,7,9]:
    worldpop+=1
  if uwp['worldatmo'] in [5,8]:
    worldpop+=2
  if uwp['worldatmo'] in [6]:
    worldpop+=3
  if worldpop<0:
    worldpop=0
  if worldpop>10:
    worldpop=10
  return worldpop #outputs population number
  
def starport_gen (uwp): #inputs the world population number
  """
  generate uwp['starport'] letter
  """
  starport="X"
  starport_roll=stellagama.dice(2,6) - 7 + uwp['worldpop']
  if starport_roll < 4:
    starport="X"
#  if starport_roll in [2,3,4]:
#    starport="E"
  if starport_roll in [4,5]:
    starport="D"
  if starport_roll in [6,7,8]:
    starport="C"
  if starport_roll in [9,10]:
    starport="B"
  if starport_roll>=11:
    starport="A"
  return starport #outputs the uwp['starport'] letter

def gov_gen (uwp): #inputs the world population number
  """
  generate government number
  """
  worldgov=0
  worldgov=stellagama.dice(2,6) - 7 + uwp['worldpop']
  if worldgov<0:
    worldgov=0
  if worldgov>12:
    worldgov=12
  return worldgov #outputs the world government number

def law_gen (uwp): #inputs the world government number
  """
  generate law level number
  """
  worldlaw=0
  worldlaw=stellagama.dice(2,6) - 2
  return worldlaw #outputs the world law level number

def tech_gen (uwp): #input the world's uwp['starport'], size, atmosphere, hydrographics, population, and government ratings - 6 parameters
    """
    generate tech-level number
    """
    worldtech=0
    worldtech=stellagama.dice(1,6)
    if uwp['starport'] == "A":
      worldtech+=6
    if uwp['starport']== "B":
      worldtech+=4
    if uwp['starport']== "C":
      worldtech+=2

    if uwp['worldsize'] in [0, 1]:
      worldtech+=2

    if uwp['worldatmo'] in [0, 1, 2, 3, 4,7,9, 10, 11, 12]:
      worldtech+=1

    if uwp['worldhyd'] in [0,1,9]:
      worldtech+=1
    if uwp['worldhyd'] in [10]:
      worldtech+=2

    if uwp['worldpop'] in [0, 1, 2, 3, 4, 5, 9]:
      worldtech+=1
    if uwp['worldpop']==10:
      worldtech+=2

    if uwp['worldatmo'] in [4, 7, 9] and worldtech < 5:
      worldtech=5
    if uwp['worldhyd'] in [0, 10] and worldtech < 7:
      worldtech=7
    if uwp['worldatmo'] in [1, 2, 10, 11, 12] and worldtech < 7:
      worldtech=7

    if worldtech<0:
      worldtech=0
    if worldtech>12:
      worldtech=12

    return worldtech #outputs the world tech level number

def uwp_list_gen(uwp): #input the world's uwp['starport'], size, atmosphere, hydrographics, population, government, law, and tech-level ratings - 8 parameters
  """
  convert world variables into a UWP list
  """
  uwp_list=[uwp['starport'], uwp['worldsize'], uwp['worldhyd'], uwp['worldatmo'], uwp['worldpop'], uwp['worldgov'], uwp['worldlaw'], uwp['worldtech']]
  return uwp_list #outputs the UWP list

def trade_gen (uwp_list): #input UWP list
  """
  determine trade codes from a UWP list
  """
  trade_list=[]
  if uwp_list['worldatmo'] in [4, 5, 6, 7, 8, 9] and uwp_list['worldhyd'] in [4, 5, 6, 7, 8, 9] and uwp_list['worldpop'] in [5, 6, 7, 8]:
    trade_list.append("Ag")
  if uwp_list['worldsize'] == 0:
    trade_list.append("As")
  if uwp_list['worldatmo'] > 1 and uwp_list['worldhyd'] == 0:
    trade_list.append("De")
  if uwp_list['worldatmo'] >= 10 and uwp_list['worldhyd'] >= 1:
    trade_list.append ("Fl")
  if uwp_list['worldatmo'] in [5, 6, 8] and uwp_list['worldhyd'] in [4, 5, 6, 7, 8, 9] and uwp_list['worldpop'] in [4, 5, 6, 7, 8]:
    trade_list.append("Ga")
  if uwp_list['worldpop'] > 8:
    trade_list.append("Hi")
  if uwp_list['worldtech'] >= 12:
    trade_list.append("Ht")
  if uwp_list['worldatmo'] in [0, 1] and uwp_list['worldhyd'] >= 1:
    trade_list.append("Ic")
  if uwp_list['worldatmo'] in [0, 1, 2, 3, 4, 7, 9,10,11,12] and uwp_list['worldpop'] > 7:
    trade_list.append("In")
  if uwp_list['worldpop'] < 5:
    trade_list.append("Lo")
  if uwp_list['worldtech'] < 5:
    trade_list.append("Lt")
  if uwp_list['worldatmo'] in [0, 1, 2, 3,10,11,12] and uwp_list['worldhyd'] in [0, 1, 2, 3] and uwp_list['worldpop'] >= 6:
    trade_list.append("Na")
  if uwp_list['worldpop'] in [4, 5, 6]:
    trade_list.append("Ni")
  if uwp_list['worldatmo'] in [2, 3, 4, 5] and uwp_list['worldhyd'] in [0, 1, 2, 3]:
    trade_list.append("Po")
  if uwp_list['worldatmo'] in [6, 8] and uwp_list['worldpop'] in [6, 7, 8]:
    trade_list.append("Ri")
  if uwp_list['worldhyd'] == 10:
    trade_list.append("Wa")
  if uwp_list['worldatmo'] == 0:
    trade_list.append("Va")
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
  for i in range (1, trade_count):
    trade_list.append("  ")
  trade_string= " ".join(trade_list)
  return trade_string #output trade code string  

def pop_mod (uwp): #inputs the world population number
  """
  generates the population multiplier
  """
  popmod=0
  popmod=stellagama.lodice(2,3,6)-2
  if popmod in [0,10]:
    popmod=1

  if uwp['worldpop'] in [1,4,7,9]:
    popmod = str(popmod) + "0"
  if uwp['worldpop'] in [2,5,8]:
    popmod = str(popmod) + "00"
  if uwp['worldpop'] in [3,4,5]:
    popmod = str(popmod) + "k"
  if uwp['worldpop'] in [6,7,8]:
    popmod = str(popmod) + "mn"
  if uwp['worldpop'] in [9,10]:
    popmod = str(popmod) + "bn"
  return popmod #outputs the world population multiplier  


def gcode_gen (uwp):
  """
  calculate gravity for planet
  """
  if uwp['worldsize'] == 0:
    gcode = 0
  if uwp['worldsize'] == 1:
    gcode = 0.05
  if uwp['worldsize'] == 2:
    gcode = 0.15
  if uwp['worldsize'] == 3:
    gcode = 0.4
  if uwp['worldsize'] == 4:
    gcode = 0.6
  if uwp['worldsize'] == 5:
    gcode = 0.8
  if uwp['worldsize'] == 6:
    gcode = 1
  if uwp['worldsize'] == 7:
    gcode = 1.1
  if uwp['worldsize'] == 8:
    gcode = 1.2
  if uwp['worldsize'] == 9:
    gcode = 1.3
  if uwp['worldsize'] == 10:
    gcode = 1.4

  return gcode


def hab_gen (uwp):
  """
  generate habitable zone variance (-2 inferno to +2 frozen)
  """
  worldhab_tag= 'Vr'
  worldhab_roll=stellagama.dice(2,6)-2


  if uwp['worldatmo'] in [3,4,5,6,7,8,9]:
    worldhab_roll += 2
  if uwp['worldatmo'] > 9:
    worldhab_roll += 4

  if worldhab_roll in [0,1]:
    worldhab_tag = 'Fz'

  if uwp['worldatmo'] in [3,4,5,6,7,8,9]:
    if worldhab_roll in [2,3,4]:
      worldhab_tag = 'Tu'
    if worldhab_roll in [5,6,7,8,9]:
      worldhab_tag = 'Te'
    if worldhab_roll in [10,11,12]:
      worldhab_tag = 'Tr'

  if worldhab_roll in [13,14]:
    worldhab_tag = 'If'

 # Calculate atmospshere requirements for humanoids
  if uwp['worldatmo'] in [0,1]:
    worldhab_tag = worldhab_tag + " Vx"
  if uwp['worldatmo'] in [2,3]:
    worldhab_tag = worldhab_tag + " Cx"
  if uwp['worldatmo'] in [4,7,9]:
    worldhab_tag = worldhab_tag + " Fx"
  if uwp['worldatmo'] in [10]:
    worldhab_tag = worldhab_tag +  " Ox"
  if uwp['worldatmo'] in [11,12]:
    worldhab_tag = worldhab_tag +  " Hx"

  return "[" + worldhab_tag + "]" #outputs the world habitable zone variance

def planetoid_gen(uwp): #input world size
  """
  determine planetoid presence
  """
  planetoid=0
  planetoid_presence=0
  planetoid_presence=stellagama.dice(2,6)
  if planetoid_presence >= 4 or uwp['worldsize'] == 0:
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

def pbg_gen(uwp): #input world UWP list
  """
  generates a three-digit code of the population multiplier, planetoid belt number, and gas giant number
  """
  popmod=pop_mod(uwp)
  planetoid=planetoid_gen(uwp)
  gas=gas_gen()
  pbg = "%s;%s;%s" % (popmod, planetoid, gas)
  return pbg #output "PBG" three-digit code
  
def base_gen(uwp): #input starship letter
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
  if uwp['starport'] in ["A", "B"]:
    naval_presence=stellagama.dice(2, 6)
    if naval_presence >= 8:
      naval=1
    else:
      naval=0
  if uwp['starport'] in ["A", "B", "C", "D"]:
    scout_presence=stellagama.dice(2, 6)
    if uwp['starport'] == "C":
      scout_presence -= 1
    if uwp['starport'] == "B":
      scout_presence -= 2
    if uwp['starport'] == "A":
      scout_presence -= 3
    if scout_presence >= 7:
      scout=1
  if uwp['starport'] != "A" and naval != 1:
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
  if uwp_list['worldatmo'] >= 10 or uwp_list['worldgov'] in [0, 7, 10] or uwp_list['worldlaw'] == 0 or uwp_list['worldlaw'] >= 9:
    zone=" A "
  else:
    zone="   "
  return zone #output Amber Zone

def uwp_gen():
    """
    generate world UWP list
    List explanation:
    h - uwp['starport']
    uwp_list['worldsize'] - size
    uwp_list['worldatmo'] - atmosphere
    uwp_list['worldhyd'] - hydrographics
    uwp_list['worldpop'] - population
    uwp_list['worldgov'] - government
    uwp_list['worldlaw'] - law level
    uwp_list['worldtech'] - tech-level
    """

    uwp={}
    uwp['worldsize']=size_gen() #generate world size
    uwp['worldatmo']=atmo_gen(uwp) #generate world atmosphere
    uwp['worldhyd']=hyd_gen(uwp) #generate world hydrographics
    uwp['worldpop']=pop_gen(uwp) #generate world population
    uwp['starport']=starport_gen(uwp) #generate world uwp['starport']
    uwp['worldgov']=gov_gen(uwp) #generate world government
    uwp['worldlaw']=law_gen(uwp) #generate world law level
    uwp['worldtech']=tech_gen(uwp) #generate world tech-level
    uwp_list=uwp #convert everything to a list
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
    if size=="D" and uwp_list['worldatmo']>=1:
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
  char_list=[base_name]
  length_count=int(7-len(base_name)//2)
  if int(len(base_name)%2)==0:
    length_count+=1
  if length_count<=0:
    length_count=0
  for i in range (1, length_count):
    char_list.append(" ")
  name= " ".join(char_list)
  return name #output random name
  
# Testing area

print (name_gen())