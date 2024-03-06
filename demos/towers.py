# Towers of Hanoi
# source: https://www.geeksforgeeks.org/python-program-for-tower-of-hanoi/ 
# Recursive Python function to solve the tower of hanoi


def TowerOfHanoi(n, start, end, helper):
  # base case
  if n == 1:
    print("Move disk 1 from", start, "to", end)
  
  # recursive step
  else: 
    TowerOfHanoi(n-1, start, helper, end)
    print("Move disk", n, "from", start, "to", end)
    TowerOfHanoi(n-1, helper, end, start)
  
def main():
  n = 4
  TowerOfHanoi(n, 'A', 'C', 'B')
  #A, B, C names of rods 

if __name__ == "__main__":
  main()
