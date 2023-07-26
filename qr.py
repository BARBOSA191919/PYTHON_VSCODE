import pyqrcode
from pyqrcode import QRCode

url = pyqrcode.create('https://www.youtube.com/watch?v=ZaCo_tnOMtw&ab_channel=SoyMiguelIdiomas') #codigo pa agregar las url
url.svg('miweb.svg', scale=8) #pa agegar la escala y ponerle la extension svg pa que abra en la web
print(url) # ejecute la url




