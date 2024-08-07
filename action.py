import Text_to_Speech
import Speech_to_text
import datetime
import webbrowser
import weather
import os
import platform

user_data = Speech_to_text.speech_to_txt()

def Action(data):
    user_data = data.lower()

    if "what is your name" in user_data:
        Text_to_Speech.text_to_Speech("I am your virtual assistant")
        return "I am your virtual assistant"
    
    elif "virtual assistant" in user_data or "ok jarvis" in user_data:
        Text_to_Speech.text_to_Speech("I'm here to help you")
        return "I'm here to help you"
    
    elif "hello" in user_data or "hi" in user_data or "hye" in user_data:
        Text_to_Speech.text_to_Speech("Hi, how can I help you?")
        return "Hi, how can I help you?"
    
    elif "good morning" in user_data:
        Text_to_Speech.text_to_Speech("Good morning sir")
        return "Good morning sir"

    elif "what is time now" in user_data or "time" in user_data:
        current_time = datetime.datetime.now()
        time_str = f"{current_time.hour} Hour: {current_time.minute} Minute"
        Text_to_Speech.text_to_Speech(time_str)
        return time_str
    
    elif "date" in user_data or "what is date" in user_data or "get date" in user_data:
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        Text_to_Speech.text_to_Speech(f"Today's date is {current_date}")
        return f"Today's date is {current_date}"
    
    elif "shutdown" in user_data:
        Text_to_Speech.text_to_Speech("Ok sir")
        return "Ok sir"
    
    elif "open google" in user_data:
        webbrowser.open("https://www.google.com")
        Text_to_Speech.text_to_Speech("Opening Google")
        return "Opening Google"

    elif "open youtube" in user_data or "open yt" in user_data:
        webbrowser.open("https://www.youtube.com")
        Text_to_Speech.text_to_Speech("YouTube is ready")
        return "YouTube is ready"
    
    elif "open gmail" in user_data:
        webbrowser.open("https://mail.google.com")
        Text_to_Speech.text_to_Speech("Opening Gmail")
        return "Opening Gmail"
    
    elif "play music" in user_data:
        webbrowser.open("https://www.gaana.com")
        Text_to_Speech.text_to_Speech("Ok sir, enjoy the music")
        return "Ok sir, enjoy the music"

    elif "weather" in user_data or "what is temperature" in user_data or "what is weather" in user_data:
        ans = weather.weather()
        Text_to_Speech.text_to_Speech(ans)
        return ans
    
    elif "open vscode" in user_data or "open visual studio code" in user_data:
        try:
            os.system("code")  # This command assumes `code` is in your PATH.
            Text_to_Speech.text_to_Speech("Opening Visual Studio Code")
            return "Opening Visual Studio Code"
        except Exception as e:
            Text_to_Speech.text_to_Speech("Failed to open Visual Studio Code")
            return "Failed to open Visual Studio Code"
    
    elif "calculate" in user_data:
        try:
            # Calculating values from user_data
            expression = user_data.replace("calculate", "").replace("plus", "+").replace("minus", "-").replace("multiply by", "*").replace("divided by", "/")
            result = eval(expression)
            Text_to_Speech.text_to_Speech(f"The result is {result}")
            return f"The result is {result}"
        except Exception as e:
            Text_to_Speech.text_to_Speech("There was an error in calculation")
            return "There was an error in calculation"
    
    elif "increase brightness" in user_data:
        if platform.system() == "Windows":
            os.system("powershell (Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,((Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightness).CurrentBrightness + 10))")
            Text_to_Speech.text_to_Speech("Increasing brightness")
            return "Increasing brightness"
        else:
            Text_to_Speech.text_to_Speech("This command is not supported")
            return "This command is not supported  "
    
    elif "decrease brightness" in user_data:
        if platform.system() == "Windows":
            os.system("powershell (Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,((Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightness).CurrentBrightness - 10))")
            Text_to_Speech.text_to_Speech("Decreasing brightness")
            return "Decreasing brightness"
        else:
            Text_to_Speech.text_to_Speech("This command is not supported")
            return "This command is not supported  "
    
    elif "open command prompt" in user_data or "open cmd" in user_data:
        if platform.system() == "Windows":
            os.system("start cmd")
            Text_to_Speech.text_to_Speech("Opening Command Prompt")
            return "Opening Command Prompt"
        else:
            Text_to_Speech.text_to_Speech("This command is not supported")
            return "This command is not supported  "
    
    elif "open notepad" in user_data:
        if platform.system() == "Windows":
            os.system("notepad")
            Text_to_Speech.text_to_Speech("Opening Notepad")
            return "Opening Notepad"
        else:
            Text_to_Speech.text_to_Speech("This command is not supported")
            return "This command is not supported  "

    elif "open word" in user_data or "open ms word" in user_data:
        if platform.system() == "Windows":
            os.system("start winword")
            Text_to_Speech.text_to_Speech("Opening Microsoft Word")
            return "Opening Microsoft Word"
        else:
            Text_to_Speech.text_to_Speech("This command is not supported")
            return "This command is not supported  "
    
    elif "open ppt" in user_data or "open power point" in user_data:
        if platform.system() == "Windows":
            os.system("start powerpnt")
            Text_to_Speech.text_to_Speech("Opening Microsoft PowerPoint")
            return "Opening Microsoft PowerPoint"
        else:
            Text_to_Speech.text_to_Speech("This command is not supported  ")
            return "This command is not supported  "
    
    elif "open excel" in user_data:
        if platform.system() == "Windows":
            os.system("start excel")
            Text_to_Speech.text_to_Speech("Opening Microsoft Excel")
            return "Opening Microsoft Excel"
        else:
            Text_to_Speech.text_to_Speech("This command is not supported")
            return "This command is not supported  "
    
    else:
        Text_to_Speech.text_to_Speech("I am not able to understand that")
        return "I am not able to understand that"
