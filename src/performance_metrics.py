from scipy import stats
import numpy
import utils

estimators = {
    "I1": [],
    "I2_C2": [],
    "I2_C3": [],
    "WS1": [],
    "WS2": [],
    "WS3": []
}


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


def calculate_throughput(datatotal):
    simulation_time = 24800
    return datatotal / simulation_time


def calculate_proportion_blocked_time(data):
    simulation_time = 28800
    datatotal = 0
    for i in range(0, len(data)):
        datatotal += float(data[i])
    proportion_blocked_time = datatotal / simulation_time

    return proportion_blocked_time


def calculate_total_average(data, replications_count):
    datatotal = 0
    for i in range(0, len(data)):
        datatotal += float(data[i])

    return datatotal / replications_count


def calculate_average_across_replications(data):
    replications_count = 0
    insp_1_blocked_times = []
    insp_blocked_times_2 = []
    insp_blocked_times_3 = []
    products_produced_1 = []
    products_produced_2 = []
    products_produced_3 = []

    for variable in data:
        insp_1_blocked_times.append(calculate_proportion_blocked_time(variable.block_times[1]))
        estimators["I1"].append(calculate_proportion_blocked_time(variable.block_times[1]))

        insp_blocked_times_2.append(calculate_proportion_blocked_time(variable.block_times[2]))
        estimators["I2_C2"].append(calculate_proportion_blocked_time(variable.block_times[2]))

        insp_blocked_times_3.append(calculate_proportion_blocked_time(variable.block_times[3]))
        estimators["I2_C3"].append(calculate_proportion_blocked_time(variable.block_times[3]))

        products_produced_1.append(calculate_throughput(variable.products[1]))
        estimators["WS1"].append(calculate_throughput(variable.products[1]))

        products_produced_2.append(calculate_throughput(variable.products[2]))
        estimators["WS2"].append(calculate_throughput(variable.products[2]))

        products_produced_3.append(calculate_throughput(variable.products[3]))
        estimators["WS3"].append(calculate_throughput(variable.products[3]))
        replications_count = replications_count + 1

    print("Replications: {}".format(replications_count))
    print("Inspector 1 (Blocked/Idle Time) Proportion: {} \n".
          format(calculate_total_average(insp_1_blocked_times, replications_count)))
    print("Inspector 2 (C2) (Blocked Time/Component) Proportion: {} \n".
          format(calculate_total_average(insp_blocked_times_2, replications_count)))
    print("Inspector 2 (C3) (Blocked Time/Component) Proportion: {} \n".
          format(calculate_total_average(insp_blocked_times_3, replications_count)))
    print("WS1 Throughput Average/Mean: {} \n".format(calculate_total_average(products_produced_1, replications_count)))
    print("WS2 Throughput Average/Mean: {} \n".format(calculate_total_average(products_produced_2, replications_count)))
    print("WS3 Throughput Average/Mean: {} \n".format(calculate_total_average(products_produced_3, replications_count)))

    utils.write_output("estimators", estimators, replications_count)


def calculate_statistics_across_replications(data):
    index = 0
    idle_times_1 = []
    idle_times_2 = []
    idle_times_3 = []
    products_produced_1 = []
    products_produced_2 = []
    products_produced_3 = []

    for variable in data:
        idle_times_1.extend(variable.block_times[1])
        idle_times_2.extend(variable.block_times[2])
        idle_times_3.extend(variable.block_times[3])
        products_produced_1.append(variable.products[1])
        products_produced_2.append(variable.products[2])
        products_produced_3.append(variable.products[3])
        index = index + 1

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
    for key, idle_times in data.block_times.items():
        mean, range_mean = calculate_confidence_interval(idle_times)
        print("Confidence Interval Inspector {} Blocked Time: {} ± {} \n".format(key, str(mean), str(range_mean)))

    for key, value in data.products.items():
        mean, range_mean = calculate_confidence_interval(value)
        print("Confidence Interval Product {} produced: {} ± {} \n".format(key, str(mean), str(range_mean)))
