import serv_proto_pb2
import serv_proto_pb2_grpc
import grpc
from concurrent import futures
from configparser import ConfigParser

class CalculatorServicer(serv_proto_pb2_grpc.CalculatorServicer):
    def Calculate(self,request_msg, context):
        first_num = request_msg.Operand1
        second_num = request_msg.Operand2
        operation = request_msg.Operation
        if(operation=='MUL'):
            result = first_num * second_num
        if(operation=='DIV'):
            result = first_num // second_num
        if (operation == 'SUB'):
            result = first_num - second_num
        if (operation == 'SUM'):
            result = first_num + second_num
        response = serv_proto_pb2.CalculatedMessage(result = result)
        return response

configur = ConfigParser()
configur.read('serv_config.ini')
ip = configur.get('network', 'ip')
port = configur.get('network', 'port')
server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
serv_proto_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
print('Starting server on ' + str(ip) + ':' + str(port))
server.add_insecure_port( str(ip) + ':' + str(port) )
server.start()
server.wait_for_termination()