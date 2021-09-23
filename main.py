# ----- Connecting to an FTP Server -----
# We will connect anonymously to Port 21 - Default FTP Port

# Anonymous FTP Connection
# Use an anonymous login to the FTP server.
from ftplib import FTP

try:
    print("\nAttempting anonymous login...")
    with FTP("ftp.dlptest.com") as ftp:
        print(f"\t{ftp.getwelcome()}")
        # A "with" statement will automatically close the connection when it reaches the end of the code block.
except Exception as e:
    print(f"\tException... {e}")
else:
    print("\tSuccess!")

# Authenticated Login
# Use an authenticated login to the FTP server using two different methods.
# Method #1: Passing in the 'user' and 'passwd' parameters to the 'FTP()' constructor.
# Note: I've intentionally passed in the wrong credentials for this example.
try:
    print("\nMethod #1\n\tAttempting authenticated connection with login details...")
    with FTP(host="ftp.dlptest.com", user="user", passwd="password") as ftp:
        print(f"\t{ftp.getwelcome()}")
except Exception as e:
    print(f"\tException... {e}")
else:
    print("\tSuccess!")
# Method #2: Calling 'connect()' and 'login()'.
try:
    print("\nMethod #2\n\tAttempting authenticated connection with login details...")
    ftp = FTP()
    ftp.connect("ftp.dlptest.com")
    ftp.login("dlpuser", "rNrKYTX9g7z3RgJRmxWuGHbeu")
    print(f"\t{ftp.getwelcome()}")
    ftp.close()
except Exception as e:
    print(f"\tException... {e}")
else:
    print("\tSuccess!")

# Connection with SSL/TLS Over Default Port 21
from ftplib import FTP_TLS

try:
    print(
        "\nConnection with SSL/TLS\n\tAttempting authenticated connection with login details..."
    )
    with FTP_TLS("ftp.dlptest.com", "dlpuser", "rNrKYTX9g7z3RgJRmxWuGHbeu") as ftp:
        print(f"\t{ftp.getwelcome()}")
except Exception as e:
    print(f"\tException... {e}")
else:
    print("\tSuccess!")

# ----- Working with Directories -----
# Printing the current working directory.
try:
    print(
        "\nConnection with SSL/TLS\n\tAttempting authenticated connection with login details..."
    )
    with FTP_TLS("ftp.dlptest.com", "dlpuser", "rNrKYTX9g7z3RgJRmxWuGHbeu") as ftp:
        print(f"\t{ftp.pwd()}")  # Usually the default is /

        try:
            ftp.mkd("my_dir")  # Make a directory
            print("\tMade a new directory.")
        except Exception as e:
            print(f"\tException... {e}")

        try:
            ftp.rmd("my_dir")  # Remove a directory
            print("\tRemoved the directory.")
        except Exception as e:
            print(f"\tException... {e}")

        try:
            ftp.cwd("other_dir")  # Change current working directory
            print("\tChanged the current working directory.")
        except Exception as e:
            print(f"\tException... {e}")

        try:
            # Listing directory files
            # files = []
            # ftp.dir(files.append)  # Takes a callback for each file

            # for file in files:
            #     print(f"\tfile")
            for name in ftp.nlst():
                print(f"\t{name}")
        except Exception as e:
            print(f"\tException... {e}")
except Exception as e:
    print(f"\tException... {e}")

# ----- Working with Files -----
try:
    print(
        "\nConnection with SSL/TLS\n\tAttempting authenticated connection with login details..."
    )
    with FTP_TLS("ftp.dlptest.com", "dlpuser", "rNrKYTX9g7z3RgJRmxWuGHbeu") as ftp:
        print(f"\tAttempting to upload test files.")

        # Upload a test file.
        # For text or binary file, always use `rb`
        print(f"\nUploading text file...")
        with open("text.txt", "rb") as text_file:
            ftp.storlines(
                "STOR text.txt", text_file
            )  # 'storlines()' should not be used to transfer binary files

        print(f"\tUploading image file...")
        with open("cat_image.jpg", "rb") as image_file:
            ftp.storbinary("STOR cat_image.jpg", image_file)
        print(f"\tSuccessfully uploaded test files.")

        print(f"\tGetting a list of new files...")
        for name in ftp.nlst():
            print(f"\t{name}")

        # Get the size of a file.
        print(f"\nGetting file size...")
        try:
            ftp.sendcmd('TYPE I') # 'TYPE I' denotes an image or binary data
            print(ftp.size('\tImage size in bytes:' + 'cat_image.jpg'))
        except Exception as e:
            print(f"\tError checking image size: {e}")

         # Rename a file.
        print(f"\nRenaming file...")
        try:
            ftp.rename('cat_image.jpg', 'cat.jpg') # Change 'cat_image.jpg' to 'cat.jpg'
            print('\tSuccessfully renamed file!')
        except Exception as e:
            print(f"\tError renaming file: {e}")

        # Download a file.
        print(f"\nDownloading file...")
        with open("local_text.txt", "w") as local_file: # Open local file for writing
            response = ftp.retrlines('RETR text.txt', local_file.write)
            
            # Check the response code
            print(f"\tChecking response code...")
            # https://en.wikipedia.org/wiki/List_of_FTP_server_return_codes
            if response.startswith('226'):  # Transfer complete
                print('\tTransfer complete.')
            else:
                print('\tError transferring. Local file may be incomplete or corrupt.')
except Exception as e:
    print(f"\tException... {e}")
