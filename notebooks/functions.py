import pandas as pd
import numpy as np

def extract_data(xml_root_element):

    """ Function to extract the data from the first tag of the XML file string, contained in the main root (Response). It returns a dictionary 
    having the tags (attribute .tag) of the child elements (for example "donor age" in <donor--age>25 yrs</donor--age>) as keys and 
    the text content (attribute .text) as value ("25 yrs" in <donor--age>25 yrs</donor--age>). 
    -> This function can be executed inside the create_dataframe() function of function.py"""
    
    data = {}
    for child in xml_root_element:
        data[child.tag] = child.text
    return data  

def create_dataframe(root, first_tag:str):
    """ The function creates a dataframe from XLM files from which the data were extracted with extract_data() function.
    As argument it takes the first tag (string) within the root that incorporates all the elements associated"""
    df_rows = []
    for x in root.findall(first_tag):
        df_rows.append(extract_data(x))

    df = pd.DataFrame(df_rows)

    return df

def drop_col(df):
    """The functon drops any column containing all null values and specific columns not needed for the analysis"""
    df.dropna(how="all", axis = 1, inplace = True)
    df.drop(["Unnamed: 0", "donor--id", "donor--name", "donor--race", "donor--species", "threshold-i-long-square", 
             "fast-trough-v-long-square", "peak-t-ramp", "tau", "upstroke-downstroke-ratio-long-square", 
             "ephys-inst-thresh-thumb-path", "ephys-thumb-path", "erwkf--id", "m--biophys-perisomatic",
             "m--glif", "nr--max-euclidean-distance", "nr--average-contraction", 
             "nr--average-parent-daughter-ratio", "nr--number-stems", "specimen--hemisphere",
             "specimen--id", "specimen--name", "structure--acronym", "structure-parent--acronym", 
             "structure-parent--id", "tag--apical", "donor--years-of-seizure-history", "si--path",
             "si--height", "nrwkf--id", "si--width", "m--biophys-all-active", "morph-thumb-path", "nr--reconstruction-type",
            "m--biophys", "m--biophys-all-active"], axis = 1, inplace = True)
    return df   

def rename_ef(df):
    """Function that renames the column starting with ef-- (=electrophysiology), by removing ef--"""
    
    df.columns = [x.replace("ef--", "") if x.startswith("ef--") else x for x in df.columns]

    return df

def round_col(df):

    """The function rounds to 2 decimals the vlaues in columns 'vrest', 'avg-isi' and 'ri', 
    and to 3 decimals the values in the column 'adaptation' """
    
    df["adaptation"] = df["adaptation"].apply(lambda x: round(x, 3))
    df["vrest"] = df["vrest"].apply(lambda x: round(x, 2))
    df["avg-isi"] = df["avg-isi"].apply(lambda x: round(x, 2))
    df["ri"] = df["ri"].apply(lambda x: round(x, 2))

    return df

def n_age(df):
    """ Function to format age. Age data are strings in the format of "n yrs" (string), 
    thus the function removes "yrs" and converts the numbers to integers. 
    The function handles NaN values and leaves them as they are, if present"""
    
    df["donor--age"] = df["donor--age"].str.replace(" yrs", "")
    #df["donor--age"] = [int(x) if pd.notnull(x) else np.nan for x in df["donor--age"]]
    df["donor--age"] = df["donor--age"].apply(lambda x: int(x) if pd.notnull(x) else np.nan)

    return df

def age_category(age):
    """Functions that creates age categories. 
    It returns different categories of age, so can be applied to the column "donor--age" 
    and to create a new column where each donor has an assignedage category"""

    if isinstance(age, int):
        if 18 <= age <= 24:
            return "18-24 years"
        elif 25 <= age <= 30:
            return "25-30 years"
        elif 31 <= age <= 40:
            return "31-40 years"
        elif 41 <= age <= 50 :
            return "41-50 years"
        elif 51 <= age <= 65:
            return "51-65 years"
        elif 66 <= age <= 83:
            return "66-83 years"
        else:
            return np.nan
    else:
        return np.nan

def format_firing(df):
    """ Function that converts the firing rates object in floats with two decimals. 
    It handles NaN values and leaves them as they are, if present"""
    
    df["avg-firing-rate"] = df["avg-firing-rate"].apply(lambda x: round(float(x), 2) if pd.notnull(x) else np.nan)

    return df

def format_curve_slope(df):
    """ Function that converts values of f-i curve slope from strings to floats with 3 decimals.
    It handles NaN values and leaves them as they are, if present"""
    
    df["f-i-curve-slope"] = df["f-i-curve-slope"].apply(lambda x: round(float(x), 3) if pd.notnull(x) else np.nan)

    return df

def categorize_regions(df):

    """ Function to group different subregions in the correspondent lobes. """
    
    mapping = {'"frontal lobe"' : 'frontal lobe',
               '"middle temporal gyrus"' : 'temporal lobe',
               '"temporal lobe"': 'temporal lobe',
               '"middle frontal gyrus"' : 'frontal lobe',
               '"planum polare"' : 'planum polare',
               '"angular gyrus"' : 'angular gyrus',
               '"superior frontal gyrus"': 'frontal lobe',
               '"inferior temporal gyrus"' : 'temporal lobe',
               '"inferior frontal gyrus"' : 'frontal lobe'}
    
    df["structure--name"] = df["structure--name"].replace(mapping)

    return df

