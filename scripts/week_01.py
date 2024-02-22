import src.simplefuncs as smfc

"""
*** Poznamka ke cviceni
* cvicici: Frantisek Gaspar
* aktivni ucast
* zapoctova uloha
* max 3 neomluvene absence
* cviceni streda a/nebo ctvrtek
"""
"""
overeni vstupu 
vypocitat const
dosadit do vzorce
"""


if __name__ == '__main__':
    # a = 1
    # b = -1
    # c = -2
    # x1, x2 = smfc.real_quadratic_roots(a, b, c)

    smfc.print_tree(5)

    n_value = 20
    f_rec = smfc.fib_number_recursion(n_value)
    f_cyc = smfc.fib_number_cyclus(n_value)
    f_cls = smfc.fib_number_close(n_value)

    print(f_rec)
    print(f_cyc)
    print(f_cls)
