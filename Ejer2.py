
#ejercicio #2

class Libro:
    def __init__(self, titulo, autor, anio_publicacion, num_pag):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicacion = anio_publicacion
        self.num_pag = num_pag

    def informacion(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Año de Publicación: {self.anio_publicacion}")
        print(f"Número de Páginas: {self.num_pag}")


mi_libro = Libro("Cartas sobre la mesa", "Agatha Christie", 1936, 400)
mi_libro.informacion()

