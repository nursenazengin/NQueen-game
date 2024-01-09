from simpleai.search import SearchProblem, astar
from simpleai.search.models import SearchProblem
from simpleai.search.traditional import breadth_first, depth_first, uniform_cost, limited_depth_first, iterative_limited_depth_first, greedy, astar 
from simpleai.search.local import hill_climbing, hill_climbing_random_restarts, genetic
import random
from timeit import default_timer as timer


def string_to_list(string_):
         return [int(x) for x in string_]
def list_to_string(list_):
    return ''.join(map(str, list_))


class NQueens(SearchProblem):
    def __init__(self, N):
        self.N = N
        self.initial_state = self._set_state()
        
        
        
    def __str__(self):
        return f"N: {self.N}, state: {self.initial_state}"
     
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
    
    
    def actions(self, state):
      state_list = string_to_list(state)
      n = [i for i in range(1, self.N + 1)] 
      possible_actions = []
      a = []
      haha ="" 
      for j in range(self.N):
          a =[]
          for i in n:
              if i != state_list[j]:
                  a.append(i)
              else: continue
          for p in a:
              haha = f"move queen {state_list[j]} to row {p}"
              possible_actions.append(haha)
      return possible_actions
    

    def result(self,state,action):
        state_list = string_to_list(state)  
        
        digit_list = [int(char) for char in action if char.isdigit()]
        
        queen = digit_list[0] 
        row = digit_list[1]
       
        state_list[queen-1] = row
        self.state = list_to_string(state_list) 
        return self.state

    

    def is_goal(self, state):
        if self._count_attacking_pairs(state) == 0:
            return True
        else:
            return False
        

    def heuristic(self,state):
        heuristic_function = self._count_attacking_pairs(state)
        return heuristic_function
    

    def value(self, state):
        count = 0
        a = 0
        
        counts = {}
        for c in state:
          counts[c] = counts.get(c, 0) + 1
        for v in counts.values():
          if v > 1:
              a = a + 2
        number1 = len(state) - a
        count1 = (number1 * (number1 - 1)) / 2

        consecutive = []
        for i in range(len(state)):
          if state[i].isdigit():
            if consecutive and state[i] == str(int(state[i-1]) + 1):
              consecutive[-1] += 1
            else:
              consecutive.append(1) 
        b = 0
        if(max(consecutive) != 1):
          max1 = max(consecutive)
          b += max1
        number2 = len(state) - b
        count2 = (number2 * (number2 - 1)) / 2

        consecutive2 = []
        for i in range(len(state)):
          if state[i].isdigit():
            if consecutive2 and state[i] == str(int(state[i-1]) - 1):
              consecutive2[-1] += 1
            else:
              consecutive2.append(1)
        c = 0
        if(max(consecutive2) != 1):
          max2 = max(consecutive2)
          c += max2
        number3 = len(state) - c
        count3 = (number3 * (number3 - 1)) / 2

        count = count1 + count2 + count3
        return count           
    
    def crossover(self, state1, state2):
        state3 = ""
        if len(state1) == len(state2):
            n = random.randint(1, len(state1) - 1)
            state3 = state1[:n] + state2[n:]
        return state3 
    
    def mutate(self, state): 
        m = random.randint(1, len(state) - 1)
        s = random.randint(1, 9)
        state3 = state[:m] + str(s) + state[m + 1:]
        if(state3 != state):
           state3 = state[:m] + str(s) + state[m + 1:]        
        return state3 
   

problem = NQueens(4) 
print(problem) 
print(problem._count_attacking_pairs(problem.initial_state)) 
print("All possible actions from initial state: ", problem.actions(problem.initial_state))
print("A* Algorithm with Tree Search: ")
start = timer()
result = astar(problem)
print("Resulting path: " , result.path())
print("Total cost: ", result.cost)
print("Resulting state: ", result.state)
print("Correct solution? ", problem.is_goal(result.state))
end = timer()
print(f"Time taken {end-start} seconds.")
print("number of non-attacking pairs : ",problem.value(problem.initial_state))
state1 = problem.generate_random_state()
state2 = problem.generate_random_state()
print("state1 : ",state1 , "state2 : ", state2)
print("crossover state: ",problem.crossover(state1,state2)) 
print("mutation state : ",problem.mutate(problem.crossover(state1,state2)))
start = timer()
resultt = hill_climbing(problem)
print("hill climbing search : ", resultt)
end = timer()
print(f"Time taken {end-start} seconds.")

