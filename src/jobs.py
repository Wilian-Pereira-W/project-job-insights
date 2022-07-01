from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as jobs_file:
        jobs_list = csv.DictReader(jobs_file)
        results = []
        for jobs in jobs_list:
            results.append(jobs)

    return results
