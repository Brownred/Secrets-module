# Secrets Module in python

The secrets library is a library similar to the random library in python3.10 but way more secure. 
Due to its high secure features it can thus be used to create randomly generated passwords, One-Time_passwords(OTP) e.t.c

Example scenario:  
        Generating a temporay password and send this password on a temporary hard-to-guess URL so the client can reset their password using this URL.

### steps
    -Generate a ten-character alphanumeric password with atleast one lowercase character, 
    atleast one uppercase character, atleast one digits, and one special symbol.
    -Generate a temporary URL.
