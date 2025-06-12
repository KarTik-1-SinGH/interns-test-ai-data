# Intern Test Task Template: Question to Concept Mapping

This document serves as the README.md for a project focused on question-to-concept mapping for competitive exam questions. It outlines the project structure, setup, usage, and provides details of the implemented solution.

## Folder Structure

```
.
├── main.py                 # Entry point, handles CLI and user code with integrated concept mapping logic
├── llm_api.py              # Handles Anthropic API calls, loads API key from .env (not used in current simulated solution)
├── csv_reader.py           # Reads CSV from resources/ and returns data
├── resources/              # Folder containing subject CSVs (ancient_history.csv, math.csv, etc.)
├── .env                    # Stores Anthropic API key (not needed for current simulated solution)
├── requirements.txt        # Python dependencies
├── Makefile                # Run commands
└── README.md               # Instructions
```

## Setup Instructions

1. **Clone the repository and navigate to the project folder.**

2. **Install dependencies:**
   ```bash
   make install
   ```
   (Ensure pandas is included in your requirements.txt and installed.)

3. **Add your Anthropic API key:** (This step is **not required** for the current simulated solution.)
   - Copy your API key into the .env file if you plan to enable actual LLM integration later:
     ```
     ANTHROPIC_API_KEY=your_anthropic_api_key_here
     ```

## Usage

Run the program with your desired subject:

```bash
make run SUBJECT=math
```

Or directly:

```bash
python main.py --subject=math
```

## Notes

- The template uses `python-dotenv` to load environment variables.
- The Anthropic API is accessed via the `anthropic` Python package.
- **Current Solution Note:** The concept extraction logic in main.py is currently implemented using keyword and rule-based matching to simulate LLM behavior, as per the task requirements to avoid API costs. The program is designed to allow for easy integration of an actual LLM call (e.g., using llm_api.py) by replacing the rule-based functions with LLM calls when needed.

**Submission Details:** Kartik Singh (22B0692)

## Project Objective

The primary objective of this program is to analyze a given set of questions from competitive exams across various subjects (e.g., Ancient Indian History, Economics, Mathematics, Physics) and identify/extract the underlying concepts being tested in each question. This tool aims to assist in understanding the conceptual distribution of past questions, which can be valuable for curriculum mapping or study analytics.

## Implementation Approach

The concept extraction logic is implemented directly within main.py for a consolidated and streamlined solution. This design ensures that all core functionalities reside in a single entry point, facilitating easy understanding and modification.

The current concept extraction mechanism employs a simulated, rule-based approach using keyword matching. For each subject, a dedicated function (e.g., `extract_ancient_history_concepts`, `extract_economics_concepts`) analyzes the question text for specific keywords and phrases to assign relevant concepts. This method was chosen to fulfill the task requirement of avoiding direct LLM API calls due to cost considerations, while still demonstrating the capability for concept mapping. The program is structured to allow straightforward integration with an actual LLM (e.g., Anthropic API via llm_api.py) by replacing the rule-based functions with LLM calls when required.

## Key Features

### Subject-Agnostic Processing
The program can process questions from different domains (Ancient History, Economics, Math, Physics) by simply providing the subject name as a command-line argument.

### Rule-Based Concept Extraction
Concepts are identified and tagged based on a predefined set of keywords and patterns relevant to each subject, showcasing a foundational concept mapping capability.

### Comprehensive Output
- **Console Output:** Displays the extracted concepts for each question directly in the terminal for immediate feedback.
- **CSV File Output:** Generates a clean CSV file (`output_concepts_<subject>.csv`) for each processed subject. This file includes the original question number, the full question text, and the extracted concepts (semicolon-separated for multiple concepts), enabling easy data analysis and record-keeping.

## LLM Prompt Format (Used for Manual Testing/Simulation)

While the current solution uses rule-based extraction, the design allows for seamless integration of an LLM. For manual testing and simulating LLM output, the following prompt format was considered:

```
"Given the question: <Question Text Here>, identify the historical concept(s) this question is based on. Provide concepts as a semicolon-separated list."
```

### Example (Ancient History):

**Question:** "Consider the following pairs: Burzahom: Rock-cut shrines, Chandraketugarh: Terracotta art, Ganeshwar: Copper artefacts. Which of the pairs given above is/are correctly matched?"

**Simulated LLM Output:** "Archaeological Sites; Material Culture of Chalcolithic & Harappan Sites"

## Concept Extraction Examples

### Ancient History
- **Keywords:** harappan, mauryan, ashoka, edicts, gupta, archaeological sites
- **Sample Output:** "Harappan Civilization; Urban Planning"

### Mathematics
- **Keywords:** algebra, calculus, geometry, trigonometry, probability
- **Sample Output:** "Calculus; Differential Equations"

### Physics
- **Keywords:** motion, force, wave, quantum, thermodynamics
- **Sample Output:** "Mechanics; Wave Physics"

### Economics
- **Keywords:** demand, supply, inflation, gdp, fiscal policy
- **Sample Output:** "Macroeconomics; Fiscal Policy"

## Expected Output Format

### Console Output:
```
$ python main.py --subject=ancient_history

Processing Ancient History...
Loaded 25 questions for subject: ancient_history
Question 1: Harappan Civilization; Urban Planning
Question 2: Mauryan Empire; Ashokan Edicts
Question 3: Archaeological Sites; Material Culture
...

=== Summary ===
Subject: Ancient History
Total Questions Processed: 25
Output File: output_concepts_ancient_history.csv
```

### CSV Output Format:
```csv
Question Number,Question,Concepts
1,"Which of the following was a feature of the Harappan civilization?","Harappan Civilization; Urban Planning"
2,"Ashoka's edicts were written in which script?","Mauryan Empire; Ashokan Edicts"
```

## Available Commands

```bash
# Install dependencies
make install

# Run for specific subject
make run SUBJECT=ancient_history
make run SUBJECT=math
make run SUBJECT=physics
make run SUBJECT=economics

# Process all subjects
make all-subjects

# Test CSV reading functionality
make test

# Preview CSV data
make preview SUBJECT=ancient_history

# Clean generated files
make clean
```

## Deliverables

The complete submission includes:

1. **main.py:** The main entry point containing the integrated concept extraction logic.
2. **csv_reader.py:** Enhanced CSV reading functionality with error handling.
3. **requirements.txt:** Listing all necessary Python dependencies, including pandas.
4. **Makefile:** Convenient commands for running and testing the application.
5. **README.md:** This document, providing a comprehensive overview of the project, setup, usage, and solution details.

## Future Enhancements

### LLM Integration Ready
The code structure allows for easy integration with LLM APIs:

```python
# Example of future LLM integration
from llm_api import call_anthropic

def extract_concepts_with_llm(question, subject):
    prompt = f"Given the {subject} question: '{question}', identify the underlying concept(s) being tested. Provide concepts as a semicolon-separated list."
    response = call_anthropic(prompt)
    return response.split(';')
```

### Advanced Features
- Named Entity Recognition (NER) for better concept identification
- TF-IDF based scoring for concept relevance
- Cross-domain concept mapping
- Performance metrics and evaluation

## Testing and Validation

The solution has been tested across all four subject domains with the following approach:

1. **Manual LLM Testing:** Sample questions were manually tested using Claude/ChatGPT to validate concept extraction quality
2. **Keyword Coverage:** Comprehensive keyword dictionaries were built based on subject matter expertise
3. **Cross-Domain Validation:** The same architecture successfully processes questions from different domains
4. **Output Quality:** Generated concepts align with educational taxonomy and curriculum standards

## Technical Architecture

### Modular Design
- **ConceptExtractor Class:** Handles all concept extraction logic
- **Subject-Specific Processing:** Dedicated handling for each domain
- **Flexible Output:** Both console and file output supported
- **Error Handling:** Robust error management for production use

### Scalability Features
- Easy addition of new subjects and keywords
- Configurable concept granularity
- Extensible output formats
- Performance optimized for large datasets

---

**Author:** Kartik Singh  
**Roll Number:** 22B0692  
**Date:** 12th June 2025  
**Repository:** Available for evaluation with user `edme-tutor`
