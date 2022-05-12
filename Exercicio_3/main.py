from xml.dom.minidom import Document
from mongoengine import *
from mongoengine.connection import connect
import mongoengine
from mongoengine.document import Document
from flask import Flask, request, jsonify
import redis
import sys

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)

#DEFINE A ROTA E O MÉTODO
@app.route("/restapi/cadastrar", methods=['POST'])
def post_repository():
    try:
        produto = request.json
        salvar(produto['NOME'],produto['DESCRICAO'], produto['VALOR'])
    
        return "Produto cadastrado!"
    except Exception as e :
       return str(e)
    
@app.route("/restapi/atualizar", methods=['PUT'])
def atualizar_repository():
    try:
        produto = request.json
        atualizar(produto['NOME'],produto['DESCRICAO'], produto['VALOR'])

        return "Produto atualizado!"
    except Exception as e :
       return str(e)

@app.route("/restapi/deletar", methods=['DELETE'])
def delete_repository():
    try:
        produto = request.json
        deletar(produto['NOME'])

        return "Produto deletado!"
    except Exception as e :
       return str(e)

@app.route("/restapi/listar", methods=['GET'])
def get_repository():
    try:
        produto = request.json
        dic = listar(produto['NOME'])     
        return jsonify(dic)
    except Exception as e :
       return str(e)



def salvar(name, desc,valor):
    
    try:
        #SALVANDO DOCUMENTO
        variavelqq = Colecao(NOME = name, DESCRICAO =desc, VALOR = valor)
        variavelqq.save()
        print("salvo ok")
    except Exception as e:
        print(str(e))

def atualizar(name, desc,valor):
    Colecao.objects(NOME = name).update_one(DESCRICAO = desc)
    Colecao.objects(NOME = name).update_one(VALOR = valor)

def deletar(identificacao): 
    item = Colecao.objects(NOME = identificacao)
    item.delete()

#conectar no banco dentro de outro container (nome do banco + ip do banco dentro do container + a porta)
mongoengine.connect(host="mongodb://mongo:27017" )


class Colecao(Document):
    NOME = mongoengine.StringField()
    DESCRICAO = mongoengine.StringField()
    VALOR = mongoengine.FloatField()

    
def listar(escolha):
    
    dic = {} 
    contador = 0 
    #SELECIONA UM PRODUTO EM ESPECIFICO DE ACORDO COM O FILTRO (QUE NO CASO É O NOME)
    if len(escolha) >= 2:
        for  registro in Colecao.objects():
            if registro['NOME'] == escolha:
                dic[contador] = { "NOME": registro['NOME'], "DESCRICAO" : registro['DESCRICAO'], "VALOR" :registro['VALOR'] }
                contador +=1
        print("passo 1 ok")
    #PUXA A LISTA INTEIRA CASO NÃO TENHA NOME 
        
    else:
        for  registro in Colecao.objects():
            dic[contador] = { "NOME": registro['NOME'], "DESCRICAO" : registro['DESCRICAO'], "VALOR" :registro['VALOR'] }
            contador +=1
        print("passo 2 ok")
    return dic
    
def tamanho():
    print("pega tamanho ok")
    return len(Colecao.objects())   

if __name__=='__main__':
    app.run (host="0.0.0.0")