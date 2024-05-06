def read_input():
    my_file = open('input_3_cap1.txt','r')
    return my_file

def calculate_score(point):
    score = {'A X': 2, 'A Y': 4, 'A Z': 9, 'B X': 1, 'B Y': 5, 'B Z': 7, 'C X': 1, 'C Y': 6, 'C Z': 7}
    total_score = 0
    for line in point:
        key = line.strip()
        value_in_dict = score.get(key, None)
        if value_in_dict is not None:
            total_score += value_in_dict
    print("Total score :", total_score)


calculate_score(read_input())
