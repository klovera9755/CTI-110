# CTI-110
# P2HW2-Tip Tax Total
# Adam klover
# 06/20/18

mealprice = float(input("please enter the charge of the food"))
tip = 0.18 * mealprice

salestax = 0.07 * mealprice

total = mealprice + tip + salestax

print("mealprice $" + format(mealprice,",.2f"), "Tip: $" + \
      format( tip, ",.2f"),"salestax $" + format(salestax, ",.2f"), \
     "total $" + format(total,",.2f"), sep = "\n" )
