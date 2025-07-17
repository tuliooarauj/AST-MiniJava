"""
astminijava.py
Este arquivo deve conter a definição das classes que representam a Árvore de Sintaxe Abstrata (AST)
para o subconjunto da linguagem MiniJava definido na Atividade da disciplina IF688.
"""

from typing import List, Optional

class ASTNode:
    pass

class Program(ASTNode):
    def __init__(self, main_class, classes: List['ClassDecl']):
        self.main_class = main_class
        self.classes = classes

class MainClass(ASTNode):
    def __init__(self, name: str):
        self.name = name
        self.main_method = MainMethod()

class MainMethod(ASTNode):
    def __init__(self):
        self.body = PrintStatement()

class PrintStatement(ASTNode):
    def __init__(self):
        pass  # Apenas System.out.println();

class ClassDecl(ASTNode):
    def __init__(self, name: str, superclass: Optional[str], var_decls: List['VarDecl']):
        self.name = name
        self.superclass = superclass
        self.var_decls = var_decls

class VarDecl(ASTNode):
    def __init__(self, var_type: 'Type', name: str):
        self.var_type = var_type
        self.name = name

class Type(ASTNode):
    def __init__(self, name: str, is_array: bool = False):
        self.name = name
        self.is_array = is_array
