import os
file= open(r"C:\Users\KIIT\Documents\Rainmeter\Skins\NewFolder\test.txt", "r+")
lines=file.readlines()
print("Present quote: "+lines[19][6:])
quote = raw_input("New quote : ")
lines[19]="Text = "+quote
print(lines[19])
file.truncate(0)
for line in lines:
    file.write(line)
file.close()
nf=open(r"C:\Users\KIIT\Documents\Rainmeter\Skins\NewFolder\selfQuote.ini", "r+")
nf.truncate(0)
for line in lines:
    nf.write(line)
nf.close()
os.system('cmd /c"rainmeter"')