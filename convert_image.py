try:
    from PIL import Image
    import os
    
    # Check if the avif file exists
    if os.path.exists("messi1.avif"):
        print("Found messi1.avif, attempting to convert to JPG...")
        
        # Try to open the image (this may fail if PIL doesn't support AVIF)
        try:
            img = Image.open("messi1.avif")
            # Save as JPG
            img.save("messi1.jpg")
            print("Successfully converted to messi1.jpg")
        except Exception as e:
            print(f"Error converting image: {e}")
            print("You may need to manually convert the AVIF file to JPG.")
    else:
        print("messi1.avif not found. Please provide an image file.")
except ImportError:
    print("PIL (Pillow) library not found. Install with: pip install pillow") 