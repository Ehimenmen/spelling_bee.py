import random
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

# Function to select a word randomly from the selected difficulty level
def get_random_word(difficulty):
    return random.choice(words[difficulty])

# Main Streamlit app
def main():
    st.title("📝 Spelling Bee Game 🐝")
    st.write("Test your spelling skills across different difficulty levels!")

    player_name = st.text_input("Enter your name:", "").strip()
    if player_name:
        score = 0

        # Loop through the difficulty levels
        for difficulty in ["easy", "intermediate", "advanced"]:
            st.write(f"### {difficulty.capitalize()} Round")
            word = get_random_word(difficulty)
            st.write(f"Your word is: **{word}**")

            user_input = st.text_input(f"Spell the word ({difficulty}):", key=difficulty).strip()
            if st.button(f"Submit ({difficulty})"):
                if user_input.lower() == word.lower():
                    st.success("✅ Correct!")
                    score += 1
                else:
                    st.error(f"❌ Incorrect! The correct spelling is: {word}")

        st.write(f"## 🏆 Game Over! {player_name}, your final score is: {score}/3")

        # Bonus round if all answers are correct
        if score == 3:
            st.write("🎉 Bonus Round Unlocked! 🎉")
            bonus_word = get_random_word("advanced")
            st.write(f"Bonus word: **{bonus_word}**")

            bonus_input = st.text_input("Spell the bonus word:", key="bonus").strip()
            if st.button("Submit Bonus Word"):
                if bonus_input.lower() == bonus_word.lower():
                    st.success("✅ Amazing! You nailed the bonus round!")
                else:
                    st.error(f"❌ Close! The correct spelling is: {bonus_word}")

if __name__ == "__main__":
    main()
