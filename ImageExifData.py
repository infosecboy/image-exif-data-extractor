#!/usr/bin/python


from PIL import Image
from PIL.ExifTags import TAGS

def Exifdataextractor(ImageFileName):
	
	try:
		ImageFile  = Image.open(ImageFileName)
		info = ImageFile._getexif()
		if info:
			for (tag,value) in info.items():
				tags = TAGS.get(tag,tag)
				
				print(str(tags)  + ":" + str(value) )
		else:
			print("Sorry meta data was not found")
	except Exception,e:
		print(e)
			
				
input_file = raw_input("Enter image file: ")
Exifdataextractor(input_file)

			
	
