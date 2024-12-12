class Nodo:
    """Clase Nodo para la lista enlazada."""
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    """Clase para gestionar la lista enlazada."""
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        """Agrega un nodo al final de la lista."""
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def eliminar(self, dato):
        """Elimina un nodo de la lista."""
        if not self.cabeza:
            return
        if self.cabeza.dato == dato:
            self.cabeza = self.cabeza.siguiente
            return
        actual = self.cabeza
        while actual.siguiente and actual.siguiente.dato != dato:
            actual = actual.siguiente
        if actual.siguiente:
            actual.siguiente = actual.siguiente.siguiente

    def buscar(self, dato):
        """Busca un nodo en la lista."""
        actual = self.cabeza
        while actual:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return False

    def recorrer(self):
        """Devuelve todos los elementos de la lista."""
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(actual.dato)
            actual = actual.siguiente
        return elementos

class Playlist:
    """Aplicación para gestionar una playlist de música."""
    def __init__(self):
        self.lista = ListaEnlazada()

    def menu(self):
        while True:
            print("\n--- Sistema de Gestión de Playlists ---")
            print("1. Agregar canción")
            print("2. Eliminar canción")
            print("3. Ver canciones")
            print("4. Buscar canción")
            print("5. Salir")
            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                cancion = input("Nombre de la canción: ")
                self.lista.agregar(cancion)
                print(f"Canción '{cancion}' añadida.")
            elif opcion == "2":
                cancion = input("Nombre de la canción a eliminar: ")
                self.lista.eliminar(cancion)
                print(f"Canción '{cancion}' eliminada.")
            elif opcion == "3":
                print("Playlist:", self.lista.recorrer())
            elif opcion == "4":
                cancion = input("Nombre de la canción a buscar: ")
                if self.lista.buscar(cancion):
                    print("La canción está en la playlist.")
                else:
                    print("La canción no está en la playlist.")
            elif opcion == "5":
                print("¡Gracias por usar el gestor de playlists!")
                break
            else:
                print("Opción no válida.")
