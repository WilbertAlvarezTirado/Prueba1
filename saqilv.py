def validar_campo(texto):
    """
    Valida si un texto contiene palabras SQL específicas.
    
    Args:
        texto (str): El texto a validar
        
    Returns:
        tuple: (bool, str) - (True si es válido, mensaje de resultado)
    """
    # Lista de palabras SQL a detectar (en minúsculas)
    palabras_prohibidas = ['select', 'insert', 'update']
    
    # Convertir el texto a minúsculas para hacer la comparación
    texto = texto.lower()
    
    # Verificar cada palabra prohibida
    for palabra in palabras_prohibidas:
        if palabra in texto:
            return False, "Error campo incorrecto"
    
    return True, "Campo válido"

# Ejemplo de uso
def main():
    # Simular entrada de usuario
    print("Ingrese texto (o 'salir' para terminar):")
    
    while True:
        entrada = input("> ")
        
        if entrada.lower() == 'salir':
            break
            
        es_valido, mensaje = validar_campo(entrada)
        print(f"Resultado: {mensaje}")
        
if __name__ == "__main__":
    main()
