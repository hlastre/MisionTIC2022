print("¡Bienvenido! En esta aplicación los estudiantes podrán gestionar las notas de su materia.")
    
    nombre = input("Por favor ingresa tu nombre: ").capitalize()
    materia = input("Ingresa el nombre de la materia: ").capitalize()
    
    suma_porcentaje = 0
    nota_acumulada = 0
    aprobacion = ""
    
    while True:
        nota_obtenida = float(input("Ingresa la nota obtenida: "))
        
        porcentaje_nota = float(input("Ingresa el porcentaje de la nota: "))
        if porcentaje_nota > 100:
            print("El porcentaje evaluado de una materia no puede ser mayor a 100")
            
        cal_nota = nota_obtenida * (porcentaje_nota/100)
        nota_acumulada = nota_acumulada + cal_nota
        nota_acumulada = round(nota_acumulada, 2)
        
        suma_porcentaje = suma_porcentaje + porcentaje_nota
        
        if suma_porcentaje < 100:
            respuesta = input("¿Falta añadir notas? S/N ")
            
        if suma_porcentaje > 100:
            print("El porcentaje evaluado de una materia no puede ser mayor a 100")
            suma_porcentaje = suma_porcentaje - porcentaje_nota
            nota_acumulada = nota_acumulada - cal_nota