class Heroi(object):
    def __init__(self, nome, descricao, imagem):
        self._nome = nome
        self._descricao = descricao
        self._imagem = imagem

            
    def getNome(self):
        return self._nome
   
    def getDescricao(self):
        return self._descricao
    
    def getImagem(self):
        return self._imagem
