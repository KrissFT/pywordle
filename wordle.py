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
maximo = 6
#contenedor de palabra, tal vez podría ser una lista de la que buscar palabras para variarlo
palabra = "copia"
victoria = 0

#input
while intentos <= maximo and victoria != 1:

    mensajeInput = "(%d/%d) Palabra de %d letras: "%(intentos+1, maximo, len(palabra))

    inputPalabra = input(str(mensajeInput))

    if len(inputPalabra) != len(palabra):
        print("Debe tener %d letras"%len(palabra))
    else:
        inputPalabra = inputPalabra.lower()
        intentos += 1
        victoria = chequeo(palabra, inputPalabra)

if intentos > maximo:
    print("Perdiste :(")
elif intentos == 1:
    print("Ganaste en %d intento!"%intentos)
else:
    print("Ganaste en %d intentos!"%intentos)