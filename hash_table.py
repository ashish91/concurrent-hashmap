from hashing_strategy import HashingStrategy

class HashTable:
  def __init__(self, size: int) -> None:
      self.strategy = HashingStrategy()
      self.entry = BuckectEntry()
      self.buckets = []

  def get(key: str) -> str:
    pass

  def put(key: str, val: str) -> None:
    pass
