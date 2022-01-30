from strategies.simple_hashing_strategy import SimpleHashingStrategy

class HashingStrategy:

  def __init__(self) -> None:
    self.strategy = SimpleHashingStrategy()

  def generate_hash(self, key: str) -> int:
    return self.strategy.generate_hash(key)
