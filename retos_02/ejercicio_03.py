frase = input().lower()
answer_cantidad_palabras = len(frase.split())
answer_cantidad_vocales = (
    frase.count("a")
    + frase.count("e")
    + frase.count("i")
    + frase.count("o")
    + frase.count("u")
)
frase = frase.replace(" ", "")
answer_palidromo = frase == frase[::-1]
print("Cantidad de palabras:", answer_cantidad_palabras)
print("Cantidad de vocales:", answer_cantidad_vocales)
print("Es palíndromo:", answer_palidromo)
