import random
import os
from gtts import gTTS
import streamlit as st

# Word bank for the spelling bee game
words = {
    "easy": [
        "Abundance", "Aerobics", "Acacia", "Akimbo", "Algae", "Advocate", "Accessible"
    ],
    "intermediate": [
        "Accentuate", "Agoraphobia", "Algorithm", "Alleviate", "Amphibians", 
        "Anagram", "Acrimonious"
    ],
    "advanced": [
        "Amniocentesis", "Apatosaurus", "Acuity", "Anaphylaxis", "Acciaccatura", 
        "Achromatic", "Aesculapian"
    ]
}

# Function to select a random word
def get_random_word(difficulty):
    return random.choice(words[difficulty])

# Function to pronounce the word using gTTS
def pronounce_word(word):
    tts = gTTS(text=word, lang='en')
    filename = f"{word}.mp3"
    tts.save(filename)
    return filename

# Main Streamlit app
def main():
    st.title("📝 Spelling Bee Game 🐝 with Pronunciation")
    st.write("Test your spelling skills! Click the button to hear the word and type it correctly.")

    player_name = st.text_input("Enter your name:", "").strip()
    
    if player_name:
        score = 0

        # Loop through the difficulty levels
        for difficulty in ["easy", "intermediate", "advanced"]:
            st.write(f"### {difficulty.capitalize()} Round")

            word = get_random_word(difficulty)
            audio_file = pronounce_word(word)

            if st.button(f"Play Word ({difficulty})"):
                # Play the word
                st.audio(audio_file, format="audio/mp3")

            user_input = st.text_input(f"Spell the word ({difficulty}):", key=difficulty).strip()
            if st.button(f"Submit ({difficulty})"):
                if user_input.lower() == word.lower():
                    st.success("✅ Correct!")
                    score += 1
                else:
                    st.error(f"❌ Incorrect! The correct spelling is: {word}")

            # Clean up the audio file after playing
            if os.path.exists(audio_file):
                os.remove(audio_file)

        st.write(f"## 🏆 Game Over! {player_name}, your final score is: {score}/3")

        # Bonus round if all answers are correct
        if score == 3:
            st.write("🎉 Bonus Round Unlocked! 🎉")
            bonus_word = get_random_word("advanced")
            bonus_audio = pronounce_word(bonus_word)

            if st.button("Play Bonus Word"):
                st.audio(bonus_audio, format="audio/mp3")

            bonus_input = st.text_input("Spell the bonus word:", key="bonus").strip()
            if st.button("Submit Bonus Word"):
                if bonus_input.lower() == bonus_word.lower():
                    st.success("✅ Amazing! You nailed the bonus round!")
                else:
                    st.error(f"❌ Close! The correct spelling is: {bonus_word}")

            # Clean up the bonus audio file
            if os.path.exists(bonus_audio):
                os.remove(bonus_audio)

if __name__ == "__main__":
    main()
