class Dog:
    def speak(self):
        print("Dog Barks!")
class Cat:
    def speak(self):
        print("Cat Meows!")

def animal_sound():
    speak_call = [Dog(),Cat()]
    for call in speak_call:
        call.speak()
animal_sound()