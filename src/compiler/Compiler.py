'''
Created on 19 kwi 2014

@author: tpalys
'''

import ply.yacc as yacc
import Parser as Parser

class Compiler(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''

    def compile(self, text):
        graphParser = Parser.Parser()
        parser = yacc.yacc(module=graphParser)
# parser.parse(text, lexer=graphParser.scanner)

        ast = parser.parse(text, lexer=graphParser.scanner)
        #print "===========>\n" + str(ast) + "\n===================>\n"

        return ast.toScene()
