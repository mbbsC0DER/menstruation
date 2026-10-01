


from gtts import gTTS

from IPython.display import Audio, display

# Text to be converted into speech

text = "Hello, this is a simple text to speech example."

# Convert text to speech

tts = gTTS(text)

# Save the audio file

tts.save("output_speech.mp3")

# Play the generated speech (optional, only in Colab or Jupyter)

display(Audio("output_speech.mp3"))
