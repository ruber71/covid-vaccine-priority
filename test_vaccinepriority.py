   
#    test_headers = ['Age', 'Underlying Diseease', 'Serious Illnes', 'Nursing Home','Priority'] # Informational


import pytest
import vaccinepriority

@pytest.mark.parametrize('age,underlying_diseases,serious_illnes,nursing_home,priority,text', [
# each element of this list will provide values for the
# topics "value_A" and "value_B" of the test and will
# generate a stand-alone test case.
(40,False,False,True,1,"Residents in nursing homes"),
(40,False,True,True,1,"Residents in nursing homes AND Serious illness"),
(40,False,True,True,1,"Residents in nursing homes AND Serious illness"),
(40,True,True,True,1,"Residents in nursing homes AND Serious illness AND underlying disease"),
                
(85,False,False,False,2,"Age 85 years and older"),
# TODO: Add variations of 'Underlying Diseease', 'Serious Illnes', 'Nursing Home'

(84,False,False,False,3,"Age 75-84 years old"),
(75,True,False,False,3,"Age 75-84 years old"),
# TODO: Add variations of 'Underlying Diseease', 'Serious Illnes', 'Nursing Home'

(74,False,False,False,4,"Age 65-74 years old"),
(65,False,False,False,4,"Age 65-74 years old"),
# TODO: Add variations of 'Underlying Diseease', 'Serious Illnes', 'Nursing Home'

(64,False,True,False,4,"Age 18-64 år with serious illnesses"),
(18,False,True,False,4,"Age 18-64 år with serious illnesses"),
# TODO: Add variations of 'Underlying Diseease', 'Serious Illnes', 'Nursing Home'

(64,True,False,False,5,"Age 55-64 years old with underlying diseases"),
(55,True,False,False,5,"Age 55-64 years old with underlying diseases"),
# TODO: Add variations of 'Underlying Diseease', 'Serious Illnes', 'Nursing Home'

(54,True,False,False,6,"Age 45-54 years old with underlying diseases"),
(54,True,False,False,6,"Age 45-54 years old with underlying diseases"),
# TODO: Add variations of 'Underlying Diseease', 'Serious Illnes', 'Nursing Home'

(44,True,False,False,7,"Age 18-44 years old with underlying diseases"),
(18,True,False,False,7,"Age 18-44 years old with underlying diseases"),
# TODO: Add variations of 'Underlying Diseease', 'Serious Illnes', 'Nursing Home'

(64,False,False,False,8,"Age 55-64 years old"),
(55,False,False,False,8,"Age 55-64 years old"),
# TODO: Add variations of 'Underlying Diseease', 'Serious Illnes', 'Nursing Home'


(54,False,False,False,9,"Age 45-54 years old"),
(45,False,False,False,9,"Age 45-54 years old"),
# TODO: Add variations of 'Underlying Diseease', 'Serious Illnes', 'Nursing Home'

(24,False,False,False,10,"Age 18-24 years old"),
(18,False,False,False,10,"Age 18-24 years old"),
# TODO: Add variations of 'Underlying Diseease', 'Serious Illnes', 'Nursing Home'

(44,False,False,False,10,"Age 40-44 years old"),
(40,False,False,False,10,"Age 40-44 years old"),
# TODO: Add variations of 'Underlying Diseease', 'Serious Illnes', 'Nursing Home'

(39,False,False,False,12,"Age 25-39 years old"),
(25,False,False,False,12,"Age 25-39 years old"),
# TODO: Add variations of 'Underlying Diseease', 'Serious Illnes', 'Nursing Home'

(17,False,False,False,13,"Age 16-17 years old"),
(16,False,False,False,13,"Age 16-17 years old"),
# TODO: Add variations of 'Underlying Diseease', 'Serious Illnes', 'Nursing Home'

(15,False,False,False,14,"Age 12-15 years old"),
(12,False,False,False,14,"Age 12-15 years old"),                
# TODO: Add variations of 'Underlying Diseease', 'Serious Illnes', 'Nursing Home'
])
    
def test_find_priority(age, underlying_diseases, serious_illnes, nursing_home, text, priority):
    assert vaccinepriority.find_priority(age, underlying_diseases, serious_illnes, nursing_home) == priority #, text
    
"""
COVID-19 vaccination priorities in Norway
These priorities has been changed since the program was written
1. Residents in nursing homes
2. Age 85 years and older
3. Age 75-84 years old  
4. Age 65-74 years old
4. Age 18-64 år with serious illnesses
5. Age 55-64 years old with underlying diseases
6. Age 45-54 years old with underlying diseases
7. Age 18-44 years old with underlying diseases
8. Age 55-64 years old  
9. Age 45-54 years old
10. Age 18-24 years old
10. Age 40-44 years old
12. Age 25-39 years old
13. Age 16-17 years old
14. Age 12-15 years old 
"""
