# Write any import statements here

def getArtisticPhotographCount(N: int, C: str, X: int, Y: int) -> int:
  # Write your code here
  return explore("", C, 0, X, Y)

def explore(running_photo, remaining, running_distance, X, Y):
  if len(running_photo) == 3:
    return 1
  if not remaining:
    return 0
    
  photos = 0
  current_photo = running_photo + remaining[0]
  remaining = remaining[1:]
    
  if is_artistic_photo(current_photo, running_distance, X, Y):
    photos += explore(current_photo, remaining, 1, X, Y)
  photos += explore(running_photo, remaining, running_distance + 1, X, Y)
  return photos

def is_artistic_photo(current_photo, running_distance, X, Y):
  return (is_photo(current_photo) and is_artistic(running_distance, X, Y))


def is_photo(current):
  return current in combinations

def is_artistic(distance, X, Y):
  return distance in list(range(X, Y + 1))

combinations = [
    "P",
    "B",
    "BA",
    "PA",
    "PAB",
    "BAP",
]
