import cv2

def decrypt_message(image_path):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found!")
        return

    try:
        with open("password.txt", "r") as file:
            saved_password = file.read().strip()
    except FileNotFoundError:
        print("Error: Password file not found!")
        return

    pas = input("Enter passcode for Decryption: ")
    if pas != saved_password:
        print("YOU ARE NOT AUTHORIZED")
        return

    c = {i: chr(i) for i in range(256)}

    message = ""
    n, m, z = 0, 0, 0

    # First, read the length of the message
    msg_len_str = ""
    while True:
        char = c[img[n, m, z]]
        if char == ":":
            break
        msg_len_str += char
        z = (z + 1) % 3
        if z == 0:
            n = (n + 1) % img.shape[0]
            m = (m + 1) % img.shape[1]

    msg_len = int(msg_len_str)
    message = ""

    # Now, read the actual message
    for _ in range(msg_len):
        z = (z + 1) % 3
        if z == 0:
            n = (n + 1) % img.shape[0]
            m = (m + 1) % img.shape[1]
        message += c[img[n, m, z]]

    print("Decryption message:", message)

decrypt_message("encryptedImage.png")
