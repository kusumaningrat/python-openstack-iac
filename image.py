from conn import get_connection
from dotenv import load_dotenv
import os

conn = get_connection()

def list_images():
    print("List Images: ")

    # get images with images() function
    images = conn.image.images()

    for image in images:
        print(image.id)
        print(image.name)

def upload_image():
    
    # create image metadata
    image_metadata = {
        'name': 'cirros-test',
        'disk_format': 'qcow2',
        'description': 'image cirros test upload with python',
        'container_format': 'bare',
        'visibility': 'private'
    }

    # path to image file
    image_file = open('image/cirros-0.4.0-x86_64-disk.img', 'rb')

    # upload image with create_image() function
    image = conn.image.create_image(
        **image_metadata,
        data=image_file
    )

    image_file.close()

    print('Image Name:', image.name)

def delete_image():
    
    image_id = '872e80ac-cbda-4bdf-9ce3-971c1d31d38c'

    image = conn.image.find_image(name_or_id=image_id)

    conn.image.delete_image(image)

    print('Deleted')

list_images()