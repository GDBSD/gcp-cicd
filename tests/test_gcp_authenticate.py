def test_gcp_credentials():
    """If this works GCP can find our credentials"""
    from google.cloud import storage

    # The client library will look for credentials in the environment.
    storage_client = storage.Client()

    # Make an authenticated API request
    buckets = list(storage_client.list_buckets())
    return buckets


if __name__ == '__main__':
    buckets_list = test_gcp_credentials()
    assert len(buckets_list) > 0, 'There are np buckets created for this account.'
