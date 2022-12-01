class Heroi(object):
    def __init__(self, nome, descricao, imagem):
        self._imagem = imagem
        self._nome = nome
        self._descricao = descricao
        
    def getImagem(self):
        return self._imagem
    
    def getNome(self):
        return self._nome
    
    def getDescricao(self):
        return self._descricao