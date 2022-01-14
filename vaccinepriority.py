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

