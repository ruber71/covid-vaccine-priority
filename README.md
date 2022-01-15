# covid-vaccine-priority
Used to try out pytest.py library with parameterization.

vaccinepriority.py finds the COVID-19 vaccine priority in Norway for a person based on age, underlying diseases, serious illnes and nursing home.
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
