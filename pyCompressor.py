# -*- coding: utf-8 -*-
# ================================================================ #
#               The script is created by @zcxw_sudo                #
# ================================================================ #

import io
import json
import lzma
import os

import autopep8
import python_minifier
from rich import print
from rich.panel import Panel


banner = u'\u005b\u0023\u0066\u0065\u0064\u0036\u0034\u0037\u005d\u000d\u000a\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u005f\u005f\u005f\u005f\u005f\u005f\u000d\u000a\u005b\u0023\u0033\u0036\u0037\u0033\u0061\u0032\u005d\u0020\u0020\u0020\u0020\u005f\u005f\u005f\u005f\u0020\u0020\u005f\u005f\u0020\u0020\u005f\u005f\u005b\u002f\u0023\u0033\u0036\u0037\u0033\u0061\u0032\u005d\u0020\u002f\u0020\u005f\u005f\u005f\u005f\u002f\u005f\u005f\u005f\u0020\u0020\u005f\u005f\u005f\u005f\u0020\u005f\u005f\u005f\u0020\u0020\u005f\u005f\u005f\u005f\u0020\u0020\u005f\u005f\u005f\u005f\u005f\u005f\u005f\u005f\u0020\u0020\u005f\u005f\u005f\u005f\u005f\u005f\u005f\u005f\u005f\u005f\u005f\u005f\u005f\u005f\u0020\u0020\u005f\u005f\u005f\u005f\u005f\u000d\u000a\u005b\u0023\u0033\u0036\u0037\u0033\u0061\u0032\u005d\u0020\u0020\u0020\u002f\u0020\u005f\u005f\u0020\u005c\u002f\u0020\u002f\u0020\u002f\u0020\u002f\u005b\u002f\u0023\u0033\u0036\u0037\u0033\u0061\u0032\u005d\u002f\u0020\u002f\u0020\u0020\u0020\u002f\u0020\u005f\u005f\u0020\u005c\u002f\u0020\u005f\u005f\u0020\u0060\u005f\u005f\u0020\u005c\u002f\u0020\u005f\u005f\u0020\u005c\u002f\u0020\u005f\u005f\u005f\u002f\u0020\u005f\u0020\u005c\u002f\u0020\u005f\u005f\u005f\u002f\u0020\u005f\u005f\u005f\u002f\u0020\u005f\u005f\u0020\u005c\u002f\u0020\u005f\u005f\u005f\u002f\u000d\u000a\u005b\u0023\u0033\u0036\u0037\u0033\u0061\u0032\u005d\u0020\u0020\u002f\u0020\u002f\u005f\u002f\u0020\u002f\u0020\u002f\u005f\u002f\u0020\u002f\u005b\u002f\u0023\u0033\u0036\u0037\u0033\u0061\u0032\u005d\u002f\u0020\u002f\u005f\u005f\u005f\u002f\u0020\u002f\u005f\u002f\u0020\u002f\u0020\u002f\u0020\u002f\u0020\u002f\u0020\u002f\u0020\u002f\u0020\u002f\u005f\u002f\u0020\u002f\u0020\u002f\u0020\u0020\u002f\u0020\u0020\u005f\u005f\u0028\u005f\u005f\u0020\u0020\u007c\u005f\u005f\u0020\u0020\u0029\u0020\u002f\u005f\u002f\u0020\u002f\u0020\u002f\u000d\u000a\u005b\u0023\u0033\u0036\u0037\u0033\u0061\u0032\u005d\u0020\u002f\u0020\u002e\u005f\u005f\u005f\u002f\u005c\u005f\u005f\u002c\u0020\u002f\u005b\u002f\u0023\u0033\u0036\u0037\u0033\u0061\u0032\u005d\u0020\u005c\u005f\u005f\u005f\u005f\u002f\u005c\u005f\u005f\u005f\u005f\u002f\u005f\u002f\u0020\u002f\u005f\u002f\u0020\u002f\u005f\u002f\u0020\u002e\u005f\u005f\u005f\u002f\u005f\u002f\u0020\u0020\u0020\u005c\u005f\u005f\u005f\u002f\u005f\u005f\u005f\u005f\u002f\u005f\u005f\u005f\u005f\u002f\u005c\u005f\u005f\u005f\u005f\u002f\u005f\u002f\u000d\u000a\u005b\u0023\u0033\u0036\u0037\u0033\u0061\u0032\u005d\u002f\u005f\u002f\u0020\u0020\u0020\u0020\u002f\u005f\u005f\u005f\u005f\u002f\u005b\u002f\u0023\u0033\u0036\u0037\u0033\u0061\u0032\u005d\u0020\u0020\u0020\u0020\u0020\u0020\u005b\u0064\u0069\u006d\u0020\u0023\u0063\u0064\u0061\u0065\u0033\u0063\u005d\u0040\u007a\u0063\u0078\u0077\u005f\u0073\u0075\u0064\u006f\u005b\u002f\u0064\u0069\u006d\u0020\u0023\u0063\u0064\u0061\u0065\u0033\u0063\u005d\u0020\u0020\u0020\u0020\u0020\u0020\u002f\u005f\u002f\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u0020\u000d\u000a\u000d\u000a'


class pyCompressor:
    def __init__(self) -> None:
        with open('schema.json', 'r') as schema:
            self.schema = dict(json.load(schema))
            if self.schema.get('files') is None:
                raise Exception('From schema.json not found "files"')
        self.main_path = os.path.abspath('.')
        name_output_dir = f'{self.main_path}/{os.path.basename(self.main_path)}_compress/'
        if not os.path.exists(name_output_dir):
            os.mkdir(name_output_dir)
        self.file_output = f'{name_output_dir}/output.py'

    def minifier(self, data: str) -> str:
        data = python_minifier.minify(data, remove_annotations=True, remove_pass=True, remove_literal_statements=True,
                                      combine_imports=True, hoist_literals=True, rename_locals=True, remove_object_base=True, convert_posargs_to_args=True, preserve_shebang=True)
        return data

    def fix_data(self, data: str) -> io.StringIO:

        result = autopep8.fix_code(data, encoding='utf-8')
        buf = io.StringIO(result)
        return buf

    def file_data(self, file: str):
        result = ''
        data_fp = open(file, 'r', encoding='utf-8', errors='ignore')
        data = data_fp.read()
        data_fix = self.fix_data(data)
        data_line = data_fix.readlines()

        for line in data_line:
            is_import = False
            for dir in self.schema.get('dirs', []):
                if (f'from {dir}' in line) or (f'import {dir}' in line):
                    is_import = True
            if not is_import:
                result += line

        return result

    def compress_data(self, data: str) -> str:
        value = lzma.compress(data.encode('utf-8'))
        return f'import lzma as g;exec(g.decompress({value}).decode("utf-8"))'

    def run(self) -> None:
        main_data = ''
        size_all = 0
        files = self.schema.get('files')
        if files is not None:
            for file in files:
                if not os.path.exists(file):
                    raise Exception('The %s file does not exist!' % file)
                else:
                    size_all += os.path.getsize(file)
                    data = self.file_data(file)
                    main_data += data+'\n\n'
                    print('[green]File [magenta]%s[/magenta] read.' % file)
            for file in files:
                if os.path.dirname(file) != '.':
                    main_data = main_data.replace(os.path.basename(file).replace('.py', '.'), '')
            main_data_fix = self.fix_data(main_data).getvalue()
            print('[green]Code fix.')
            main_data_minify = self.minifier(main_data_fix)
            print('[green]Code minify.')
            main_data_compress = self.compress_data(main_data_minify)
            print('[green]Code compress.')
            open(self.file_output, 'w', encoding='utf-8',
                 errors='ignore').write(main_data_compress)
            size_new = os.path.getsize(self.file_output)
            print(
                f'[green]Successfully! [green dim]Files without compression: {size_all} bytes, and files compressed into a single file: {size_new} bytes.')
            print('[green]Code save. To [magenta]%s[/magenta]' %
                  self.file_output)

        else:
            raise Exception('From schema.json not found "files"')


if __name__ == '__main__':
    print(banner)

    compressor = pyCompressor()
    compressor.run()
