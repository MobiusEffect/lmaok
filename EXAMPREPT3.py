import os
import sys
import random
import time
import pip._vendor.colorama
from pip._vendor.colorama import Fore, Back, Style

#While Loop
count = 0
while (count < 5):
  number = input(Fore.GREEN + "Enter Number \n" + Fore.BLUE + " : ")
  print (Fore.RED + number):
  time.sleep(3)
  count = count + 1

#For loop
fruits= ["Apple","Orange"]
for i in fruits:
  print(i)

#If and Else
v1 = 11
if v1 == "11":
  print("Test")
else:
  print("TestBadRIPlol")

#elif
cccc = input("Imput a number between 0-10")
cccc_int = int(cccc)
if cccc_int == 5:
  print('Whoo')
elif cccc_int == 6:
  print("Bahahahhaha")
elif cccc_int == 4:
  print("RIPdesuka")
else:
  print("kek")
  