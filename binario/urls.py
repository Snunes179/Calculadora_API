from django.urls import path
from .views import binarioCalc

# Para fazer o calculo digite operador(+,-,*,@ ou %)/primeiro numero em binario/segundo numero em binario
# exemplo: http://127.0.0.1:8000/+/00000010/00000011
# PS: operador '@' é usado para divisão

urlpatterns = [
    path('<str:op>/<str:num1>/<str:num2>', binarioCalc),
]