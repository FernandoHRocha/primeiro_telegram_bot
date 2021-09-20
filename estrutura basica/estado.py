class Estado:
    estado = {
        0:'ocioso',
        1:'avaliando',
        2:'conversando'
    }
    def __init__(self,estado:int):
        self.estado = estado
    
    def __str__(self):
        return str(self.estado)

    def resetar(self):
        self.estado = 0