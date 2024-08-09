import os
import random
import xml.etree.ElementTree as ET

# Define the directory containing the XML files
xml_directory = 'C:/Users/GabrielL/Downloads/1/'
# Define the output file
output_file = 'C:/Users/GabrielL/Downloads/1/output.txt'

# Initialize the header for the output file
header = """data_

loop_
_rlnCoordinateX #1
_rlnCoordinateY #2
_rlnCoordinateZ #3
_rlnAngleRot #4
_rlnAngleTilt #5
_rlnAnglePsi #6
_rlnTomoName #7
_rlnObjectNumber #8
"""

# Function to extract data from XML files
def extract_data_from_xml(xml_file, tomo_name):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    
    data_lines = []
    for obj in root.findall('object'):
        x = float(obj.get('x')) * 8  # Multiply x by 8
        y = float(obj.get('y')) * 8  # Multiply y by 8
        z = float(obj.get('z')) * 8  # Multiply z by 8
        # Generate random angles between 0 and 360
        angle_rot = f"{random.uniform(0, 360):.6f}"
        angle_tilt = f"{random.uniform(0, 360):.6f}"
        angle_psi = f"{random.uniform(0, 360):.6f}"
        object_number = obj.get('class_label')
        
        data_lines.append(f"{x}\t{y}\t{z}\t{angle_rot}\t{angle_tilt}\t{angle_psi}\t{tomo_name}\t{object_number}")
    
    return data_lines

# Process each XML file
for xml_file in os.listdir(xml_directory):
    if xml_file.endswith('.xml'):
        xml_path = os.path.join(xml_directory, xml_file)
        # Extract the file name without the extension for tomo_name and output file name
        tomo_name = os.path.splitext(os.path.basename(xml_file))[0]
        data_lines = extract_data_from_xml(xml_path, tomo_name)
        
        # Define the output file name with .star extension
        output_file = os.path.join(xml_directory, f"{tomo_name}.star")
        
        # Write the collected data to the output file in .star format
        with open(output_file, 'w') as file:
            file.write(header)
            file.write('\n'.join(data_lines))

print("Data written to .star files.")

#### Remove any existing .star files in the directory
#for file in os.listdir(xml_directory):
#    if file.endswith('.star'):
#        os.remove(os.path.join(xml_directory, file))