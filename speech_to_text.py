import speech_recognition as sr
import text_to_speech

def speech_to_text():
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            text_to_speech.text_to_speech("Listening")

            # 🔥 Faster + better detection
            r.dynamic_energy_threshold = True
            r.pause_threshold = 0.8   # faster response
            r.adjust_for_ambient_noise(source, duration=0.5)

            audio = r.listen(source, timeout=3, phrase_time_limit=4)

            # 🔥 Better recognition for Indian English
            voice_data = r.recognize_google(audio, language='en-IN')

            return voice_data.lower()

    except sr.WaitTimeoutError:
        return ""

    except sr.UnknownValueError:
        text_to_speech.text_to_speech("Please speak clearly")
        return ""

    except sr.RequestError:
        text_to_speech.text_to_speech("Check internet")
        return ""

    except Exception:
        text_to_speech.text_to_speech("Microphone problem")
        return ""