import csv
from pathlib import Path

OUT_DIR = '../output'


def write_output(metrics, sim_data, sim_rep):
    Path(OUT_DIR).mkdir(parents=True, exist_ok=True)
    if 'service_time' == metrics:
        for key, value in sim_data.service_times.items():
            with open('{}/{}_{}_R{}.csv'.format(OUT_DIR, metrics, key, sim_rep), 'w', newline='') as file:
                writer = csv.writer(file)
                for data in value:
                    writer.writerow([data])

    if 'idle_time' == metrics:
        for key, value in sim_data.idle_times.items():
            with open('{}/{}_{}_R{}.csv'.format(OUT_DIR, metrics, key, sim_rep), 'w', newline='') as file:
                writer = csv.writer(file)
                for data in value:
                    writer.writerow([data])

    if 'blocked_time' == metrics:
        for key, value in sim_data.block_times.items():
            with open('{}/{}_{}_R{}.csv'.format(OUT_DIR, metrics, key, sim_rep), 'w', newline='') as file:
                writer = csv.writer(file)
                for data in value:
                    writer.writerow([data])

    if 'product' == metrics:
        with open('{}/{}_summary_R{}.csv'.format(OUT_DIR, metrics, sim_rep), 'w') as file:
            for key, value in sim_data.products.items():
                writer = csv.writer(file)
                writer.writerow([key, value])

    if 'batched_time' == metrics:
        for key, value in sim_data.batched_inspector_block_times.items():
            with open('{}/{}_{}_R{}.csv'.format(OUT_DIR, metrics, key, sim_rep), 'w', newline='') as file:
                writer = csv.writer(file)
                for data in value:
                    writer.writerow([data])

        for key, value in sim_data.batched_product_assembled_times.items():
            with open('{}/{}_product_{}_R{}.csv'.format(OUT_DIR, metrics, key, sim_rep), 'w', newline='') as file:
                writer = csv.writer(file)
                for data in value:
                    writer.writerow([data])

    if 'estimators' == metrics:
        for key, value in sim_data.items():
            with open('{}/{}_{}_R{}.csv'.format(OUT_DIR, metrics, key, sim_rep), 'w', newline='') as file:
                writer = csv.writer(file)
                for data in value:
                    writer.writerow([data])

