from utils import batch_handler
from utils import format_handler
from utils import batch_handler
from utils import filter_handler
import cv2 as cv

if __name__ == "__main__":
    batch_handler.process()
    cv.imwrite(
        "color_img.jpg",
        (
            filter_handler.grey_scale(
                format_handler.path_to_image("images/input/images.jpeg")
            )
        ),
    )
    print(f"SIZE: {batch_handler.file_size("images/input/20.jpg")}")
    print(f"SIZE: {batch_handler.file_size("images/input/A13.jpg")}")
    print(f"SIZE: {batch_handler.file_size("images/input/images.jpeg")}")
    print(
        f"SIZE: {batch_handler.file_size("images/input/German-Shepherd-dog-Alsatian.webp")}"
    )
    print(f"SIZE: {batch_handler.file_size("images/input/example.txt")}")
