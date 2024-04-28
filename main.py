# ANOTAÇÕES GERAIS
'''
    Autor: BRUNO RIBEIRO RODRIGUES RA: 2415050013 Curso: ADS Instituição: Unifacisa

    • 1) Listagem das Manifestações - ok
    • 2) Listagem de Manifestações por Tipo - ok
    • 3 ) Criar uma nova Manifestação - ok
    • 4 ) Exibir quantidade de manifestações - ok
    • 5 ) Pesquisar uma manifestação por código - ok
    • 6 ) Excluir uma Manifestação pelo Código - ok
    • 7 ) Sair do Sistema - ok
'''
from operacoesbd import *
from datetime import datetime

# VARIAVEIS GLOBAIS
opcao = -1
tiposManifestacao = ['Sugestão', 'Elogio', 'Solicitação', 'Reclamação', 'Denúncia', 'SAIR']
dataAtual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# CONEXÃO COM O BANCO DE DADOS
conn = criarConexao("localhost", "root", "matteo013", "bancohonda")

# INICIANDO O PROGRAMA
titulo = "*SISTEMA DE OUVIDORIA 2.0*"
print()
print("*" * len(titulo))
print(titulo)
print("*" * len(titulo))

# MENU DE OPÇÕES
while opcao != 7:
    try:
        opcao = int(input("\n1-Listar Manifestações.\n2-Lista Manifestação por tipo.\n3-Criar Manifestação."
                          "\n4-Exibir quantidade de manifestações.\n5-Pesquisar Manifestação."
                          "\n6-Excluir Manifestação.\n7-Sair Do Sistema.\n\nDigite uma opção: "))
        # LISTAR MANIFESTAÇÕES EM MASSA.
        if opcao == 1:
            print("\nManifestações Abertas: ")
            print()
            contagemManifestacao = f"SELECT count(*) FROM Manifestacao"
            resultadoContagem = listarBancoDados(conn, contagemManifestacao)
            count = resultadoContagem[0][0]
            if count > 0:
                selectManifestacoes = "SELECT * FROM MANIFESTACAO"
                resultado = listarBancoDados(conn, selectManifestacoes)
                for itens in resultado:
                    print(f"Codigo: {itens[0]}.\nDescrição: {itens[1]}.\nTipo: {itens[2]}.\nData: {itens[3]}.\n ")
            else:
                print("Não existem manifestações para serem listadas.")
        # LISTAR MANIFESTAÇÕES POR TIPO.
        elif opcao == 2:
            # VALIDA LOOP DO SUBMENU DE TIPOS DE MANIFESTAÇÃO.
            erroOpcao2 = True
            while erroOpcao2:
                try:
                    for index, item in enumerate(tiposManifestacao, start=1):
                        print(f"{index}-{item}")
                    opcaoSelecionada = int(input("\nSelecione o tipo de manifestação: "))
                    if 1 <= opcaoSelecionada <= len(tiposManifestacao) - 1:
                        tipoSelecionado = tiposManifestacao[opcaoSelecionada - 1]
                        contagemManifestacao = f"SELECT count(*) FROM MANIFESTACAO WHERE TIPO = '{tipoSelecionado}'"
                        # MÉTODO QUE TRÁS AS INFORMAÇÕES NO BANCO DE DADOS.
                        resultadoContagem = listarBancoDados(conn, contagemManifestacao)
                        count = resultadoContagem[0][0]
                        if count > 0:
                            selectManifestacoes = f"SELECT * FROM MANIFESTACAO WHERE TIPO ='{tipoSelecionado}' "
                            resultado = listarBancoDados(conn, selectManifestacoes)
                            for itens in resultado:
                                print(
                                    f"Codigo: {itens[0]}.\nDescrição: {itens[1]}.\nTipo: {itens[2]}.\nData: {itens[3]}.\n ")
                        else:
                            print("Não existem manifestações para serem listadas.")
                        erroOpcao2 = False
                    elif opcaoSelecionada == 6:
                        erroOpcao2 = False
                    else:
                        print("Opção inválida, tente novamente")
                except ValueError as err:
                    print("\nSó é permitido números:", err)
        # CRIAR NOVAS MANIFESTAÇÕES.
        elif opcao == 3:
            # VALIDA LOOP DO SUBMENU DE TIPOS DE MANIFESTAÇÃO.
            erroOpcao3 = True
            while erroOpcao3:
                try:
                    for index, item in enumerate(tiposManifestacao, start=1):
                        print(f"{index}-{item}")
                    opcaoSelecionada = int(input("\nSelecione o tipo de manifestação: "))
                    if 1 <= opcaoSelecionada <= len(tiposManifestacao) - 1:
                        tipoSelecionado = tiposManifestacao[opcaoSelecionada - 1]
                        print(f"\nVocê selecionou a opção:{tipoSelecionado}.")
                        descricao = input("Informe sua Manifestação: ")
                        insertManifestacao = "INSERT INTO MANIFESTACAO(DESCRICAO,TIPO,DATA_HORA)VALUES(%s,%s,%s)"
                        dados = [descricao.upper(), tipoSelecionado.upper(), dataAtual]
                        #MÉTODO QUE INSERIR AS INFORMAÇÕES NO BANCO DE DADOS.
                        #RETORNA ID
                        getId = insertNoBancoDados(conn, insertManifestacao, dados)
                        print("\nSua manifestação foi inserida com sucesso!\nSeu número de manifestação é:",getId)
                        ######
                        erroOpcao3 = False
                    elif opcaoSelecionada == 6:
                        erroOpcao3 = False
                    else:
                        print("Opção inválida, tente novamente.")
                except ValueError as err:
                    print("\nSo é permitido números:", err)
        # LISTAR A QUANTIDADE DE MANIFESTAÇÕES INSERIDAS NO BANCO DE DADOS
        elif opcao == 4:
            print()
            quantidadeManifestacoes = 'SELECT COUNT(*) FROM MANIFESTACAO'
            # MÉTODO QUE TRÀS AS INFORMAÇÕES DO BANCO DE DADOS
            quantidade = listarBancoDados(conn, quantidadeManifestacoes)
            for item in quantidade:
                print(f"Existem '{item[0]}' manifestações abertas.")
        # PESQUISAR MANIFESTAÇÃO POR CÓDIGO
        elif opcao == 5:
            print()
            try:
                id = int(input("\nPesquise sua manifestação por ID: "))
                print()
                contagemManifestacao = f"SELECT count(*) FROM MANIFESTACAO WHERE ID_MANIFESTACAO = '{id}'"
                resultadoContagem = listarBancoDados(conn, contagemManifestacao)
                count = resultadoContagem[0][0]
                if count > 0:
                    selectID = f"SELECT * FROM MANIFESTACAO WHERE ID_MANIFESTACAO = '{id}'"
                    resultado = listarBancoDados(conn, selectID)
                    for itens in resultado:
                        print(f"Codigo: {itens[0]}.\nDescrição: {itens[1]}.\nTipo: {itens[2]}.\nData: {itens[3]}.\n ")
                else:
                    print(f"Não existe nenhuma manifestação com esse ID {id}")
            except ValueError as err:
                print("\nSo é permitido números:", err)
        # EXCLUIR MANIFESTAÇÃO POR CÓDIGO.
        elif opcao == 6:
            try:
                idDelete = int(input("\nDelete/Apagar sua manifestação por ID: "))
                deleteID = f"DELETE FROM MANIFESTACAO WHERE ID_MANIFESTACAO = (%s)"
                dadosDelete = [idDelete]
                deleteRow = excluirBancoDados(conn, deleteID, dadosDelete)
                if deleteRow > 0:
                    print("Excluido com sucesso. ")
                else:
                    print(f"Não existe nenhuma manifestação com esse ID {idDelete}")
            except ValueError as err:
                print("\nSo é permitido números:", err)
        # SAIR DO SISTEMA
        elif opcao == 7:
            saudacaoSaida = "Obrigado por utilizar o nosso sistema."
            print("*" * len(saudacaoSaida))
            print(saudacaoSaida)
            print("*" * len(saudacaoSaida))
            # AQUI ENCERRA A CONEXÃO COM O BANCO DE DADOS.
            encerrarBancoDados(conn)
        else:
            print("\nOpção Invalida, tente novamente. ")
    except ValueError:
        print("\nSo é permitido números:")