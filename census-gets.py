from census import Census
from us import states

c = Census('82d15734a7d6fa98f0968b97f19fdcf6052009b6')
response = c.acs5.state(('NAME', 'SUMLEVEL'), '66')

print(response)
