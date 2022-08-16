#                  ReSimple
##           Renaming samples, simply.
### Overiew: Python App to preview, play, and rename batches of .wav files.

Menu Heirarchy


        1. path to sample directory
        2. display sample directory contents  <--------
        3. choose sample folder to enter              |
        4. Menu                                       |
            4.1 display samples, preview or full      |
            4.2 play samples one by one               |
            4.3 rename a batch of samples             |
            4.4 ability to return to Step 2  ----------      
        5. exit program.


Dev-Notes:

- Originally started with a simple module called playsound. Was so enthralled at getting sound to play from the terminal,
    that I ignored a critical error coming from playsound for ~72 hours.
- Switched to PyAudio for playing the audio files. Much more complicated, but in that sense more "robust" and friendly.
                /PyAudio play() func takes in filepath to .wav file.
                /Basically functions like a 'with open' with a mode that reads the binary structure of the wav file.
- reperlib acts as repr() function but allows for limits on print outputs, just in case there's 5000 kick drum samples.
