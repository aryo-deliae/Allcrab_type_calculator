#GENERATEUR DE FAIBLESSES RESISTANCES

type_num1 = int(input("Type 1 : "))
type_num2 = int(input("Type 2 : "))
t_num1 = []
t_num2 = []

t_num_final = []

#table des type

f_a = [1001, 12, 7, 8, 9, 10, 104]                    # humain
f_b = [1002, 1, 5, 10, 11, 104, 108, 117]             # bestial
f_c = [1003, 14, 15, 10, 113, 117]                    # insect
f_d = [1004, 3, 10, 11, 13, 115, 112, 116, 117]       # plante
f_e = [1005, 7, 9, 15, 102, 108, 111, 112, 113, 210]  # dragon
f_f = [1006, 10, 101, 106, 107]                       # sacré
f_g = [1007, 3, 8, 11, 105, 106, 107,]                # tenebre
f_h = [1008, 2, 5, 7, 101, 109, 118]                  # magie
f_i = [1009, 8, 17, 104, 105, 109]                    # poison
f_j = [1010, 6, 209, 210]                             # mort
f_k = [1011, 12, 13, 16, 17, 104, 111, 114, 118]      # feu
f_l = [1012, 4, 14, 15, 111, 112, 116, 118]           # eau
f_m = [1013, 14, 15, 16, 106, 217]                    # air
f_n = [1014, 11, 12, 18, 102, 103, 114,]              # glace
f_o = [1015, 16, 17, 106, 113, 118]                   # foudre
f_p = [1016, 4, 12, 17, 103, 113, 109, 110, 111, 118] # roche
f_q = [1017, 3, 4, 12, 111, 215]                      # terre
f_r = [1018, 1, 11, 17, 103, 104, 110, 114, 116, 209] # metal

f_effet = [f_a, f_b, f_c, f_d, f_e, f_f, f_g, f_h, f_i, f_j, f_k,
    f_l, f_m, f_n, f_o, f_p, f_q, f_r ]

#selection du type de la creature cible

for i in f_effet :
  for j in i :
      if i[0] == type_num1 + 1000 :
        t_num1.append(int(j))

for i in f_effet :
  for j in i :
      if i[0] == type_num2 + 1000 :
        t_num2.append(int(j))

t_num1.sort()
t_num2.sort()
print("-")
print(t_num1)
print(t_num2)

t_num_final = []

#immunités du 1er type
for i in t_num1 :
   if i > 200 and i < 220 :
    t_num_final.append(i+300)

#immunités du 2e type
for j in t_num2:
   if j > 200 and j < 220 and j not in t_num_final :
    t_num_final.append(j+300)

#doubles resistances
for i in t_num1 :
  for j in t_num2:
   if i == j and i > 100 and i+400 not in t_num_final:
    t_num_final.append(i)

#double faiblesses
for i in t_num1 :
  for j in t_num2:
   if i == j and i < 20 and i+500 not in t_num_final:
    t_num_final.append(i + 400)

#faiblesses simples du 1er type
for i in t_num1 :
    if i < 20 and i+300 not in t_num_final and i+100 not in t_num2 and i+400 not in t_num_final and i+500 not in t_num_final:
      t_num_final.append(i+300)


#faiblesses simples du 2e type
for j in t_num2:
  for i in t_num1 :
   if j < 20 and j and j not in t_num1 and j+300 not in t_num_final and j+100 not in t_num1 and j+400 not in t_num_final and i+500 not in t_num_final:
    t_num_final.append(j+300)

#resistances du 1er type
for i in t_num1 :
    if i > 100 and i < 120 and i not in t_num_final and i-100 not in t_num2 and i+200 not in t_num_final and i+100 not in t_num_final and i+400 not in t_num_final:
      t_num_final.append(i+100)

#resistances du 2e type
for j in t_num2 :
    if j > 100 and j < 120 and j not in t_num_final and j-100 not in t_num1 and j+200 not in t_num_final and j+100 not in t_num_final and i+400 not in t_num_final:
      t_num_final.append(j+100)

t_num_final.sort()

print("-")
print(t_num_final)

# Double R = 100
# Resistance = 200
# Faiblesse = 300
# Double F = 400
# Immunité = 500