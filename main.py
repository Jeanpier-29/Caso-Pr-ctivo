def registrar_solicitud(codigo, nombre, tipo, descripcion):
    solicitud = {
        "codigo": codigo,
        "nombre": nombre,
        "tipo": tipo,
        "descripcion": descripcion
    }
    return solicitud

# Ejemplo de ejecución
sol1 = registrar_solicitud("202601", "Ana", "matricula", "Problema con inscripción")

print("Código:", sol1["codigo"])
print("Nombre:", sol1["nombre"])
print("Tipo:", sol1["tipo"])
print("Descripción:", sol1["descripcion"])
