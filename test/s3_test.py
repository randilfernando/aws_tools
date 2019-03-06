import aws.s3 as s3

if __name__ == '__main__':
    bucket_downloader = s3.BucketDownloader('ustocktrade-trade-analysis')
    bucket_downloader.download_file('Test/test.txt', '../test-files/test.txt')
