from scipy import stats
import numpy


def calculate_confidence_interval(data, confidence=0.95):
    """
    Computing the standard error of the mean using sem()
    :param data: Data from Simulation Run
    :param confidence: Confidence Interval
    :return: Sample Mean and Standard error of mean
    """
    if not isinstance(data, list):
        return data, 0
    sample_size = len(data)
    if sample_size == 0:
        return 0, 0
    mean, std_dev = numpy.mean(data), stats.sem(data)

    print("Sample Mean (Generated Using Numpy): {:.4f}".format(mean))
    print("Standard deviation (Numpy Generated): {:.4f}".format(std_dev))

    h = std_dev * stats.t.ppf((1 + confidence) / 2., sample_size - 1)
    return mean, h


def calculate_output_statistics(data):
    print("\nSimulation Output Metrics")
    for key, service_times in data.service_times.items():
        mean, range_mean = calculate_confidence_interval(service_times)
        print("Confidence Interval Workstation {} Block Time: {} ± {} \n".format(key.split('_')[1],
                                                                                 str(mean), str(range_mean)))

    for key, idle_times in data.idle_times.items():
        mean, range_mean = calculate_confidence_interval(idle_times)
        print("Confidence Interval Inspector {} Idle Time: {} ± {} \n".format(key, str(mean), str(range_mean)))

    for key, value in data.block_times.items():
        mean, range_mean = calculate_confidence_interval(value)
        print("Confidence Interval Product {} produced: {} ± {} \n".format(key, str(mean), str(range_mean)))