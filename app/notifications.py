"""Send notification to user."""

import appinfo
import plyer
import pyaudio
import wave


def send_notification(message: str, title: str):
    """Send push notification on user's PC"""
    plyer.notification.notify(message=message, app_name=appinfo.APP_NAME, app_icon=appinfo.APP_ICON, title=title)


def play_sound():
    """Plays alarm on user's PC"""
    chunk = 1024

    f = wave.open(r"../media/alarm.wav", "rb")
    p = pyaudio.PyAudio()
    stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                    channels=f.getnchannels(),
                    rate=f.getframerate(),
                    output=True)
    data = f.readframes(chunk)

    while data:
        stream.write(data)
        data = f.readframes(chunk)

    stream.stop_stream()
    stream.close()

    p.terminate()
