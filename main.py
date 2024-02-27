from barcode.writer import ImageWriter
from barcode import EAN13


barcode_number = ""  # Enter the desired number for the barcode here.
barcode = EAN13(barcode_number, ImageWriter())
barcode.save("")  # Enter the name of the barcode image here.