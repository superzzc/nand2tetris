import re
keyword_dict={
  'class': 'CLASS',
  'constructor': 'CONSTRUCTOR',
  'function': 'FUNCTION',
  'method': 'METHOD',
  'field': 'FIELD',
  'static': 'STATIC',
  'var': 'VAR',
  'int': 'INT',
  'char': 'CHAR',
  'boolean': 'BOOLEAN',
  'void': 'VOID',
  'true': 'TRUE',
  'false': 'FALSE',
  'null': 'NULL',
  'this': 'THIS',
  'let': 'LET',
  'do': 'DO',
  'if': 'IF',
  'else': 'ELSE',
  'while': 'WHILE',
  'return': 'RETURN'
}

keyword_list = [
    'class','constructor','function','method','field','static','var',
    'int','char','boolean','void','true','false','null','this',
    'let','do','if','else','while','return'
]

symbol_list = [
    '{','}','(',')','[',']','.',';',',','+','-','*','/','&','|','<','>','=','~'
]

# 转义符号
escaped_symbols = ''.join(map(re.escape, symbol_list))
symbol_str = f'[{escaped_symbols}]'

# 正则模式
p_string = r'"[^"\n]*"'           # 双引号字符串
p_int = r'\d+'                     # 整数
p_keyword = r'\b(?:' + '|'.join(keyword_list) + r')\b'
p_identifier = r'[A-Za-z_]\w*'     # 标识符
p_symbol = symbol_str

# 合并所有模式
token_pattern = re.compile(f'{p_string}|{p_int}|{p_keyword}|{p_identifier}|{p_symbol}')
comment= re.compile(r'^(.*?)\s*(//.*$|/\*[\s\S]*?\*/|/\*\*[\s\S]*?\*/)?$')
