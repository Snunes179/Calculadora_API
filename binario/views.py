from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json


def binarioCalc(request, op, num1, num2):

    if request.method == 'GET':
        operador = op
        numero_binario_1 = int(num1, 2)  # realiza a conversão de base 2 para base 10
        numero_binario_2 = int(num2, 2)  # realiza a conversão de base 2 para base 10

        # condição de execução "numero não pode ser maior que 255 ou menor que zero"
        if (numero_binario_1 <= 255) and (numero_binario_1 >= 0) and (numero_binario_2 <= 255) and (numero_binario_2 >= 0):

            # operações de adição

            if operador == "+":
                numero_resultado = numero_binario_1 + numero_binario_2
                
                # converte de base 10 para base 2 e tira os digitos 0b
                numero_resultado = bin(numero_resultado)[2:]

                resultado_final = alinharTamanhoBinario(numero_resultado)

                # converte para dicionario json

                dic = json.dumps({"Resultado": resultado_final})
                json_lib = json.loads(dic)

                return JsonResponse(json_lib)

            # operações de subtração

            elif operador == "-":
                numero_resultado = numero_binario_1 - numero_binario_2
                
                # converte de base 10 para base 2 e tira os digitos 0b
                numero_resultado = bin(numero_resultado)[2:]

                resultado_final = alinharTamanhoBinario(numero_resultado)

                # converte para dicionario json

                dic = json.dumps({"Resultado": resultado_final})
                json_lib = json.loads(dic)

                return JsonResponse(json_lib)

            # operações de multiplicação

            elif operador == "*":
                numero_resultado = numero_binario_1 * numero_binario_2
                
                # converte de base 10 para base 2 e tira os digitos 0b
                numero_resultado = bin(numero_resultado)[2:]

                resultado_final = alinharTamanhoBinario(numero_resultado)

                # converte para dicionario json

                dic = json.dumps({"Resultado": resultado_final})
                json_lib = json.loads(dic)

                return JsonResponse(json_lib)

            # operações de divisão

            elif operador == "@":
                if numero_binario_2 > 0:  # prevenir o erro da divisão por zero
                    numero_resultado = numero_binario_1 // numero_binario_2

                    # converte de base 10 para base 2 e tira os digitos 0b
                    numero_resultado = bin(numero_resultado)[2:]
                    
                    resultado_final = alinharTamanhoBinario(numero_resultado)

                    # converte para dicionario json

                    dic = json.dumps({"Resultado": resultado_final})
                    json_lib = json.loads(dic)

                    return JsonResponse(json_lib)

                else:
                    return HttpResponse("Não É Possivel Dividir Por Zero")

            # operações de resto

            elif operador == "%":
                numero_resultado = numero_binario_1 % numero_binario_2
                
                # converte de base 10 para base 2 e tira os digitos 0b
                numero_resultado = bin(numero_resultado)[2:]
                
                resultado_final = alinharTamanhoBinario(numero_resultado)

                # converte para dicionario json

                dic = json.dumps({"Resultado": resultado_final})
                json_lib = json.loads(dic)

                return JsonResponse(json_lib)

            else:
                return HttpResponse("Operador Inválido")

        else:
            return HttpResponse("Numero Inválido")

# alinha o tamanho do resultado_final para o padrão binario de oito digitos
# exemplo: 00000001
def alinharTamanhoBinario(num_binario):
    str(num_binario)

    if len(num_binario) == 1:
        binario = "0000000"
        resultado_final = binario + num_binario

    elif len(num_binario) == 2:
        binario = "000000"
        resultado_final = binario + num_binario

    elif len(num_binario) == 3:
        binario = "00000"
        resultado_final = binario + num_binario

    elif len(num_binario) == 4:
        binario = "0000"
        resultado_final = binario + num_binario

    elif len(num_binario) == 5:
        binario = "000"
        resultado_final = binario + num_binario

    elif len(num_binario) == 6:
        binario = "00"
        resultado_final = binario + num_binario

    elif len(num_binario) == 7:
        binario = "0"
        resultado_final = binario + num_binario

    return resultado_final
