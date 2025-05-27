ctc=int(input('enter monthly salary:'))
pf=input('if pf applicable than type (Y) or not than (N) ').upper()
total = int(input('total:'))
present = int(input('present:'))
def fixed_gross_wages(ctc):
    if pf == 'Y':
        if ctc > 24299:
            fgv=ctc-1800
            return fgv
        elif ctc > 15000:
            fgv =((ctc-7500) / 1.12 ) + 7500
            return fgv
        else:
            fgv = ctc / 1.06
            return fgv
    elif pf == 'N':
        fgv=ctc
        return fgv
    else:
        print('incorrect input')

def pro_rated_gross_wages(c):
    pgw = c * (present/total)
    return pgw

def house_rent_allowance(work):
    hra=min(work *0.50 ,7500 *(present/total))
    return hra

def basic_wages(work,in_hand):
    basic=work-in_hand
    return basic

def provident_fund(b):
    x=min(b,15000 *(present/total))
    p=x*0.12
    return p



x=fixed_gross_wages(ctc)
print(x)
y=pro_rated_gross_wages(x)
print(y)
z=house_rent_allowance(y)
print(z)
basic=basic_wages(y,z)
print(basic)
print(provident_fund(basic))