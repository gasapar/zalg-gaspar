import src.simplefuncs as smfc

"""
*** Poznamka ke cviceni
* cvicici: Frantisek Gaspar
* aktivni ucast
* zapoctova uloha
* max 3 neomluvene absence
* cviceni streda a/nebo ctvrtek
"""


if __name__ == '__main__':
    # a = 1
    # b = -1
    # c = -2
    # x1, x2 = smfc.real_quadratic_roots(a, b, c)

    smfc.print_tree(5)

    f_rec = smfc.fib_number_recursion(20)
    f_cyc = smfc.fib_number_cyclus(20)

    print(f_rec)
    print(f_cyc)
