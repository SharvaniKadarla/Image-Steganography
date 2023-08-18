
# Image Steganography

Image Steganography, as the name implies, is the process of concealing data within an image
file. The image chosen for this purpose is referred to as the cover image, and the image
obtained after steganography is referred to as the stego image. 
Steganography is a method of hiding secret data, by embedding it into an audio, video, image, or text file. It is one of the methods employed to protect secret or sensitive data from malicious attacks. 


## Hardware and Software Requirements
**Hardware Requirements:**

● A PC or laptop that can satisfy software requirements

**Software Requirements:**

● Python IDLE (Version 3.7 or more)

● Python libraries and modules (like OpenCV, NumPy, Tkinter, Random and Pillow )
## Algorithm
The LSB (Least Significant Bit) algorithm is a widely used and simple steganographic
technique for hiding information within a digital signal, such as an image, audio, or video file,
without significantly affecting its perceptual quality. The technique is based on manipulating
each byte or pixel's least significant bit (LSB) in the signal to embed the hidden information.

Here's a general overview of how the LSB algorithm works:
1. **Binary Representation:** The data you want to hide (e.g., text, image, or other files) is
converted into binary form. A sequence of bits represents each character or pixel value.

2. **Cover Signal:** The "cover signal" is the original digital signal (e.g., an image) you want to use to hide the data. It can be any digital file where you can modify individual bits without
causing noticeable changes to the human eye or ear.

3. **LSB Replacement:** The least significant bit is replaced with the first bit(i.e. the least
significant bit) of the hidden data for each byte or pixel in the cover signal. The changes are
typically imperceptible since the LSB has the most minor effect on the overall value.

4. **Embedding Data:** Continue replacing the LSB of each byte or pixel in the cover signal with
the bits of the hidden data until all the data has been embedded.

5. **Save the Modified Signal:** The modified signal (e.g., the modified image) is saved once all the data has been hidden.
---
To extract the hidden data from the modified signal, you perform the reverse process:


1. **Access the LSB:** Extract the least significant bit for each byte or pixel in the modified signal.

2. **Reconstruct Hidden Data:** Combine the extracted bits to reconstruct the hidden data.

## Images/Output Screens

* **Main Window**
![Main Window](https://i.ibb.co/ryc5K6s/Screenshot-2023-08-18-131135.png)


* **Cover Image**
![Cover Image](https://images.hdqwalls.com/download/mountains-minimalism-16-2880x1800.jpg)


* **Secret Text**
Steganography is the technique of hiding secret data within an ordinary, non-secret, file or message in order to avoid detection; the secret data is then extracted at its destination. The use of steganography can be combined with encryption as an extra step for hiding or protecting data.


* **Secret Image**
![Secret Image](https://s3-alpha.figma.com/hub/file/1407877333/b958324e-d526-4e83-a4c9-abe02c4ea3a6-cover.png)


* **Stego Image/Encrypted Image**
![Secret Image](https://images.hdqwalls.com/download/mountains-minimalism-16-2880x1800.jpg)

* **Text in Image Steganography** **-** When we decode the Stego Image/Encrypted Image, we get the secret text if it is the "Text in Image Steganography" method.

* **Image in Image Steganography** **-** When we decode the Stego Image/Encrypted Image, we get the secret image if it is the "Image in Image Steganography" method.


## Applications
1. **Secure Communication:** Image Steganography finds applications in secure communication by concealing sensitive
messages within innocent-looking images, safeguarding data from unauthorized access.

2. **Data Privacy and Confidentiality:** The mini-project can be utilized to protect data privacy and confidentiality, ensuring that
confidential information remains hidden from prying eyes.

3. **Digital Watermarking:** Image Steganography can be applied to embed digital watermarks into images, helping to
verify the authenticity and ownership of digital media.

4. **Covert Communication:** Steganography enables covert communication, where secret messages can be exchanged in
plain sight without attracting suspicion.

5. **Copyright Protection:** The project's steganographic techniques can be used for copyright protection, embedding
copyright information into digital media to prevent unauthorized use.

6. **Forensics and Investigations:** Image Steganography plays a role in digital forensics and investigations, allowing experts to
analyze hidden information in suspect images.

## References
* [Link for hiding secret text in an image](https://data-flair.training/blogs/python-image-steganography-project/)
* [Link for hiding secret text in an image using MATLAB](https://www.geeksforgeeks.org/lsb-based-image-steganography-using-matlab/)
* [Link for hiding secret image in an image using OpenCV](https://www.geeksforgeeks.org/image-steganography-using-opencv-in-python/?ref=rp)
* [Link for hiding secret text in an image without GUI](https://www.geeksforgeeks.org/image-based-steganography-using-python/)
* [A Guide to Video Steganography Using Python](https://betterprogramming.pub/a-guide-to-video-steganography-using-python-4f010b32a5b7/)
* [Research Paper for References](https://www.ijltet.org/wp-content/uploads/2015/02/60.pdf) 

