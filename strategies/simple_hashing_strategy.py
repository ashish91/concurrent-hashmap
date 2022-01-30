class SimpleHashingStrategy:
  PRIME = 2069

  def generate_hash(self, key: str) -> int:
    code = 0
    N = len(key)
    for i in range(N):
      c = key[i]
      code += (ord(c)*i)

    return code%2069
