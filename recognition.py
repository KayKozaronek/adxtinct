import boto3
import streamlit as st

def detect_faces_local_file(photo, selection, verbose=False):

    client=boto3.client('rekognition')

    with open(photo, 'rb') as image:
        response = client.detect_faces(
            Image={
                'Bytes': image.read()
                },
            Attributes=['ALL'])

    for faceDetail in response['FaceDetails']:
        labels = dict()
        mean_age = str((float(faceDetail['AgeRange']['Low']) + float(faceDetail['AgeRange']['High'])) /2 )
        
        labels['Mean_Age'] = mean_age
        # Access predictions for individual face details and st.write them
        if verbose:
            st.write('The detected face is between ' + str(faceDetail['AgeRange']['Low']) 
                + ' and ' + str(faceDetail['AgeRange']['High']) + ' years old')
        
        for attribute in selection:
            if attribute == 'Emotions':
                attr = str.capitalize(faceDetail['Emotions'][0]['Type'])
                if verbose:
                    st.write("Emotion: " + attr)           
            else:
                attr = str(faceDetail[attribute]['Value'])
                if verbose:
                    st.write(f'{attribute}: ' + attr)
            
            labels[attribute] = attr

    return labels 