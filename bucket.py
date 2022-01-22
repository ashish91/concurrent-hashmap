from bucket.bucket_entry import BucketEntry


from bucket.linked_list_entry import LinkedListEntry

class Bucket:

  def __init__(self, size: int) -> None:
    self.buckets = [LinkedListEntry()] * size

  def put(self, index: int, key: str, value: str) -> None:
    self.buckets[index].insert(key, value)

  def get(self, index: int, key: str) -> str:
    return self.buckets[index].get(key)
