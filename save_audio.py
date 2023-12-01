import os

def save_audio(audio_file):
    if audio_file is None:
        return None  # Return None if no file is uploaded

    # Specify the directory where you want to save audio files
    save_directory = 'D:/SIH/Sentiment Analysis/uploaded_audio/'
    
    # Ensure the directory exists, create it if necessary
    if not os.path.exists(save_directory):
        os.makedirs(save_directory)
    
    # Specify the full file path including the directory and file name
    save_location = os.path.join(save_directory, audio_file.name)
    
    # Save the uploaded audio file
    with open(save_location, 'wb') as f:
        f.write(audio_file.read())
    
    return save_location
