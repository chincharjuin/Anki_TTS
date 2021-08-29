import azure.cognitiveservices.speech as speechsdk
import xml.etree.ElementTree as ET

#with open("text.txt", "r") as text_file:
#    text = text_file.read()

#tree = ET.parse('ssml.xml')
#root = tree.getroot()
#root[0][0].text = text
#tree.write('ssml.xml')

speech_key, service_region = "c6f976d4776f4835a2c71134b78a523d", "southeastasia"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

speech_config.set_speech_synthesis_output_format(speechsdk.SpeechSynthesisOutputFormat["Audio24Khz48KBitRateMonoMp3"])

synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=None)
ssml_string = open("ssml.xml", "r", encoding="utf8").read()
result = synthesizer.speak_ssml_async(ssml_string).get()
stream = speechsdk.AudioDataStream(result)
stream.save_to_wav_file("result.mp3")
print("Speech Synthesized.")