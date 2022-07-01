#función de chequeo

def chequeo (og, word):
    id = 0
    if word == og:
        victoria = 1
        return victoria
    else:
        for letra in word:
            if letra == og[id]:
                print(letra, "es correcta")
            elif letra != og[id] and letra in og:
                for letras in og:
                    if letras == letra:
                        print(letra, "se encuentra en otro lugar")
            else:
                print(letra, "no se encuentra")
            id += 1
            
intentos = 0
#contenedor de palabra, tal vez podría ser una lista de la que buscar palabras para variarlo
palabra = "copia"
victoria = 0

#input
while intentos < 7 and victoria != 1:
    inputPalabra = input(str("Palabra de 5 letras: "))
    intentos += 1
    victoria = chequeo(palabra, inputPalabra)

if intentos == 7:
    print("Perdiste :(")
else:
    print("Ganaste en", intentos, "intentos!")