import sys
from PIL import Image, ImageOps


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_ext = sys.argv[1].lower().split(".")[-1]
    output_ext = sys.argv[2].lower().split(".")[-1]

    valid_extensions = ["jpg", "jpeg", "png"]

    if input_ext not in valid_extensions:
        sys.exit("Invalid input")
    if output_ext not in valid_extensions:
        sys.exit("Invalid output")
    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

    overlay_shirt(sys.argv[1], sys.argv[2])


def overlay_shirt(input_file, output_file):
    try:
        shirt = Image.open("took.png")
        with Image.open(input_file) as input_img:
            input_cropped = ImageOps.fit(input_img, shirt.size)
            input_cropped.paste(shirt, shirt)
            input_cropped.save(output_file)
    except FileNotFoundError:
        sys.exit("Input does not exist")


if __name__ == "__main__":
    main()
