def get_max_min_scores(score_dict):
    return (max(score_dict.values()), min(score_dict.values()))

score_dict = {"Peter": 25, "Jane": 32, "Kathy": 36, "Mark": 28}
max_score, min_score = get_max_min_scores(score_dict)
print(f"Max score: {max_score}, Min score: {min_score}")
