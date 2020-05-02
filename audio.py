# import PyAudio
import wave


def play(filename):
    chunk = 1024
    wf = wave.open(filename, 'rb')
    pa = PyAudio.PyAudio()

    stream = pa.open(
        format=pa.get_format_from_width(wf.getsampwidth()),
        channel=wf.getchannels(),
        rate=wf.getframerate(),
        output=True
    )

    data_stream = wf.readframes(chunk)

    while data_stream:
        stream.write(data_stream)
        data_stream = wf.readframes(chunk)

    stream.close()
    pa.terminate()


play('audio_notification.mp3')
