import os 
import boto3 
import numpy as np
import pandas as pd
import base64
import random 

def save_photo_to_s3(uploaded_file):
    s3 = boto3.resource('s3', region_name='us-east-1')
    file_name = uploaded_file.name
    bucket = 'adxtinct-test'
    S3Name = "streamlit-" + file_name
    s3.meta.client.upload_file(f'./TestImages/{file_name}',
                                bucket, S3Name)

def save_file_to_local(uploaded_file):
    path = os.path.join("TestImages", uploaded_file.name)
    with open((path), "wb") as f:
        f.write(uploaded_file.getbuffer())

def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=True)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}">Download csv file</a>'
    return href 
    

def get_dummy_labels():
    if np.random.randint(low=0, high=2, size=1) == 0:
        df = pd.DataFrame(
            {'ID': [1,2,3],
            'Tag':['#Couple', '#Beach','#AdventureTime']})
        df
        
    else:
        df = pd.DataFrame(
            {'Tag':['height', 'age', 'sex', 'style'],
            'Value':['1.90 cm', '24','male','leisure']})
        df 

def show_ad(age_range, gender):
    
    # age_dict = {0:'0-2',
    # 1:'3-9',
    # 2:'10-19',
    # 3:'20-29',
    # 4:'30-39',
    # 5:'40-49',
    # 6:'50-59',
    # 7:'60-69',
    # 8:'70-79',
    # 9:'80-89',
    # }

    if gender == 'Female':
        if age_range == '0-2' or age_range == '3-9':
            return './ads/female0-9_babysale.png'
        elif age_range == '10-19':
            return './ads/female10-19_salad.png'
        elif age_range == '20-29':
            return './ads/female20-29_bfsale.png'
        elif age_range == '30-39':
            return './ads/female30-39_fragnance.png'
        elif age_range == '40-49':
            return './ads/female40-49_yoga.png'
        else:   
            return './ads/female50+_travel.png'
    elif gender == 'Male':
        if age_range == '0-2' or age_range == '3-9':
            return './ads/male0-9_babysale.png'
        elif age_range == '10-19':
            return './ads/male10-19_chicken.png'
        elif age_range == '20-29':
            return './ads/male20-29_bfsale.png'
        elif age_range == '30-39':
            return './ads/male30-39_wine.png'
        elif age_range == '40-49':
            return './ads/male40-49_denim.png'
        else:   
            return './ads/male50+_retirement.png'    
    