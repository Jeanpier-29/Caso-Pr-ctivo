# Req.2: Validar código
def validar_codigo(codigo):
    return codigo != "" and len(codigo) >= 5

# Req.3: Validar tipo de consulta
TIPOS_VALIDOS = ["matricula", "pagos", "constancia", "plataforma", "otro"]

def validar_tipo(tipo):
    return tipo.lower() in TIPOS_VALIDOS

# Req.1: Registrar solicitud
def registrar_solicitud(codigo, nombre, tipo, descripcion):
    if not validar_codigo(codigo):
        return "Error: código inválido"
    if not validar_tipo(tipo):
        return "Error: tipo inválido"

    solicitud = {
        "codigo": codigo,
        "nombre": nombre,
        "tipo": tipo,
        "descripcion": descripcion
    }
    return solicitud

# Ejemplo de ejecución válido
sol1 = registrar_solicitud("202601", "Ana", "matricula", "Problema con inscripción")
print("Código:", sol1["codigo"])
print("Nombre:", sol1["nombre"])
print("Tipo:", sol1["tipo"])
print("Descripción:", sol1["descripcion"])

# Prueba con tipo inválido
sol2 = registrar_solicitud("202602", "Luis", "biblioteca", "Consulta sobre préstamo")
print(sol2)

