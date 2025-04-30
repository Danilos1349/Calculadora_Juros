# 🧮 Calculadora Financeira (Juros Simples e Compostos)

Este projeto é uma calculadora financeira desenvolvida em Python para realizar cálculos envolvendo juros simples e juros compostos. A aplicação é interativa, executada no terminal, e permite que o usuário escolha o tipo de cálculo que deseja realizar.

## 💡 Funcionalidades

A calculadora oferece as seguintes opções:

### 1. Juros Simples

- **Calcular Montante (M)**: Valor total acumulado ao final do período.
- **Calcular Capital (C)**: Valor inicial aplicado.
- **Calcular Taxa de Juros (i)**: Taxa de juros ao período, em percentual.
- **Calcular Prazo (t)**: Tempo da aplicação, em períodos.

Fórmula usada:  
`M = C * (1 + i * t)`

### 2. Juros Compostos

- **Calcular Montante (VF)**: Valor futuro da aplicação.
- **Calcular Capital (VP)**: Valor presente (capital inicial).
- **Calcular Taxa de Juros (i)**: Taxa de crescimento por período, em percentual.
- **Calcular Prazo (n)**: Tempo de aplicação.

Fórmula usada:  
`VF = VP * (1 + i)ⁿ`

## ▶️ Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Salve o arquivo com o código Python (ex: `calculadora_financeira.py`).
3. Execute o script no terminal:

```bash
python calculadora_financeira.py
```

4. Siga as instruções no menu para realizar os cálculos desejados.

## Requisitos

- Python 3.x
- Biblioteca padrão (`math`) – já inclusa no Python

## Observações

- As taxas de juros devem ser fornecidas em **percentual** (por exemplo, digite `5` para 5%).
- Os prazos são tratados como períodos inteiros, sendo **arredondados para cima** nos cálculos que envolvem logaritmo ou divisão.
- O programa possui tratamento básico para opções inválidas nos menus.

## Licença

Este projeto é livre para fins educacionais e pessoais.

## 👨‍💻 Desenvolvido por

Danilo 🧠  
