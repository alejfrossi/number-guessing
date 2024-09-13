import random

# FUNCIONES

def number_guessing () :

    try :

        guessed_number = 0

        complexity = 0

        while not 0 < complexity < 4 :
            
            complexity = int( input( "\nElige una dificultad:\n1 - FÁCIL (Número entre 1 y 25)\n2 - INTERMEDIO (Número entre 1 y 100)\n3 - DÍFICIL (Número entre 1 y 1000)\n") )

            if not 0 < complexity < 4 :

                print( "ERROR. Ingresa uno de los números solicitados.\n\n")

        number_to_guess = generate_number( complexity )

        while not ( number_to_guess == guessed_number ) :

            guessed_number = int( input( "Ingresa un número:\n" ) )

            if ( guessed_number < number_to_guess ) :

                print( "El número a adivinar es MAYOR al ingresado.\n" )

            else :

                print( "El número a adivinar es MENOR al ingresado.\n" )

        print( "\nTin!Tin!Tin!\nFelicitaciones! Has adivinado! El número CORRECTO era" , number_to_guess )

    except ValueError :

        print( "ERROR. Ingrese un carácter válido." )

        number_guessing()

def generate_number ( complexity ) :

    if complexity == 1 : # EASY

        print( "Adivina el número. RECUERDA, debe ser entre 1-25")

        return random.randint(1,25)
    
    elif complexity == 2 :  # MEDIUM

        print( "Adivina el número. RECUERDA, debe ser entre 1-100")

        return random.randint(1,100)
    
    else : # HARD
        
        print( "Adivina el número. RECUERDA, debe ser entre 1-1000")

        return random.randint(1,1000)
    
# PROGRAMA


print( "Bienvenidx a NUMBER GUESSING!" )

number_guessing()




