# DHA Residential License Generator

A web application that generates DHA (Defence Housing Authority) Residential License documents in DOCX format based on user input.

## Features

- User-friendly web form for entering DHA license details
- Generates professional DHA Residential License documents in DOCX format
- Form validation for all required fields
- Modern, responsive UI using Bootstrap
- Downloadable documents with unique timestamps

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone this repository:
```bash
git clone <repository-url>
cd dha-license-generator
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Fill out the license form with the required information:
   - Licensee (2nd Party) information
   - Plot details and boundaries
   - Land details
   - KPT details
   - Payment information
   - Transfer/Allotment details
   - Witness information

4. Click "Generate License Documents" to create the DHA license document

5. Download the generated document in DOCX format

## File Structure

```
dha-license-generator/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── README.md           # This file
├── generated_docs/     # Directory for generated documents
└── templates/          # HTML templates
    ├── base.html       # Base template with common styling
    ├── form.html       # Main form template
    └── success.html    # Success page template
```

## Security Notes

- The application uses Flask's CSRF protection for form submission
- Generated documents are stored in the `generated_docs` directory
- In production, you should:
  - Change the Flask secret key
  - Implement user authentication
  - Use secure file storage
  - Configure proper server deployment

## Contributing

Feel free to submit issues and enhancement requests! 