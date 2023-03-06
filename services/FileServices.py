import os
import uuid


def get_file_path(instance, filename):
    return os.path.join(f'documents/{uuid.uuid4()}', filename)
