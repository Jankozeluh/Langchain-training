
# Document Miner

## Overview
Document Miner is a Python application designed to load, process, and store content from various document formats including PDFs, Word documents, Excel files, text files, JSON files, and CSVs. This script uses several libraries to extract text and utilizes SQLite for efficient data management and storage.

## Features
- Support for multiple file types: `.pdf`, `.docx`, `.xlsx`, `.txt`, `.json`, `.csv`.
- Text extraction and tokenization.
- Duplicate detection based on content hashing.
- Data storage in SQLite database.
- Multi-threaded document processing for improved performance.

## Prerequisites
- Python 3.8 or higher
- Required Python libraries: `nltk`, `pdfplumber`, `python-docx`, `openpyxl`, `sqlite3`

## Installation

### Step 1: Install Python Libraries
```bash
pip install nltk pdfplumber python-docx openpyxl sqlite3
```

### Step 2: NLTK Package
Ensure that the NLTK tokenization models are installed:
```bash
python -m nltk.downloader punkt
```

## Usage

### Setup Document Storage
Place your documents in a folder named `storage` located in the same directory as the script. You can also configure this path in the `DocumentLoader` class.

### Running the Script
Execute the script by running:
```bash
python miner.py
```

## Configuration
You can adjust parameters such as `storage_folder` and `db_file` in the `DocumentLoader` class to meet your specific storage and database needs.

## Contributing
Contributions are welcome! If you have suggestions for improvements or encounter any issues, feel free to modify the script as needed.

## License
This project is open for public use. Please provide appropriate credit when using or modifying this tool.

## Contact
For further inquiries or support, please contact the script maintainer at your email address.
