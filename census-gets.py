from census import Census
from us import states

varsList = ['NAME', 'SUMLEVEL']

bigList = [['place', '03000', '02', ''], ['cousub', '77255', '36', '007']]

c = Census(key='82d15734a7d6fa98f0968b97f19fdcf6052009b6', year=2022)

for loc in bigList:
    if loc[0] == 'place':
        response = c.acs5.state_place(varsList, loc[2], loc[1])[0]
    elif loc[0] == 'cousub':
        response = c.acs5.state_county_subdivision(varsList, loc[2], loc[1], loc[3])
    print(response)
