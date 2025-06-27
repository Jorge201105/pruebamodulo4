from abc import ABC, abstractmethod


class Anuncio(ABC):
    def __init__(self,ancho,alto,url_archivo,url_click,sub_tipo):
        self.__ancho = ancho if ancho > 0 else 1  ## esto es una forma de filtrar en la misma linea, se evita el validador que debería realizarse en otro archivo
        self.__alto = alto if alto > 0 else 1
        self.__url_archivo = url_archivo
        self.__url_click = url_click
        self.__sub_tipo = sub_tipo

    @property
    def ancho(self):
        return self.__ancho
    
    @ancho.setter
    def ancho(self,ancho):
        self.__ancho = ancho

    @property
    def alto(self):
        return self.__alto
    
    @ancho.setter
    def alto(self,alto):
        self.__alto = alto

    @property
    def url_archivo(self):
        return self.__url_archivo
    
    @url_archivo.setter
    def url_archivo(self,url_archivo):
        self.__url_archivo = url_archivo

    @property
    def url_click(self):
        return self.__url_click
    
    @ancho.setter
    def url_click(self,url_click):
        self.__url_click = url_click

    @property
    def sub_tipo(self):
        return self.__sub_tipo
    
    @ancho.setter
    def sub_tipo(self,sub_tipo):
        self.__sub_tipo = sub_tipo

    @staticmethod
    def mostrar_formatos():
        pass
    @abstractmethod
    def comprimir_anuncio():
        pass

    @abstractmethod
    def redimensionar_anuncio():
        pass





    


class Campana:
    pass







class Video(Anuncio):
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")  ## Parentesis redondo para especificar una tupla

    def __init__(self,duracion):
        self.ancho =1
        self.alto = 1
        self.__duracion = duracion if duracion > 0 else 5

    @property
    def duracion(self):
        return self.__duracion
    
    @duracion.setter
    def duracion(self,duracion):
        self.__duracion = duracion

    
    def comprimir_anuncio():
        print("compresion de video no implementado aun")

    
    def redimensionar_anuncio():
        print("recorte de video no implementado")

class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional", "native")  ## Parentesis redondo para especificar una tupla



    def comprimir_anuncio():
        print("compresion de video no implementado aun")

    
    def redimensionar_anuncio():
        print("recorte de video no implementado")


class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")  ## Parentesis redondo para especificar una tupla



    def comprimir_anuncio():
        print("compresion de video no implementado aun")

    
    def redimensionar_anuncio():
        print("recorte de video no implementado")







