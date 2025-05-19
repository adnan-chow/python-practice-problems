from PIL import Image

def convert_to_grayscale(input_path, output_path):
    image = Image.open(input_path)
    grayscale_image = image.convert("L")
    grayscale_image.save(output_path)
    return f"Saved grayscale image to {output_path}"

# Test the function (assume input.jpg exists)
print(convert_to_grayscale("input.jpg", "output.jpg"))