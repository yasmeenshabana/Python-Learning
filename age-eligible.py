def  am_I_eligible(age):
    if age>=18:
        return True
    else:
        return False
    
eligibility=am_I_eligible(18)
print("Eligibility for provided age is",eligibility)