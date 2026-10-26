from personagem import Personagem

class Heroi(Personagem):
    """"
    A classe heroi  representa as caracteristicas de um personagem no jogo.
    Herda da classe Personagem.
    """
    def __init__(self, nome, idade, vida, ataque, defesa):
        super().__init__(nome, idade, vida, ataque, defesa)

    def atacar(self, Personagem):
        if Personagem.vida > 0:
            print(f'{self.nome} atacou {Personagem.nome}')
            self.downgrade_vida(Personagem)
        elif Personagem.vida <= 0:
            Personagem.vida = 0
            print(f'Vida de {Personagem.nome} após ataque fatal {Personagem.vida}')

    def usar_pocao(self, pocao):
        lista_pocoes = ["Pequena", "media", "grande"]
        if pocao == "Pequena":
            self.upgrade_vida(20)

        elif pocao == "media":
            self.upgrade_vida(40)

        elif pocao == "grande":
            self.upgrade_vida(70)

        else:
            print('opção inválida')

    def __str__(self):
        return f'Heroi: {self.nome}, idade: {self.idade}, vida: {self.vida}, ataque: {self.ataque}, defesa: {self.defesa}'