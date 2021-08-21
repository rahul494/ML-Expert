def get_statistics(input_list):

    stats = {
        "mean": 0,
        "median": 0,
        "mode": 0,
        "sample_variance": 0,
        "sample_standard_deviation": 0,
        "mean_confidence_interval": [0, 0],
    }

    stats["mean"] = sum(input_list) / len(input_list)

    if len(input_list) % 2 == 0:
        stats["median"] = (input_list[len(input_list)/2 - 1] +
                           input_list[len(input_list)/2]) / 2.0
    else:
        stats["median"] = input_list[len(input_list)/2]
    return stats


print(get_statistics([2, 1, 3, 4, 4, 5, 6, 7]))
