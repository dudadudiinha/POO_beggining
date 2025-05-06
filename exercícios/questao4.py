class Ingresso:
    def __init__(self):
        self.dia = "dom"
        self.hora = 18
    def entrada_inteira(self):
        if self.dia == "qua": return 8
        if self.dia in ['seg', 'ter', 'qua']: valor = 20
        if self.hora == 0 or self.hora >= 17: valor = 1.5*valor
        return valor
    def meia_entrada(self):
        if self.dia == 'qua': return 8
        return self.entrada_inteira()/2
         
x = Ingresso()
print(x.entrada_inteira(), x.dia, x.hora)

y=Ingresso()
y.dia = 'sab'
y.hora = 15
print(y.entrada_inteira(), y.dia, y.hora)

z=Ingresso()
z.dia = 'seg'
print(z.entrada_inteira(), z.dia, z.hora)