import argparse
import pandas as pd
from csv_reader import read_subject_csv

def extract_ancient_history_concepts(question):
    concepts = []
    question_lower = str(question).lower()

    if "harappan" in question_lower or "indus valley" in question_lower:
        concepts.append("Indus Valley Civilization")
        if "city planning" in question_lower or "urban" in question_lower:
            concepts.append("Urban Planning")
        if "seal" in question_lower:
            concepts.append("Harappan Seals")
        if "drainage" in question_lower:
            concepts.append("Harappan Drainage System")
        if "citadel" in question_lower:
            concepts.append("Harappan Architecture")
    if "mauryan" in question_lower or "ashoka" in question_lower or "kautilya" in question_lower or "arthashastra" in question_lower or "edict" in question_lower:
        concepts.append("Mauryan Empire")
        if "ashokan edicts" in question_lower:
            concepts.append("Ashokan Edicts")
        if "kautilya" in question_lower or "arthashastra" in question_lower:
            concepts.append("Kautilya's Arthashastra")
    if "gupta" in question_lower:
        concepts.append("Gupta Period")
        if "literature" in question_lower or "science" in question_lower or "art" in question_lower:
            concepts.append("Gupta Period Achievements")
    if "buddhism" in question_lower or "buddha" in question_lower or "jainism" in question_lower or "jain" in question_lower:
        concepts.append("Ancient Indian Religions")
        if "buddhism" in question_lower:
            concepts.append("Buddhism")
        if "jainism" in question_lower:
            concepts.append("Jainism")
    if "vedic" in question_lower or "rigveda" in question_lower or "samaveda" in question_lower or "atharvaveda" in question_lower or "yajurveda" in question_lower:
        concepts.append("Vedic Period")
    if "site" in question_lower or "archaeological" in question_lower or "burzahom" in question_lower or "chandraketugarh" in question_lower or "ganeshwar" in question_lower:
        concepts.append("Archaeological Sites")
        if "artifact" in question_lower or "terracotta" in question_lower or "copper" in question_lower:
            concepts.append("Material Culture")
    if "revenue" in question_lower or "land system" in question_lower or "eripatti" in question_lower or "taniyurs" in question_lower:
        concepts.append("Revenue and Land Systems")
    if "temple" in question_lower or "ghatikas" in question_lower:
        concepts.append("Temple-based Education")
    if "science" in question_lower or "surgical" in question_lower or "sine" in question_lower or "quadrilateral" in question_lower:
        concepts.append("History of Indian Science")
        concepts.append("Chronological Reasoning")

    if not concepts:
        concepts.append("General Ancient History Concept")
    return list(set(concepts)) # Return unique concepts

def extract_economics_concepts(question):
    concepts = []
    question_lower = str(question).lower()

    if "gdp" in question_lower or "gross domestic product" in question_lower:
        concepts.append("Gross Domestic Product (GDP)")
    if "inflation" in question_lower or "price rise" in question_lower:
        concepts.append("Inflation")
    if "monetary policy" in question_lower or "interest rates" in question_lower or "reserve bank" in question_lower or "rbi" in question_lower:
        concepts.append("Monetary Policy")
    if "fiscal policy" in question_lower or "government spending" in question_lower or "taxation" in question_lower:
        concepts.append("Fiscal Policy")
    if "budget" in question_lower or "deficit" in question_lower:
        concepts.append("Government Budget and Deficit")
    if "poverty" in question_lower or "inequality" in question_lower:
        concepts.append("Poverty and Inequality")
    if "unemployment" in question_lower or "jobless" in question_lower:
        concepts.append("Unemployment")
    if "trade" in question_lower or "export" in question_lower or "import" in question_lower or "balance of payment" in question_lower:
        concepts.append("International Trade")
    if "banking" in question_lower or "loan" in question_lower or "credit" in question_lower or "financial sector" in question_lower:
        concepts.append("Banking and Financial Sector")
    if "agriculture" in question_lower or "farming" in question_lower or "crop" in question_lower:
        concepts.append("Agriculture Economy")
    if "industry" in question_lower or "manufacturing" in question_lower:
        concepts.append("Industrial Sector")
    if "market" in question_lower or "demand" in question_lower or "supply" in question_lower:
        concepts.append("Market Dynamics")
    if "bond market" in question_lower or "forex market" in question_lower or "money market" in question_lower or "stock market" in question_lower:
        concepts.append("Financial Markets")
    if "resettlement" in question_lower:
        concepts.append("Resettlement Policies")
    if "oversight" in question_lower or "regulating" in question_lower:
        concepts.append("Regulatory Bodies and Oversight")
    if "debt" in question_lower:
        concepts.append("Public Debt")

    if not concepts:
        concepts.append("General Economics Concept")
    return list(set(concepts)) # Return unique concepts

def extract_math_concepts(question):
    concepts = []
    question_lower = str(question).lower()

    if "algebra" in question_lower or "equation" in question_lower or "variable" in question_lower:
        concepts.append("Algebra")
    if "geometry" in question_lower or "triangle" in question_lower or "circle" in question_lower or "angle" in question_lower or "area" in question_lower or "perimeter" in question_lower or "volume" in question_lower:
        concepts.append("Geometry")
    if "arithmetic" in question_lower or "number" in question_lower or "digit" in question_lower or "prime" in question_lower or "ratio" in question_lower or "percentage" in question_lower or "fraction" in question_lower or "decimal" in question_lower:
        concepts.append("Arithmetic")
    if "calculus" in question_lower or "derivative" in question_lower or "integral" in question_lower or "limit" in question_lower:
        concepts.append("Calculus")
    if "probability" in question_lower or "chance" in question_lower or "event" in question_lower:
        concepts.append("Probability")
    if "statistics" in question_lower or "mean" in question_lower or "median" in question_lower or "mode" in question_lower or "data" in question_lower:
        concepts.append("Statistics")
    if "series" in question_lower or "sequence" in question_lower or "progression" in question_lower:
        concepts.append("Sequences and Series")
    if "trigonometry" in question_lower or "sine" in question_lower or "cosine" in question_lower or "tangent" in question_lower:
        concepts.append("Trigonometry")
    if "matrix" in question_lower or "vector" in question_lower:
        concepts.append("Linear Algebra")
    if "quadratic" in question_lower:
        concepts.append("Quadratic Equations")
    if "logarithm" in question_lower:
        concepts.append("Logarithms")
    if "set" in question_lower:
        concepts.append("Set Theory")

    if not concepts:
        concepts.append("General Mathematics Concept")
    return list(set(concepts))

def extract_physics_concepts(question):
    concepts = []
    question_lower = str(question).lower()

    if "motion" in question_lower or "velocity" in question_lower or "acceleration" in question_lower or "force" in question_lower or "newton" in question_lower or "mechanics" in question_lower or "work" in question_lower or "energy" in question_lower or "power" in question_lower:
        concepts.append("Mechanics")
    if "electricity" in question_lower or "current" in question_lower or "voltage" in question_lower or "resistance" in question_lower or "circuit" in question_lower:
        concepts.append("Electricity")
    if "magnetism" in question_lower or "magnetic field" in question_lower or "electromagnetism" in question_lower:
        concepts.append("Magnetism")
    if "light" in question_lower or "optics" in question_lower or "lens" in question_lower or "mirror" in question_lower or "reflection" in question_lower or "refraction" in question_lower:
        concepts.append("Optics")
    if "sound" in question_lower or "wave" in question_lower or "frequency" in question_lower or "amplitude" in question_lower:
        concepts.append("Waves and Sound")
    if "heat" in question_lower or "temperature" in question_lower or "thermodynamics" in question_lower or "entropy" in question_lower:
        concepts.append("Thermodynamics")
    if "atomic" in question_lower or "nucleus" in question_lower or "quantum" in question_lower or "electron" in question_lower or "proton" in question_lower or "neutron" in question_lower:
        concepts.append("Atomic and Nuclear Physics")
    if "relativity" in question_lower or "einstein" in question_lower:
        concepts.append("Relativity")
    if "gravity" in question_lower or "gravitational" in question_lower:
        concepts.append("Gravity")
    if "oscillation" in question_lower or "simple harmonic motion" in question_lower:
        concepts.append("Oscillations")

    if not concepts:
        concepts.append("General Physics Concept")
    return list(set(concepts))

def main():
    parser = argparse.ArgumentParser(description="Intern Test Task: Question to Concept Mapping")
    parser.add_argument('--subject', required=True, choices=['ancient_history', 'math', 'physics', 'economics'], help='Subject to process')
    args = parser.parse_args()

    # Read the CSV file for the specified subject
    # Assuming read_subject_csv returns a list of dictionaries, not necessarily a pandas DataFrame
    data = read_subject_csv(args.subject)
    print(f"Loaded {len(data)} questions for subject: {args.subject}")

    # Determine which concept extraction function to use
    extract_func = None
    if args.subject == 'ancient_history':
        extract_func = extract_ancient_history_concepts
    elif args.subject == 'economics':
        extract_func = extract_economics_concepts
    elif args.subject == 'math':
        extract_func = extract_math_concepts
    elif args.subject == 'physics':
        extract_func = extract_physics_concepts
    else:
        print(f"Error: No concept extraction logic defined for subject: {args.subject}")
        return

    # Apply concept extraction, adapting for list of dictionaries
    processed_data = []
    for row in data:
        # Ensure 'Question' key exists in the row dictionary
        if 'Question' not in row:
            print(f"Warning: 'Question' column not found in row: {row}. Skipping this row.")
            continue
        question_text = row['Question']
        concepts = extract_func(question_text)
        
        # Create a new dictionary for the processed row to avoid modifying original 'data' during iteration
        row_with_concepts = row.copy() 
        row_with_concepts['Concepts'] = concepts
        processed_data.append(row_with_concepts)

    # Convert processed_data (list of dicts) to DataFrame for easier printing/saving
    data_df = pd.DataFrame(processed_data)

    # Print to console as specified
    print(f"\nConcepts extracted from {args.subject.replace('_', ' ').title()} questions:")
    for index, row in data_df.iterrows():
        question_num = row.get('Question Number', 'N/A') # Use .get() for robustness
        question_text = row.get('Question', 'N/A')
        
        # Ensure concepts are a list before joining
        concepts_list = row['Concepts'] if isinstance(row['Concepts'], list) else [row['Concepts']]
        concepts_str = "; ".join(concepts_list)
        print(f"Question {question_num}: {question_text} -> Concepts: {concepts_str}")

    # Write to output CSV file
    output_filename = f"output_concepts_{args.subject}.csv"
    
    # Ensure only required columns are saved, and Concepts is joined
    # Check if 'Question Number' and 'Question' columns exist before selecting
    cols_to_save = ['Question Number', 'Question', 'Concepts']
    existing_cols = [col for col in cols_to_save if col in data_df.columns]
    output_df = data_df[existing_cols].copy()
    
    output_df['Concepts'] = output_df['Concepts'].apply(lambda x: "; ".join(x) if isinstance(x, list) else x)
    output_df.to_csv(output_filename, index=False)
    print(f"\nConcepts saved to {output_filename}")

if __name__ == "__main__":
    main()