#install the below dependencies
pip !pip install pdfplumber pandas




import pdfplumber
import pandas as pd

# Function to extract data from a password-protected PDF and convert to CSV
def pdf_to_csv(pdf_file, csv_file, password):
    data = []

    # Open the PDF file with the provided password
    with pdfplumber.open(pdf_file, password=password) as pdf:
        for page in pdf.pages:
            # Extract text from the page
            text = page.extract_text()
            if text:
                # Split the text into lines
                lines = text.split('\n')
                for line in lines:
                    # Assuming the data is separated by spaces or tabs
                    # You may need to adjust this based on your PDF structure
                    data.append(line.split())

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Save DataFrame to CSV
    df.to_csv(csv_file, index=False, header=False)

# Usage
pdf_file_path = 'path/to/your/mpesa_statement.pdf'  # Replace with your PDF file path
csv_file_path = 'path/to/your/mpesa_statement.csv'  # Replace with your desired CSV file path
pdf_password = 'your_password_here'  # Replace with your PDF password

pdf_to_csv(pdf_file_path, csv_file_path, pdf_password)

print("PDF data has been extracted to CSV successfully.")
