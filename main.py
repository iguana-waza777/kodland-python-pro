meme_dict = {
            "CRINGE" : "Algo excepcionalmente raro o embarazoso",
            "LOL" : "Una respuesta común a algo gracioso",
            "BAIT" : "Ase referencia a un acto el cual es mentira o un engaño",
            "HATE" : "Odio asi algo o alguien no nescesariamente especificamente",
            "CREEPY" : "Algo tenebroso o que da miedo",
            "WAZA" : "SIgno para mostrar alegria en cierto momento"
            }
word = input("Escribe una palabra que no entiendas (¡con mayusculas):")
if word in meme_dict.keys():
    print("El significado de", {word}, "es:", {meme_dict[word]})
else:
    print("Lo siento, no conozco esa palabra. ¡Inténtalo con otra!")
