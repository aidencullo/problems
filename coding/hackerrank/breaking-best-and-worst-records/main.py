def breakingRecords(scores):
    min_record = scores[0]
    max_record = scores[0]
    min_count = 0
    max_count = 0
    for score in scores:
        if score < min_record:
            min_record = score
            min_count += 1
        elif score > max_record:
            max_record = score
            max_count += 1
    return max_count, min_count
