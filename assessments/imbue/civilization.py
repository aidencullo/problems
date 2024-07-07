import sys

def read_file():
    if len(sys.argv) != 2:
        print("Usage: python read_file.py <filename>")
        sys.exit(1)
    
    filename = sys.argv[1]
    
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except IOError:
        print(f"Error: Could not read file '{filename}'.")
    return content

def build_grid(input_str):
    grid = []
    for line in input_str.split('\n'):
        grid.append(list(line))
    return [line for line in grid if line]

class Agent:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def location(self):
        return (self.x, self.y)

def simulate(grid):
    if is_stable(grid):
        return 0
    agents = [Agent(x, y) for y, line in enumerate(grid) for x, space in enumerate(line) if space == 'A']
    for agent in agents:
        print(agent.location)
    
def is_stable(grid):
    return not any(space == 'A' for line in grid for space in line)

def main():
    input_str = read_file()
    grid = build_grid(input_str)
    print(simulate(grid))
        
if __name__ == "__main__":
    main()
