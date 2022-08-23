ingreso = float(input("Ingreso anual: "))

extension_fiscal = 556.2
impuesto = 0.

if ingreso > 0. and ingreso <= 85528.:
    impuesto = (ingreso * 0.18) - extension_fiscal
    if impuesto < 0.:
        impuesto = 0.0
elif ingreso > 85528:
    impuesto = 14839.2 + ((ingreso - 85528) * 0.32)
else:
    impuesto = 0.0

print("Impuesto: {} pesos".format(round(impuesto, 0)))