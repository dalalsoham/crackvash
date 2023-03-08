# crackvash
A simple tool that can exploit the poorly configured authentication system of udvash.com. 

It can retrieve registration number from Nickname and phone number;
or, Change password of any account with phone number and registration.

The OTP sent to the phone number is only 4 digits. So, if we use a little bit of permutation, there is only 10000 possible combination.
This tool tries them all! And eventually crack it.
Possible metigations: Longer OTP, Limit clients after a certain amount wrong OTP attempt.

I built it out of boredom!

Warning: Don't use this to commit any crime, I'll not be responsible for any of your bad acts.
I just hope the folks from Udvash finds this tool and fix the bug! 
