name = input("Ingresa tu nombre: ")

title = """ Bienvenido a 
.-..-.   .-.   .-. .-..-.  .-. .-..--. .-..-..-. .-..--. .-..-.   .-..-.   .-..-..-. 
| | ~.-. | |   | | | | ~.-.| | | | ~~   ~ | | ~  | | ~~  | | ~.-. | | ~.-. | | ~ | | 
| |.-.~  | |   | | | |   ~ | | | | _      | |    | | _   | |.-.~  | |.-.~  | |.-.| | 
| | ~.-. | |   | | | |     | | | |`-'     | |    | |`-'  | | ~.-. | | ~.-. | | ~ | | 
| |  | | | | _ | | | |     | | | | __     | |    | | __  | |  | | | |  | | | |   | | 
`-'  `-' `-'`-'`-' `-'     `-' `-'`--'    `-'    `-'`--' `-'  `-' `-'  `-' `-'   `-' 
"""

def bienvenida(hero):
    return(f"Bienvenido {hero} a una nueva aventura en el mundo de Arcane")

print(title)

print(bienvenida(name))

want_to_play = input("Quieres jugar? Si/No ").lower()



if want_to_play == "si":
    print("Te sientas alrededor de una mesa de madera astillada, rodeado por el sonido de carcajadas ruidosas y tragos generosos del mejor ron de Bilgewater. En una esquina, una mujer con un llamativo abrigo morado pone los pies sobre la mesa.") 
    print("Y ahí estábamos,") 
    print("dice ella, con los ojos solemnes, " )
    print("yo y mi tripulación, escarbando en ese maldito naufragio. Cuando de repente—¡zas!") 
    print("Mueve su brazo, casi tirando una jarra de cerveza. ")
    print("Algo oscuro vino desde el horizonte. ¡Nunca sentí algo tan aterrador y frío en mi vida, te lo juro! El barco está embrujado, te digo. Nunca debimos sacar ese naufragio de las mareas.")
    print("Una figura rechoncha con ropas oscuras interviene desde unas mesas más allá. ")
    print("¡Vamos Tala, ya sabemos que no debemos creer en tus cuentos exagerados!")
    print("Un grito repentino se eleva por encima de la multitud.")
    print("Te mostrare lo que pasa si no crees en los cuentos de la bucanera")
    print("Los nudillos crujen contra el hueso, y el mismo hombre rechoncho con ropas oscuras sale volando cuando la mujer de morado le estrella el puño en la cara. Uno de los compañeros de bebida del hombre lo ayuda a levantarse del suelo, mientras otro se lanza hacia la mujer. Alguien en la taberna levanta una jarra en señal de aprobación, y una multitud bulliciosa comienza a animar la pelea. ¿Qué haces?")
    decision = input("Que haces al escuchar. Apoyas a Tala, a Diana o no haces nada? Tala / Diana / Nada").lower

    if decision == "tala":
        
    elif decision == "diana":

    else:
        print("Vuelve a iniciar")
else:
    print("Vuelve mas tarde")


