# Triangulation of Rectangular Mesh

This Python script generates a triangular mesh for a rectangular area with specified dimensions. It calculates the area of each triangle in the mesh and saves the data to a JSON file. Additionally, it provides the flexibility to set the number of elements separately in the x and y directions.

## Prerequisites

Before running the script, ensure that you have Python installed on your system.

## Setup

1. Clone this repository or download the script file.

2. Open a terminal or command prompt and navigate to the directory where the script is located.

3. Create a virtual environment (venv) for this project. Run the following commands:

   ```shell
   python -m venv .venv  # Create a virtual environment
   source .venv/bin/activate  # Activate the virtual environment (Linux/Mac)
   # Or, on Windows:
   venv\Scripts\Activate```

4. Install requirements.txt
    ```shell
    pip install requirements.txt```

## Usage

1. With the virtual environment activated (as shown in the Setup section), run the script for Task1 using the following command:
```shell
cd task1
python task1.py
```

1. The script will prompt you to enter the new number of x and y elements, separated by a comma. For example, you can enter 5,5 to create a 5x5 mesh.

2. The script will display a plot of the triangular mesh.

3. The data, including triangle vertices, triangle areas, and the current date and time, will be saved to a JSON file named triangulation.json in the same directory.

4. To exit the script, simply enter 'q' when prompted to enter the number of elements.
