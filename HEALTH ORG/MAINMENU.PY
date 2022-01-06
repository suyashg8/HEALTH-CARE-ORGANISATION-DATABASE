#!C:\Python34\python.exe
import cgi
import htmlhelpers
import dbhelpers

# Connect to database
conn = dbhelpers.connecttodb()
cur = conn.cursor()

#
# Get input from form if any. If none, print main menu.
# variable screen tells the program what section to process.
# Other variables (if any) are retrived in the section functionality
#
formdata = cgi.FieldStorage()

#
# Create a "pseudo switch" for the various values formdata can contain
#
# Do an orderly exit
#
if (formdata.getfirst('screen', '') == 'Exit'):
    htmlhelpers.printheader('Main Menu')
    print('Goodbye!')
    htmlhelpers.printfooter()
    # close database
    conn.close()

#
elif (formdata.getfirst('screen', '') == 'Inventory'):
    htmlhelpers.printheader('Inventory Menu')
    htmlhelpers.inventory()
    htmlhelpers.printfooter()
elif (formdata.getfirst('screen', '') == 'AddInventory'):
    htmlhelpers.printheader('Add Inventory')
    htmlhelpers.addinventory(cur, formdata, formdata.getfirst('subcommand', ''))
    htmlhelpers.printfooter()
elif (formdata.getfirst('screen', '') == 'EditInventory'):
    htmlhelpers.printheader('Edit Inventory')
    htmlhelpers.editinventory(cur, formdata, formdata.getfirst('subcommand', ''))
    htmlhelpers.printfooter()
elif (formdata.getfirst('screen', '') == 'DeleteInventory'):
    htmlhelpers.printheader('Delete Inventory')
    htmlhelpers.deleteinventory(cur, formdata, formdata.getfirst('subcommand', ''))
    htmlhelpers.printfooter()
