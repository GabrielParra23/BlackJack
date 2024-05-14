from replit import clear
from logo import logo
   
def soma(valor1, valor2):
    return valor1 + valor2

def divisao(valor1, valor2):
    return valor1 / valor2

def multiplicacao(valor1, valor2):
    return valor1 * valor2

def subtracao(valor1, valor2):
    return valor1 - valor2

operacoes = {
    "-":subtracao,
    "+":soma,
    "/":divisao,
    "*":multiplicacao 
}
fim = "novo"
print(logo)
while fim == "novo":
    num1 = float(input("Digite um numero: "))
    for key in operacoes:
        print(key)
    operacao = input("Qual será a operacao: ")
    num2 = float(input("Digite o proximo numero: "))
    
    funcao = operacoes[operacao]
    resultado = funcao(valor1=num1, valor2=num2)

    print(f"{num1} {operacao} {num2} = {resultado}")

    fim = input(f"Se deseja continuar calculando com o resultado {resultado} digite \"Sim\", se deseja terminar o calculo digite \"Não\" ou se deseja começar um novo calculo digite \"Novo\"").lower()  
    clear()
  
    while fim == "sim":
    
        operacao = input("Qual será a operacao: ")
        num2 = int(input("Digite o proximo numero: "))
    
        funcao = operacoes[operacao]
        resultado1 = resultado
        resultado = funcao(valor1=resultado, valor2= num2) 
    
        print(f"{resultado1} {operacao} {num2} = {resultado}")
    
        fim = input(f"Se deseja continuar calculando com p resultado {resultado} digite \"Sim\", se deseja teminar o calculo digite \"Não\" ou se deseja começar um novo calculo digite \"Novo\"").lower()  
        clear()

