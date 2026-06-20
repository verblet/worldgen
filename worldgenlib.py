# worldgenlib.py
# Cepheus Engine world generation data and rules library
# v1.1,March 31st,2018
# This is open source code,feel free to use it for any purpose.
# Contact the author at golan2072@gmail.com.

#import modules
import random
import string
import stellagama

def size_gen(uwp):
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
  if uwp['worldsize'] in [0]:
    worldatmo=0

  if worldatmo<0:
    worldatmo=0
  if worldatmo>12:
    worldatmo=12

  return worldatmo #outputs atmosphere number

def hyd_gen(uwp): #inputs world size number
  """
  generates the hydrographics number
  """
  worldhyd=0
  worldhyd=stellagama.dice(2,6) - 7 + uwp['worldatmo']
  if uwp['worldatmo'] in [0,1,10,11,12]:
    worldhyd-=2
  if worldhyd<0:
    worldhyd=0
  if worldhyd>10:
    worldhyd=6
  return worldhyd #outputs hydrographics number

def pop_gen (uwp): #inputs world size,atmospehere,and hydrographics numbers
  """
  generates the population number
  """
  worldpop=0
  worldpop=stellagama.dice(2,6)-2

  if uwp['worldatmo']<2 or uwp['worldatmo']>9:
    worldpop-=4
  if uwp['worldatmo'] in [5,6,8]:
    worldpop+=1
  if uwp['worldatmo'] in [4,7,9]:
    worldpop+=2

#  if uwp['worldatmo'] in [4,5,7,8,9]:
#    worldpop+=2
#  if uwp['worldatmo'] in [6]:
#    worldpop+=3

  if worldpop<0:
    worldpop=0
  if worldpop>10:
    worldpop=10

  return worldpop #outputs population number
  
def starport_gen (uwp): #inputs the world population number
  starport="E"
  starport_roll=stellagama.dice(2,6) - 7 + uwp['worldpop']
  if starport_roll<4:
    starport="E"
  if starport_roll in [4,5,6]:
    starport="D"
  if starport_roll in [7,8]:
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
  worldlaw=stellagama.dice(2,6) - 7 + uwp['worldgov']
  if worldlaw<0:
    worldlaw=0
  if worldlaw>12:
    worldlaw=12
  return worldlaw #outputs the world law level number

def tech_gen (uwp): #input the world's uwp['starport'],size,atmosphere,hydrographics,population,and government ratings - 6 parameters
    """
    generate tech-level number
    """
    worldtech=0
    worldtech=stellagama.dice(1,6)

    if uwp['starport'] == "A":
      worldtech+=6
    if uwp['starport'] == "B":
      worldtech+=4
    if uwp['starport'] == "C":
      worldtech+=2

    if uwp['worldsize'] in [0,1]:
      worldtech+=2

    if uwp['worldatmo'] in [0,1,2,3,4,7,9,10,11,12]:
      worldtech+=1

    if uwp['worldhyd'] in [0,1,9]:
      worldtech+=1
    if uwp['worldhyd'] in [10]:
      worldtech+=2

    if uwp['worldpop'] in [0,1,2,3,4,5,9]:
      worldtech+=1
    if uwp['worldpop']==10:
      worldtech+=2

    """
    if uwp['worldatmo'] in [4,7,9] and worldtech<5:
      worldtech=5
    if uwp['worldhyd'] in [0,10] and worldtech<7:
      worldtech=7
    if uwp['worldatmo'] in [1,2,10,11,12] and worldtech<7:
      worldtech=7
    """

    if worldtech<0:
      worldtech=0
    if worldtech>12:
      worldtech=12

    return worldtech #outputs the world tech level number

def uwp_list_gen(uwp): #input the world's uwp['starport'],size,atmosphere,hydrographics,population,government,law,and tech-level ratings - 8 parameters
  """
  convert world variables into a UWP list
  """
  uwp_list=[uwp['starport'],uwp['worldsize'],uwp['worldhyd'],uwp['worldatmo'],uwp['worldpop'],uwp['worldgov'],uwp['worldlaw'],uwp['worldtech']]
  return uwp_list #outputs the UWP list

def gov_tag(uwp_list):
  gov=""
  if uwp_list['worldgov'] == 0:
    gov="No central govt"
  if uwp_list['worldgov'] == 1:
    gov="Corporate"
  if uwp_list['worldgov'] == 2:
    gov="Communal"
  if uwp_list['worldgov'] == 3:
    gov="Theocratic"
  if uwp_list['worldgov'] == 4:
    gov="Feudal"
  if uwp_list['worldgov'] == 5:
    gov="Participative"
  if uwp_list['worldgov'] == 6:
    gov="Captive"
  if uwp_list['worldgov'] == 7:
    gov="Disunited"
  if uwp_list['worldgov'] == 8:
    gov="Representative"
  if uwp_list['worldgov'] == 9:
    gov="Oligarchic"
  if uwp_list['worldgov'] == 10:
    gov="Bureaucratic"
  if uwp_list['worldgov'] == 11:
    gov="Technocratic"
  if uwp_list['worldgov'] == 12:
    gov="Dictatorship"

  return gov


def trade_gen (uwp_list): #input UWP list
  """
  determine trade codes from a UWP list
  """
  trade_list=[]
  if uwp_list['worldatmo'] in [4,5,6,7,8,9] and uwp_list['worldhyd'] in [4,5,6,7,8,9] and uwp_list['worldpop'] in [5,6,7]:
    trade_list.append("Ag")
  if uwp_list['worldatmo'] in [2,3,4,5,6,7,8,9] and uwp_list['worldhyd'] in [1,2]:
    trade_list.append("Ar")
  if uwp_list['worldsize'] == 0:
    trade_list.append("As")
  if uwp_list['worldatmo'] in [2,3,4] and uwp_list['worldhyd'] in [0,1,2,3] and uwp_list['worldpop'] >= 5:
    trade_list.append("Bk")
  if uwp_list['worldatmo'] >= 2 and uwp_list['worldhyd'] == 0:
    trade_list.append("De")
  if uwp_list['worldatmo'] >= 10 and uwp_list['worldhyd'] >= 1:
    trade_list.append("Fl")
  if uwp_list['worldatmo'] in [5,6,8] and uwp_list['worldhyd'] in [4,5,6,7,8,9] and uwp_list['worldpop'] in [4,5,6,7,8]:
    trade_list.append("Ga")
  if uwp_list['worldtech'] >= 12:
    trade_list.append("Ht")
  if uwp_list['worldatmo'] in [0,1] and uwp_list['worldhyd'] >= 1:
    trade_list.append("Ic")
  if uwp_list['worldatmo'] not in [5,6,8] and uwp_list['worldpop'] >= 8 and uwp_list['worldtech'] >= 5:
    trade_list.append("In")
  if uwp_list['worldtech'] <= 4:
    trade_list.append("Lt")
  if uwp_list['worldpop'] >= 5 and (uwp_list['worldhyd'] in [0,1,2,10] or uwp_list['worldatmo'] in [0,1,2,3,10,11,12]):
    trade_list.append("Na")
  if uwp_list['worldpop'] in [4,5,6]:
    trade_list.append("Ni")
  if uwp_list['worldpop'] <= 4:
    trade_list.append("Ou")
  if uwp_list['worldatmo'] in [5,6,8] and uwp_list['worldhyd'] in [4,5,6,7,8,9] and uwp_list['worldpop'] <= 3:
    trade_list.append("Re")
  if uwp_list['worldatmo'] in [5,6,8] and uwp_list['starport'] in ['A','B'] and uwp_list['worldpop'] >= 5:
    trade_list.append("Ri")
  if uwp_list['worldpop'] >= 9:
    trade_list.append("Ur")
  if uwp_list['worldhyd'] == 10:
    trade_list.append("Wa")
  if uwp_list['worldatmo'] == 0:
    trade_list.append("Va")
  if uwp_list['worldlaw'] <= 3:
    trade_list.append("Ll")
  if uwp_list['worldlaw'] >= 7:
    trade_list.append("Op")

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
  for i in range (1,trade_count):
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
    popmod=str(popmod) + "0"
  if uwp['worldpop'] in [2,5,8]:
    popmod=str(popmod) + "00"
  if uwp['worldpop'] in [3,4,5]:
    popmod=str(popmod) + "k"
  if uwp['worldpop'] in [6,7,8]:
    popmod=str(popmod) + "mn"
  if uwp['worldpop'] in [9,10]:
    popmod=str(popmod) + "bn"
  return popmod #outputs the world population multiplier  


def grav_gen (uwp):
  """
  calculate gravity for planet
  """
  if uwp['worldsize'] == 0:
    grav=0
  if uwp['worldsize'] == 1:
    grav=0.05
  if uwp['worldsize'] == 2:
    grav=0.15
  if uwp['worldsize'] == 3:
    grav=0.35
  if uwp['worldsize'] == 4:
    grav=0.45
  if uwp['worldsize'] == 5:
    grav=0.7
  if uwp['worldsize'] == 6:
    grav=1
  if uwp['worldsize'] == 7:
    grav=1.2
  if uwp['worldsize'] == 8:
    grav=1.35
  if uwp['worldsize'] == 9:
    grav=1.5
  if uwp['worldsize'] == 10:
    grav=1.7

  return grav


def hab_gen (uwp):
  """
  generate habitable zone variance
  """
  worldhab=temp=gear=''
  worldhab_roll=stellagama.dice(2,6)-2

  if uwp['worldatmo'] in [0,1]:
    worldhab_roll+=6
  if uwp['worldatmo'] in [4,5,6,7,8,9]:
    worldhab_roll+=2
  if uwp['worldatmo'] >= 10:
    worldhab_roll-=6

  if worldhab_roll<0:
    worldhab_roll=0
  if worldhab_roll >14:
    worldhab_roll=14

  if worldhab_roll in [0,1]:
      temp='If'
  if worldhab_roll in [2,3,4]:
      temp='Tr'
  if worldhab_roll in [5,6,7,8,9]:
      temp='Te'
  if worldhab_roll in [10,11,12]:
      temp='Tu'
  if worldhab_roll in [13,14]:
      temp='Fz'

 # Calculate atmospshere requirements for humanoids
  if uwp['worldatmo'] in [0,1]:
    gear='Vx'
  if uwp['worldatmo'] in [2,3]:
    gear='Cx'
  if uwp['worldatmo'] in [4,7,9]:
    gear='Fx'
  if uwp['worldatmo'] in [10]:
    gear='Ox'
  if uwp['worldatmo'] in [11,12]:
    gear='Hx'

  worldhab=temp, gear

  return str.join(' ', worldhab) #outputs the world habitable zone variance

def planetoid_gen(uwp): #input world size
  """
  determine planetoid presence
  """
  planetoid=0
  planetoid_roll=0
  planetoid_roll=stellagama.dice(2,6)
  if planetoid_roll >= 4 or uwp['worldsize'] == 0:
    planetoid=stellagama.dice(1,6) - 3
    if planetoid<1:
      planetoid=1
  else:
    planetoid=0
  return planetoid #output planetoid belt number

def gas_gen():
  """
  determine gas giant presence
  """
  gas=0
  gas_roll=0
  gas_roll=stellagama.dice(2,6)
  if gas_roll >= 5:
    gas=stellagama.dice(1,6) - 2
    if gas<1:
      gas=1
  else:
    gas=0
  return gas #output gas giant number

def pbg_gen(uwp): #input world UWP list
  """
  generates a three-digit code of the population multiplier,planetoid belt number,and gas giant number
  """
  popmod=pop_mod(uwp)
  planetoid=planetoid_gen(uwp)
  gas=gas_gen()
  pbg="%s;%s;%s" % (popmod,planetoid,gas)
  return pbg #output "PBG" three-digit code
  
def base_gen(uwp): #input starship letter
  """
  determine base presence
  """
  base=" "
  naval=0

  # NAVAL BASE
  if uwp['starport'] in ["A","B"]:
    naval_roll=stellagama.dice(2,6)
    if uwp['starport'] == "B":
      naval_roll -= 2
    if naval_roll >= 6:
      naval=1
      base=base + "N"

  # SCOUT BASE
  if uwp['starport'] in ["B","C","D","E"]:
    scout_roll=stellagama.dice(2,6)
    if uwp['starport'] == "D":
      scout_roll -= 1
    if uwp['starport'] == "C":
      scout_roll -= 2
    if uwp['starport'] == "B":
      scout_roll -= 3
    if scout_roll >= 8:
      base=base + "S"      

  # MINING BASE
  if uwp['starport'] in ["C","D"]:
    mining_roll=stellagama.dice(2,6)
    if mining_roll >= 9:
      base=base + "M"

  # RESEARCH BASE
  if uwp['starport'] in ["D","E"]:
    research_roll=stellagama.dice(2,6)
    if uwp['starport'] == "D":
      research_roll -= 2
    if research_roll >= 8:
      base=base + "R"

  # MERCENARY FORCES BASE
  if uwp['worldlaw']<4 and naval != 1:
    merc_roll=stellagama.dice(2,6)
    if merc_roll >= 10:
      base=base + "F"

  return base #output base letter

def zone_gen(uwp_list): #input UWP list
  """
  determine Amber Zone presence
  """
  zone=""
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
    uwp['worldsize']=size_gen(uwp) #generate world size
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

def stellar_gen(uwp_list): #generates realistic stellar data using Constantine Thomas' rules (version 3.0).
    n_stars=0
    startext=[]

    throw=stellagama.dice(2,6)
    if throw<=7:
        n_stars=1
    if throw>=8 and throw<=11:
        n_stars=2
    if throw==12:
        n_stars=3

    startext.append(star_gen(uwp_list,1))
    if n_stars in [2,3]:
      startext.append(star_gen(uwp_list,0))
    if n_stars==3: 
      startext.append(star_gen(uwp_list,0))

    startext_string=str.join('',startext)
    return startext_string


def star_gen(uwp_list,primary):
  decimal=0
  size=""
  star_type=""

  # Star Type
  type_throw=stellagama.dice(2,6)
  if primary:
      if 4<=uwp_list['worldatmo']<=9 and uwp_list['worldpop']>=8:
        type_throw+=4
  if type_throw<=1:
      star_type="B"
  if type_throw==2:
      star_type="A"
  if 3<=type_throw<=8:
      star_type="M"
  if type_throw==9:
      star_type="K"
  if type_throw==10:
      star_type="G"
  if type_throw>=11:
      star_type="F"
  if type_throw==12:
      star_type="K"
  if type_throw>=13:
      star_type="G"

  # Luminosity
  decimal=stellagama.dice(1,10)-1

  # Star Size
  size_throw=stellagama.dice(2,6)
  if size_throw==2:
      size_throw2=stellagama.dice(1,6)
      if 1<=size_throw2<=3:
          size="D"
      if 4<=size_throw2<=5:
          size="III"
      if size_throw2==6:
          size="II"
  if size_throw==3:
      size="IV"
  if size_throw>=4:
      size="V"

  ## Constrain Sizes by Type
  if star_type in ["A","F","G"] and size in ["D","II","III"]:
      size="V"
  if star_type=="M" and size=="IV":
      size="V"
  if star_type=="K" and size=="IV" and decimal>=2:
      size="V"
  if size=="D":
      star_type=""
      decimal=""

  startext="%s%s%s " % (star_type,decimal,size)
  return startext


def name_gen():
  """
  randomly chooses a world name from a list
  """
  with open("names.txt") as namefile:
    name_list=namefile.readlines()
  base_name=stellagama.random_choice(name_list)
  base_name=base_name.strip()
  char_list=[base_name]
  length_count=int(7-len(base_name)//2)
  if int(len(base_name)%2)==0:
    length_count+=1
  if length_count<=0:
    length_count=0
  for i in range (1,length_count):
    char_list.append(" ")
  name= " ".join(char_list)
  return name #output random name
  
# Testing area

print (name_gen())