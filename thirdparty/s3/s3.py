import os
from uuid import uuid4

from django.core.files.storage import default_storage
from rest_framework.exceptions import ValidationError

from config import settings
from config.settings.base import AWS_S3_CUSTOM_DOMAIN, AWS_STORAGE_BUCKET_NAME, AWS_UPLOAD_BASE_URL


def upload(image):
    if not image:
        raise ValidationError('Image is required')

    name, extension = os.path.splitext(image.name)
    if extension.lower() not in ['.jpg', '.jpeg', '.png']:
        raise ValidationError('Image must be JPEG or PNG')

    if image.content_type not in ['image/jpeg', 'image/jpg', 'image/png']:
        raise ValidationError('Invalid image content type')

    try:
        path = f'{str(uuid4())}{extension}'
        join_path = os.path.join(settings.base.IMAGE_ROOT, path)
        save = default_storage.save(join_path, image)
        s3path = f'https://{AWS_UPLOAD_BASE_URL}/{save}'
    except Exception as e:
        raise ValidationError(f'Error saving image: {e}')

    return s3path
