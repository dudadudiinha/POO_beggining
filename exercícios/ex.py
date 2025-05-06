class Cinema:
    def __init__(self):
        self.dia = ""
        self.horario = 0

    def valor_base(self):
        dia_lower = self.dia.lower()
        if dia_lower in ['segunda', 'terça', 'quinta']:
            return 16.0
        elif dia_lower == 'quarta':
            return 8.0  # já é meia-entrada para todos
        elif dia_lower in ['sexta', 'sábado', 'domingo']:
            return 20.0
        else:
            return None  # dia inválido

    def entrada_inteira(self):
        preco = self.valor_base()
        if preco is None:
            return "Dia inválido"
        if self.dia.lower() == 'quarta':
            return preco  # quarta todos pagam meia
        if 17 <= self.horario <= 24:
            preco *= 1.5  # acréscimo de 50%
        return preco

    def meia_entrada(self):
        inteira = self.entrada_inteira()
        if isinstance(inteira, str):  # verifica se deu erro (retornou mensagem)
            return inteira
        if self.dia.lower() == 'quarta':
            return inteira  # na quarta já é meia para todos
        return inteira / 2

# Programa para testar
sessao = Cinema()
sessao.dia = input("Digite o dia da semana: ")
sessao.horario = int(input("Digite o horário da sessão (0-24): "))

valor_inteira = sessao.entrada_inteira()
valor_meia = sessao.meia_entrada()

print(f"\nDia: {sessao.dia}, Horário: {sessao.horario}h")
print(f"Valor da entrada inteira: {valor_inteira}")
print(f"Valor da meia-entrada: {valor_meia}")
