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
