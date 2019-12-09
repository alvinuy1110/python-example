import pyttsx3

engine = pyttsx3.init()

## settings
# engine = pyttsx3.init(driverName="sapi5")
# engine = pyttsx3.init(driverName="espeak")
### rate words per minute, 200 is default
engine.setProperty('rate', 150)

## sample
engine.say('Good morning.')



voices = engine.getProperty('voices')

#  iterate through the system settings of voices available
for voice in voices:

    print("Voice:")
    print(" - ID: %s" % voice.id)
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)
    # print("voice id {0}".format(voice.id))

    engine.setProperty('voice', voice.id)
    engine.say('The quick brown fox jumped over the lazy dog.')

engine.runAndWait()
