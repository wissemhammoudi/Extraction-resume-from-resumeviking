# Resume Template Extractor

A Python-based web scraping tool that automatically extracts and downloads resume templates from ResumeViking.com. This project uses Selenium WebDriver and BeautifulSoup to scrape resume template URLs and then downloads all available PDF templates.

##  Features

- **Automated Web Scraping**: Uses Selenium WebDriver to navigate through paginated content
- **PDF Template Extraction**: Automatically identifies and extracts PDF download links
- **Batch Download**: Downloads all templates to a local directory



##  Installation

### 1. Clone the Repository
```bash
git clone https://github.com/wissemhammoudi/Extraction-resume-from-resumeviking
cd Extraction-resume-from-resumeviking
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Verify Chrome Installation
Make sure you have Google Chrome installed on your system. The script will automatically download the appropriate ChromeDriver version.

##  Project Structure

```
Extraction-resume-from-resumeviking/
├── main.py                 # Main scraping script
├── downlodFromLink.py      # Download script for extracted URLs
├── downloads/              # Directory containing downloaded PDFs
├── resume_templates.txt    # Generated file with extracted URLs
├── README.md              # This file
└── .git/                  # Git repository
```

##  Usage

### Step 1: Extract Resume Template URLs
Run the main scraping script to extract all PDF download links:

```bash
python main.py
```

This script will:
- Navigate to ResumeViking.com templates page
- Automatically paginate through all available pages
- Extract PDF download links
- Save URLs to `resume_templates.txt`

**Note**: The script may take several minutes depending on the number of pages and your internet connection.

### Step 2: Download All Templates
After the URLs are extracted, run the download script:

```bash
python downlodFromLink.py
```

This script will:
- Read all URLs from `resume_templates.txt`
- Create a `downloads/` directory if it doesn't exist
- Download all PDF templates
- Display progress for each download

##  Output

### Generated Files
- **`resume_templates.txt`**: Contains all extracted PDF download URLs
- **`downloads/`**: Directory containing all downloaded resume templates
