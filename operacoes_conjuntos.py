# Definição dos conjuntos
s1 = {1,2,3,4,5,}
s2 = {4,5,6,7,8}
print("=" * 50)
print("OPERACÕES COM CONJUNTOS (SETS)")
print("=" * 50)
print()

# União
unicao = s1.union(s2)
print('União (union)',unicao)
print('União (|) ',s1|s2)
print()

# Interseção
intersecao = s1.intersection(s2)
print('Interseção (intersection): ',intersecao)
print('Interseção (&):',s1 & s2)
print()

# Diferença (s1 - s2)
diferencia = s1.difference(s2)
print('Diferença s1 - s2 (difference): ',diferencia)
print('Diferença s1 - s2 (-): ',s1 - s2)
print()



# Diferença simétrica
diferenca_simetrica = s1.symmetric_difference(s2)
print('Diferença simétrica (symmetric_difference): ',diferenca_simetrica)
print('Diferença simétrica (^): ',s1 ^ s2)
print()

# Subconjunto
subset = s1.issubset(s2)
print('s1 é subconjunto de s2? ',subset)
print()

# Superconjunto
superset = s1.issuperset(s2)
print('s1 é superconjunto de s2? ',superset)