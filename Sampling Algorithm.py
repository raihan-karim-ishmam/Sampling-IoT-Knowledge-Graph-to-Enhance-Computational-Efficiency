''' 
### INTRODUCTION & PROSPECT ###
The following code when run on the Source KG build on SAREF ontolgy and inhibtting the limitations mentioned in the paper,
it will sample a reduced Knolwedge graph with the data sought for using the parameeters. The filters in the algorithm implemented below,
sampled the KG containing all te relevant data for answering the chosen set of questions in the project. 
 
### VALIDITY ###
If new data is added while holding the same format, this code will also be valid to make an appropriate mapping from the new set with the 
additional data.


'''

import os
import shutil

# Funtion for the algoruithm 
# directory = directory of the source KG
# realtions = the parameters, also called the semantic based filters, to fine tune the sampling
# target-directory =  this is where our sampled KG will be found

def filter_files_with_relations(directory, relations, target_directory):
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    for filename in os.listdir(directory):
        if filename.endswith(".ttl"):   # Locating our source KG
            filepath = os.path.join(directory, filename)
            with open(filepath, "r") as file:
                content = file.read()
                if any(relation in content for relation in relations):
                    target_filepath = os.path.join(target_directory, filename)
                    shutil.copy2(filepath, target_filepath)
                    print(f"File '{filename}' copied to target directory.")
                    

# Provide the directory path, desired relations, and the target directory
directory_path = "D:\\VU Stuff\\Study stuff\\Thesis\\graphs"
desired_relations = ['saref:hasModel "Z-Wave Door/Window Sensor"^^xsd:string',
                     'saref:hasModel "Zigbee Thermostat"^^xsd:string',
                     'saref:hasModel "Z-Wave Radiator Thermostat"^^xsd:string']
target_directory = "D:\\VU Stuff\\Study stuff\\Thesis\\test xx"


print('running')    # Status 
filter_files_with_relations(directory_path, desired_relations, target_directory)    # Sampling the KG
print('done')       # Status update
 


