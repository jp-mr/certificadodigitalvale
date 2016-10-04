def table(model_class):

    produtos = list(model_class.objects.all())

    # CSS para a primeira e a última linha
    if produtos:
        produtos[0].first_row = 'first-row'
        produtos[-1].last_row = 'last-row'

    # Verifica se há imagem e passa um valor para usar um atributo CSS
    # do contrário, centraliza o texto em dois blocos brancos'
    # Verifica os blocos vazios e passa um valor para usar a propriedade CSS
    # "display:none", usado em larguras <= 600px
    for modelos in produtos:
        if modelos.imagem:
            modelos.img_produto = 'img-product'
        if not modelos.bloco_vermelho_validade and not modelos.bloco_vermelho_preço:
            modelos.vermelho_vazio = "hide-block"
        if not modelos.bloco_verde_validade and not modelos.bloco_verde_preço:
            modelos.verde_vazio = "hide-block"
        if not modelos.bloco_azul_validade and not modelos.bloco_azul_preço:
            modelos.azul_vazio = "hide-block"

    # Se a página for a NF-e, executa a verificação para e escolha de qual
    # estrutura de tabela utitlizar
    if model_class.certificado == 'PJ NF-e':

        # recebe por meio do método .append os valor 1 ou 0
        # 1 se mais de um bloco estiver preenchido
        # 0 se 1 bloco estiver preenchido
        lista_verificacao = []

        # itera por cada modelo (cada linha da tabela) 
        for modelos in produtos:

            # cria uma dicionário com os atributos da classe
            attributes = vars(modelos)

            # captura os valores dos atributos
            blc_vm_vl = attributes.get('bloco_vermelho_validade')
            blc_vm_pr = attributes.get('bloco_vermelho_preço')
            blc_vd_vl = attributes.get('bloco_verde_validade')
            blc_vd_pr = attributes.get('bloco_verde_preço')
            blc_az_vl = attributes.get('bloco_azul_validade')
            blc_az_pr = attributes.get('bloco_azul_preço')

            # uma lista de listas dos pares de atributos
            attr_blocos = [
                [blc_vm_vl, blc_vm_pr],
                [blc_vd_vl, blc_vd_pr],
                [blc_az_vl, blc_az_pr]
            ]
            # Exemplo de saída: attr_blocos -> [['', ''], ['', ''], ['Validade: 36 meses', 'R$ 380,00']]

            # Para cada lista 'lt_attr' dentro de 'attr_blocos', atribui o
            # valor zero para os elementos de lt_attr que forem uma string 
            # vazia, do contrário atribui o valor 1
            # no final de cada iteração por 'attr_blocos', que representa uma
            # linha da tabela (um modelo do NF-e), soma o valor dessa lista e
            # caso o valor seja menor que 2, coloca o valor zero em uma lista
            # de verificação, do contrário, coloca o valor 1
            for num, lt_attr in enumerate(attr_blocos):
                sm = 0
                for n, attr in enumerate(lt_attr):
                    if attr == '':
                        lt_attr[n] = 0
                    else:
                        lt_attr[n] = 1

                sm += sum(lt_attr)

                if sm == 0:
                    attr_blocos[num] = 0
                else:
                    attr_blocos[num] = 1

            # Exemplo de saída: attr_blocos -> [0, 0, 1]

            if sum(attr_blocos) < 2:
                lista_verificacao.append(0)
                # O bloco preenchido recebe os atributos para utilizar a
                # propriedade CSS adequada e passar valores no template
                # Os atributos 'validade' e 'preço' só são usados no bloco de
                # código da tabela que implementa um bloco colorido por linha
                # É dessa forma que é filtrado qual bloco deve ser exibido
                if attr_blocos[0] > 0:
                    modelos.validade = modelos.bloco_vermelho_validade
                    modelos.preço = modelos.bloco_vermelho_preço
                    modelos.cor_bloco = 'meses12-nfe'
                elif attr_blocos[1] > 0:
                    modelos.validade = modelos.bloco_verde_validade
                    modelos.preço = modelos.bloco_verde_preço
                    modelos.cor_bloco = 'meses24-nfe'
                else:
                    modelos.validade = modelos.bloco_azul_validade
                    modelos.preço = modelos.bloco_azul_preço
                    modelos.cor_bloco = 'meses36'
            else:
                lista_verificacao.append(1)

        # Se ao final da iteração por todos os modelos (linha da tabela), o
        # valor da soma da lista verificação for zero, isso indica que somente
        # um bloco de cada linha está preenchido
        if sum(lista_verificacao) == 0:
            tabela_nfe = True
            return produtos, tabela_nfe

        tabela_nfe=False
        return produtos, tabela_nfe

    return produtos

