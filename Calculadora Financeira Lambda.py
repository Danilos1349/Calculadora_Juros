import math

menu1 = '''
        Calculadora financeira

Selecione o regime de juros:

[1] Juros Simples
[2] Juros Compostos
[3] Encerrar Programa
'''

menu2 = '''
        Calculadora financeira de juros simples

Selecione o que deseja calcular:

[1] Montante
[2] Capital
[3] Taxa de Juros
[4] Prazo
[5] Voltar
'''

menu3 = '''
        Calculadora financeira de juros compostos

Selecione o que deseja calcular:

[1] Montante
[2] Capital
[3] Taxa de Juros
[4] Prazo
[5] Voltar
'''

while True:
    opcao1 = int(input(menu1))
    
    if opcao1 == 1:
        while True:
            opcao2 = int(input(menu2))
            
            if opcao2 == 1:
                capital = float(input('Digite o valor do capital: '))
                juros = float(input('Digite a taxa de juros (em percentual): '))
                juros = juros / 100
                prazo = float(input('Digite o prazo: '))
                m = lambda c, j, t: c * (1 + j * t)
                print(f'O valor do montante é de R$ {m(capital, juros, prazo):.2f}')

            elif opcao2 == 2:
                montante = float(input('Digite o valor do montante: '))
                juros = float(input('Digite a taxa de juros (em percentual): '))
                juros = juros / 100
                prazo = float(input('Digite o prazo: '))
                c = lambda m, j, t: m / (1 + j * t)
                print(f'O valor do capital é de R$ {c(montante, juros, prazo):.2f}')

            elif opcao2 == 3:
                capital = float(input('Digite o valor do capital: '))
                montante = float(input('Digite o valor do montante: '))
                prazo = float(input('Digite o prazo: '))
                j = lambda c, m, t: (((m / c) - 1) / t) * 100
                print(f'A taxa de juros é de {j(capital, montante, prazo):.2f}%')

            elif opcao2 == 4:
                capital = float(input('Digite o valor do capital: '))
                montante = float(input('Digite o valor do montante: '))
                juros = float(input('Digite a taxa de juros (em percentual): '))
                juros = juros / 100
                t = lambda c, m, j: (m - c) / ( c * j)
                prazo = math.ceil(t(capital, montante, juros))
                print(f'O prazo da aplicação foi de {prazo} período(s)')
            
            elif opcao2 == 5:
                break

            else:
                print('Opção inválida!')

    elif opcao1 == 2:
        while True:
            opcao2 = int(input(menu3))

            if opcao2 == 1:
                capital = float(input('Digite o valor do capital: '))
                juros = float(input('Digite a taxa de juros (em percentual): '))
                juros = juros / 100
                prazo = float(input('Digite o prazo: '))
                vf = lambda vp, i, n: vp * (math.pow(1 + i, n))
                print(f'O valor do montante é de R$ {vf(capital, juros, prazo):.2f}')

            elif opcao2 == 2:
                montante = float(input('Digite o valor do montante: '))
                juros = float(input('Digite a taxa de juros (em percentual): '))
                juros = juros / 100
                prazo = float(input('Digite o prazo: '))
                vp = lambda vf, i, n: vf / (math.pow(1 + i, n))
                print(f'O valor do capital é de R$ {vp(montante, juros, prazo):.2f}')

            elif opcao2 == 3:
                capital = float(input('Digite o valor do capital: '))
                montante = float(input('Digite o valor do montante: '))
                prazo = float(input('Digite o prazo: '))
                i = lambda vp, vf, n: ((math.pow(vf / vp, 1 / n) - 1)) * 100
                print(f'A taxa de juros é {i(capital, montante, prazo):.2f}%')

            elif opcao2 == 4:
                capital = float(input('Digite o valor do capital: '))
                montante = float(input('Digite o valor do montante: '))
                juros = float(input('Digite a taxa de juros (em percentual): '))
                juros = juros / 100
                n = lambda vp, vf, i: math.log(vf / vp) / math.log(1 + i)
                prazo = math.ceil(n(capital, montante, juros))
                print(f'O prazo da aplicação foi de {prazo} período(s)')
            
            elif opcao2 == 5:
                break

            else:
                print('Opção inválida!')

    elif opcao1 == 3:
        print('Encerrando aplicação!')
        break
    elif opcao1 not in [1, 2, 3]:
        print('Opção inválida! Tente novamente.')