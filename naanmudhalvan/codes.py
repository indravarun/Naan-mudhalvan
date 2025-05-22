# healthcare_diagnosis.py

def diagnose(symptoms):
    """
    Simple rule-based diagnosis based on input symptoms
    """
    symptoms = [s.lower().strip() for s in symptoms]

    if 'fever' in symptoms and 'cough' in symptoms and 'fatigue' in symptoms:
        return "Flu", ["Rest", "Hydration", "Paracetamol"]
    elif 'chest pain' in symptoms and 'shortness of breath' in symptoms:
        return "Possible Heart Issue", ["Seek immediate medical attention", "Call emergency"]
    elif 'headache' in symptoms and 'nausea' in symptoms and 'sensitivity to light' in symptoms:
        return "Migraine", ["Pain relievers", "Rest in dark room", "Avoid triggers"]
    elif 'fever' in symptoms and 'rash' in symptoms:
        return "Possible Dengue or Viral Infection", ["Consult doctor", "Avoid NSAIDs", "Stay hydrated"]
    else:
        return "Unknown Condition", ["Consult a healthcare provider for proper diagnosis"]

def main():
    print("Welcome to the Simple Healthcare Diagnosis System")
    user_input = input("Enter your symptoms separated by commas (e.g., fever, cough, fatigue): ")
    symptom_list = user_input.split(',')

    diagnosis, treatment = diagnose(symptom_list)

    print(f"\nDiagnosis: {diagnosis}")
    print("Suggested Treatment:")
    for t in treatment:
        print(f"- {t}")

if __name__ == "__main__":
    main()
