from PIL import Image
import pandas as pd 
import streamlit as st
from recognition import detect_faces_local_file
from utils import save_file_to_local, show_ad, get_table_download_link

attributes = ['Gender', 'Smile', 'Eyeglasses', 'Emotions']
selection = []

st.image('./logos/Adxtinct-logos_white_banner.png')
st.write('Welcome to Adxtinct. Customize Ads for your target group!')

st.write('### 1. Upload Image')
uploaded_file = st.file_uploader(
    label = '',
    type=['png', 'jpg'])

if uploaded_file is not None:
    st.image(uploaded_file)
    # save_photo_to_s3(uploaded_file)
    save_file_to_local(uploaded_file)

# if uploaded_file is not None:
#     st.image(uploaded_file)
#     image = Image.open(uploaded_file)

st.write('### 2. Choose Labels')
left, right = st.columns(2)

for idx, attribute in enumerate(attributes): 
    if idx > 1:
        check = right.checkbox(attribute)
    else:
        check = left.checkbox(attribute)
    
    if check:
        selection.append(attribute)

st.write('### 3. Get Labels')
button = st.button('Let the magic happen!')
if button:
    labels = detect_faces_local_file('./TestImages/' + uploaded_file.name, selection, verbose=False)

st.write('### 4. Export Data')
if uploaded_file is not None and button:

    df = pd.DataFrame(data=labels.items(), columns=['Label', 'Value'])
    df

    st.markdown(get_table_download_link(df), unsafe_allow_html=True)

st.write('### 5. Target Ad')
st.write('Your targeted ad could look like this!')

if uploaded_file is not None and button:
    st.image(show_ad(
        age_range=labels['Mean_Age'],
        gender = labels['Gender']
    ))

st.write('### 6. Share Love')
st.write('Check out our [Website](https://kozaronek.wixsite.com/website) to read up on our vision.')
