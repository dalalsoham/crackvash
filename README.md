
# Crackvash

It's a tool that lets you hack into udvash accounts. 



## warning:

This is a POC (Proof Of Concept) script. I found the voulnaribility and I made a tool that can exploit it, just to proove a point. I you use it with ill intent, well; you are on your own. I will not be responsible for what you do.


## Contributing

Contributions are always welcome!

If you want to customize this code, just do it.
some things I'd like to change are:
1. Build a better Command Line Interface.
2. Verify the cridentials provided by the user before starting and attack.

## Features

- Change Password
- Get registration number by name and phone number
- Multi threading support
- Randomized OTP brute-forcing


## Installation and Usage

You have to install the required modules before runnig it. Just run the follwing commands:

- clone the repository:
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
- Then, just follow the onscreen instruction.

    
## How does it work?

The web portal sends a 4 digit OTP to the user, this tool just cracks it trying all 10 thousand combinations. 
It first loads all the combinations from the 4digits.txt file and randomize it. After that, it loads all the combinations to a queue so that multi threading can be used. Then It just tries all of them untill one is matched.

Then brute-force can take 20 seconds if you are lucky or can also extend upto 3-4 minutes. But if you have a fast internet connection, I promise it wont take much longer than that.
