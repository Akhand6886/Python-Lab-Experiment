#    Q2. At an airport, a traveler is allowed entry into the ﬂight only if he clears the following checks:
#    1. Baggage Check
#    2. Immigration Check
#    3. Security Check


baggage_weight=35
def check_baggage(baggage_weight):
    if(baggage_weight>=0 and baggage_weight<=40):
        return True
    else:
        return False
def check_immigration(expiry_year):
    if(expiry_year>=2030 and expiry_year<=2050):
          return True
    else:
        return False
def check_security(noc_status):
    if noc_status=='VALID':
        return True
    else:
        return False
def traveler():
    traveller_id=1001
    traveller_name="Jim"
    baggage_weight=35
    expiry_year=2034
    noc_status='VALID'
    x=check_baggage(baggage_weight)
    y=check_immigration(expiry_year)
    z=check_security(noc_status)
    if x==True and y==True and z==True:
        print(traveller_id)
        print(traveller_name)
        print("Allow Traveler to ﬂy!")
    else:
        print("Detain Traveler for Re-checking!")
traveler()
