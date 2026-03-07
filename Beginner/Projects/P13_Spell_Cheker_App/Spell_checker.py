
# step - 1 : Importing the required library

from spellchecker import SpellChecker

# step - 2 : Creating the App class

class SpellCheckerApp:
    def __init__(self):
        self.spell = SpellChecker()

    def correct_text(self , text):
        words = text.split()  #----> hello world [ 'hello' , 'world' ]
        corrected_words = []

        for word in words:
            corrected_word = self.spell.correction(word)
            if corrected_word != word.lower():
                print(f"Correcting '{word}' to '{corrected_word}' ")
                corrected_words.append(corrected_word)

        
        # step : 3 returning the corrected text
        return ''.join(corrected_words)



    #step : 4 running the app

    def run(self):
        print("__SPELL CHECKER___")

        while True:
            text = input('Enter text to check ( or type "exit" to quit ) :')

            if text.lower() == 'exit':
                print("Closing the program.....")
                break 

            correct_text = self.correct_text(text)
            print(f'Corrected Text : {correct_text}')


# Step : 5 running the main program 

if __name__ == "__main__":
    SpellCheckerApp().run()