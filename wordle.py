#función de chequeo

def chequeo (rx, gm):
    id = 0
    acertadas = 0
    for letra in gm:
        if letra == rx[id]:
            print(letra, "es correcta")
            acertadas += 1
        elif letra != rx[id]:
            for letras in rx:
                if letras == letra:
                    print(letra, "se encuentra en otro lugar")
        else:
            print(letra, "no se encuentra")
        id += 1
    if acertadas == 5:
        mensaje = "Ganaste en", intentos, "intentos!"
        return mensaje

            
intentos = 1
#contenedor de palabra, tal vez podría ser una lista de la que buscar palabras para variarlo
palabra = "comer"

#input
while intentos < 7:
    inputPalabra = input(str("Palabra de 5 letras: "))
    chequeo(palabra, inputPalabra)