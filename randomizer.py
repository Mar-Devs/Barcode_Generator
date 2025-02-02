import random
import os
import pandas as pd
from openpyxl import load_workbook

sn_file = "generated_sn.txt"   #file to sotre generated serial numbers


if os.path.exists(sn_file):
    with open(sn_file, "r") as file:
        generated_sn = set(file.read().splitlines())  #load the generated serial numbers into a set, to prevent duplications
else:
    generated_sn = set()

def sn_generator():
    while True:  
        sn = ""  
        for _ in range(8): 
            number = random.randint(0, 9)  
            sn += str(number) 
                                        #generate an eight digit serial number, if it doesn't match with the set, added it
        if sn not in generated_sn:  
            generated_sn.add(sn)  
            return sn  

# Load Excel file
excel_file = "Barcode_Project.xlsx"
file = pd.read_excel(excel_file)
workbook = load_workbook(excel_file)
sheet = workbook.active

with open(sn_file, "w") as file:
    file.write("\n".join(generated_sn))
