from typing import List
# Write any import statements here


def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  # Write your code here

  class Cell:
    def process(self, other):
      return 0

    def getPA(self):
      return 0

    def getBA(self):
      return 0


  class A(Cell):
    P=0
    B=0    
    def getPA(self):
      return self.P
    
    def getBA(self):
      return self.B

    def process(self, other):
      if isinstance(other, P):
        self.P += 1
      elif isinstance(other, B):
        self.B += 1
      return 0

  class B(Cell):
    total=0
    def process(self, other):
      return other.getPA()

  class P(Cell):
    total=0
    def process(self, other):
      return other.getBA()

  class Dot(Cell):
    pass
  
  cells: List[Cell] = list()
    
  for cell in C:
    if cell == 'P':
      cells.append(P())
    elif cell == 'A':
      cells.append(A())
    elif cell == 'B':
      cells.append(B())
    elif cell == '.':
      cells.append(Dot())

  total = 0
      
  for index, cell in enumerate(cells):
    for nextIndex, nextCell in enumerate(cells):
      if nextIndex - index > Y:
        break
      if nextIndex > index and nextIndex - index >= X:
        total += cells[nextIndex].process(cell)

  return total
