from sly import Lexer, Parser


class CalcLexer(Lexer):
    tokens = {STRING, RPAREN, RMAIOR, RMENOR, RMAIORIGUAL, RMENORIGUAL, RIGUAL, RDIFERENTE, ID, NUM, PLUS, TIMES, MINUS, DIVIDE, ATRIB, LPAREN, RPAREN, INTEIRO, FIMPARA, SE, INICIO, FIM, IMPRIMA, LEIA, ENTAO, PARA, LOGE, LOGOU, FIMSE, SENAO, PONTOVIRGULA, DOISPONTOS}
    ignore = ' \t'

    # Tokens
    ID = r'[a-zA-Z_][a-zÃãA-Z0-9_]*' #^[A-Za-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑ ]+$
    STRING = r'["].*"'
    NUM = r'\d+'
    PLUS = r'\+'
    MINUS = r'-'
    TIMES = r'\*'
    DIVIDE = r'/'
    PONTOVIRGULA = r'\;'
    DOISPONTOS = r'\:'
    ATRIB = r'<-'
    LPAREN = r'\('
    RPAREN = r'\)'
    RMENORIGUAL = r'<='
    RMAIORIGUAL = r'>='
    RMAIOR = r'>'
    RMENOR = r'<'    
    RIGUAL = r'='
    RDIFERENTE = r'<>'

    # Special cases (ex.: palavras reservadas)
    ID['inteiro'] = INTEIRO
    ID['inicio'] = INICIO
    ID['fim'] = FIM
    ID['imprima'] = IMPRIMA
    ID['leia'] = LEIA
    ID['se'] = SE
    ID['então'] = ENTAO
    ID['senão'] = SENAO
    ID['fim_se'] = FIMSE
    ID['para'] = PARA
    ID['fim_para'] = FIMPARA
    ID['e'] = LOGE
    ID['ou'] = LOGOU


    # Ignored pattern
    ignore_newline = r'\n+'

    # Extra action for newlines
    def ignore_newline(self, t):
        self.lineno += t.value.count('\n')

    def error(self, t):
        print("Illegal character '%s'" % t.value[0])
        self.index += 1



diretorio = 'C:/Users/ygors/Desktop/PUCPR/4Periodo/Interpretadores/Projeto1/teste.txt'
fp = open(diretorio,"r", encoding="UTF-8")
texto = fp.read()
fp.close

lexer = CalcLexer()

for tok in lexer.tokenize(texto):
        print('token=%r, lexema=%r' % (tok.type, tok.value))
