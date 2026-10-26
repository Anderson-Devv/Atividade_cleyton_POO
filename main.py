from personagem import Personagem
from vilao import Vilao
from heroi import Heroi

def main():
        # Criando personagens e vilões
        heroi = Heroi('Giyu', 17, 150, 30, 30)
        npc = Personagem('Zelda', 28, 80, 20, 10)
        vilao = Vilao('Alaska', 19, 200, 40, 30, 'Alta')

        # Mostrando personagens
        print(heroi)
        print(npc)
        print(vilao)

        lutar = input('Heroi quer batalhar contra o vilão?(S/N)').lower()
        if lutar == "s":
            while True:
                opcao = input('heroi deseja atacar(1), usar poção(2) ou fugir(3)?(1/2/3)')
                if opcao == "1":
                    heroi.atacar(vilao)

                elif opcao == "2":
                    # Melhorando a vida do herói
                    qualidade_pocao = input("qual o tipo de poção você quer usar?(Pequena/Media/Grande)").lower()
                    heroi.usar_pocao(qualidade_pocao)
                    print(f'{heroi.nome} após upgrade de vida: {heroi.vida}')

                elif opcao == "3":
                     print('Heroi não se sente forte o suficiente e decide fugir...')
                
                else:
                     print('Opção inválida')
                
                if heroi.vida == 0:
                     print('''infelizmente nossoa Heroina Giyu não foi capaz de derrotar a Vilã alaska, mas não desista Heroi, você pode ficar mais fort
                     e conseguirá derrotar essa vilã!!!''')

                if vilao.vida == 0:
                     print("""Parabens!! Você conseguiu, depois de toda essa jornada, derrotar a vilã que estava assolando a vila, Obrigada Heroina!!""")
                # Vilão ataca o herói
                vilao.atacar(heroi)

        # Mudando nome do NPC
        # npc.update_nome('Princesa Zelda')
        # print(f'Nome atualizado: {npc.nome}')

if __name__ == "__main__":
    main()
