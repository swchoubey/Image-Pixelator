# Image Pixelator

This Python script utilizes Pillow to transform images into their pixelated versions. It's a simple program that takes an image as input, resizes it, extracts each color from the smaller image, and uses these colors to create a pixelated representation.

### Expected Outcome

<img src = "https://github.com/swchoubey/Image-Pixelator/assets/97143500/774321a6-06a9-4345-b77b-869386203d34" width="100">
<img src = "https://github.com/swchoubey/Image-Pixelator/assets/97143500/2be7939c-a94e-4b27-90e2-c1ec3a9fb9b6" width="100">
<img src = "https://github.com/swchoubey/Image-Pixelator/assets/97143500/e7f00ef2-0f35-411d-b6ca-0fdd85ac6fec" width="100">

## Usage

1. Clone the Repository
2. Install Requirements

`pip install -r requirements.txt`

3. Pass the required arguments via the command line using sys.argv. For example:

`python generate_pixels.py sample.jpg pix.jpg 64`

Note: If you want to input a URL via the command line, add an extra parameter after the last one (e.g., a single letter) to indicate it is a URL and not a file.

## Creating Color Palettes

You can leverage this script to generate color palettes from an image. Follow the same process as pixelating, but use a smaller number of columns (e.g., 6 or 10) to obtain unique palettes for each image.
The resulting image will contain a limited set of colors. By making slight adjustments to the code, you can extract the RGB values of each pixel if needed. For example, the palette above was generated using the following:

`python generate_pixels.py sample.jpg palette.jpg 6`

Feel free to explore and experiment with different images, sizes, and color palettes!

