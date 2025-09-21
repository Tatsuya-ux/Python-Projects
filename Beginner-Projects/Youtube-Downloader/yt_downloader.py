from pytube import YouTube
import os

class Style:
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

# Function to download video with user-selected resolution
def download_video(url):
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        print(f"{Style.BOLD}Title:{Style.RESET} {yt.title}")

        # Filter for progressive streams (video + audio) in mp4 format
        print(f"{Style.BOLD}Avalable Resolutions:{Style.RESET}")
        streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
        for i, stream in enumerate(streams):
            print(f"[{i}] {stream.resolution} - {stream.mime_type}")

        # Prompt user to select resolution
        choice = int(input("Choose resolution index: "))
        selected_stream = streams[choice]
        print(f"{Style.YELLOW}Downloading...{Style.RESET}")
        selected_stream.download()
        print(f"{Style.GREEN}Video Downloaded Successfully!{Style.RESET}")
    except Exception as e:
        print(f"{Style.RED}Error: {e}{Style.RESET}")

# Function to download audio only and convert to mp3
def download_audio(url):
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        print(f"{Style.BOLD}Title:{Style.RESET} {yt.title}")

        # Get the first available audio-only stream
        audio_stream = yt.streams.filter(only_audio=True).first()

        print(f"{Style.YELLOW}Downloading audio...{Style.RESET}")
        out_file = audio_stream.download()

        # Rename the file to .mp3 extension
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        print(f"{Style.GREEN}Audio Downloaded Sucessfully as MP3!{Style.RESET}")
    
    except Exception as e:
        print(f"{Style.RED}Error: {e}{Style.RESET}")

# Progress callback function
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    print(f"\r{Style.YELLOW}Downloading... {percentage_of_completion:.2f}% completed{Style.RESET}", end='', flush=True)

# Main loop for user interaction
def main():
    print(f"{Style.BOLD}{Style.GREEN}Welcome to YouTube Downloader!{Style.RESET}")

    while True:
        # Display menu options
        print(f"""\n{Style.BOLD}Menu:{Style.RESET}
              [1] Download Video (MP4)
              [2] Download Audio only (MP3)
              [3] Exit""")
        
        choice = input("Choose an option: ")

        if choice == '1':
            url = input("Enter YouTube video URL: ")
            download_video(url)
        elif choice == '2':
            url = input("Enter YouTube video URL: ")
            download_audio(url)
        elif choice == '3':
            print(f"{Style.BOLD}{Style.GREEN}Thank you for using YouTube Downloader!{Style.RESET}")
            break
        else:
            print(f"{Style.RED}Invalid choice. Please try again.{Style.RESET}")

if __name__ == "__main__":
    main()