import json
from os.path import join, dirname
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('izKXL1fCRj2lTqS5RaxzuTETZwMK1yKGFaL1pgENE1Z8')
speech_to_text = SpeechToTextV1(
    authenticator=authenticator
)

speech_to_text.set_service_url('https://api.eu-gb.speech-to-text.watson.cloud.ibm.com/instances/179661be-e3fe-4209-bf77-46df2ba958ab')

with open(join(dirname(__file__), './.', 'new_file.mp3'),'rb') as audio_file:
    speech_recognition_results = speech_to_text.recognize(
        audio=audio_file,
        content_type='audio/mp3',
        
    ).get_result()
print(json.dumps(speech_recognition_results, indent=2))