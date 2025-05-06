'''
#1
class Circle:
    def __init__(self):
        self.raio = 0
    def calc_perimetro_area(self):
        area = self.raio**2*3.14
        perimetro = self.raio*2*3.14
        return area, perimetro
circulo = Circle()
circulo.raio = int(input('Digite o valor do raio do círculo: '))
area, perimetro = circulo.calc_perimetro_area()
print(f'A circunferência do círculo é {perimetro:.2f}\nA área do círculo é {area:.2f}')

#2
class Trip:
    def __init__(self):
        self.distancia = 0
        self.horas = 0
        self.minutos = 0
    def veloc_media(self):
        tempoh = self.horas+self.minutos/60
        if tempoh == 0:
            return 0
        return self.distancia/tempoh
viagem = Trip()
viagem.distancia = int(input('Quantos km você percorreu para chegar ao destino? '))
viagem.horas = int(input('Quantas horas levou? '))
viagem.minutos = int(input('Quantos minutos foram necessários? '))
veloci_media = viagem.veloc_media()
print(f'A velocidade média atingida na viagem foi {veloci_media:.2f} km/h')

#3
class cBanco():
    def __init__(self):
        self.name = ""
        self.num = ""
        self.saldo = 0.0
    def depositar(self, money):
        if money > 0:
            self.saldo += money
            print(f'Seu depósito de R${money:.2f} foi concluído com êxito.')
        else:
            print('Não é possível deposistar um valor negativo.')
    def sacar(self, money):
        if money > 0 and self.saldo >= money:    
            self.saldo -= money
            print(f'Seu saque de R${money:.2f} foi concluído com êxito.')
        elif self.saldo < money:
            print('Saldo insusficiente. Você terá divídidas.')
        else:
            print('Valor de saque inválido.')
conta = cBanco()
conta.name = input('Digite seu nome: ')
conta.num = input('Digite o número da sua conta bancária: ')
conta.saldo = float(input('Digite seu saldo: '))
print(f'\nConta criada para {conta.name} (Conta Nº {conta.num})\nSaldo: R${conta.saldo:.2f}\n')

deposito = float(input('Quanto você deseja depositar? '))
conta.depositar(deposito)
print(f'Seu saldo atual é {conta.saldo:.2f}\n')

saque = float(input('Quanto você deseja sacar? '))
conta.sacar(saque)
print(f'Seu saldo atual é {conta.saldo:.2f}')
'''

#4


