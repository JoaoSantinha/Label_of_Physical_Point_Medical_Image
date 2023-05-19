# Import the library
import csv
import numpy as np
import SimpleITK as sitk
import argparse

# Create the parser
parser = argparse.ArgumentParser()

# Add an argument
parser.add_argument('--csv', type=str, required=True)
parser.add_argument('--segmentation', type=str, required=True)
parser.add_argument('--output', type=str, required=True)
parser.add_argument('--label', type=int, required=True)

# Parse the argument
args = parser.parse_args()

csv_filename = args.csv
segmentation_filename = args.segmentation
output_filename = args.output

# read segmentation file
seg_image = sitk.ReadImage(segmentation_filename)
# create empty list for labels 
list_label = []

# reads input file with physical world coordinates from scanner and iterates over different coordinates
with open(csv_filename, newline='') as csvfile:
    cvs_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in cvs_reader:
        # get x, y, z indeces of matrix from physical world coordinates
        coordinates_index = seg_image.TransformPhysicalPointToIndex(np.asarray([float(row[0]), float(row[1]), float(row[2])]))
        
        # args.label == -1 -> list_label will contain the labels; otherwise returns whether the coordinates belong to provided label
        if args.label == -1:
            list_label.append([seg_image.GetPixel(coordinates_index)])
        elif seg_image.GetPixel(coordinates_index) == args.label:
            list_label.append([1])
        else:
            list_label.append([0])
        
# now write the list of labels into output
with open(output_filename, 'w') as f:
    write = csv.writer(f)
    write.writerows(list_label)

