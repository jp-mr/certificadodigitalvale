from django.core.management.base import BaseCommand
import argparse
import re

from info.models import Ecnpj, Ecpf, NFe


class Command(BaseCommand):
    help = """

        Teste inicial pra ver se a bagaça funciona com docstring ...bom,
        funciona, agora só falta escrever o help

        """

    cls = {'ecnpj': Ecnpj(),'ecpf': Ecpf(), 'nfe': NFe()}

    def add_arguments(self, parser):
        parser.add_argument(
                '--file',
                type=argparse.FileType('r'),
                help='Arquivo com os dados de entrada'
                )

        parser.add_argument(
                '--class',
                type=str,
                help="Opções de modelos: 'ecnpj', 'ecpf', 'nfe'."
                )

    def _create_info_db(self, options):
        data = self._read_file(options)
        parsed_data = self._parse_data(data)
        self._save_data(parsed_data, options)

    def _read_file(self, options):
        file_text = options['file']
        data = file_text.readlines()
        #print(data)
        return data

    def _parse_data(self, data):

        # Cria uma única string
        s = ''
        for d in data:
            s += d

        # Separa as strings que estão entre < > e as que estão fora 
        regex = re.compile(r'[^<|>]+')
        rgx = regex.findall(s)

        # Itera devolvendo 2 itens por iteração, criando uma lista de
        # dicionários
        iterador = iter(rgx)
        parsed_data = []
        for titulo, descricao in zip(*[iterador]*2):
            desc = ''
            for linha in descricao:
                desc += linha.strip('\n')
            parsed_data.append({
                'título': titulo,
                'descrição': desc,
                })

        # Desempacota simultaneamente os itens de duas listas criando uma lista de dicionários
        # lista = [{'titulo': t, 'descricao': d} for t, d in zip(tit, desc)]

        #print(parsed_data)
        return parsed_data

    def _save_data(self, parsed_data, options):
        cls = options['class']
        for data in parsed_data:
            obj = self.cls[cls]
            obj.título = data['título']
            obj.descrição = data['descrição']
            # obj.save()
            print(type(obj))
            print('Object "%s" created\n' % obj.título)

    # Esse método deve ser sempre implementado e é chamado quando o comando é
    # executado
    def handle(self, *args, **options):
        self._create_info_db(options)
