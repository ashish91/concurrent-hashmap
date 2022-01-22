from bucket_entry import BucketEntry
from bucket_item import BucketItem
from data_structures.linked_list import LinkedList

class LinkedListEntry(BucketEntry):

  def __init__(self) -> None:
    self.list = LinkedList()

  def insert(self, key: int, value: str) -> None:
    self.list.add(BucketItem(key,value))

  def get(self, key: int) -> None:
    self.list.search(key)
