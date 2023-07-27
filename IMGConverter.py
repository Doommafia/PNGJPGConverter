import os
from PIL import Image
from tkinter import Tk
from tkinter import filedialog

def convJP(jpgFile, outFolder):
    image = Image.open(jpgFile)
    outFile = os.path.join(outFolder, os.path.splitext(os.path.basename(jpgFile))[0] + '.png')
    image.save(outFile)
    print(f'Converted {jpgFile} to {outFile}')

def convPJ(pngFile, outFolder):
    image = Image.open(pngFile)
    rgb_image = image.convert('RGB')
    outFile = os.path.join(outFolder, os.path.splitext(os.path.basename(pngFile))[0] + '.jpg')
    rgb_image.save(outFile)
    print(f'Converted {pngFile} to {outFile}')

def convChoose():
    Tk().withdraw()
    filePath = filedialog.askopenfilename()
    outFolder = filedialog.askdirectory()

    if filePath:
        _, extension = os.path.splitext(filePath)
        if extension.lower() == '.jpg':
            convJP(filePath, outFolder)
        elif extension.lower() == '.png':
            convPJ(filePath, outFolder)
        else:
            print("Invalid file type.")
    else:
        print("No file selected.")

convChoose()
