import speech_recognition as sr
import time
import json
import requests
import thread
import subprocess

# API credentials.  IBM is required but you can enter either Slack or Hipchat credentials.
IBM_USERNAME = ""
IBM_PASSWORD = ""
SLACK_TOKEN = ""
SLACK_CHANNEL = ""
HIPCHAT_URL = ""
HIPCHAT_TOKEN = ""
HIPCHAT_USER_ID = ""

# You name and platform of choice!
name = ""
# Please choose either slack or hipchat
platform = ""

def translate(audio,r):
    # The translated output from IBM's Watson speech-to-text api
    # The r param is an instance of SpeechRecognition

    results = {}
    text = False
    try:
        text = r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD)
        print("Results:" + text)
    except sr.UnknownValueError:
        # print("IBM Speech to Text could not understand audio")
        pass
    except sr.RequestError as e:
        print("Could not request results from IBM Speech to Text service; {0}".format(e))

    if text:
        if name.lower() in text.lower():
            results['text'] = text

    return results


def consumer(audio,r):
    # Received audio, now transcribe it and send to Slack or Hipchat
    results = translate(audio,r)
    if 'text' in results:
        if platform.lower() == "slack":
            requests.post('https://slack.com/api/chat.postMessage?token={}&channel={}&text={}&pretty=1'.format(SLACK_TOKEN,SLACK_CHANNEL,results['text']))
        if platform.lower() == "hipchat":
            data = {
                'message': results['text'],
                'notify': True,
                'message_format': 'text'
            }

            r = requests.post('{}/v2/user/{}/message'.format(HIPCHAT_URL, HIPCHAT_USER_ID),
                data=json.dumps(data),
                headers = {
                    'content-type': 'application/json',
                    "Authorization": "Bearer {}".format(HIPCHAT_TOKEN)
                    }
                )
    else:
        print "[--Silence--]"


def main():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
            thread.start_new_thread(consumer,(audio,r))

if __name__ == '__main__':
    main()
