# Image Pixelator

This Python script utilizes Pillow to transform images into their pixelated versions. It's a simple program that takes an image as input, resizes it, extracts each color from the smaller image, and uses these colors to create a pixelated representation.

### Original Image

<p align = "center">
![strawbs](https://github.com/swchoubey/Image-Pixelator/assets/97143500/9fc1a172-d8dc-4f15-b14c-ed5ccb8007a1)
</p>

### Pixelated Image

<p align = "center">
  ![pix](https://github.com/swchoubey/Image-Pixelator/assets/97143500/02d7f666-7f2d-45eb-ac89-c647bdd94019)
</p>

### Extracting Color Palette

<p align = "center">
  ![pallette](https://github.com/swchoubey/Image-Pixelator/assets/97143500/349fb2c4-f257-43cf-8157-e31479eb13d8)
</p>

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

