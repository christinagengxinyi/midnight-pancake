#calculate individual income tax for bonus
bonus=input("Enter your annual bonus:")
#tax=bonus*rate-deduct

b=int(bonus)
if b<=36000:
    tax=b*0.03
elif 36000<b<=144000:
    tax=b*0.1-2520/12
elif 144000<b<=300000:
    tax=b*0.2-16920/12
elif 300000<b<=420000:
    tax=b*0.25-31920/12
elif 420000<b<=660000:
    tax=b*0.3-52920/12
elif 660000<b<=960000:
    tax=b*0.35-85920/12
elif b>960000:
    tax=b*0.45-181920/12

print("Your annual individual tax for bonus:", tax)
