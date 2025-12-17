from google.cloud import storage
def download_from_gcs(gs_path, local_path):
    """
    gs_path: gs://bucket-name/path/to/file.xlsx
    local_path: /tmp/file.xlsx
    """
    assert gs_path.startswith("gs://")

    path = gs_path.replace("gs://", "", 1)
    bucket_name, blob_name = path.split("/", 1)

    client = storage.Client()
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(blob_name)


    blob.download_to_filename(local_path)
