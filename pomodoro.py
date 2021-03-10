import pyaudio
import wave
import sys
import asyncio


FOCUS_SOUND = 'sounds/synth.wav'
RELAX_SOUND = 'sounds/ocarina.wav'
FOCUS_TIME = 20*60    # seconds
RELAX_TIME =  5*60    # seconds


async def play_sound(filepath):
    CHUNK = 1024
    p = pyaudio.PyAudio()
    with wave.open(filepath, 'rb') as wf:
        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)
        while len(data := wf.readframes(CHUNK)) > 0:
            stream.write(data)
        stream.stop_stream()
        stream.close()


async def start_pomodoro(focus_time, relax_time):
    while True:
        await asyncio.gather(play_sound(FOCUS_SOUND), asyncio.sleep(focus_time))
        await asyncio.gather(play_sound(RELAX_SOUND), asyncio.sleep(relax_time))


async def main():
    await start_pomodoro(FOCUS_TIME, RELAX_TIME)


if __name__ == '__main__':
    asyncio.run(main())

