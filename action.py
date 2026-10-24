import text_to_speech                                                    # imports ur custom python file and allows you to use functions inside it 
import speech_to_text
import datetime                                                          # imports built-in pyhton module
import webbrowser
import os
import weather
import shutil

def find_folder(folder_name, search_path):
    for root, dirs, files in os.walk(search_path):
        for dir_name in dirs:
            if folder_name.lower() in dir_name.lower():   # partial match
                return os.path.join(root, dir_name)
    return None


def Action(data):
    user_data=data.lower()                                            # calls the function and result is stored in user_data

# 🔥 Keyboard shortcuts for fast commands
    shortcuts = {
        "g": "open google",
        "y": "open youtube",
        "m": "play music",
        "t": "time",
        "d": "date",
        "day": "day",
        "w": "weather",
        "q": "quit"
    }

    # if user typed shortcut → convert to full command
    if user_data in shortcuts:
            user_data = shortcuts[user_data]

    if "what is your name" in user_data or "your name" in user_data or "tell me your name" in user_data:                                     # in(checks substring inside the text, if the user said that)
        text_to_speech.text_to_speech("My name is virtual assistant")
        return "My name is virtual assistant"
    
    elif user_data in ["hello", "hi", "hey", "hye"]:
        text_to_speech.text_to_speech("Hey, how can I help you")
        return "Hey, how can I help you"

    elif "good morning" in user_data or "hey, good morning" in user_data:
        text_to_speech.text_to_speech("Good morning dear")
        return "Good morning dear"
    
    elif "afternoon" in user_data:
        text_to_speech.text_to_speech("Good afternoon dear")
        return "Good afternoon dear"
    
    elif "good evening" in user_data or "good evening" in user_data:
        text_to_speech.text_to_speech("Good evening dear")
        return "Good evening dear"

    elif "shutdown" in user_data or "quit" in user_data:
        text_to_speech.text_to_speech("ok sir")
        exit()
        
    elif "music" in user_data or "song" in user_data:
        webbrowser.open("https://gaana.com/")   
        text_to_speech.text_to_speech("gaana.com is now ready for you, enjoy your music")     
        return "gaana.com is now ready for you, enjoy your music"                                
        
    elif "google" in user_data:
        webbrowser.open("https://google.com/")
        text_to_speech.text_to_speech("google.com is now ready for you")  
        return "google.com is now ready for you"
    
    elif "youtube" in user_data:
        webbrowser.open("https://youtube.com/")
        text_to_speech.text_to_speech("YouTube.com is now ready for you") 
        return "YouTube.com is now ready for you"

    
    elif "open folder" in user_data or "folder" in user_data:

        # remove extra words
        for word in ["open", "folder", "please", "my"]:
            user_data = user_data.replace(word, "")

        folder_name = user_data.strip()

        try:
            # 🔥 IMPORTANT: Use OneDrive path
            base_path = os.path.join(os.path.expanduser("~"), "OneDrive")

            full_path = find_folder(folder_name, base_path)

            if full_path:
                os.startfile(full_path)
                text_to_speech.text_to_speech(f"Opening {folder_name}")
                return f"Opening {folder_name}"
            else:
                text_to_speech.text_to_speech("Folder not found")
                return "Folder not found"

        except Exception as e:
            print(e)   # debug
            text_to_speech.text_to_speech("Error opening folder")
            return "Error opening folder"
        
    elif "copy" in user_data or "move" in user_data:

        words = user_data.split()

        try:
            action_type = "copy" if "copy" in words else "move"

            if "from" in words and "to" in words:
                from_index = words.index("from")
                to_index = words.index("to")

                item_name = " ".join(words[1:from_index])
                # FIX
                item_name = (
                    item_name.replace("folder", "")
                    .replace("file", "")
                    .strip()
                )

                source_folder = " ".join(words[from_index + 1:to_index])
                dest_folder = " ".join(words[to_index + 1:])

            else:
                text_to_speech.text_to_speech("Please specify from and to folders")
                return "Invalid command"

            # 🔥 SEARCH IN MULTIPLE LOCATIONS
            home = os.path.expanduser("~")
            search_paths = [
                os.path.join(home, "OneDrive"),
                os.path.join(home, "Desktop"),
                os.path.join(home, "Downloads"),
                os.path.join(home, "Documents")
            ]

            source_path = None
            dest_path = None

            for path in search_paths:
                if not source_path:
                    source_path = find_folder(source_folder, path)
                if not dest_path:
                    dest_path = find_folder(dest_folder, path)

            if not source_path:
                text_to_speech.text_to_speech("Source folder not found")
                return "Source folder not found"

            if not dest_path:
                text_to_speech.text_to_speech("Destination folder not found")
                return "Destination folder not found"

            # 🔥 FIXED item search
            item_path = None
            for root, dirs, files in os.walk(source_path):
                for name in dirs + files:
                    if item_name.lower() in name.lower():
                        item_path = os.path.join(root, name)
                        break
                if item_path:
                    break   # 🔥 important

            if not item_path:
                text_to_speech.text_to_speech("File or folder not found")
                return "File or folder not found"

            # 🔥 PERFORM ACTION
            if action_type == "copy":
                if os.path.isdir(item_path):
                    shutil.copytree(
                        item_path,
                        os.path.join(dest_path, os.path.basename(item_path)),
                        dirs_exist_ok=True
                    )
                else:
                    shutil.copy2(item_path, dest_path)

                text_to_speech.text_to_speech("Copied successfully")
                return "Copied successfully"

            else:
                shutil.move(item_path, dest_path)
                text_to_speech.text_to_speech("Moved successfully")
                return "Moved successfully"

        except Exception:
            text_to_speech.text_to_speech("Error in file transfer")
            return "Error in file transfer"

    elif "weather" in user_data:

        user_data = user_data.lower()
        words = user_data.split()

        remove_words = ["what", "is", "the", "weather", "in", "of", "for", "today", "now", "please", "tell", "me" , "how" , "What" , "How" , "Weather" , "Today" , "?" , "display" , "give"]

        # keep only useful words (city)
        city_words = [word for word in words if word not in remove_words]

        city = " ".join(city_words)

        # if empty → ask via voice
        if city == "":
            text_to_speech.text_to_speech("Please tell me the city name")
            city = speech_to_text.speech_to_text()

            if not city:
                return "Sorry, I didn't get the city name"

        result = weather.get_weather(city)

        text_to_speech.text_to_speech(result)
        return result
        
    # TIME
    elif "time" in user_data and "weather" not in user_data:
        current_time = datetime.datetime.now()
        time = current_time.strftime("%I:%M %p")

        text_to_speech.text_to_speech("The time is " + time)
        return "The time is " + time

    # DATE
    elif "date" in user_data:
        current_time = datetime.datetime.now()
        date = current_time.strftime("%d %B %Y")

        text_to_speech.text_to_speech("Today's date is " + date)
        return "Today's date is " + date

    # DAY
    elif "day" in user_data:
        current_time = datetime.datetime.now()
        day = current_time.strftime("%A")

        text_to_speech.text_to_speech("Today is " + day)
        return "Today is " + day


    else:
        text_to_speech.text_to_speech("I am not able to understand")
        return "I am not able to understand"

