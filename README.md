
# MRKL Application

## Overview
This application integrates various tools and technologies to answer user questions. It uses an AI model from OpenAI, enhanced with search capabilities, a mathematical solver, and a specialized database chain for queries related to specific domains like ichthyology and taxonomy (atleast thats what I use it for).

## Features
- **AI-Powered Answers:** Uses the OpenAI API to answer questions and provide information.
- **Database Chain:** A specialized query system that pulls information from a SQLite database for detailed answers in specific domains.
- **User Interaction:** Streamlit is used to create an interactive web application where users can submit their questions and get responses.

## Setup
To run this application, follow these steps:

1. **Clone the Repository:**
   ```
   git clone git@github.com:Jankozeluh/Langchain-training.git
   cd Langchain-training
   ```

2. **Install Dependencies:**
   Ensure Python 3.8+ is installed and then run:
   ```
   pip install -r requirements.txt
   ```

3. **Configuration:**
   Create a `config.ini` file in the root directory with the following content:
   ```ini
   [api]
   key = YOUR_OPENAI_API_KEY
   ```

4. **Database Setup:**
   Ensure the SQLite database is set up at the path specified in the script, or update the path as necessary.

5. **Run the Application:**
   ```
   streamlit run main.py
   ```

## Usage
Once the application is running:
- Open your web browser and go to the address shown in the Streamlit output.
- Input your question in the provided text box and click "Submit Question" to see the answer.

## Contributing
Contributions to this project are welcome. Please fork the repository and submit pull requests with your suggested changes.

## License
project is unlicensed and free to use.
