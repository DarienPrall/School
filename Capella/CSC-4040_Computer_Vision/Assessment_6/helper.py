import os

dataset_1_filepath = ('/Users/darienprall/Downloads/resources-nn_dataset_1')
dataset_2_filepath = ('/Users/darienprall/Downloads/resources-nn_dataset_2')
counter = 1

for file in os.listdir(dataset_2_filepath):

    if file:
        print(f"File {counter}) {file}")
        counter += 1

