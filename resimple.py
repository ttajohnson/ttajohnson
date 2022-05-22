import os
import wave
import pyaudio
import reprlib
from array import array
from struct import pack
from pathlib import Path

class resimple():
    def __init__(self):
        self.filepath = input("Enter path to sample directory: ")
        self.folders = os.listdir(self.filepath)
        print(f'Sample directory includes these folders: {self.folders}')
        while True:
            choose_folder = input("Choose folder to enter: ")
            if choose_folder in self.folders:
                samples = os.listdir(self.filepath + '/' + choose_folder)
                folder = self.filepath + '/' + choose_folder
                break
            else:
                print(f'Folder not in sample directory...\nPlease choose from {self.folders}: ')
            # return samples
        self.samples = samples
        self.folder = folder
        self.og_dir = os.getcwd()
        self.newdir = os.chdir(self.filepath + '/' + choose_folder)
        

    def switch_folders(self):
        print(f'Sample directory includes these folders: {self.folders}')
        while True:
            choose_folder = input("Choose folder to enter: ")
            if choose_folder in self.folders:
                samples = os.listdir(self.filepath + '/' + choose_folder)
                folder = self.filepath + '/' + choose_folder
                break
            else:
                print(f'Folder not in sample directory...\nPlease choose from {self.folders}: ')            
        self.samples = samples
        self.folder = folder
        self.og_dir = os.getcwd()
        self.newdir = os.chdir(self.filepath + '/' + choose_folder)
        
    def display_samples(self):
        pre_full = input('See (P)review or (F)ull list of files? ').lower()
        if pre_full == 'f':
            print('\n'.join(self.samples))
        elif pre_full == 'p':
            r = reprlib.Repr()
            r.maxlist = 4
            r.maxstring = 20
            print(r.repr(self.samples))

    def play(self, file):
        CHUNK = 1024
        wf = wave.open(file, 'rb')
        p=pyaudio.PyAudio()
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                            channels=wf.getnchannels(),
                            rate = wf.getframerate(),
                            output = True)
        data = wf.readframes(CHUNK)
        while len(data)>0:
            stream.write(data)
            data = wf.readframes(CHUNK)
        stream.stop_stream()
        stream.close
        p.terminate

    def play_samples(self):
        for i in range(len(self.samples)):
            while True:
                print(self.samples[i])
                self.play(self.folder + '/' + self.samples[i])
                repextop = input('(N)ext or (S)top ').lower()
                if repextop == 'r':
                    continue
                elif repextop == 'n':
                    break
                elif repextop == 's':
                    return False
        self.samples = os.listdir(self.folder)
    
    def rename_samples(self):
        i = 0
        batch_name = input("Enter batch-name for samples: ").title()
        for file in self.samples:
            new_name = batch_name + '(' + str(i) + ')' + '.wav'
            if new_name == file:
                break
            else: os.rename(os.path.join(self.folder, file), os.path.join(self.folder, new_name))
            i += 1
        print(f'Samples renamed to {batch_name}().wav')
        self.samples = os.listdir(self.folder)

def main():

    print('\t- ReSimple -\n   Renaming samples, simply!')

    open = resimple()

    while True:

        print("\nType the associated number of the action you would like to perform:")
        command = input("\n1. Display samples\n2. Play samples\n3. Rename samples\n4. Switch folders\n5. Quit\n- ")
        if command == '1':
            open.display_samples()
        elif command == '2':
            open.play_samples()
        elif command == '3':
            open.rename_samples()
        elif command == '4':
            open.switch_folders()
        elif command == '5':
            print('\nThank you for using ReSimple!')
            return False
        else: print('\nThat option does not exist.')

main()
