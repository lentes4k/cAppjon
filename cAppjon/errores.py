class Error_personalizado (Exception):

    def __init__(self, *args):

        if args:
            self.mensaje = args[0]
        else:
            self.mensaje = None

    def __str__(self):
        if self.mensaje:
            return self.mensaje
        else:
            return "Error" 
