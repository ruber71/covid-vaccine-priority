# Find priority for COVID-19 vaccination
def find_priority(age, underlying_diseases, serious_illnes, nursing_home):    
    if nursing_home:
        priority = 1
    elif int(age) >= 85:
        priority = 2
    elif int(age) >= 75 and int(age) <= 84:
        priority = 3
    # TODO: Add the rest of the categories as 'elif'
    else:
        priority = 0
    return priority

# Ask user for input
def yes_no_bool(answer):
  return str(answer).lower() in ("yes", "yeah", "ja", "jawuhl", "si", "qui")

if __name__ == "__main__":
    age = input('Hvor gammel er personen?')
    underlying_diseases = yes_no_bool(input('Har personen underliggende sykdommer(JA eller NEI)?'))
    serious_illnes = yes_no_bool(input('Har personen seriousIllnes(JA eller NEI)?'))
    nursing_home = yes_no_bool(input('Bor personen på sykehjem? (JA eller NEI)'))

    priority = find_priority(age, underlying_diseases, serious_illnes, nursing_home)
    print("Personen har følgende priritet:", priority)


"""
vaccinepriority.py finds the COVID-19 vaccine priority in Norway for a person based on age, underlying_diseases, serious_illnes and nursing home.
See the below list of priorities.

test_vaccinepriority.py uses pytest.py to run unit tests on the priority finder.


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
