from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from playsound import playsound

authenticator = IAMAuthenticator('ts89j5bMBWLYT6VScb2J7JVLEnsM0Bi5yvo1L3pVKSqv')
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)

text_to_speech.set_service_url('https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/229c9936-726f-4a8e-9f6b-9a5b5cebf9a4')

with open('new_file.mp3', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            'Hello all how are you hope every one is doing well good morning hemangini maam ',
            voice='en-US_AllisonV3Voice',
            accept='audio/mp3'        
        ).get_result().content)

playsound('new_file.mp3')
