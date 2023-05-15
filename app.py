from youtube_transcript_api import YouTubeTranscriptApi
import openai

# Set up OpenAI API credentials
openai.api_key = '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'

# Specify the video ID or URL
video_id = "8musxkEil6w"

# Retrieve the transcript for the video
transcript = YouTubeTranscriptApi.get_transcript(video_id)

# Extract the text from the transcript
text = ""
for line in transcript:
    text += line['text'] + " "

# Generate the optimized blog post using OpenAI's API
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt="Make this in the form of an Seo Blog Post" + text,
    temperature=0.7,
    max_tokens=500,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=None,
)

# Extract the generated blog post
blog_post = response.choices[0].text.strip()

# Save the blog post to a file
output_file = "blog_post.txt"
with open(output_file, "w") as file:
    file.write(blog_post)

# Print the success message
print("Blog post generated and saved to", output_file)
