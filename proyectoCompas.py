# crear un proyecto con compañeros el proyecto se compone de 3 partes
# cada uno agrega una parte al proyecto hasta completarlo 
# en esta oportunidad usaremos def y match 
# pueden ser proyectos y/o trabajos anteriormente vistos
# ejemplo calculadora, calcular promedio, verificar edad si es mayor o menor, etc.
# Importante (Dejer e incluir notas para que nosotros las veamos)

# Primera parte realizada por Ernesto
def calcuPromedio():
    nota1 = float(input("Ingrese la primera nota: "))
    nota2 = float(input("Ingrese la segunda nota: "))
    nota3 = float(input("Ingrese la tercera nota: "))
    promedio = (nota1+nota2+nota3/3)
    
    print(f"Su promedio final es {promedio}")
    

def calcuBasica():
    num1 = int(input("numero 1 ")) 
    num2 = int(input("numero 2 ")) 

    operacion = input("introduce una operacion (+ - * /)")

    match operacion:
        case "+":
            res = num1+num2
        case "-":
            res = num1-num2
        case "*":
            res = num1*num2
        case "/":
            res = num1/num2

    print(f"resultado de {num1} {operacion} {num2} = {res}")
   

# def 3 (Aqui debe ir un tercer def)

# Parte realizada por Ernesto
def opcion():
    while True:
        op = int(input("""
                       Bienvenido al programa de verificaciones
                       1.-Calcular promedio.
                       2.-
                       3.-
                       4.-Salir.
                       """))
        match op:
            case 1:
                print("""
                      Seleccionaste el Calcular promedio.
                      Ingresa tres notas para saber tu promedio.
                      """)
                calcuPromedio()
                
            case 2: 
                print("calculadora basica ")
                calcuBasica()
                
            
            # case 3: (Completar)
            
            case _:
                print("Saliendo...")
                break
opcion()

