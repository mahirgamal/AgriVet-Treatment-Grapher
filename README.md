# AgriVet Treatment Grapher

AgriVet Treatment Grapher is a Python-based tool designed to visualise treatment data for animals. It processes JSON data to generate insightful visualisations, helping veterinarians and researchers analyse treatment patterns and dosages.

## Features

- **Treatment Summary**: Bar chart showing the number of animals treated with each type of treatment.
- **Daily Treatment Distribution**: Stacked bar chart displaying the distribution of treatments over time.
- **Treatment Proportions**: Pie chart illustrating the proportion of each treatment type.
- **Dose Statistics**: Bar chart with error bars showing the average, minimum, and maximum doses for each treatment.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/mahirgamal/AgriVet-Treatment-Grapher.git
    cd AgriVet-Treatment-Grapher
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Place your treatment data JSON file in the project directory. Update the `file_path` variable in the script to point to your JSON file.

2. Run the script:
    ```bash
    python agrivet_treatment_grapher.py
    ```

3. The script will generate and display the visualisations.

## Data Processing

The script processes the JSON data to extract relevant information such as treatment names, doses, and dates. It then converts this data into a pandas DataFrame for easy manipulation and analysis. The data is aggregated to create summaries and statistics, which are then visualised using matplotlib.

## Customisation

You can customise the script to fit your specific needs:
- **File Path**: Update the `file_path` variable to point to your JSON file.
- **Visualisation Styles**: Modify the matplotlib settings to change the appearance of the charts.
- **Data Aggregation**: Adjust the data aggregation logic to include additional metrics or different groupings.

## Troubleshooting

If you encounter any issues, consider the following steps:
- Ensure that your JSON file is correctly formatted and matches the expected structure.
- Verify that all required dependencies are installed.
- Check for any error messages in the console and address them accordingly.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgments
We acknowledge that this work originates from the Trakka project and builds on the existing TerraCipher Trakka implementation. We appreciate the support and resources provided by the Trakka project team. Also, we thank Dave Swain and Will Swain from TerraCipher for their guidance and assistance throughout this project.


## License
This project is licensed under Apache License 2.0 - see the [LICENSE][lic] file for details.

## Contact
If you have any questions, suggestions or need assistance, please don't hesitate to contact us at mhabib@csu.edu.au, akabir@csu.edu.au.

[//]: #
  [lic]: <https://github.com/mahirgamal/AgriVet-Treatment-Grapher/blob/main/LICENSE>
