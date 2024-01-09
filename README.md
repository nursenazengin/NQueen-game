# NQueen-game
N  Queens  Problem:“This  is  the  problem  of  placing  N  chess  queens  on  an  NxN  chessboard  so  that  no queens threaten each other;thus, a solution requires that no two queens share the same row, column, or diagonal.” (Wikipedia)The most common form of this problem is 8-Queens.
According  to  the  problem  definition, a  solution  requires  that  no  two  queens  share  the  same  row, column,  or  diagonal.Our  representation  of  the  problem  already  restricts  any  two  queens  to  be  on  the same  column. Thus, you don’t have to check for columns. You should check the rows and  diagonals  in  both  directions.You  may usemathmodulefor  implementation.The calculation of number of attacking pairs.
Allowed to move a single queen in its column at each step and each move is of cost 1.In other words, each action will be in the form of “Move Queen 𝑖to row 𝑗”, where 1≤𝑖,𝑗≤𝑁.
There are 3main functions(actions, is_goal, result)that i have to implement for uninformed search  algorithms,  and  one  function  (heuristic)  for  informed  search algorithms.
to make the problem solvable by local search algorithms.
