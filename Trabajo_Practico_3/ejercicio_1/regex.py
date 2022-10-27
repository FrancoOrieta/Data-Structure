import re

patron = "^\(0345\)\s15\d{7}$|^\+549345\d{7}$|^345\d{7}$"

print("Patron valido - (0345) 154123456:",re.findall(patron, "(0345) 154123456"))
print("Patron valido - +5493454123456:",re.findall(patron, "+5493454123456"))
print("Patron valido - 3454123456:",re.findall(patron, "3454123456"))
print("Patron invalido - +54011123456:",re.findall(patron, "+54011123456"))
print("Patron invalido - 34564123456:",re.findall(patron, "34564123456"))