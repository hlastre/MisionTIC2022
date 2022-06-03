pensum = [{'0123' : {'creditos': 2, 'nombre': 'intro a la ing'},
           '4567' : {'creditos': 1, 'nombre': 'inglés'}},
          {},
          {}]

mensaje = ' '
semestre = 1
materia = '0123'
nombre = 'lectoescritura'
creditos = 3


if semestre < 1 or semestre > 3:
  mensaje = 'Ingrese un semestre válido'
elif (semestre == 2 or semestre == 3):
  mensaje = 'El semestre no tiene materias'
elif (semestre == 1):
  if materia != '0123' and materia != '4567':
    mensaje = 'La materia no existe'
  else:
    mensaje = 'Modificada con éxito'
    pensum[0]['0123'] = {'creditos': creditos, 'nombre': nombre}

print(pensum)