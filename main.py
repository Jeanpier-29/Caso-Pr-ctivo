# Req.2: Validar código
def validar_codigo(codigo):
    return codigo != "" and len(codigo) >= 5

# Req.3: Validar tipo de consulta
TIPOS_VALIDOS = ["matricula", "pagos", "constancia", "plataforma", "otro"]

def validar_tipo(tipo):
    return tipo.lower() in TIPOS_VALIDOS

# Req.6: Validar texto obligatorio
def validar_texto(texto):
    return texto != "" and texto.strip() != ""

# Req.1: Registrar solicitud
def registrar_solicitud(codigo, nombre, tipo, descripcion):
    if not validar_codigo(codigo):
        return "Error: código inválido"
    if not validar_tipo(tipo):
        return "Error: tipo inválido"
    if not validar_texto(nombre):
        return "Error: nombre inválido"
    if not validar_texto(descripcion):
        return "Error: descripción inválida"

    solicitud = {
        "codigo": codigo,
        "nombre": nombre,
        "tipo": tipo,
        "descripcion": descripcion
    }
    return solicitud

# Req.4: Mostrar menú principal
def mostrar_menu():
    print("=== MENÚ PRINCIPAL ===")
    print("1. Registrar solicitud")
    print("2. Consultar solicitudes")
    print("3. Salir")

# Req.5: Calcular prioridad
def calcular_prioridad(tipo):
    if tipo.lower() in ["matricula", "pagos", "plataforma"]:
        return "Alta"
    else:
        return "Baja"
# Ejemplos de ejecución

# Caso válido
sol1 = registrar_solicitud("202601", "Ana", "matricula", "Problema con inscripción")
print("Código:", sol1["codigo"])
print("Nombre:", sol1["nombre"])
print("Tipo:", sol1["tipo"])
print("Descripción:", sol1["descripcion"])
print("Prioridad:", calcular_prioridad(sol1["tipo"]))

# Caso inválido: código vacío
sol2 = registrar_solicitud("", "Luis", "pagos", "Consulta sobre deuda")
print(sol2)

# Caso inválido: tipo incorrecto
sol3 = registrar_solicitud("202602", "María", "biblioteca", "Consulta sobre préstamo")
print(sol3)

# Caso inválido: nombre vacío
sol4 = registrar_solicitud("202603", "", "constancia", "Solicitud de certificado")
print(sol4)

# Caso inválido: descripción vacía
sol5 = registrar_solicitud("202604", "Pedro", "constancia", "")
print(sol5)

# Mostrar menú principal
mostrar_menu()
