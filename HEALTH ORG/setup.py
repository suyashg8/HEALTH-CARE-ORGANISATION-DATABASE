#!C:\Python34\python.exe
import cgi
import htmlhelpers
import dbhelpers

# Connect to database
conn = dbhelpers.connecttodb()
cur = conn.cursor()

# Create database tables - or do nothing if tables already exist
dbhelpers.createtables(cur)

htmlhelpers.printheader('Main Menu')
print('Welcome to the Health care ORG. <a href="mainmenu.py">Run Main Menu</div>')
htmlhelpers.printfooter()

# close database
conn.close()

