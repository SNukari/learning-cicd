import os
# making bandit trigger for code flaw with insecure line for security check
os.system("ls -l")

def get_weather():
    return "It's always sunny in the terminal"

if __name__ == "__main__":
    print(get_weather())