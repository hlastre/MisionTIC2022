def es_semestre_valido(p, s):
    # ESTA VEZ TU DEFINES TUS RETORNOS
    return len(p) >= s and s > 0

def es_semestre_vacio(p, s):
    # ESTA VEZ TU DEFINES TUS RETORNOS
    return len(p[s-1]) == 0

def es_materia_valida(p, s, m):
    # ESTA VEZ TU DEFINES TUS RETORNOS
    return m in list(p[s-1].keys())

def modificar_materia(pensum, semestre, materia, nombre, creditos):
    # ACÁ INICIA LA FUNCIÓN

    pensum[semestre-1][materia]['nombre'] = nombre
    pensum[semestre-1][materia]['creditos'] = creditos