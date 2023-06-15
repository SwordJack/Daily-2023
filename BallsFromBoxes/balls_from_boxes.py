#! python3
# -*- encoding: utf-8 -*-
'''
@File    :   balls_from_boxes.py
@Created :   2023/06/12 00:44
@Author  :   SwordJack
@Version :   1.0
@Contact :   https://github.com/SwordJack/

三个完全相同的盒子，一个盒子里面装了两个红球，一个盒子里面装了两个蓝球，一个盒子里面装了一个红球一个蓝球。
从三个盒子中随机选择了一个盒子，从里面拿出了一个球发现是红色的，问这个盒子里剩下的那个球是红色的概率有多大？
'''

# Here put the import lib.
import random

test_time = 6000   # How many times would you like to test?

box_list = [    # A list of boxes containing balls in red or blue.
    ('red', 'red'),
    ('red', 'blue'),
    ('blue', 'blue')
]

results = []    # The result of taking balls.
statistics = {  # We need to count how many first and second balls are in red.
    "first_ball_match": 0,
    "second_ball_match": 0
}

for i in range(test_time):
    box_index = random.randint(0, 2)            # Three boxs, so random from 0 to 2.
    first_ball_index = random.randint(0, 1)     # Each box contains two balls, so random from 0 to 1.
    second_ball_index = 1 - first_ball_index    # Another ball in the box.
    new_result = {          # The result of the current round.
        "box": box_index,
        "first_ball": box_list[box_index][first_ball_index],
        "second_ball": box_list[box_index][second_ball_index],
    }
    results.append(new_result)

    if (new_result["first_ball"] == 'red'):     # Check if the first ball is in red.
        statistics['first_ball_match'] += 1
        if (new_result['second_ball'] == 'red'):    # Check if the second ball is in red.
            statistics['second_ball_match'] += 1
    
    # print('Time: {0:>2}, Box: {1}, First: {2}, Second: {3}'.format(i+1, new_result['box'], new_result["first_ball"], new_result['second_ball']))
    continue

print(statistics)