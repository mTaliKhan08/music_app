import pygame
import os

pygame.mixer.init()

playlist = []

def add_to_playlist(file_path):
    if os.path.isfile(file_path):
        playlist.append(file_path)
        print(f"Added to playlist: {os.path.basename(file_path)}")
    else:
        print("File not found. Please enter a valid file path.")

def play_next_in_playlist():
    if playlist:
        next_song = playlist.pop(0)
        play_music(next_song)
    else:
        print("Playlist is empty.")

def play_music(file_path):
    try:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        print(f"Now playing: {os.path.basename(file_path)}")
    except Exception as e:
        print(f"An error occurred: {e}")

def stop_music():
    pygame.mixer.music.stop()
    print("Music stopped.")

def pause_music():
    pygame.mixer.music.pause()
    print("Music paused.")

def unpause_music():
    pygame.mixer.music.unpause()
    print("Music unpaused.")

def show_menu():
    print("\n--- Simple Music Player ---")
    print("1. Add to playlist")
    print("2. Play next song")
    print("3. Stop music")
    print("4. Pause music")
    print("5. Unpause music")
    print("6. Exit")
    print("---------------------------")

def main():
    show_menu()

    while True:
        choice = input("Enter your choice: ")

        if choice == '1':
            file_path = input("Enter the path to the music file: ").strip()
            add_to_playlist(file_path)
        elif choice == '2':
            play_next_in_playlist()
        elif choice == '3':
            stop_music()
        elif choice == '4':
            pause_music()
        elif choice == '5':
            unpause_music()
        elif choice == '6':
            print("Exiting music player.")
            break
        else:
            print("Invalid choice. Please try again.")
            show_menu()

if __name__ == "__main__":
    main()
