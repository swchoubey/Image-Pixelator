from PIL import Image as img
import sys
import requests

def saveFromURL(url, path):
    try:
        with open(path, "wb") as handle:
            response = requests.get(url, stream=True)

            if not response.ok:
                return
            
            for pixel in response.iter_content(8192):
                if not pixel:
                    break
                handle.write(pixel)

        return True
    except:
        return False
    
def main(src, dst, columns=50, url=False):
    ## src = path or url of image, dst = location it is being saved to, columns regulate the number of pixels in the generated image

    if url:
        if not saveFromURL(src, dst):
            return
        file = dst

    else:
        file = src

    initial = img.open(file, "r")

    rows = int(initial.height / (initial.width/columns))
    resized = initial.resize((columns, rows))

    output_image_width = initial.width + (columns - initial.width % columns)
    output_image_height = initial.height + (rows - initial.height % rows)

    pixelated = img.new("RGB", (output_image_width, output_image_height), "red")

    width_ratio = output_image_width // resized.width
    height_ratio = output_image_height // resized.height

    finish_w = 0
    finish_h = 0

    for x in range(resized.width):
        finish_w += width_ratio

        for y in range(resized.height):
            pix_color = resized.getpixel((x,y))

            finish_h += height_ratio

            for w in range(finish_w - width_ratio, finish_w + 1):
                if w >= pixelated.width:
                    continue

                for h in range(finish_h - height_ratio, finish_h + 1):
                    if h >= pixelated.height:
                        continue
                    pixelated.putpixel((w, h), pix_color)

        finish_h = 0

    pixelated.save(dst)

if __name__ == "__main__":
    arguments = sys.argv
    if arguments[1]:
        src = arguments[1]
        dst = arguments[2]
        col = int(arguments[3])
        is_url = False

        if len(arguments) > 4:
            is_url = True

        main(src, dst, col, is_url)

    else:
        pass
