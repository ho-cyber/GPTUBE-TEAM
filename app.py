from flask import Flask, render_template, request
from youtube_transcript_api import YouTubeTranscriptApi
import openai

app = Flask(__name__)

# Set up OpenAI API credentials
openai.api_key = 'API_KEY HERE'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the YouTube video ID from the form
        video_id = request.form['video_id']
        
        # Retrieve the transcript for the video
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        
        # Extract the text from the transcript
        text = ""
        for line in transcript:
            text += line['text'] + " "
        
        # Generate the optimized blog post using OpenAI's API
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt="Make this in the form of an SEO blog post also make it intuitive and captivating" + text,
            temperature=0.9,
            max_tokens=500,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=None,
        )
        
        # Extract the generated blog post
        blog_post = response.choices[0].text.strip()
        
        return render_template('index.html', blog_post=blog_post)
    
    return render_template('index.html', blog_post='')

if __name__ == '__main__':
    app.run(debug=True)
