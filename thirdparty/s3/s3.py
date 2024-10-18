import os
from uuid import uuid4

from django.core.files.storage import default_storage

from bigbro.exception.CustomException import CustomException
from bigbro.settings import IMAGE_ROOT


class S3Client:
    def upload(self, image):
        if not image:
            raise ValueError('image is empty')

        extension = image.split('.')[-1]

        try:
            bucket_domain = '%s.s3.%s.amazonaws.com' % (
                os.environ.get("AWS_STORAGE_BUCKET_NAME"),
                os.environ.get('AWS_REGION_NAME')
            )

            path = f'{str(uuid4())}{extension}'
            join_path = os.path.join(IMAGE_ROOT, path)
            save = default_storage.save(join_path, image)
            s3path = f'https://{bucket_domain}/{save}'
        except Exception as e:
            raise CustomException.S3UnExpectedError

        return s3path