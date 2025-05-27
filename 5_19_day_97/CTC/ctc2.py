ctc=float(input('enter monthly salary:'))
pf=input('if pf applicable than type (Y) or not than (N) ').upper()
total = float(input('total:'))
present = float(input('present:'))

# def fixed_gross_wages(ctc):
#     fgv=0
#     if pf == 'Y':
#         if ctc > 24299:
#             fgv=ctc-1800
#         elif ctc > 15000:
#             fgv =((ctc-7500) / 1.12 ) + 7500
#         else:
#             fgv = ctc / 1.06
#     elif pf == 'N':
#         fgv=ctc
#     else:
#         print('incorrect input')
#     print(fgv)
#
#     provident_fund = min(fgv * float(present / total)-min(fgv * float(present / total) * 0.50,7500 *float(present/total)),
#                 15000 * float(present / total)) * 0.12
#
#     # print((15000 * (present/total)) * 0.12)
#     return provident_fund
#
# print(fixed_gross_wages(ctc))

# prorated_fgv = fgv * (present / total)
    # provident_fund = min(prorated_fgv, 15000 * (present / total)) * 0.12

# prorated_fgv = fgv * (present / total)
    # hra=min(prorated_fgv * 0.50,7500 *(present/total))
    # basic=prorated_fgv-hra
    # provident_fund=min(basic, 15000 * (present / total)) * 0.12


def provident_fund(ctc,present,total):
    fgw=0
    if pf == 'Y':
        if ctc > 24299:
            fgw =ctc-1800
        elif ctc > 15000:
            fgw = ((ctc-7500)/1.12)+7500
        else:
            fgw=ctc/1.06
    elif pf == 'N':
        fgw=ctc
    else:
        print('incorrect value')

    prov= (ctc-fgw) * (present/total)
    print(prov)
    with24= prov * 2
    return with24

print(provident_fund(ctc,present,total))

