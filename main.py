def escribe(mifichero, datos):
    f = open(mifichero, 'w')

    for frases in datos:
        if not frases.endswith('\n'):
            frases = frases + '\n'

        f.write(frases)

    f.close()

frases = [
    'hola',
    'aprendiendo python'
]
def segunda_escritura(mifichero, colors):
    f = open(mifichero, 'a')

    for colores in colors:
        if not colores.endswith('\n'):
            colores = colores + '\n'

        f.write(colores)
    f.close()

colores = [
    'rojo',
    'azul',
    'amarillo',
    'verde'
]

escribe('mifichero.txt', frases)
segunda_escritura('mifichero.txt', colores)
