s=float(input("Enter your Annual Salary: ")) #annual salary
t=0 #tax counter
if(s <= 250000):
    t=0
if(s>250000 and s<=500000):
    t=(s-250000)*0.05
if(s>500000 and s<=750000):
    t=((s-500000)*0.1)+12500
if(s>750000 and s<=1000000):
    t=((s-750000)*0.15)+37500
if(s>1000000 and s<=1250000):
    t=((s-1000000)*0.2)+75000
if(s>1250000 and s<=1500000):
    t=((s-1250000)*0.25)+125000
if(s>1500000):
    t=((s-1500000)*0.3)+187500
print("Annual IT: Rs. ",t,"on CTC Rs. ",s)
print("Annual In Hand Salary: Rs.",(s-t))
print("Tax/pm:Rs. ",(t/12) ,"on", "CTC/pm: Rs. ",(s/12))
print("Per month CTC after IT deduction:Rs. ",((s-t)/12))