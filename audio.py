import pyglet

file = pyglet.resource.media('audio_notification.mp3')
file.play()

pyglet.app.run()
