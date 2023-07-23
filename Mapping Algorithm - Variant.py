''' 
### INTRODUCTION & PROSPECT ###
The following code when run on the Source Data set from the video lab or a Super-set of the data set, it will return a mapping 
of the respective files that makes up our Custom test set which has been the outcome of our project. The set as of now, gathers all 
the relevant data that the data dump has, for answering the chosen set of questions in the project. 
 
### VALIDITY ###
If new data is added while holding the same format, this code will also be valid to make an appropriate mapping from the new set with the 
additional data.


'''

import os
import subprocess
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet


# directory = directory of the file, where our sample is sought to be found OR the mapping files are sought
# filters = the parameters to fine tune the mapping [if we want to find our sample file in some unknown file/KG, the paramters are same as the ones in sampling algorithm]
# labels = labels defining the mapped files, representing knowledge bases

def generate_file_table(directory, filters, labels):
    table = []
    counter = {}  # Counter for each filter
    index = 1  # Index for enumerating files
    for filename in os.listdir(directory):
        if filename.endswith(".ttl"):
            filepath = os.path.join(directory, filename)
            with open(filepath, "r") as file:
                content = file.read()
                matched = False
                for i in range(len(filters)):
                    if filters[i] in content:
                        filter_label = labels[i]
                        counter[filter_label] = counter.get(filter_label, 0) + 1
                        counter_label = f"{filter_label}{counter[filter_label]}"
                        table.append([index, filename, counter_label])
                        matched = True
                        break
                if not matched:
                    continue
                index += 1
    return table

def generate_pdf_report(file_table, output_path):
    # Create a PDF document
    doc = SimpleDocTemplate(output_path, pagesize=letter)

    # Define table data and style
    table_data = [['Index', 'File Name', 'Counter']] + file_table
    table_style = TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#2C3E50")),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor("#FFFFFF")),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor("#ECF0F1")),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor("#34495E")),
    ])

    # Create table and apply style
    table = Table(table_data)
    table.setStyle(table_style)

    # Define document elements
    elements = []

    # Add title
    title_style = getSampleStyleSheet()["Title"]
    title = Paragraph("<b><i><u>Mapping of The Files to Their Respective Device Categories</u></i></b>", title_style)
    elements.append(title)
    elements.append(Paragraph("<br/><br/>", title_style))

    # Add table to elements
    elements.append(table)

    # Build the PDF document
    doc.build(elements)

# Provide the directory path, filters, and labels
# directory_path = "D:\\VU Stuff\\Study stuff\\Thesis\\graphs"    #'graphs' is the source folder with all the video lab data 
directory_path = "D:\\VU Stuff\\Study stuff\\Thesis\\Custom_test_set"
filters = ['saref:hasModel "Zigbee Thermostat"^^xsd:string', 'saref:hasModel "Z-Wave Door/Window Sensor"^^xsd:string', 'saref:hasModel "Z-Wave Radiator Thermostat"^^xsd:string']
labels = ['Zigbee Thermostat', 'Z-Wave Door/Window Sensor', 'Z-Wave Radiator Thermostat']

print('Running...')     #status check

file_table = generate_file_table(directory_path, filters, labels)

# Specify the output path for the PDF document
output_path = "Mappings_to_Custom_Test_Set.pdf"

# Generate the PDF report
generate_pdf_report(file_table, output_path)

print(f"PDF report generated successfully: {output_path}")

# Open the PDF file
subprocess.Popen(["start", output_path], shell=True)

print('Done.')      #status check