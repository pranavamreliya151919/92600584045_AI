print("==================================")
print("     CAREER GUIDANCE SYSTEM      ")
print("==================================")

print("Answer The Following Question With Yes Or No.")

code=input("Do You Like Coding? : ").lower().strip()
math=input("Do You Like Mathematics : ").lower().strip()
bio=input("Do You Like Biology : ").lower().strip()
draw=input("Do You Like Drawing : ").lower().strip()

print("\n====== CAREER SUGGESTION ======\n")

if 'no' in code and math and bio and draw:
    print("Explore Your Interest and Carrer Option Further")

elif 'no' in code and math and bio and 'yes' in draw:
    print("Biomedical Softwere Engineer / Medical Technology Specialist")

elif 'no' in code and math and draw and 'yes' in bio:
    print("Pharmacist / Nurse")

elif 'no' in code and math and 'yes' in bio and 'yes' in draw:
    print("Medical Illustrator / HealthCare Eductor")

elif 'no' in code and bio and draw and 'yes' in math:
    print("Enginner / Data Analiyst")

elif 'no' in code and bio and 'yes' in draw and 'yes' in math:
    print("Architech")

elif 'no' in code and draw and 'yes' in math and 'yes' in bio:
    print("Doctor")

elif 'no' in code and 'yes' in math and 'yes' in bio and 'yes' in draw:
    print("Medical Illustrator / BioMedical Designer")

elif 'yes' in code and 'no' in  math and 'no' in bio and 'no' in draw:
    print("Programmer / Web Developer")

elif 'yes' in code and draw and 'no' in math and 'no' in bio:
    print("Web Designer / UI-UX Designer")

elif 'yes' in code and bio and 'no' in draw and 'no' in math:
    print("Health App Developer")

elif 'yes' in code and bio and draw and 'no' in math:
    print("Medical Illustrator")

elif 'yes' in code and math and 'no' in bio and 'no' in draw:
    print("Softwere Engineer / Computer Scientist")

elif 'yes' in code and math and draw and 'no' in bio:
    print("Game Developer / UI Engineer")
    
elif 'yes' in code and math and bio and 'no' in draw:
    print("BioInformatics Scientist")
    
elif 'yes' in code and math and bio and draw:
    print("Biomedical Softwere Engineer / Medical Technology Specialist")
    
print("\nThank You For Using The Carrer Guidance Expert System:)")
