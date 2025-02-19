import cv2
import os

def encrypt_message(image_path, output_image):
    img = cv2.imread(image_path)
    if img is None:
        print("Error: Image not found!")
        return

    msg = input("Enter secret message: ")
    password = input("Enter a passcode: ")

    d = {chr(i): i for i in range(256)}
    msg = str(len(msg)) + ":" + msg  # Store message length in the image

    n, m, z = 0, 0, 0

    for char in msg:
        img[n, m, z] = d[char]  # Store ASCII value in pixel
        z = (z + 1) % 3
        if z == 0:
            n = (n + 1) % img.shape[0]
            m = (m + 1) % img.shape[1]

    cv2.imwrite(output_image, img)  # Save encrypted image
    with open("password.txt", "w") as file:
        file.write(password)  # Store password separately

    print("Message encrypted and saved in", output_image)
    os.system("start " + output_image)  # Opens the image (Windows only)

encrypt_message("mypic.png", "encryptedImage.png")
