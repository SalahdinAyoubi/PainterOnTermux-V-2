import  os ,  time ,  sys ,  re

D_prog="""
{}                         ''~``
                        ( o o )
{}+------------------{}.oooO{}--{}(_){}--{}Oooo{}.--------------------+
{}             _____      _       _            
            |  __ \    (_)     | |           
            | |__) |_ _ _ _ __ | |_ ___ _ __ 
            |  ___/ _` | | '_ \| __/ _ \ '__|
{}  __^__ {}    | |  | (_| | | | | | ||  __/ |       {} __^__{}
 ( ___ ){}    |_|   \__,_|_|_| |_|\__\___|_|   {}    ( ___ )
  | / | {}          Painter on Termux   {}            | / |
  | / |  {}           Version 0.002    {}             | / |
  | / |                                           | / |
  |___|             .oooO                         |___|
 (_____)             (   )   Oooo.               (_____) 
{}+---------------------{}\ ({}----{}(   ){}----------------------+
 {}[Creat by:Python Dz] {} \_)    ) /  
                             (_/   
"""
# Colors
g ='\033[92m'
r ='\033[91m'
b ='\033[94m'
y ='\033[93m'
w = '\033[0m'
m = '\033[95m'
bl  = '\033[96m'

me = D_prog.format(y, r, y, r, y, r, y, r, g, y, g, y, w, g, w, bl, w, b, w, r, w, r, w, r, y, w)


###########################
# Path and write command
path ="/data/data/com.termux/files/usr/etc/"
link = 'sh -c "$(curl -fsSL https://github.com/Cabbagec/termux-ohmyzsh/raw/master/install.sh)" '
bash ="""
clear
#cmatrix -s
figlet -f big Name #| lolcat -s
echo " "
echo " "
PS1=' ~ $ '"""

zshrc =""". /data/data/com.termux/files/usr/etc/profile
command_not_found_handler() {
        /data/data/com.termux/files/usr/libexec/termux/command-not-found $1
}
#set nomatch so *.sh would not error if no file is available
setopt +o nomatch
. /data/data/com.termux/files/usr/etc/profile"""

##############


# function About
def about():
	os.system("clear")
	print(me)
	abou = bl+"   Creat by :  Python Dz  \n   Github   :  SalahdinAyoubi \n   Facebook :  sami.rabih.925\n   update   :  08-01-2020\n   Version  :  V 0.002\n\n"
	
	for i in abou:
	    time.sleep(0.1)
	    sys.stdout.write(i)
	    sys.stdout.flush()
	time.sleep(2.5)
	print(w)
	os.system("clear")	
	
	
#  function choice 
def choice():
	ch="""{}
  01{}  - Creat your Name on termux
  {}02 {} - change  Style in termux
  {}03 {} - Add Button on pantel 
  {}04{}  - About 
  {}05{}  - Exit
"""
	print(ch.format(y, g, y, g, y, g, y, g, y, g))
	choice = input("  - Enter your choice : "+w)
	if choice == "1" or choice == "01":
		creat_name()
	elif choice == "2" or choice == "02":
		creat_style()
		time.sleep(5) 	   
	elif choice =="3" or choice == "03":
		AddButton()
	elif  choice == "4" or choice == "04":
		about()
	elif choice == "5" or choice == "05":
		os.system("clear")
		print(me)
		print("\n"*3)
		print(g+"                Good bey   ^__^  "+w)
		print("\n"*2)
		exit()
		
	else:
		print(r+" !!  Plz Enter choice number !! "+w)
		time.sleep(2)
		

# function Creat Name 	
def creat_name():
	os.system("clear")
	print(me)	
	
	nam = input(" - Enter your Name : ")
	name = input(" - Confirm your Name : ")
	if nam == name:
		key = bash.replace("Name" ,  name)		
		print(y+"\n......    Loading ....…... "+w)
		os.system("pkg install figlet -y")
		os.system("clear")
		print(me)
		print(g+" - [√] Save Name Successfully!"+w)
		
		cm = input(" - Are you add cmatrix [y/n] ? : ")
		if cm == "Y" or cm == "y":
			os.system("clear")
			print(me)
			print(y+"....   Loading  ............ "+w)
			os.system("pkg install cmatrix -y")
			key = key.replace("#cmatrix -s" ,"cmatrix -s")
			os.system("clear")
			print(me)
			print(g+" - [√] Add Cmatrix Successfully! "+w)
			print("\n\n")
			
	
	
			
		lol = input(" -  Are you Add Colors  [n\y] : ")
		if lol =="Y"  or lol == "y":
			os.system("clear")
			print(me)
			print(y+"..........  Loading  ............... "+w)
			time.sleep(0.5)
			os.system("pkg install ruby -y")
			os.system("gem install lolcat")
			key = key.replace("#| lolcat -s" ,"| lolcat -s")
			os.system("clear")
			print(me)
			print(g+" [√] Add Cloros Successfully!\n"+w)
			
	elif nam != name:
		print(r+" -!!  The name does not match"+w)
		time.sleep(2.5)
		creat_name()
		
	else:
		pass

			
	f = open(path+"bash.bashrc" , "w")
	f.write(key)
	f.close()
	print(g+" [√] The operation ended successfully\n ")
	print(" [√]  Open a new session to see this"+w)
	try:
		os.system("touch "+path+"zshrc")
		Read()
		Write()
		Append(data)
	except:
		os.system("rm "+path+"zshrc")

	time.sleep(4)

      
def Read():
	global data
	global D_zshrc
	r = open(path+"zshrc", "r")
	D_zshrc  = r.read()
	r.close()
	
	f = open(path+"bash.bashrc" ,"r")
	data = f.read()
	f.close() 
	
def Append(a):
	f =  open(path+"zshrc" ,"a")
	f.write(a)
	f.close()

def Write():
	f =  open(path+"zshrc", "w")
	f.write(zshrc)
	f.close()
	
	
# functoin Creat Style 
def creat_style():
	os.system("clear")
	print(me)
	print(y+" .. …... Loading .......... "+w)
	try:
		os.system("~/.termux/colors.sh")
		os.system("~/.termux/fonts.sh")
		Read()
		result = re.search(data , D_zshrc)
		if result:
			os.system("pkg install curl -y")
			os.system(link)
		else:
			Write()
			Append(data)

				
	except:
		os.system("pkg install curl -y")
		os.system(link)
		Read()
		result = re.search(data , D_zshrc)
		if result:
			pass
		else:
			Write()
			Append(data)
		
	os.system("clear") 
	print(me)
	print(g+" [√] Add Style  Successfully!\n"+w)
	print(g+" [√] The operation ended successfully\n ")
	print(" [√]  Open a new session to see this"+w)
	time.sleep(4)
	
		
def AddButton():
	os.system('clear')
	print(me)
	print(y+'[+] Proses..')
	time.sleep(1)
	print(y+'\n[+] making termux properties directory..')
	time.sleep(1)
	try:
    	 os.mkdir('/data/data/com.termux/files/home/.termux')
	except:
    	 pass
	print(g+'[√] Successfully !')
	time.sleep(1)
	print(y+'\n[+] Making setup file..')
	time.sleep(1)

	key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"

	kontol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
	kontol.write(key)
	kontol.close() 

	time.sleep(1)
	print(g+'[√] Successfully!')
	time.sleep(1)
	print(y+'\n[+] Setting up..')
	time.sleep(1)
	os.system('termux-reload-settings')
	print(g+'[√] Successfully !!') 		
			
	       

 


while True:
	os.system("clear")
	print(me)
	choice()
	os.system("clear")

 
