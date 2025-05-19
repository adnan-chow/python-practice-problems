def isLandscape(width, height):
    if width > height:
        return "Landscape"
    else:
        return "Portrait"

# Example usage
print(isLandscape(1920, 1080))  # Landscape
print(isLandscape(720, 1280))   # Portrait
