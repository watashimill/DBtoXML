import mysql.connector as mariadb
import xml
from xml.dom.minidom import Document

mariadb_connection = mariadb.connect(user='root', password='s%W!B#AN', database='restaurant')
print ("connect")
cursor = mariadb_connection.cursor(dictionary=True)
some_name = 5
cursor.execute("SELECT Food_ID,FoodName,Price FROM  food")


####

# Write XML File (minidom)
#doc = Document()
 
root = doc.createElement("Restaurant")
root.setAttribute( "name", "SelectedCafe" )
doc.appendChild(root)

for value in cursor:
	print(("ID: {}, FoodName: {}, Price: {}").format(value['Food_ID'],value['FoodName'],value['Price']))
	# Create Element
	food = doc.createElement('Food')
	root.appendChild(food)

	# Create Element
	tempChild = doc.createElement('Name')
	food.appendChild(tempChild)
	# Write Text
	nodeText = doc.createTextNode( value['FoodName'].strip() )
	tempChild.appendChild(nodeText)
	# Create Element
	tempChild = doc.createElement('Price')
	food.appendChild(tempChild)
	# Write Text
	nodeText = doc.createTextNode( value['Price'].strip() )
	tempChild.appendChild(nodeText)


'''
for value in XMLvalues:
	# Create Element
	tempChild = doc.createElement(value)
	root.appendChild(tempChild)
 
	# Write Text
	nodeText = doc.createTextNode( XMLvalues[value].strip() )
	tempChild.appendChild(nodeText)
'''
doc.writexml( open('data.xml', 'w'),
              indent="	",
              addindent="	",
              newl='\n')
 
doc.unlink()