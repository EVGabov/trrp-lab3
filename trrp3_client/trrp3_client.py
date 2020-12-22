import serv_proto_pb2
import serv_proto_pb2_grpc
import grpc
from concurrent import futures
from configparser import ConfigParser

configur = ConfigParser()
configur.read('cl_config.ini')
ip = configur.get('network', 'ip')
port = configur.get('network', 'port')
print('Connect ' + str(ip) + ':' + str(port))
channel = grpc.insecure_channel(str(ip) + ':' + str(port))
stub = serv_proto_pb2_grpc.CalculatorStub(channel)
row_num = 0

while (row_num != 5):
    print('Выберите операцию: ')
    print('1. Сложение')
    print('2. Вычитание')
    print('3. Умножение')
    print('4. Целочисленное деление')
    print('5. Выход')
    row_num = int(input('Введите номер: '))
    while row_num != 5:
        first_num = float(input('Введите первое число: '))
        second_num = float(input('Введите второе число: '))
        if (row_num == 1):
            reaqest = serv_proto_pb2.CalculateMessage(Operation='SUM', Operand1=first_num, Operand2=second_num)
            response = stub.Calculate(reaqest)
        if (row_num == 2):
            reaqest = serv_proto_pb2.CalculateMessage(Operation='SUB', Operand1=first_num, Operand2=second_num)
            response = stub.Calculate(reaqest)
        if (row_num == 3):
            reaqest = serv_proto_pb2.CalculateMessage(Operation='MUL', Operand1=first_num, Operand2=second_num)
            response = stub.Calculate(reaqest)
        if (row_num == 4):
            reaqest = serv_proto_pb2.CalculateMessage(Operation='DIV', Operand1=first_num, Operand2=second_num)
            response = stub.Calculate(reaqest)
        print('Результат: ' + str(response.result))
        row_num = int(input('Введите номер: '))

print('Работа программы завершена')