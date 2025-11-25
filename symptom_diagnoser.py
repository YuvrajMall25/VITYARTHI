"""
Symptom-Based Disease Diagnoser (Chatbot)
A simple text-based diagnostic system using decision tree logic.
"""

def ask_question(question):
    """Ask a Yes/No question and return True for Yes, False for No."""
    while True:
        answer = input(f"\n{question} (Yes/No): ").strip().lower()
        if answer in ['yes', 'y']:
            return True
        elif answer in ['no', 'n']:
            return False
        else:
            print("Please answer 'Yes' or 'No'.")


def diagnose():
    """Main diagnostic function using decision tree logic."""
    print("=" * 50)
    print("Welcome to the Symptom-Based Disease Diagnoser!")
    print("=" * 50)
    print("\nI'll ask you some questions about your symptoms.")
    print("Please answer with 'Yes' or 'No'.\n")
    
    # Decision Tree Logic
    # First level: Check for fever
    has_fever = ask_question("Do you have a fever?")
    
    if has_fever:
        # Branch with fever
        has_cough = ask_question("Do you have a cough?")
        
        if has_cough:
            # Fever + Cough branch
            has_body_aches = ask_question("Do you have body aches or muscle pain?")
            
            if has_body_aches:
                has_fatigue = ask_question("Do you feel tired or fatigued?")
                
                if has_fatigue:
                    print("\n" + "=" * 50)
                    print("DIAGNOSIS: You might have the FLU (Influenza)")
                    print("=" * 50)
                    print("\nCommon symptoms: Fever, cough, body aches, fatigue")
                    print("Recommendation: Rest, stay hydrated, and consult a doctor if symptoms worsen.")
                else:
                    has_sore_throat = ask_question("Do you have a sore throat?")
                    
                    if has_sore_throat:
                        print("\n" + "=" * 50)
                        print("DIAGNOSIS: You might have a COLD or FLU")
                        print("=" * 50)
                        print("\nCommon symptoms: Fever, cough, sore throat")
                        print("Recommendation: Rest, drink plenty of fluids, and monitor your symptoms.")
                    else:
                        print("\n" + "=" * 50)
                        print("DIAGNOSIS: You might have a RESPIRATORY INFECTION")
                        print("=" * 50)
                        print("\nCommon symptoms: Fever, cough")
                        print("Recommendation: Rest and consult a doctor if symptoms persist.")
            else:
                has_shortness_of_breath = ask_question("Do you have shortness of breath?")
                
                if has_shortness_of_breath:
                    print("\n" + "=" * 50)
                    print("DIAGNOSIS: You might have PNEUMONIA or BRONCHITIS")
                    print("=" * 50)
                    print("\nCommon symptoms: Fever, cough, shortness of breath")
                    print("Recommendation: Consult a doctor immediately. This may require medical attention.")
                else:
                    print("\n" + "=" * 50)
                    print("DIAGNOSIS: You might have a COLD or MILD RESPIRATORY INFECTION")
                    print("=" * 50)
                    print("\nCommon symptoms: Fever, cough")
                    print("Recommendation: Rest and monitor your symptoms.")
        else:
            # Fever but no cough
            has_headache = ask_question("Do you have a headache?")
            
            if has_headache:
                has_nausea = ask_question("Do you feel nauseous or have vomiting?")
                
                if has_nausea:
                    print("\n" + "=" * 50)
                    print("DIAGNOSIS: You might have GASTROENTERITIS (Stomach Flu)")
                    print("=" * 50)
                    print("\nCommon symptoms: Fever, headache, nausea/vomiting")
                    print("Recommendation: Stay hydrated, rest, and eat light meals. Consult a doctor if symptoms worsen.")
                else:
                    has_stiff_neck = ask_question("Do you have a stiff neck?")
                    
                    if has_stiff_neck:
                        print("\n" + "=" * 50)
                        print("DIAGNOSIS: You might have MENINGITIS (URGENT)")
                        print("=" * 50)
                        print("\nCommon symptoms: Fever, headache, stiff neck")
                        print("Recommendation: SEEK IMMEDIATE MEDICAL ATTENTION!")
                    else:
                        print("\n" + "=" * 50)
                        print("DIAGNOSIS: You might have a VIRAL INFECTION")
                        print("=" * 50)
                        print("\nCommon symptoms: Fever, headache")
                        print("Recommendation: Rest, stay hydrated, and monitor your symptoms.")
            else:
                print("\n" + "=" * 50)
                print("DIAGNOSIS: You might have a GENERAL VIRAL INFECTION")
                print("=" * 50)
                print("\nCommon symptoms: Fever")
                print("Recommendation: Rest, stay hydrated, and monitor your temperature.")
    else:
        # Branch without fever
        has_runny_nose = ask_question("Do you have a runny or stuffy nose?")
        
        if has_runny_nose:
            has_sneezing = ask_question("Do you have frequent sneezing?")
            
            if has_sneezing:
                has_itchy_eyes = ask_question("Do you have itchy or watery eyes?")
                
                if has_itchy_eyes:
                    print("\n" + "=" * 50)
                    print("DIAGNOSIS: You might have ALLERGIES")
                    print("=" * 50)
                    print("\nCommon symptoms: Runny nose, sneezing, itchy/watery eyes")
                    print("Recommendation: Avoid allergens if possible, and consider antihistamines. Consult a doctor if severe.")
                else:
                    print("\n" + "=" * 50)
                    print("DIAGNOSIS: You might have a COLD or ALLERGIES")
                    print("=" * 50)
                    print("\nCommon symptoms: Runny nose, sneezing")
                    print("Recommendation: Rest and monitor your symptoms.")
            else:
                has_cough = ask_question("Do you have a cough?")
                
                if has_cough:
                    print("\n" + "=" * 50)
                    print("DIAGNOSIS: You might have a COLD or SINUS INFECTION")
                    print("=" * 50)
                    print("\nCommon symptoms: Runny nose, cough")
                    print("Recommendation: Rest, stay hydrated, and use nasal decongestants if needed.")
                else:
                    print("\n" + "=" * 50)
                    print("DIAGNOSIS: You might have a COLD or MILD ALLERGY")
                    print("=" * 50)
                    print("\nCommon symptoms: Runny nose")
                    print("Recommendation: Monitor your symptoms and rest.")
        else:
            has_headache = ask_question("Do you have a headache?")
            
            if has_headache:
                has_dizziness = ask_question("Do you feel dizzy or lightheaded?")
                
                if has_dizziness:
                    print("\n" + "=" * 50)
                    print("DIAGNOSIS: You might have MIGRAINE or DEHYDRATION")
                    print("=" * 50)
                    print("\nCommon symptoms: Headache, dizziness")
                    print("Recommendation: Rest in a dark, quiet room. Stay hydrated. Consult a doctor if severe or persistent.")
                else:
                    print("\n" + "=" * 50)
                    print("DIAGNOSIS: You might have a HEADACHE or MIGRAINE")
                    print("=" * 50)
                    print("\nCommon symptoms: Headache")
                    print("Recommendation: Rest, stay hydrated, and consider over-the-counter pain relief if needed.")
            else:
                has_fatigue = ask_question("Do you feel tired or fatigued?")
                
                if has_fatigue:
                    print("\n" + "=" * 50)
                    print("DIAGNOSIS: You might have FATIGUE or STRESS")
                    print("=" * 50)
                    print("\nCommon symptoms: Fatigue")
                    print("Recommendation: Ensure adequate sleep, maintain a balanced diet, and manage stress levels.")
                else:
                    print("\n" + "=" * 50)
                    print("DIAGNOSIS: Your symptoms are not matching common patterns.")
                    print("=" * 50)
                    print("\nRecommendation: Consult a healthcare professional for a proper diagnosis.")
    
    print("\n" + "=" * 50)
    print("Thank you for using the Symptom-Based Disease Diagnoser!")
    print("REMEMBER: This is a simple educational tool and NOT a substitute")
    print("for professional medical advice. Always consult a healthcare")
    print("professional for accurate diagnosis and treatment.")
    print("=" * 50)


def main():
    """Main function to run the program."""
    try:
        diagnose()
        
        # Ask if user wants to run againy
        while True:
            run_again = input("\nWould you like to diagnose again? (Yes/No): ").strip().lower()
            if run_again in ['yes', 'y']:
                print("\n")
                diagnose()
            elif run_again in ['no', 'n']:
                print("\nThank you for using the Symptom-Based Disease Diagnoser. Get well soon!")
                break
            else:
                print("Please answer 'Yes' or 'No'.")
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please try again.")


if __name__ == "__main__":
    main()

