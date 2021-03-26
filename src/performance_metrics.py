from scipy import stats
import numpy


def calculate_confidence_interval(data, confidence=0.95):
    """
    Confidence Interval Estimation

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
    mean, std_error = numpy.mean(data), stats.sem(data)

    print("Sample Mean (Generated Using Numpy): {}".format(mean))
    print("Standard Error (Generated Using Scipy): {}".format(std_error))

    # Calculate the confidence intervals using calculated margin of error
    error_range = std_error * stats.t.ppf((1 + confidence) / 2., sample_size - 1)
    return mean, error_range


def calculate_replication_average(data):
    """
    Mainly focused on collection of Estimators for Throughput/Products Produced & Inspector Idle Time
    :param data: Simulation Output
    :return:
    Prints the Average and Variance of the simulation output
    """
    for key, value in data.block_times.items():
        print("Inspector {} (Idle Time/Component) Average/Mean: {} \n".format(key, numpy.mean(value)))
    for key, value in data.products.items():
        print("Product {} (produced in 8 hour period) Average/Mean: {} \n".format(key, numpy.mean(value)))

def calculate_statistics_across_replications(data):
    idle_times_1 = []
    idle_times_2 = []
    idle_times_3 = []
    products_produced_1 = []
    products_produced_2 = []
    products_produced_3 = []

    for variable in data:
        idle_times_1.extend(variable.idle_times[1])
        idle_times_2.extend(variable.idle_times[2])
        idle_times_3.extend(variable.idle_times[3])
        products_produced_1.append(variable.products[1])
        products_produced_2.append(variable.products[2])
        products_produced_3.append(variable.products[3])

    m, h = calculate_confidence_interval(idle_times_1)
    print("Confidence interval for inspector 1 block times is " + str(m) + " ±" + str(h) + "\n")
    m, h = calculate_confidence_interval(idle_times_2)
    print("Confidence interval for inspector 2 block times is " + str(m) + " ±" + str(h) + "\n")
    m, h = calculate_confidence_interval(idle_times_3)
    print("Confidence interval for inspector 3 idle times is " + str(m) + " ±" + str(h) + "\n")
    m, h = calculate_confidence_interval(products_produced_1)
    print("Confidence interval for product 1 produced in 8 hrs is " + str(m) + " ±" + str(h) + "\n")
    m, h = calculate_confidence_interval(products_produced_2)
    print("Confidence interval for product 2 produced in 8 hrs is " + str(m) + " ±" + str(h) + "\n")
    m, h = calculate_confidence_interval(products_produced_3)
    print("Confidence interval for product 3 produced in 8 hrs is " + str(m) + " ±" + str(h) + "\n")


def calculate_output_statistics(data):
    """
    Mainly focused on Collection of CI for Throughput/Products Produced & Inspector Idle Time
    :param data: Simulation Output
    :return:
    Prints the Mean/Average and Standard Error
    """
    print("\nSimulation Output Metrics")
    for key, idle_times in data.idle_times.items():
        mean, range_mean = calculate_confidence_interval(idle_times)
        print("Confidence Interval Inspector {} Idle Time: {} ± {} \n".format(key, str(mean), str(range_mean)))

    for key, value in data.products.items():
        mean, range_mean = calculate_confidence_interval(value)
        print("Confidence Interval Product {} produced: {} ± {} \n".format(key, str(mean), str(range_mean)))
