# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 12:24:39 2020

@author: rnelson2

Testing the Google Cloud Vision API for OCR
"""


import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "C:/Users/rnelson2/asw/nomadic-zoo-293819-8ccfdaa58681.json"


def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
        
detect_text("comics/0001_myparents.jpg")