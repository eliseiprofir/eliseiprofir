import sys
import os

from PIL import Image

if len(sys.argv) != 2:
    print("Usage: python jpg-to-png.py [folder_name]\\")
    sys.exit()

source = sys.argv[1]

if not os.path.exists(f'{source[:-1]}_converted'):
    os.mkdir(f'{source[:-1]}_converted')

for file in os.listdir(source):
    img = Image.open(f'{source}{file}')
    clean = os.path.splitext(file)
    output = f'{source[:-1]}_converted'
    img.save(f'{output}\{clean[0]}.png', 'png')

print('All done!')
