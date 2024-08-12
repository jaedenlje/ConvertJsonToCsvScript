
# Convert JSON to CSV Script
## Description
This project provides a script to process JSON annotations downloaded from BasicAI (an image annotation platform) and converts them into a structured CSV format. The script extracts relevant annotation information such as class names, shape types, occlusion levels, orientations, and bounding box coordinates from the JSON files.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Installation
Install [PyCharm Community Edition](https://www.jetbrains.com/pycharm/download/?section=windows)


1. Create a new project:

![Screenshot (5)](https://github.com/user-attachments/assets/505ebcc0-a23f-41de-8e75-bd82759452ce)


2. Open settings and select "Python Intepreter" under your project. Click on the '+' sign and search for "opencv-python" to install the OpenCV package:

![Screenshot (2)](https://github.com/user-attachments/assets/1bc46e42-2b96-404d-8a32-f3347c3db87d)
![Screenshot (6)](https://github.com/user-attachments/assets/a913794f-e252-47f4-84ee-5599aa880fb0)
![Screenshot (7)](https://github.com/user-attachments/assets/18c56eba-8351-470a-b263-fdf4a6077608)

3. Create a new Python file:

![Screenshot (4)](https://github.com/user-attachments/assets/7344ef74-ca51-4d8e-be36-91933edf2906)

## Usage
To use the script, you need to provide the path to the folder containing JSON annotation files and the output path for the CSV file.

    1. Update the input_folder_path and output_csv_path variables in the script with the appropriate paths.
    2. Run the script:

### Example
Here is an example of how to use the script:

    import os
    import json
    import csv


    def process_json_annotations(input_folder_path, output_csv_path):
        # Initialize the CSV writer
        with open(output_csv_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)

            # Write the header row
            writer.writerow(['Image Filename', 'Class Name', 'Shape Type', 'Occlusion Level', 'Orientation', 'XMin', 'YMin', 'XMax', 'YMax'])

            # Iterate through all files in the input folder
            for filename in os.listdir(input_folder_path):
                if filename.endswith(".json"):
                    # Extract the image filename by replacing ".json" with ".jpg"
                    image_filename = filename.replace(".json", ".jpg")

                    # Open the JSON file
                    with open(os.path.join(input_folder_path, filename), 'r') as json_file:
                        annotation = json.load(json_file)

                        # Find the dictionary that contains the 'sourceName' key
                        for item in annotation:
                            if 'sourceName' in item:
                                # Extract the class name and bbox coordinates for each instance
                                for instance in item['instances']:
                                    class_name = instance['className']
                                    xmin = instance['contour']['points'][0]['x']
                                    ymin = instance['contour']['points'][0]['y']
                                    xmax = instance['contour']['points'][2]['x']
                                    ymax = instance['contour']['points'][2]['y']

                                    for class_value in instance["classValues"]:
                                        if class_value["name"] == "Shape Type":
                                            shape_type = class_value["value"]
                                        elif class_value["name"] == "Occlusion Level":
                                            occlusion_level = class_value["value"]
                                        elif class_value["name"] == "Orientation":
                                            orientation = class_value["value"]


                                    # Write the data to the CSV file
                                    writer.writerow([image_filename, class_name, shape_type, occlusion_level, orientation,  xmin, ymin, xmax, ymax])


    # Example usage
    input_folder_path = "/path/to/your/json/files"
    output_csv_path = "/path/to/your/csv/file"
    process_json_annotations(input_folder_path, output_csv_path)

## License
This project is licensed under the [MIT License](https://www.mit.edu/~amini/LICENSE.md).



