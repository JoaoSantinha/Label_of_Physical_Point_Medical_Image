# Label_of_Physical_Point_Medical_Image
Python script that given a list of physical coordinates and a segmentation mask returns the corresponding labels of those coordinates

### Dependencies
* SimpleITK - can be install using: 

```pip install SimpleITK```

### Examples of usage:
* Check which coordinates correspond to label 2
```python ./model_tissue_id.py --csv <csv_filepath> --segmentation <segmentation_filepath> --output <output_filepath> --label 2```

* Returns corresponding labels of provided coordinates
```python ./model_tissue_id.py --csv <csv_filepath> --segmentation <segmentation_filepath> --output <output_filepath> --label -1```
