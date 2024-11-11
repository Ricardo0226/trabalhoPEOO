class Planeta:
    def __init__(self, nome_planeta, gravidade_planeta):
        self.nome_planeta = nome_planeta
        self.gravidade_planeta = gravidade_planeta

    def get_nome_planeta(self):
        return self.nome_planeta

    def set_nome_planeta(self, nome_planeta):
        self.nome_planeta = nome_planeta

    def get_gravidade_planeta(self):
        return self.gravidade_planeta

    def set_gravidade_planeta(self, gravidade_planeta):
        self.gravidade_planeta = gravidade_planeta

    def calcular_peso(self, massa):
        peso = massa * self.gravidade_planeta
        print(f'O peso do corpo no planeta {self.nome_planeta} é: {peso} N.')


class TestarPlaneta:
    def main(self):
        nome_planeta = input("Digite o nome do planeta: ")
        gravidade_planeta = float(input("Digite a gravidade do planeta (em m/s²): "))

        planeta = Planeta(nome_planeta, gravidade_planeta)

        massa = float(input("Digite a massa do corpo (em kg): "))

        planeta.calcular_peso(massa)

        nova_gravidade = float(input("Digite o novo valor da gravidade do planeta: "))
        planeta.set_gravidade_planeta(nova_gravidade)

        planeta.calcular_peso(massa)

testar_planeta = TestarPlaneta()
testar_planeta.main()