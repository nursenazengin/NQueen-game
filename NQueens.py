import random

#class definition 
# for NQueens
class NQueens():
    
    def __init__(self, N):
        self.N = N
        self.state = self._set_state()
        
        
        
    def __str__(self):
        return f"N: {self.N}, state: {self.state}"
     
    def _set_state(self):
        print("How do you want to set state\n1. Set state manually\n2. Set state randomly")
        select = int(input("Enter selection: "))
        if select == 1:
                  state = input("Enter state: ")  
                  if self._is_valid(state) != True:
                      return self.generate_random_state()
                      print("Invalid state! Try again")
                  return state
        elif select == 2:
                  return self.generate_random_state()
        else:
                  print("Invalid selection")
                       

    
    def generate_random_state(self):
            state = ""
            for i in range(self.N):
                state += str(random.randint(1, self.N))
            return state
        
    

    def _is_valid(self,state):
              if state.isdigit() == False and len(state) != self.N:
                     return False 
              else:
                    for i in state:
                        if 1 <= int(i) <= self.N:
                           return True
                        else:
                           return False
        
 
    def _count_attacking_pairs(self, state):
        count = 0
        counts = {}
        for c in state:
          counts[c] = counts.get(c, 0) + 1
        comb1 = 0
        for v in counts.values():
          if v > 1:
            comb1 += v * (v - 1) // 2
        
        consecutive = []
        for i in range(len(state)):
          if state[i].isdigit():
            if consecutive and state[i] == str(int(state[i-1]) + 1):
              consecutive[-1] += 1
            else:
              consecutive.append(1)
        comb2 = 0

        for n in consecutive:
            comb2 += n * (n - 1) / 2
        
        consecutive2 = []
        for i in range(len(state)):
          if state[i].isdigit():
            if consecutive2 and state[i] == str(int(state[i-1]) - 1):
              consecutive2[-1] += 1
            else:
              consecutive2.append(1)
        comb3 = 0

        for n in consecutive2:
            comb3 += n * (n - 1) / 2
 
        count = comb1 + comb2 + comb3
        return (count)   
                  
    
# This is a test code. You can try with different N values and states.
problem = NQueens(5) #create NQueens instance
print(problem) #print the description of the problem
print(problem._count_attacking_pairs(problem.state)) #print the total number of attacking pairs in the board 
