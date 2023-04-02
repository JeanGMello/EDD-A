# Jean Gonçalves Mello
# RA: 1120449

import os
class  Veiculo:
    def __init__(self, placa, ano, marca_modelo, cor):
        self.placa = placa
        self.ano = ano
        self.marca_modelo = marca_modelo
        self.cor = cor
    def __str__(self):
        return '{} {} {}'.format(self.placa, self.ano, self.marca_modelo, self.cor)
    def __repr__(self):
        return '{} {} {}'.format(self.placa, self.ano, self.marca_modelo, self.cor)
    


class HashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * self.size
        self.values = [None] * self.size

    def _hash(self, key):
        hash_value = 0
        for char in key:
            hash_value += ord(char)
        return hash_value % self.size

    def insert(self, key, value):
        hash_key = self._hash(key)
        while self.keys[hash_key] is not None:
            if self.keys[hash_key] == key:
                self.values[hash_key] = value
                return
            hash_key = (hash_key + 1) % self.size
        self.keys[hash_key] = key
        self.values[hash_key] = value

    def delete(self, key):
        hash_key = self._hash(key)
        while self.keys[hash_key] is not None:
            if self.keys[hash_key] == key:
                self.keys[hash_key] = None
                self.values[hash_key] = None
                return
            hash_key = (hash_key + 1) % self.size

    def search(self, key):
        hash_key = self._hash(key)
        while self.keys[hash_key] is not None:
            if self.keys[hash_key] == key:
                return self.values[hash_key]
            hash_key = (hash_key + 1) % self.size
        return None
    
    def show_all(self):
        print(self.values)


def menu():
    print("     Cadastro de Veiculos")
    print(" Escolha o número da operação:")
    print(" 1)Consultar veículo")
    print(" 2)Cadastrar veículo")
    print(" 3)Excluir veículo")
    print(" 4)mostrar todos os registros")
    print(" 5)Fechar")
    escolha = input("")
    return escolha.lower()



hashTable = HashTable(29)

while True:
    input("->Precione enter para continuar")
    os.system("cls")
    escolha = menu()

    if escolha == '1':          #consulta
        print("")
        placa = input("->Insira a placa:")
        print(hashTable.search(placa))

    elif escolha == '2':        #inserir
        placa = input("->informe a placa do veiculo: ").lower()
        ano = input("->informe o ano de fabricação do veiculo: ").lower()
        marca_modelo = input("->informe o modelo do veiculo: ").lower()
        cor = input("->informe a cor do veiculo: ").lower()
        
        veiculo = Veiculo(placa, ano,marca_modelo,cor)
        hashTable.insert(placa, veiculo)

    elif escolha == '3':         #deletar
        placa = input("->informe a placa que deseja deletar:")
        try:
            hashTable.delete(placa)
            print(" placa excluida")
        except:
            print("/!\ Ocorreu algum erro na remoção da placa")

    elif escolha == '4':         #mostrar todos
        hashTable.show_all()
        pass

    elif escolha == '5':
        break

    else:
        print("digite um número de 1 a 5")
    print("")
