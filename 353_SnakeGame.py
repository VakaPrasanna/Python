Implement the SnakeGame class:

SnakeGame(int width, int height, int[][] food) and the positions of the food.
int move(String direction) Returns the score of the game after applying one direction move by the snake. If the game is over, return -1

----------------------------------------------------------------------------------------------------------------------------------------
from collections import deque

class SnakeGame:
    def __init__(self, width, height, food):
        self.width = width
        self.height = height
        self.food = food
        self.food_index = 0 #Food appears one after other 
        self.score = 0
        self.snake = deque([(0, 0)])        
        self.body = set([(0, 0)])#Check body collisions, easy to remove tail, snake's body positions can't be duplicated    
        

    def move(self, direction):
        
        head_row, head_col = self.snake[0]
        
        if direction == "U":
            head_row -= 1
        elif direction == "D":
            head_row += 1
        elif direction == "L":
            head_col -= 1
        elif direction == "R":
            head_col += 1

        
        if not (0 <= head_row < self.height and 0 <= head_col < self.width):
            return -1
            
        new_head = (head_row, head_col)
        tail = self.snake[-1]
        
        if new_head in self.body and new_head != tail:
            return -1

        self.snake.appendleft(new_head)
        self.body.add(new_head)

        if (self.food_index < len(self.food) and
                self.food[self.food_index] == [head_row, head_col]):
            self.score += 1
            self.food_index += 1
            
        else:
            
            removed = self.snake.pop()
            self.body.remove(removed)

        return self.score


if __name__ == "__main__":
    w, h = map(int, input("Enter space-separated Width and height: ").split())
    food_input = input("Enter space-separated (row,col):  ").strip().split()
    food = [list(map(int, f.split(','))) for f in food_input]
    game = SnakeGame(w, h, food)
    moves = input("Enter (U/D/L/R) space-separated: ").strip().split()
    print("Outputs:")
    for mv in moves:
        print(game.move(mv))
-----------------------------------------------------------------------------------------------------------------------
Enter space-separated Width and height: 3 2 
Enter space-separated (row,col):  1,2 0,1
Enter (U/D/L/R) space-separated: R D R U L U
Outputs:
0
0
1
1
2
-1
----------------------------------------------------------------------------------------------------------------


353: SnakeGame
----------------------------
width= 3 (cols -> 0,1,2)
height=2 (rows -> 0,1)
food=[ [1,2] , [0,1] ]
moves= R D R U L U
Snake= deque([(0,0)]) -> (head, tail)
body= {(0,0)}
score=0
food_indx=0 

-----------------------------
Move 'R':

head_row, head_col  = (0,0)-> head(0,0)
head(0,1)-> moved Right

#Wall collision Check: 
is 0<=0<2 and 0<=1<3-> True, No wall collision

new_head=(0,1)
tail=(0,0)

#Snake body Collision Check:
new_head(0,1) -> is in body= {(0,0)}= false, no body collision

Snake= deque( [(0,1), (0,0)] ) -> head, tail
body= { (0,0), (0,1) }

is food_indx=0 < 2: yes
     is food[0]->[1,2]== [0,1]: no food, so remove tail
             removed=snake(0,0)
             Snake= deque([(0,1)]) -> head, tail
             body= {(0,1)}

return "score=0"
----------------------------------------
Now:

head(0,1), tail(0,1), body= {(0,1)}
Snake= deque([(0,1)]) -> head, tail
body= {(0,1)}
food=[ [1,2] ], score=0

Move 'D':

head(1,1)-> moved Down

#Wall collision Check:
is 0<=1<2 and 0<=1<3-> True, No wall collision

new_head=(1,1)
tail=(0,1)

#Snake body Collision Check:
new_head(1,1) -> is in body= {(0,1)}= false, no body collision

Snake= deque( [(1,1), (0,1)] )
body= { (0,1), (1,1) }

is food_indx=0 < 2: yes
     is food[0]->[1,2]== [1,1]: no food, so remove tail
             removed=snake(0,1)
             Snake=([(1,1)])
             body= {(1,1)}

return "score=0"
-----------------------------------------------------------
Now:

head(1,1), tail(1,1), body= {(1,1)}
Snake= deque([(1,1)]) -> head, tail
body= {(1,1)}
food=[ [1,2] ], score=0


Move 'R':

head(1,2)-> moved Right

#Wall collision Check:
is 0<=1<2 and 0<=2<3-> True, No wall collision

new_head=(1,2)
tail=(1,1)

#Snake body Collision Check:
new_head(1,2) -> is in body= {(1,1)}= false, no body collision

Snake= deque( [(1,2), (1,1)] ) -> head, tail
body= { (1,2), (1,1) }

is food_indx=0 < 2: yes
     is food[0]->[1,2]== [1,2]: yes food, so update score 
             score=1
             food_indx=1->next food appears at [0,1](row,col)

return "score=1"
-----------------------------------------------------


                         








