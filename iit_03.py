#If the total annual income is determined, this calculation will figure out an optimized salary-bonus-structure with lowest tax
#income(determined)=salary+bonus

income=input("Enter your total annual income:")
salary=1 #start from salary=1
the_smallest_so_far=int(income)
while salary<=int(income):
    if salary<=36000:       #tax for annual salary
        taxsalary=salary*0.03
    elif 36000<salary<=144000:
        taxsalary=salary*0.1-2520
    elif 144000<salary<=300000:
        taxsalary=salary*0.2-16920
    elif 300000<salary<=420000:
        taxsalary=salary*0.25-31920
    elif 420000<salary<=660000:
        taxsalary=salary*0.3-52920
    elif 660000<salary<=960000:
        taxsalary=salary*0.35-85920
    elif salary>960000:
        taxsalary=salary*0.45-181920

    bonus=int(income)-salary   
    if bonus<=36000:        #tax for annual bonus
    	taxbonus=bonus*0.03
    elif 36000<bonus<=144000:
        taxbonus=bonus*0.1-2520/12
    elif 144000<bonus<=300000:
    	taxbonus=bonus*0.2-16920/12
    elif 300000<bonus<=420000:
    	taxbonus=bonus*0.25-31920/12
    elif 420000<bonus<=660000:
    	taxbonus=bonus*0.3-52920/12
    elif 660000<bonus<=960000:
    	taxbonus=bonus*0.35-85920/12
    elif bonus>960000:
    	taxbonus=bonus*0.45-181920/12

    totaltax=taxsalary+taxbonus 
    if totaltax<the_smallest_so_far:
    	the_smallest_so_far=totaltax
    	salary_when_min_totaltax=salary
    	bonus_when_min_totaltax=bonus

    salary=salary+1

min_totaltax=the_smallest_so_far
print("optimized totaltax:",min_totaltax)
print("optimized salary amount:", salary_when_min_totaltax)
print("optimized bonus amount:", bonus_when_min_totaltax)
