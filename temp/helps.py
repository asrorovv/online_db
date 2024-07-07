import uuid



class SaveMedia(object):
    def save_book(instance, file_name):
        image_path = file_name.split('.')[-1]
        return f'pic/{uuid.uuid4()}.{image_path}'

