#calculate the individual income tax for annual salary
salary=input("Enter your annual salary:")
#taxable income=salary-60000

s=int(salary)-60000
if s<=36000:
    tax=s*0.03
elif 36000<s<=144000:
    tax=s*0.1-2520
elif 144000<s<=300000:
    tax=s*0.2-16920
elif 300000<s<=420000:
    tax=s*0.25-31920
elif 420000<s<=660000:
    tax=s*0.3-52920
elif 660000<s<=960000:
    tax=s*0.35-85920
elif s>960000:
    tax=s*0.45-181920

print("Your annual individual tax for salary:", tax)
