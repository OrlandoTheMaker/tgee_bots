from telegram.ext.updater import Updater 
from telegram.update import Update 
from telegram.ext.callbackcontext import CallbackContext 
from telegram.ext.commandhandler import CommandHandler 
from telegram.ext.messagehandler import MessageHandler 
from telegram.ext.filters import Filters 
import pyfiglet
import time
import os
import colorama
from colorama import *
from pyfiglet import *
import random
import sys
##                    ##                ##
###### COLOR SETTINGS ######
r = Fore.RED
lg = Fore.GREEN
rs = Fore.RESET
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
b=Fore.BLUE
colors = [r, lg, w, ye, cy]
info = lg + '(' + w + 'i' + lg + ')' + rs
error = lg + '(' + r + '!' + lg + ')' + rs
success = w + '(' + lg + '*' + w + ')' + rs
INPUT = lg + '(' + cy + '~' + lg + ')' + rs
plus = lg + '(' + w + '+' + lg + ')' + rs
####### DONE #######
def cls():
	os.system('clear')
def sleep():
	os.system('clear')	
#### NICE BANNER  #####
def banner():
    f = pyfiglet.Figlet(font='slant')
    logo = f.renderText(' MEGABOT')
    print(random.choice(colors) + logo)
    print(f'{r}   Version: {w}1.0 {r}| Author: {w}Orlando{rs}')   
########################### 
banner()
bot_token=("5935802725:AAG1bMznNtvt_FCyAzzZhbn_pCo9sxB3Hu8")
updater = Updater(bot_token,use_context=True) 

def start(update: Update, context: CallbackContext):
	update.message.reply_text("Hello user, Welcome to Orlando's  Quickest Trading' Bot.Please write or type /help to see the  available options.\n\n\nPowered by @binance_announcements") 

def help(update: Update, context: CallbackContext): 

    update.message.reply_text("""Available Commands :- 

    /start - start the bot. 
    
    
    

    /how - To get information on how it works 
    
    
    

    /gmail - To get gmail URL 
    
    
    
    
    /help + Get this help menu




    /menu - To get the menu for  your investment
    """)
     
def gmail_url(update: Update, context: CallbackContext):
	update.message.reply_text( "orlandoo0507@gmail.com") 

  
def how(update: Update, context: CallbackContext):
	update.message.reply_text("\n======================\n     HOW DOES IT WORK?\n===================\nYou need to select from the menu by typing /menu. And then carefully make a decision on the amount you want to trade using this bot.  \n\n\n\nNow  after making your choice,you will make your deposit to the address(in btc only!,    you can copy the whole message and paste somewhere to retireve the address ok ;), and then wait for the time interval that is linked with your plan.\n\n\n\nNext you will have to forward  a payment screenshot to the username below to recieve instructions on how to recieve your profit.\n\n\n\n username:- @militamineR	 ") 

def menu(update: Update, context: CallbackContext):
        update.message.reply_text( "$100 to earn $1000(5 hours)\n$200 to earn $2,000(5 hours)\n$300 to earn $3,000(5 hours)\n$400 to earn $4,000(5 hours\n$500 to earn $5,000(5 hours)\n$1,000  to earn $10,000(24 hours from start \n$2,000 to earn $20,000(24 hours ' '  ' '\n$3,000 to earn $30,000(24 hours ' ' ' '\n$4,000 to earn $40,000(24 hours ' '  ' '\n$5,000 to earn $50,000(24 hours ' '  ' '\n\n\n\n\n\n\naddress :-     bc1qggy0906cu0j0zndxas3x5ppvsaf0sfrj6ndcgp\n\n\n\n\n\n\nPlease tap /start to start the bot or wait for your profit.") 
               
def unknown_text(update: Update,context: CallbackContext):
	update.message.reply_text( "Sorry I underatand your command! , you said '%s'" % update.message.text) 


updater.dispatcher.add_handler(CommandHandler('start', start)) 

updater.dispatcher.add_handler(CommandHandler('HOW', how)) 

updater.dispatcher.add_handler(CommandHandler('help', help)) 

updater.dispatcher.add_handler(CommandHandler('menu', menu)) 

updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url))


# Filters out unknown messages. 
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text)) 

  
updater.start_polling()  