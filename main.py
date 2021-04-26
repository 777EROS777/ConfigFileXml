import os
import xml.etree.ElementTree as ET

#XML_path - путь к файлу
def getConfigXML(XML_path):
	try:
		tree = ET.parse(XML_path)
		config = tree.getroot()
		files = config.find('file')
		file = files[0].attrib
		name = file.get('source_path') 
		name1 = file.get('destination_path')
		name2 = file.get('file_name')
		return name, name1, name2

	except IOError as e:
		print(e) 	
		
path_to_config = "D:/путь к файлу"
data_config = "config"

path_to_XML = path_to_config + data_config + 'XML_path'
files_list = os.listdir(path_to_XML)

all_file_conf = []
for file in files_list:
	all_file_conf.append(getConfigXML(path_to_XML + file))

	
