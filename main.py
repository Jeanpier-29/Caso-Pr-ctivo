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
    print("3. Eliminar solicitud")
    print("4. Consultar por tipo")
    print("5. Salir")

# Req.5: Calcular prioridad
def calcular_prioridad(tipo):
    if tipo.lower() in ["matricula", "pagos", "plataforma"]:
        return "Alta"
    else:
        return "Baja"

# Req.7: Mostrar resumen de solicitud
def mostrar_resumen(solicitud):
    if isinstance(solicitud, dict):
        print("=== RESUMEN DE SOLICITUD ===")
        print("Código:", solicitud["codigo"])
        print("Nombre:", solicitud["nombre"])
        print("Tipo:", solicitud["tipo"])
        print("Descripción:", solicitud["descripcion"])
        print("Prioridad:", calcular_prioridad(solicitud["tipo"]))
    else:
        print("No se puede mostrar resumen:", solicitud)

# Req.8: Almacenar solicitudes en una lista
solicitudes = []

def agregar_solicitud(solicitud):
    if isinstance(solicitud, dict):
        solicitudes.append(solicitud)
        print("Solicitud registrada correctamente.")
    else:
        print("No se pudo registrar la solicitud:", solicitud)

# Req.9: Consultar solicitudes por código
def consultar_solicitud(codigo):
    for s in solicitudes:
        if s["codigo"] == codigo:
            mostrar_resumen(s)
            return
    print("No se encontró ninguna solicitud con el código:", codigo)

# Req.10: Consultar solicitudes por tipo
def consultar_por_tipo(tipo):
    encontrados = [s for s in solicitudes if s["tipo"].lower() == tipo.lower()]
    if encontrados:
        print(f"=== SOLICITUDES DE TIPO: {tipo.upper()} ===")
        for s in encontrados:
            mostrar_resumen(s)
    else:
        print("No se encontraron solicitudes del tipo:", tipo)

# Req.11: Eliminar solicitud por código
def eliminar_solicitud(codigo):
    for s in solicitudes:
        if s["codigo"] == codigo:
            solicitudes.remove(s)
            print("Solicitud eliminada correctamente:", codigo)
            return
    print("No se encontró ninguna solicitud con el código:", codigo)

# Req.12: Salir del sistema
def salir():
    print("Saliendo del sistema... ¡Hasta pronto!")
    exit()

# ============================
# Ejemplos de ejecución
# ============================

# Registrar solicitudes
sol1 = registrar_solicitud("202601", "Ana", "matricula", "Problema con inscripción")
agregar_solicitud(sol1)

sol2 = registrar_solicitud("202602", "Luis", "constancia", "Solicitud de certificado")
agregar_solicitud(sol2)

# Consultar por código
consultar_solicitud("202601")

# Consultar por tipo
consultar_por_tipo("matricula")

# Eliminar solicitud
eliminar_solicitud("202602")

# Mostrar lista final
print("=== LISTA FINAL DE SOLICITUDES ===")
for s in solicitudes:
    mostrar_resumen(s)

# Mostrar menú principal
mostrar_menu()

# Salir del sistema
salir()
