import os
import aws.cli as aws_cli


class BucketDownloader:
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name

    def download_file(self, source, dest):
        if not os.path.exists(os.path.dirname(dest)):
            os.makedirs(os.path.dirname(dest))

        aws_cli.run_command(['s3', 'cp', 's3://%s/%s' % (self.bucket_name, source), dest])

    def download_directory(self, source_dir, dest_dir):
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        aws_cli.run_command(['s3', 'cp', 's3://%s/%s' % (self.bucket_name, source_dir), dest_dir, '--recursive'])
