from flask import Flask
from youtube_transcript_api import YouTubeTranscriptApi
import datetime

# define a variable to hold you app
app = Flask(__name__)

# define your resource endpoints
app.route('/')
def index_page():
    return "Hello world"

app.route('/time', methods=['GET'])
def get_time():
    return str(datetime.datetime.now())


def get_trascription(video_ids):
    transcript_object = YouTubeTranscriptApi.get_transcripts(video_ids, languages=['en', 'de'])
    transcripts = []
 #   print(transcript_object)
    for i in transcript_object[0][video_ids[0]]:
        transcripts.append(i["text"])
    return " ".join(transcripts)

# server the app when this file is run
if __name__ == '__main__':
    original_text  = get_trascription(["9QloiDcR-0U"])[:1000]
    from transformers import pipeline
    print("Model Loading Start")
    summarization = pipeline("summarization")
    print("Model Loading Done")
    print("Running inference")
    summary_text = summarization(original_text)
    print("Summary:", summary_text)
    app.run()
