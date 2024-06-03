import pygame
import os

# Initialize pygame mixer
pygame.mixer.init()

# Function to load and play a song
def play_music(file_path):
    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        print(f"Now playing: {os.path.basename(file_path)}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to stop the music
def stop_music():
    pygame.mixer.music.stop()
    print("Music stopped.")

# Function to pause the music
def pause_music():
    pygame.mixer.music.pause()
    print("Music paused.")

# Function to unpause the music
def unpause_music():
    pygame.mixer.music.unpause()
    print("Music unpaused.")

# Function to display the menu
def show_menu():
    print("\n--- Simple Music Player ---")
    print("1. Play music")
    print("2. Stop music")
    print("3. Pause music")
    print("4. Unpause music")
    print("5. Exit")
    print("---------------------------")

# Main function to run the music player
def main():
    show_menu()

    while True:
        choice = input("Enter your choice: ")

        if choice == '1':
            file_path = input("Enter the path to the music file: ").strip()
            play_music(file_path)
        elif choice == '2':
            stop_music()
        elif choice == '3':
            pause_music()
        elif choice == '4':
            unpause_music()
        elif choice == '5':
            print("Exiting music player.")
            break
        else:
            print("Invalid choice. Please try again.")
            show_menu()

if __name__ == "__main__":
    main()
