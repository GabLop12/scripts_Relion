import glob

# Define the output file name
output_file = 'combined.star'

# Get a list of all the .star files to combine
star_files = glob.glob('TS_*.star')

# Read the header from the first file
with open(star_files[0], 'r') as f:
    header = []
    for line in f:
        header.append(line)
        if line.strip() == '_rlnObjectNumber #8':
            break

# Initialize a list to store all the data rows
all_data = []

# Read data from each .star file
for file in star_files:
    with open(file, 'r') as f:
        data_section = False
        for line in f:
            if data_section:
                all_data.append(line)
            if line.strip() == '_rlnObjectNumber #8':
                data_section = True

# Write the header and all the combined data to the output file
with open(output_file, 'w') as f:
    f.writelines(header)
    f.writelines(all_data)

print(f"Combined file saved as {output_file}")
