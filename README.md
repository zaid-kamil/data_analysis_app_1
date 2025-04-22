### README for Data Analysis App

# Data Analysis Application

This repository contains a data analysis application built using **Streamlit**. The app enables users to visualize and explore data from a dataset of job roles, salaries, and related information.

---

## Dataset Overview

The dataset (`datasets/data.csv`) provides insights into job roles, salaries, and company-related data. It includes the following fields:

- **work_year**: Year of the data (e.g., 2023).
- **experience_level**: Level of experience (e.g., Entry-level, Mid-level, Senior-level, Expert-level).
- **employment_type**: Type of employment (e.g., Full-time, Part-time, Contract).
- **job_title**: Job roles (e.g., Data Scientist, Data Engineer, Machine Learning Engineer).
- **salary**: Gross salary in the original currency.
- **salary_currency**: Currency of the salary.
- **salary_in_usd**: Salary converted to USD.
- **company_location**: Location of the company.
- **company_size**: Size of the company (e.g., Small, Medium, Large).

---

## Features of the App

### 1. **Data Exploration**
   - View the uploaded dataset in a tabular format.
   - Display a quick summary of the dataset fields.

### 2. **Data Visualization**
   - **Bar Charts**: Analyze the top job titles, salary trends, and distributions.
   - **Pie Charts**: Visualize categorical data (e.g., experience levels, company sizes).
   - **Box Plots**: Explore salary distributions by category.
   - **Sunburst & Treemap**: Hierarchical visualizations based on selected columns.

### 3. **Interactive Customizations**
   - Upload your own dataset to analyze.
   - Select specific categories to focus on for visualizations.
   - Choose from different graph types (e.g., bar, pie, violin).

---

## How to Use

### Prerequisites:
1. Install Python 3.8+.
2. Ensure you have the following Python libraries installed:
   - `streamlit`
   - `pandas`
   - `numpy`
   - `plotly`

### Run the App:
1. Clone the repository:
   ```bash
   git clone https://github.com/zaid-kamil/data_analysis_app_1.git
   ```
2. Navigate to the project directory:
   ```bash
   cd data_analysis_app_1
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run main.py
   ```

### Upload Dataset:
- The app provides an option to upload your own CSV file for analysis.
- Ensure the file follows a similar structure to `data.csv`.

---

## Example Visualizations

- **Top Job Titles**: A bar chart displaying the 10 most common job titles.
- **Salary Trends**: Year-over-year salary trends grouped by job title or company location.
- **Experience Levels**: Pie charts showing the distribution of experience levels.

---

## Contributions

We welcome contributions! Feel free to submit issues or pull requests.

---

## License

This project is licensed under the [MIT License](LICENSE).

