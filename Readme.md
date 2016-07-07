# Say What?...Lite
This script listens to ambient audio and pings Slack or Hipchat when the followed name is mentioned.

It sends a transcript of what was said, in reference to the name, to the preferred messaging service (Slack or Hipchat).

Uses IBM's Speech to Text Watson API for the audio-to-text.

The two main differences between this *lite* version and joshnewlan's full proper version is:

1.	I've added a Slack option.
2.	I've removed Splunk and all logging.  When the result comes back from IBM, it goes straight to your messenger.  I removed this because, for me, that added a layer to something that was already kinda slow.  This makes it run just a little bit smoother, but there is no history to reference.  It's a trade-off.

Relies on Uberi's SpeechRecognition PyAudio and API wrapper: https://github.com/Uberi/speech_recognition

##Installation (OS X)

1. Get a [Slack](https://api.slack.com) or [Hipchat](https://www.hipchat.com/docs/apiv2) API token via instructions linked and update applicable variables in say\_what\_lite.py
2. Update ```name``` and choose ```platform``` (either *slack* or *hipchat*) in say\_what\_lite.py
6. [Create an IBM Bluemix account](https://console.ng.bluemix.net/registration/)
7. [Add a speech-to-text plan](https://new-console.ng.bluemix.net/catalog/services/speech-to-text/)
8. Add your credentials to say\_what\_lite.py for ```IBM_USERNAME``` and ```IBM_PASSWORD```
9. [Install Homebrew](http://brew.sh/)
10. ```brew install python```
11. ```brew install portaudio```
12. ```pip install pyaudio```
13. ```pip install SpeechRecognition```
14. ```pip install requests```

##Usage

1. Run say_what.py
