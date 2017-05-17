#Description

3. The washing machine
Design and implement a control module to adjust the washing cycle for a washing machine. The
wash cycle (delicate, easy, normal, intense) depends on the texture of clothes (very soft, soft, normal,
resistant) and the amount of clothes loaded in the car (small, medium, high)

##Description of the solution:
###Input Variables
- X = Texture
    - L = {very soft, soft, normal, resistant}
    - U = {x | 0 <= x <= 1}
- Y = Wash load
    - L = {small, mediu, high}
    - U = {y | 0 <= y <= 1}


###Output
- Z = (the washing cycle)
    - L = {delicate, easy, normal, intense}
