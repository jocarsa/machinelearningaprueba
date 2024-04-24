from PIL import Image,ImageFilter
import math

def decimal_to_binary_with_zeros(decimal_num, num_zeros):
    binary_str = bin(decimal_num)[2:]  # Convert to binary string, removing the '0b' prefix
    binary_with_zeros = binary_str.zfill(num_zeros)  # Add leading zeros
    return binary_with_zeros

anchurabloque = 2
longitud = pow(2,pow(anchurabloque,2))
ancho = math.sqrt(longitud)
anchopixeles = int(1+(anchurabloque+1)*ancho)
print(f"La imagen tendra {anchopixeles} pixeles")
anchura, altura = anchopixeles, anchopixeles
fondo = (127, 127, 127) 
imagen = Image.new("RGB", (anchura, altura), fondo)

pixeles = imagen.load()
contador = 0
for x in range(0,int(ancho)):
    for y in range(0,int(ancho)):
        binario = str(decimal_to_binary_with_zeros(contador, pow(anchurabloque,2)))
        pos = 0
        posy = 0
        for i in range (0,len(binario)):
            if i%anchurabloque == 0:
                posy += 1
                pos = 0
            if binario[i] == "0":
                pixeles[x*(anchurabloque+1)+pos+1,y*(anchurabloque+1)+posy] = (0,0,0)
            else:
                pixeles[x*(anchurabloque+1)+pos+1,y*(anchurabloque+1)+posy] = (255,255,255)
            pos += 1
        contador += 1

imagen.save("bloque.png")


 
    
