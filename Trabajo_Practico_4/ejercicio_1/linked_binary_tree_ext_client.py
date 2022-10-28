from python_ed_fcad_uner.data_structures import BinaryTreeNode
from linked_binary_tree_ext import LinkedBinaryTreeExt

nodo_a = BinaryTreeNode('A')
nodo_b = BinaryTreeNode('B')
nodo_c = BinaryTreeNode('C')
nodo_d = BinaryTreeNode('D')
nodo_f = BinaryTreeNode('F')
nodo_g = BinaryTreeNode('G')
nodo_h = BinaryTreeNode('H')
nodo_i = BinaryTreeNode('I')
nodo_k = BinaryTreeNode('K')
nodo_m = BinaryTreeNode('M')
nodo_n = BinaryTreeNode('N')

arbol = LinkedBinaryTreeExt()

arbol.add_left_child(None, nodo_a)
arbol.add_left_child(nodo_a, nodo_b)
arbol.add_right_child(nodo_a, nodo_f)
arbol.add_left_child(nodo_b, nodo_c)
arbol.add_right_child(nodo_b, nodo_d)
arbol.add_left_child(nodo_f, nodo_g)
arbol.add_right_child(nodo_f, nodo_k)
arbol.add_left_child(nodo_g, nodo_h)
arbol.add_right_child(nodo_g, nodo_i)
arbol.add_left_child(nodo_k, nodo_m)
arbol.add_right_child(nodo_k, nodo_n)

print("Arbol".center(36, "*"))
print(arbol,"\n")

print("Hermanos".center(36, "*"))
print(arbol.hermanos(nodo_g,nodo_k),"\n")

print("Hojas del arbol".center(36, "*"))
lista_hojas = arbol.hojas()
for hoja in lista_hojas:
    print(hoja)

print("")
print("Internos".center(36, "*"))
lista_internos = arbol.internos()
for interno in lista_internos:
    print(interno)

print("")
print("Profundidad".center(36, "*"))
print("[A] ",arbol.profundidad(nodo_a),)
print("[B] ",arbol.profundidad(nodo_b),)
print("[C] ",arbol.profundidad(nodo_c),)
print("[D] ",arbol.profundidad(nodo_d),)
print("[F] ",arbol.profundidad(nodo_f),)
print("[G] ",arbol.profundidad(nodo_g),)
print("[K] ",arbol.profundidad(nodo_k),)
print("[H] ",arbol.profundidad(nodo_h),)
print("[I] ",arbol.profundidad(nodo_i),)
print("[M] ",arbol.profundidad(nodo_m),)
print("[N] ",arbol.profundidad(nodo_n),"\n")

print("Altura".center(36, "*"))
print(arbol.altura(nodo_b))