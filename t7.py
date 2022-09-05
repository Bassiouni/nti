import re

name = input("name: ")

if (re.findall(r"[^\S\n\t]+", name)): 
  raise Exception("No spaces!")

if re.findall(r"\d+", name):
  raise Exception("No Numbers!")

email = input("email: ")

