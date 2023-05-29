# And Or y Not

#----------------------AND------------------

resultado_final = True and True;
print(resultado_final) # True

resultado_final = False and True;
print(resultado_final) # Falso

#----------------------OR------------------
resultado_final = False or True;
print(resultado_final) # True

resultado_final = False or False or 10>20;
print(resultado_final) # False

resultado_final = False or False or 10<20;
print(resultado_final) # True

#                 True and True                     
resultado_final = True and (False or 50>10);
print(resultado_final) # True
#----------------------NOT------------------
resultado_final = not True;
print(resultado_final) # False

resultado_final = not False;
print(resultado_final) # True



