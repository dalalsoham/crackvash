# Crackvash
![intro img](https://github.com/Itsmmdoha/crackvash/blob/af6678a912ac96dfa9173d5eeb6d12378d88a20d/crackvash.png?raw=true)

It's a python tool that lets you hack into Udvash accounts. It allows users to hack into Udvash accounts using OTP brute-force attack. It uses multi threading. So, the process is quick, takes no more than 2-3 minutes with decent internet connection.



## Warning:

This is a POC (Proof Of Concept) script. I found the vulnerability, and I made a tool that can exploit it, just to prove a point. If you use it with ill intent, well, you are on your own. I will not be responsible for what you do.



## Contributing

Contributions are always welcome!

If you want to customize this code, just do it.
Some things I'd like to change are:
1. Build a better Command Line Interface.
2. Verify the credentials provided by the user before starting an attack.



## Features

- Change Password
- Get registration number by name and phone number
- Multi-threading support
- Randomized OTP brute-forcing



## Installation and Usage

You have to install the required modules before running it. Just run the following commands:

- Clone the repository:
```bash
    git clone https://github.com/itsmmdoha/crackvash
```

- navigate to the crackvash directory:
```bash
    cd crackvash
```

- install required modules:
```bash
  pip install -r requirements.txt
```
- finally run the main.py file
```bash
    python3 main.py
```
- Then, just follow the onscreen instructions.

    
## How does it work?

The web portal sends a 4-digit OTP to the user; this tool cracks it by trying all 10 thousand combinations.
It first loads all the combinations from the 4digits.txt file and randomizes it. After that, it loads all the combinations into a queue so that multi-threading can be used. Then, it just tries all of them until one is matched.

The brute-force can take 20 seconds if you are lucky or can also extend up to 2-3 minutes. But if you have a fast internet connection, I promise it won't take much longer than that.

## 🚀 About Me
I'm an enthusiast.
I have a youtube channel named [HoundSec](https://youtube.com/@HoundSec)

contact me at: <the_doha@protonmail.com>
