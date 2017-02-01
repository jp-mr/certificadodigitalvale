# 14 linhas de diferença

def append_attr(num, modelos):

    if num == 0:
        modelos['validade'] = modelos['bloco_vermelho_validade']
        modelos['preço'] = modelos['bloco_vermelho_preço']
        modelos['cor_bloco'] = 'meses12-nfe'
    elif num == 1:
        modelos['validade'] = modelos['bloco_verde_validade']
        modelos['preço'] = modelos['bloco_verde_preço']
        modelos['cor_bloco'] = 'meses24-nfe'
    else:
        modelos['validade'] = modelos['bloco_azul_validade']
        modelos['preço'] = modelos['bloco_azul_preço']
        modelos['cor_bloco'] = 'meses36'


def table(model_class):

    produtos = list(model_class.objects.values())

    lista_verificacao = []

    if produtos:
        produtos[0]['first_row'] = 'first-row'
        produtos[-1]['last_row'] = 'last-row'

    for modelos in produtos:
        if modelos['imagem']:
            modelos['img_produto'] = 'img-product'
            modelos['imagem'] = '/media/' + modelos['imagem']

        if not modelos['bloco_vermelho_validade'] and not modelos['bloco_vermelho_preço']:
            modelos['vermelho_vazio'] = "hide-block"

        if not modelos['bloco_verde_validade'] and not modelos['bloco_verde_preço']:
            modelos['verde_vazio'] = "hide-block"

        if not modelos['bloco_azul_validade'] and not modelos['bloco_azul_preço']:
            modelos['azul_vazio'] = "hide-block"

        if model_class.certificado == 'PJ NF-e':

            bloco_vermelho = [ v for k, v in modelos.items() if k.startswith('bloco_vermelho')]
            bloco_verde = [ v for k, v in modelos.items() if k.startswith('bloco_verde')]
            bloco_azul = [ v for k, v in modelos.items() if k.startswith('bloco_azul')]

            blocos = [bloco_vermelho, bloco_verde, bloco_azul]

            attr_blocos = [1 for b in blocos if b != ['','']]

            if sum(attr_blocos) < 2:

                lista_verificacao.append(0)

                for num, b in enumerate(blocos):
                    if b != ['','']:
                        append_attr(num, modelos)
            else:
                lista_verificacao.append(1)

    if model_class.certificado == 'PJ NF-e':
        if sum(lista_verificacao) == 0:
            tabela_nfe = True
            return produtos, tabela_nfe

        tabela_nfe=False
        return produtos, tabela_nfe

    return produtos




def table2(model_class):

    produtos = list(model_class.objects.all())

    if produtos:
        produtos[0].first_row = 'first-row'
        produtos[-1].last_row = 'last-row'

    for modelos in produtos:
        if modelos.imagem:
            modelos.img_produto = 'img-product'
        if not modelos.bloco_vermelho_validade and not modelos.bloco_vermelho_preço:
            modelos.vermelho_vazio = "hide-block"
        if not modelos.bloco_verde_validade and not modelos.bloco_verde_preço:
            modelos.verde_vazio = "hide-block"
        if not modelos.bloco_azul_validade and not modelos.bloco_azul_preço:
            modelos.azul_vazio = "hide-block"

    if model_class.certificado == 'PJ NF-e':

        lista_verificacao = []

        for modelos in produtos:

            attributes = vars(modelos)

            blc_vm_vl = attributes.get('bloco_vermelho_validade')
            blc_vm_pr = attributes.get('bloco_vermelho_preço')
            blc_vd_vl = attributes.get('bloco_verde_validade')
            blc_vd_pr = attributes.get('bloco_verde_preço')
            blc_az_vl = attributes.get('bloco_azul_validade')
            blc_az_pr = attributes.get('bloco_azul_preço')

            attr_blocos = [
                [blc_vm_vl, blc_vm_pr],
                [blc_vd_vl, blc_vd_pr],
                [blc_az_vl, blc_az_pr]
            ]

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

            if sum(attr_blocos) < 2:
                lista_verificacao.append(0)

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

        if sum(lista_verificacao) == 0:
            tabela_nfe = True
            return produtos, tabela_nfe

        tabela_nfe=False
        return produtos, tabela_nfe

    return produtos
