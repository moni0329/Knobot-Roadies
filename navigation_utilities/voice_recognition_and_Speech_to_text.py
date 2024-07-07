import googlemaps
import os
import io
import logging
from google.cloud import speech_v1 as speech
import pyaudio
import wave

# Set the GOOGLE_APPLICATION_CREDENTIALS environment variable
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\Users\hasha\Desktop\project\stt_tts.json"

# Google Maps API Key should be replaced here
GMAPS_API_KEY = 'Google Maps API Key'

# Setup logging
logging.basicConfig(level=logging.DEBUG)

def record_audio():
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 1
    fs = 44100  # Record at 44100 samples per second
    seconds = 5
    filename = "output.wav"

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    logging.info("Recording")

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    try:
        for i in range(0, int(fs / chunk * seconds)):
            data = stream.read(chunk)
            frames.append(data)
    except Exception as e:
        logging.error(f"Error during recording: {e}")
    finally:
        # Stop and close the stream
        stream.stop_stream()
        stream.close()
        # Terminate the PortAudio interface
        p.terminate()

    logging.info("Finished recording")

    # Save the recorded data as a WAV file
    wf = wave.open(filename, "wb")
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b"".join(frames))
    wf.close()

    return filename

def speech_to_text():
    client = speech.SpeechClient()
    filename = record_audio()

    with io.open(filename, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=44100,
        language_code="en-LK",  
    )

    try:
        response = client.recognize(config=config, audio=audio)
        for result in response.results:
            transcript = result.alternatives[0].transcript
            logging.info(f"Transcript: {transcript}")
            return transcript
    except Exception as e:
        logging.error(f"Error during speech-to-text: {e}")
        return None

def find_place_on_maps(place):
    gmaps = googlemaps.Client(key=GMAPS_API_KEY)
    geocode_result = gmaps.geocode(place, region='LK')  

    if geocode_result:
        location = geocode_result[0]['geometry']['location']
        logging.info(f"Found place: {geocode_result[0]['formatted_address']}")
        logging.info(f"Latitude: {location['lat']}, Longitude: {location['lng']}")
        return geocode_result[0]['formatted_address'], location
    else:
        logging.info("Place not found")
        return None, None

if __name__ == "__main__":
    spoken_text = speech_to_text()
    if spoken_text:
        address, location = find_place_on_maps(spoken_text)
        if address:
            print(f"Found place: {address}")
            print(f"Latitude: {location['lat']}, Longitude: {location['lng']}")
        else:
            print("Place not found")
    else:
        print("No speech detected")
