from PIL import Image,ImageFilter,ImageFont,ImageDraw
import os

alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

fuentes = os.listdir("fuentes")
contador = 0
for fuente in fuentes:
    contador += 1
    anchura, altura = 512, 512
    fondo = (127, 127, 127)
    for letra in alfabeto:
        font = ImageFont.truetype("fuentes/"+fuente, 400)
        imagen = Image.new("RGB", (anchura, altura), fondo)
        draw = ImageDraw.Draw(imagen)
        draw.text((10,10), letra, fill=(0,0,0), font=font)
        imagen.save("entrenamiento/"+str(contador)+"-"+letra+".png")


 
    
