import re #Python has a regular expressions library, a good need to import it to tell the difference between hours and minutes (2h 3m)
import os #pausing the console to preview the values.

with open('timevalues.txt', 'r') as file:
    contents = file.read()

totalmin = 0

patt = re.compile(r'(\d+h)? ?(\d+m)?')
found_matches = patt.findall(contents) #We compile our regular expression template to 'patt' and then find all matches that follow with 'patt'

for matches in found_matches:
    hours, minutes = matches
    hours = int(hours[:-1]) if hours else 0
    minutes = int(minutes[:-1]) if minutes else 0
    totalmin += hours * 60 + minutes

totalh = totalmin // 60 #Thank you google
totalmin %= 60

print(f'The summary of time values are: {totalh}h {totalmin}m')
os.system("PAUSE")