
#def processInput (cliente,quantidade,entrada,bebida,principal,sobremesa):
#    cliente = str(6)
#    quantidade = str(4)
    
#    entrada = 150
#    bebida = 60
#    principal = 240
#    sobremesa = 30
    
#    des = ["entrada", "bebida", "sobremesa"]
    
#   lista = [entrada, bebida, sobremesa]
    
#    total = entrada+bebida+principal+sobremesa
    
#    desconsiderados = sum(lista)
    
#    valor_conta = total/int(cliente)
    
#    res = [total, valor_conta, desconsiderados]
    
#    return res
def processInput (cliente,quantidade,entrada,bebida,principal,sobremesa,a,b,c):
    
    lista = [int(entrada), int(bebida), int(sobremesa)]
    
    total = int(entrada)+int(bebida)+int(principal)+int(sobremesa)
    
    desconsiderados = sum(lista)
    
    valor_conta = desconsiderados/int(cliente)
    
    res = [total, valor_conta, desconsiderados]
    
    return res
    
    
    
#Este e um exemplo de processamento de entradas (inputs), sinta-se a vontade para altera-lo conforme necessidade da questao.
resposta = processInput("6","4","150","60","240","30","entrada","bebida","sobremesa")
#res = str(resposta).strip('[]')
#print(res)
for i in resposta:
    print(i)

    

def processInput (cliente,quantidade,entrada,bebida,principal,sobremesa,a,b,c):
    
    lista = [int(entrada), int(bebida), int(sobremesa)]
    
    total = int(entrada)+int(bebida)+int(principal)+int(sobremesa)
    
    desconsiderados = sum(lista)
    
    valor_conta = desconsiderados/int(cliente)
    
    res = [total, valor_conta, desconsiderados]
    
    return res
    
    
    
#Este e um exemplo de processamento de entradas (inputs), sinta-se a vontade para altera-lo conforme necessidade da questao.
resposta = processInput("6","4","entrada 150","bebida 60","principal 240","sobremesa 30","entrada,bebida, sobremesa")
#res = str(resposta).strip('[]')
#print(res)
for i in resposta:
    print(i)
