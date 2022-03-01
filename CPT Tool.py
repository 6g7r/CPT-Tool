import time,random,urllib.request,json
import time as mm
import sys as n
def slow(m):
  for sl in m + "\n":
    n.stdout.write(sl)
    n.stdout.flush()
    mm.sleep(1. / 500)
slow("""
𝑖𝑛𝑠𝑡𝑎 : @6𝑔7𝑟_ℎ𝑒𝑟𝑒

______¶¶
______¶¶______________¶¶¶¶¶
______¶¶¶____________¶¶¶¶¶¶¶
______¶¶¶____________¶¶¶¶¶¶¶¶
_____¶¶¶¶___________¶¶¶¶¶¶¶¶¶
___¶¶¶¶¶¶¶__________¶¶¶¶¶¶¶¶¶¶
___¶¶¶¶_____________¶¶¶¶¶¶¶¶¶¶
____¶¶_______________¶¶¶¶¶¶¶¶¶¶
____¶¶_____________¶¶¶¶¶¶¶¶¶¶¶
_____¶¶_______________¶¶¶¶¶¶¶
_____¶¶__________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
_____¶¶¶_______¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
_____¶¶¶___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
______¶¶¶¶¶¶¶¶¶¶¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
______¶¶¶¶¶¶¶¶____¶¶¶¶¶¶¶¶¶¶¶¶¶___¶¶¶¶
__________________¶¶¶¶¶¶¶¶¶¶¶¶¶____¶¶¶¶
___________________¶¶¶¶¶¶¶¶¶¶¶______¶¶¶¶
____________________¶¶¶¶¶¶¶¶¶¶_______¶¶¶
___________________¶¶¶¶¶¶¶¶¶¶_________¶¶¶
__________________¶¶¶¶¶¶¶¶¶¶¶_________¶¶¶
_________________¶¶¶¶¶¶¶¶¶¶¶¶__________¶¶
________________¶¶¶¶¶¶¶¶¶¶¶¶¶__________¶¶
_______________¶¶¶¶¶¶¶¶¶¶¶¶¶¶___________¶¶
______________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___________¶¶
_____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___________¶¶¶
____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶___________¶_¶¶
____________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_____________¶¶
___________¶¶¶¶¶¶¶¶____¶¶¶¶¶¶¶¶
___________¶¶¶¶¶¶¶______¶¶¶¶¶¶¶¶
__________¶¶¶¶¶¶¶________¶¶¶¶¶¶¶
__________¶¶¶¶¶¶__________¶¶¶¶¶¶¶
_________¶¶¶¶¶¶____________¶¶¶¶¶¶
_________¶¶¶¶¶______________¶¶¶¶¶¶
________¶¶¶¶¶________________¶¶¶¶¶¶
_______¶¶¶¶¶__________________¶¶¶¶¶¶
______¶¶¶¶¶_____________________¶¶¶¶¶¶
_____¶¶¶¶¶_______________________¶¶¶¶¶¶
_____¶¶¶¶¶________________________¶¶¶¶¶¶
____¶¶¶¶¶__________________________¶¶¶¶¶¶
____¶¶¶¶____________________________¶¶¶¶¶¶
___¶¶¶¶_______________________________¶¶¶¶
___¶¶¶_________________________________¶¶¶¶
___¶¶¶__________________________________¶¶¶
__¶¶¶____________________________________¶¶¶
_¶¶¶_____________________________________¶¶¶
¶¶¶¶______________________________________¶¶¶
__________________________________________¶¶¶


""")
def slow(m):
  for sl in m + "\n":
    n.stdout.write(sl)
    n.stdout.flush()
    mm.sleep(1. / 50)

slow("""
-----------------Welcome to the CPT tool !-------
1 - Create passwords from the victim's information
2 - Converting names into e-mails
3 - Extracting the victim site from the IP
-------------------------------------------------
""")
mode = input("1,2,3,: ")
if("1")in mode:
  a = input("name : ")
  b = input("nickname : ")
  c = input("age : ")
  d = input("birthday : ")
  e = ["1","2","3","4","5","6","7","8","9","0"]
  f = ["1","2","3","4","5","6","7","8","9","0"]
  g = ["1","2","3","4","5","6","7","8","9","0"]
  h = ["1","2","3","4","5","6","7","8","9","0"]
  pa = input("How many passwords do you want to create : ")
  p = random.choice(e)
  o = random.choice(f)
  l = random.choice(g)
  k = random.choice(h)
  j = [a,b,c,d,p,o,l,k]
  time.sleep(0.1)
  for i in range(int(pa)):
    w = random.choice(j)
    q = random.choice(j)
    time.sleep(0.1)
    pw = f"{w}{q}"
    print(f"{pw}")#insta : @6g7r_here
    with open("password.txt", "a") as mix:
      mix.write(f"{pw}\n")
      mix.close()
      
if("2")in mode:
  f = input("[<X>]  file name : ")
  d = input("Domain : ")
  file  = open(f).read().splitlines()
  for file in file:
    time.sleep(0.1)
    file += d
    print(file)
    with open("email.txt", "a") as mix:
      mix.write(f"{file}\n")
      mix.close()
if("3")in mode:
 print("\t       [•]IP Information[•] ")
 while True:
	 ipcheck = 0
	 print("-" * 40)
	 iip = input("Enter ip address: ")
	 try:
		 url = "https://ipinfo.io/" + iip
		 req = urllib.request.Request(url)
		 with urllib.request.urlopen(req) as response:
			 data = response.read()
			 data = json.loads(data)
	 except:
		 print("Not a valid ip")
		 ipcheck = 1

	 if ipcheck == 0:
		 try:
			 print("-" * 40)
			 print("Ip address:" , data['ip'])
		 except:
			 print("Ip address: N/A")
		 try:
			 print("City:" , data['city'])
		 except:
			 print("City: N/A")
		 try:
			 print("State:" , data['region'])
		 except:
			 print("State: N/A")
		 try:
			 print("Country:" , data['country'])
		 except:
			 print("Country: N/A")
		 try:
			 print("Location:" , data['loc'])
		 except:
			 print("Location: N/A")
		 try:
			 print("timezone:" , data['timezone'])
		 except:
			 print("timezone: N/A")
		 try:
			 print("phone:" , data['phone'])
		 except:
			 print("phone: N/A")
		 try:
			 print("Zip:" , data['postal'])
		 except:
			 print("Zip: N/A")
		 try:
			 print("ISP:" , data['org'])
		 except:
			 print("ISP: N/A")
		 try:
			 print("network:" , data['network:'])
		 except:
			 print("network: N/A")
		 print("-" * 40)
