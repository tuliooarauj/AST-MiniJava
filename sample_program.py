"""
sample_program.py
Este arquivo deve conter a criação manual de uma instância da AST
para o programa MiniJava de exemplo fornecido no enunciado da atividade.
"""

from astminijava import *

# Exemplo de instância inicial (incompleto):
program = Program(
    main_class=MainClass("Main"),
    classes=[
        ClassDecl(
            name="Point",
            superclass=None,
            var_decls=[
                VarDecl(Type("int"), "x"),
                VarDecl(Type("int"), "y")
            ]
        )
    ]
)