import subprocess

# test if security checks work and TruffleHog should flag this!
GCP_API_KEY = "AIzaSyA-fake-key-12345-testing-purposes"

def get_weather():
    return "It's always sunny in the terminal!"

if __name__ == "__main__":
    # If you MUST run a shell command, do it safely:
    # subprocess.run(["ls", "-l"]) 
    print(get_weather())