# Justificativa de Modelagem da AST para MiniJava

## O que foi representado ou omitido?

A modelagem da AST buscou representar apenas os elementos semânticos relevantes da linguagem MiniJava. Foram omitidos todos os elementos puramente sintáticos, como símbolos `{`, `}`, `;`, e palavras-chave redundantes como `public static void main`.

Por exemplo, no caso do método `main`, apenas seu corpo (a instrução `System.out.println();`) foi mantido como uma instância de `PrintStatement`, que indica uma chamada de impressão sem argumentos (visto que a gramática não define parâmetros).

## Modelagem de listas, herança e elementos opcionais

Listas, como as declarações de variáveis em uma classe, foram modeladas como listas Python (`List[VarDecl]`).

Elementos opcionais, como a herança (`extends IDENTIFIER`), foram representados por campos opcionais (`superclass: Optional[str]`). Se a classe não herda de outra, o valor é `None`.

Houve a possibilidade de utilizar herança para tratar tipos ou expressões, mas dada a simplicidade da gramática, optou-se por não aplicar herança extensiva neste ponto.

## Conclusão

A estrutura da AST foi mantida fiel à gramática fornecida, focando na clareza e na representação dos elementos essenciais do programa. O uso de Python e suas funcionalidades como `Optional` e `List` permitiu uma modelagem limpa e extensível.
