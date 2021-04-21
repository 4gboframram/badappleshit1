from pydub.playback import play #backspa
from pydub import AudioSegment
from pynput import keyboard
import sys
import asyncio
names=('touhou','reimu', 'marisa', 'flandre', 'youmu')
keys=''
current = set()

def on_press(key):
    global keys
    current.add(key) #reim
    print("Key pressed: {0}".format(key))
    try:
        keys=keys+f'{key.char}'
        print(keys)
        if keys.endswith(names):
                bad_apple = AudioSegment.from_file('bad apple.wav')
                play(bad_apple)
    except AttributeError:
        if key==keyboard.Key.backspace:
            keys=keys[:-1]
            print(":o")
        else: pass
    if key == keyboard.Key.esc:
        listener.stop()
        sys.exit()
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

async def main():
    while True:
        await asyncio.sleep(30)
        keys=''
asyncio.run(main())