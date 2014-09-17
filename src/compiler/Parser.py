'''
Created on 19 kwi 2014

@author: tpalys
'''

import Scanner
import AST

class Parser(object):
    '''
    classdocs
    '''


    def __init__(self):
        self.scanner = Scanner.Scanner()
        self.scanner.build()

    tokens = Scanner.Scanner.tokens


    precedence = (
       ("right", '='),
       #("left", 'OR'),
       #("left", 'AND'),
       #("left", 'XOR'),
       ("left", '+', '-'),
       ("left", '*', '/'),
    )


    def p_error(self, p):
        if p:
            print("Syntax error at line {0}, column {1}: LexToken({2}, '{3}')".format(p.lineno, self.scanner.find_tok_column(p), p.type, p.value))
        else:
            print('At end of input')

    def p_program(self, p):
        """program : objects_definitions scene"""
        p[0] = AST.Program(p[1], p[2])

    def p_objects_definitions(self, p):
        """objects_definitions : objects_definitions object_definition
                               | """
        if len(p) == 1:
            p[0] = AST.ObjectsDefinitions()
        else:
            p[1].append(p[2])
            p[0] = p[1]

    def p_object_definition(self, p):
        """object_definition : DEF ID '{' object_body '}'"""
        p[0] = AST.ObjectDefinition(p[2], p[4])

    def p_object_body(self, p):
        """object_body : default_color_definition ';' object_body_rest"""
        p[0] = AST.ObjectBody(p[1], p[3])

    def p_default_color_definition(self, p):
        """default_color_definition : DEFAULT_COLOR '(' FLOAT ',' FLOAT ',' FLOAT ')'"""
        p[0] = AST.ColorDefinition(float(p[3]), float(p[5]), float(p[7]))

#     def p_object_body_rest(self, p):
#         """object_body_rest : object_body_rest2
#                             | object_body_rest2 assigment ';'
#                             | object_body_rest2 if_expr
#                             | object_body_rest2 while_expr"""
#         p[0] = p[1]
#         if len(p) == 3:
#             p[0].append(p[2])
#         #TODO add assignment

    def p_block(self, p):
        """block : assigment ';'
                 | if_expr
                 | while_expr"""
        p[0] = p[1]

    def p_blocks(self, p):
        """blocks : blocks block
                  |"""
        if len(p) == 1:
            p[0] = AST.Blocks()
        else:
            p[1].append(p[2])
            p[0] = p[1]

    def p_object_body_rest(self, p):
        """object_body_rest : shape_with_transformations blocks object_body_rest
                            | shape_with_transformations blocks
                            | shape_without_transformations blocks object_body_rest
                            | shape_without_transformations blocks"""

        p[0] = AST.ObjectBodyRest()

        p[0].extend(p[1].nodeList)
        p[0].append(p[2])

        if (len(p) == 4):
            p[0].extend(p[3].nodeList)

    def p_shape_with_transformations(self, p):
        """shape_with_transformations : shape ';' transformation_nodes"""
        p[0] = AST.ObjectBodyRest()
        p[0].append(p[1])
        p[0].extend(p[3].nodes)


    def p_shape_without_transformations(self, p):
        """shape_without_transformations : shape ';'"""

        p[0] = AST.ObjectBodyRest()
        p[0].append(p[1])

    def p_transformation_nodes(self, p):
        """transformation_nodes : transformation_node ';' transformation_nodes
                                | transformation_node ';'"""
        if len(p) == 3:
            p[0] = AST.TransformationNodes()
            p[0].append(p[1])
        else:
            p[3].insert(0, p[1])
            p[0] = p[3]

    def p_transformation_node(self, p):
        """transformation_node : rotate_node
                               | translation_node
                               | scale_node
                               | color_node"""
        p[0] = p[1]

    def p_rotate_node(self, p):
        """rotate_node : ROTATE '(' FLOAT ')'"""
        p[0] = AST.Rotation(float(p[3]))

    def p_translation_node(self, p):
        """translation_node : TRANSLATE '(' INTEGER ',' INTEGER ')'"""
        p[0] = AST.Translation(int(p[3]), int(p[5]))

    def p_color_node(self, p):
        """color_node : COLOR '(' FLOAT ',' FLOAT ',' FLOAT ')'"""
        p[0] = AST.ColorDefinition(float(p[3]), float(p[5]), float(p[7]))

    def p_scale_node(self, p):
        """scale_node : SCALE '(' FLOAT ')'
                      | SCALE '(' FLOAT ',' FLOAT ')'"""

        if len(p) == 5:
            p[0] = AST.Scale(float(p[3]), float(p[3]))
        else:
            p[0] = AST.Scale(float(p[3]), float(p[5]))

    def p_shape(self, p):
        """shape : primitive
                 | usage"""
        p[0] = p[1]

    def p_primitive(self, p):
        """primitive : rectangle
                     | circle
                     | oval"""
        p[0] = p[1]

    def p_rectangle(self, p):
        """rectangle : RECTANGLE '(' INTEGER ',' INTEGER ',' INTEGER ',' INTEGER ')'
                     | RECTANGLE '(' INTEGER ',' INTEGER ',' INTEGER ',' INTEGER ',' INTEGER ')'"""

        if len(p) == 11:
            p[0] = AST.Rectangle(int(p[3]), int(p[5]), int(p[7]), int(p[9]))
        else:
            p[0] = AST.Rectangle(int(p[3]), int(p[5]), int(p[7]), int(p[9]), int(p[11]))

    def p_circle(self, p):
        """circle : CIRCLE '(' INTEGER ',' INTEGER ',' INTEGER ')'"""
        p[0] = AST.Circle(int(p[3]), int(p[5]), int(p[7]))

    def p_oval(self, p):
        """oval : OVAL '(' INTEGER ',' INTEGER ',' INTEGER ',' INTEGER ')'
                | OVAL '(' INTEGER ',' INTEGER ',' INTEGER ',' INTEGER ',' INTEGER ')'"""

        if len(p) == 11:
            p[0] = AST.Oval(int(p[3]), int(p[5]), int(p[7]), int(p[9]))
        else:
            p[0] = AST.Oval(int(p[3]), int(p[5]), int(p[7]), int(p[9]), int(p[11]))

    def p_usage(self, p):
        """usage : ID"""
        p[0] = AST.UsageNode(p[1])

    def p_scene(self, p):
        """scene : SCENE '(' INTEGER ',' INTEGER ')' '{' declarations object_body_rest '}'"""
        p[0] = AST.Scene(int(p[3]), int(p[5]), p[9], p[8])

    def p_declarations(self, p):
        """declarations : declaration ';' declarations
                        |"""
        if len(p) == 1:
            p[0] = AST.Declarations()
        else:
            p[3].insert(p[1])
            p[0] = p[3]

    def p_type(self, p):
        """type : int_type
                | float_type"""
        p[0] = p[1]

    def p_int_type(self, p):
        """int_type : INT_TYPE"""
        p[0] = AST.Type.ofInt()

    def p_float_type(self, p):
        """float_type : FLOAT_TYPE"""
        p[0] = AST.Type.ofFloat()

    def p_declaration(self, p):
        """declaration : type declarators"""
        p[0] = AST.Declaration(p[1], p[2])

    def p_declarators(self, p):
        """declarators : declarator ',' declarators
                       | declarator"""
        if len(p) == 4:
            p[3].insert(p[1])
            p[0] = p[3]
        else:
            p[0] = AST.Declarators(p[1])

    def p_declarator(self, p):
        """declarator : declarator_of_id
                      | assigment"""
        p[0] = p[1]

    def p_declarator_of_id(self, p):
        """declarator_of_id : ID"""
        p[0] = AST.Declarator(p[1])

    def p_assigment(self, p):
        """assigment : ID '=' expression"""
        p[0] = AST.Declarator(p[1])
        p[0].setExpr(p[3])

    def p_expression(self, p):
        """expression : const_expr
                      | id_expr
                      | two_arg_expr
                      | expr_in_brackets"""
        p[0] = p[1]

    def p_const_expr(self, p):
        """const_expr : int_const_expr
                      | float_const_expr"""
        p[0] = p[1]

    def p_float_const_expr(self, p):
        """float_const_expr : FLOAT"""
        p[0] = AST.Expression.ofConst(float(p[1]))

    def p_int_const_expr(self, p):
        """int_const_expr : INTEGER"""
        p[0] = AST.Expression.ofConst(int(p[1]))

    def p_id_expr(self, p):
        """id_expr : ID"""
        p[0] = AST.Expression.ofID(p[1])

    def p_two_arg_expr(self, p):
        """two_arg_expr : expression operator expression"""
        p[0] = AST.Expression.ofTwoArg(p[1], p[2], p[3])

    def p_operator(self, p):
        """operator : '+'
                    | '-'
                    | '*'
                    | '/'
                    | L
                    | LE
                    | G
                    | GE
                    | EQ
                    | NE"""
        p[0] = p[1]

    def p_expr_in_brackets(self, p):
        """expr_in_brackets : '(' expression ')'"""
        p[0] = p[2]

    def p_if_expr(self, p):
        """if_expr : IF '(' expression ')' '{' object_body_rest '}'
                   | IF '(' expression ')' '{' object_body_rest '}' ELSE '{' object_body_rest '}'"""
        if len(p) == 8:
            p[0] = AST.IfExpr.ofOnlyTrue(p[3], p[6])
        else:
            p[0] = AST.IfExpr.ofTrueFalse(p[3], p[6], p[10])

    def p_while_expr(self, p):
        """while_expr : WHILE '(' expression ')' '{' object_body_rest '}'"""
        p[0] = AST.WhileExpr(p[3], p[6])





















































