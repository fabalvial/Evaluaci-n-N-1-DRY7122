acl_num = int(input("Ingrese el número de ACL IPv4: "))
if (acl_num >= 1 and acl_num <= 99) or (acl_num >= 1300 and acl_num <= 1999):
    print("Es una ACL Estándar.")
elif (acl_num >= 100 and acl_num <= 199) or (acl_num >= 2000 and acl_num <= 2699):
    print("Es una ACL Extendida.")
else:
    print("El número no corresponde a una lista de acceso.")
