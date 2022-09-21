def palindromo(palabra):
    palabra.lower()
    primerMitad = palabra[:len(palabra)//2]
    if type(len(palabra)//2) != float:
        segundaMitad = palabra[len(palabra)//2:]
        if primerMitad == segundaMitad[::-1]:
            return True
    segundaMitad = palabra[len(palabra)//2 + 1:]
    if primerMitad == segundaMitad[::-1]:
        return True
    return False