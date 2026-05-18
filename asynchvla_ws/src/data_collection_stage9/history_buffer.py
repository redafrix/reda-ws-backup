from __future__ import annotations
from collections import deque
class HistoryBuffer:
    def __init__(self, k:int=4): self.k=int(k); self.buf=deque(maxlen=self.k)
    def append(self, item:dict): self.buf.append(dict(item))
    def to_list(self): return list(self.buf)
    def __len__(self): return len(self.buf)
