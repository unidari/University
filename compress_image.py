from PIL import Image


def compress_img(option, images, compression):
    if compression in range(1, 101):
        if option == 0:
            for i in list(images.values()):
                image_file = Image.open(i)
                image_file.save('compressed-' + i, quality=compression)
                print(f'Изображение {i} сжато')
        else:
            if type(images) is dict:
                image = images.get(option)
                image_file = Image.open(image)
                image_file.save('compressed-' + image, quality=compression)
                print(f'Изображение {image} сжато')
            else:
                for i in images:
                    image_file = Image.open(i)
                    image_file.save('compressed-' + i, quality=compression)
                    print(f'Изображение {i} сжато')
    else:
        print('Ошибка сжатия!')