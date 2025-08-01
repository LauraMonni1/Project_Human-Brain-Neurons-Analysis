# 🧠 Human Neuronal Cell Types – Electrophysiology & Morphology Analysis

This project analyzes publicly available data on human brain cell types, focusing on neurons obtained from **tumor** and **epilepsy** patients. The goal is to investigate potential differences in **neuronal firing activity** and **morphological properties** across these clinical conditions.

## Dataset

- Source: Allen Brain Institute – Cell Types Database API  
- Data type: Electrophysiological & morphological characteristics of human neurons  
- Filters applied:  
  - Species: `Homo sapiens`  
  - Disease state: `"epilepsy"` and `"healthy/tumor"`

Dataset was queried and extracted using XML-based RMA queries through the Allen Brain Cell Types API.  
API Documentation: [Allen Institute API](https://community.brain-map.org/t/cell-types-database-api/3016)

## Project Structure

.
├── data/
│ ├── raw_data.csv # Raw extracted dataset
│ └── cleaned_data.csv # Cleaned and formatted dataset
├── functions.py # Custom functions for API querying and preprocessing
├── project_notebook.ipynb # Full EDA, visualization, and analysis
└── README.md

## Tools & Libraries

- Python (pandas, NumPy, requests, xml.etree.ElementTree)
- Data visualization: matplotlib, seaborn
- API requests: requests + XML parsing
- Custom reusable pipeline via `functions.py`

## 📈 Data Pipeline Summary

1. **Data Extraction:**
   - Define API endpoint and RMA query criteria
   - Send `GET` request with parameters
   - Parse the XML response using `ElementTree`
   - Extract relevant fields into a pandas DataFrame

2. **Data Cleaning:**
   - Handle missing values and standardize units
   - Normalize key morphological and electrophysiological features
   - Store cleaned data in `data/cleaned_data.csv`

3. **Exploratory Data Analysis:**
   - Compare spike firing activity between disease states
   - Visualize morphological differences with violin plots, histograms, and scatter plots


## Key Insights

- Neurons from epilepsy patients show higher spike frequency adaptation
- Subtle but consistent differences in soma size and dendritic branching

## Presentation

Project presentation (Canva):  
🔗 [View Slides](https://www.canva.com/design/DAF-0n2KWTc/1AI-sS16rVwdij_CBGHyGQ/edit)

