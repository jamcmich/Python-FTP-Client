# Connecting to an FTP Server
# We will connect anonymously to Port 21 - Default FTP Port

# Anonymous FTP Connection
# Use an anonymous login to the FTP server.
from ftplib import FTP

try:
    print("\nAttempting anonymous login...")
    with FTP("speedtest.tele2.net") as ftp:
        print(f"\t{ftp.getwelcome()}")
except Exception as e:
    print(f"\tException... {e}")
else:
    print("\tSuccess!")

# Authenticated Login
# Use an authenticated login to the FTP server using two different methods.
# 1. Passing in the 'user' and 'passwd' parameters to the 'FTP()' constructor.
# Note: I purposefully passed in the incorrect credentials for this example.
try:
    print("\nMethod #1\n\tAttempting authenticated connection with login details...")
    with FTP(host="speedtest.tele2.net", user="user", passwd="password") as ftp:
        print(f"\t{ftp.getwelcome()}")
except Exception as e:
    print(f"\tException... {e}")
else:
    print("\tSuccess!")
# 2. Calling 'connect()' and 'login()'.
try:
    print("\nMethod #2\n\tAttempting authenticated connection with login details...")
    ftp = FTP()
    ftp.connect("speedtest.tele2.net")
    ftp.login("anonymous", "password")
    print(f"\t{ftp.getwelcome()}")
    ftp.close()
except Exception as e:
    print(f"\tException... {e}")
else:
    print("\tSuccess!")
