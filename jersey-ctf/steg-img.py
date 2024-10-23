from PIL import Image

def decode_message_from_alpha(image_path):
    # Load the image
    img = Image.open(image_path)
    pixels = img.load()
    
    # Prepare a variable to hold our extracted binary data
    binary_data = ''
    
    for y in range(img.size[1]):  # iterate over rows
        for x in range(img.size[0]):  # iterate over columns
            pixel = pixels[x, y]
            if len(pixel) == 4:  # Ensure pixel has an Alpha channel
                # Assume message is encoded in the least significant bit of the Alpha channel
                binary_data += str(pixel[3] & 1)

    # Convert binary data to bytes
    byte_data = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    message = ''.join([chr(int(byte, 2)) for byte in byte_data])
    
    return message

# Example usage
image_path = './nicc_aug3.png'
message = decode_message_from_alpha(image_path)
print("Decoded message:", message)

