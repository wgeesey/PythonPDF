##### PDFs ######

####################### Merging PDFs ######################
import PyPDF2
import sys

# Collect PDF file paths from the command line arguments
inputs = sys.argv[1:]
print(inputs)  # Print the list of input files for debugging

# Define a function to merge multiple PDFs into a single file
def pdf_combiner(pdf_list):
    # Create a PdfWriter object to hold the merged content
    pdf_writer = PyPDF2.PdfWriter()
    
    # Iterate through each PDF file in the list
    for pdf in pdf_list:
        print(f'Processing {pdf}')  # Print the current PDF being processed
        reader = PyPDF2.PdfReader(pdf)  # Read the current PDF
        # Loop through each page in the current PDF
        for page in reader.pages:
            pdf_writer.add_page(page)  # Add each page to the writer object
    
    # Write the merged content to a new PDF file ('merged.pdf')
    with open('merged.pdf', 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

# Call the pdf_combiner function with the input PDF files
pdf_combiner(inputs)

# After merging, open the merged PDF to extract and print its text content
with open('merged.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)  # Read the merged PDF
    # Loop through each page in the merged PDF
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]  # Get the current page
        text = page.extract_text()  # Extract text from the current page
        # Print the extracted text from each page
        print(f'Page {page_num + 1} contents:\n {text}\n')


####################### Watermarking ######################
import PyPDF2

# Open the merged PDF and the watermark PDF
with open('merged.pdf', 'rb') as main_pdf, open('wtr.pdf', 'rb') as watermark_pdf:
    reader = PyPDF2.PdfReader(main_pdf)  # Read the main (merged) PDF
    watermark_reader = PyPDF2.PdfReader(watermark_pdf)  # Read the watermark PDF

    # Create a PdfWriter object to write the watermarked content
    writer = PyPDF2.PdfWriter()
    # Get the first page from the watermark PDF (assumed to be the watermark page)
    watermark_page = watermark_reader.pages[0]

    # Loop through each page in the merged PDF
    for page in reader.pages:
        # Apply the watermark page to the current page
        page.merge_page(watermark_page)
        # Add the watermarked page to the writer object
        writer.add_page(page)

    # Write the watermarked PDF to a new file ('watermarked.pdf')
    with open('watermarked.pdf', 'wb') as output_pdf:
        writer.write(output_pdf)


####################### To Open a PDF and Read Its Contents ######################

# Example: Reading and extracting text from a different PDF file ('dummy.pdf')
with open('dummy.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)  # Read the 'dummy.pdf' file
    print(len(reader.pages))  # Print the number of pages in the PDF

    # Loop through each page in the PDF
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]  # Get the current page
        text = page.extract_text()  # Extract the text from the current page

        # Print the extracted text from the page
        print(f'Page {page_num + 1} content:\n {text}\n')
