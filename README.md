# Symptom-Based Disease Diagnoser (Chatbot)

A simple Python-based diagnostic chatbot that uses decision tree logic to suggest possible illnesses based on user symptoms.

## Overview

This is a text-based interface where users answer "Yes/No" questions about their symptoms. The program traverses a Decision Tree using if-else logic to suggest a possible illness.

## Features

- Simple Yes/No question interface
- Decision tree-based diagnosis logic
- Multiple symptom combinations
- Educational and beginner-friendly code structure
- Can diagnose multiple rounds

## How It Works

The program uses a hierarchical decision tree structure:

1. **First Level**: Checks for fever (primary symptom)
2. **Second Level**: Based on fever presence, checks related symptoms (cough, headache, runny nose, etc.)
3. **Third Level**: Further refines based on additional symptoms
4. **Diagnosis**: Suggests possible illnesses based on symptom combinations

### Example Decision Flow

```
Start
  ↓
Do you have a fever?
  ├─ Yes → Do you have a cough?
  │         ├─ Yes → Do you have body aches?
  │         │         ├─ Yes → Do you have fatigue?
  │         │         │         ├─ Yes → FLU
  │         │         └─ ...
  │         └─ No → Do you have a headache?
  │                   └─ ...
  └─ No → Do you have a runny nose?
            └─ ...
```

## Usage

1. Run the program:
   ```bash
   python symptom_diagnoser.py
   ```

2. Answer the questions with "Yes" or "No"

3. Receive a diagnosis suggestion

4. Option to run again

## Requirements

- Python 3.x (no external dependencies required)

## Important Disclaimer

⚠️ **This is an educational project and NOT a substitute for professional medical advice.**

- This tool is designed for learning purposes only
- It uses simplified decision tree logic
- Always consult a healthcare professional for accurate diagnosis and treatment
- Do not rely on this tool for actual medical decisions

## Common Diagnoses Included

- Flu (Influenza)
- Common Cold
- Allergies
- Pneumonia/Bronchitis
- Gastroenteritis
- Migraine
- Sinus Infection
- And more...

## Code Structure

- `ask_question()`: Helper function to ask Yes/No questions
- `diagnose()`: Main diagnostic function with decision tree logic
- `main()`: Entry point with error handling and repeat functionality

## Learning Objectives

This project demonstrates:
- Decision tree implementation using if-else statements
- User input handling and validation
- Control flow (conditionals, loops)
- Function organization
- Basic error handling
- String manipulation

## Future Enhancements

Potential improvements for advanced students:
- Add more symptoms and diseases
- Implement a data-driven approach (dictionary/JSON)
- Add symptom severity levels
- Include treatment recommendations
- Add a GUI interface
- Store diagnosis history

