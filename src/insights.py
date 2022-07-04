from src.jobs import read


def get_unique_job_types(path):
    results = read(path)
    unique_job_types = []

    for job in results:
        if job["job_type"] != "":
            unique_job_types.append(job["job_type"])

    return list(set(unique_job_types))


def filter_by_job_type(jobs, job_type):
    job_types = []

    for job in jobs:
        if job["job_type"] == job_type != "":
            job_types.append(job)

    return job_types


def get_unique_industries(path):
    results = read(path)
    unique_industries = []

    for job in results:
        if job["industry"] != "":
            unique_industries.append(job["industry"])

    return list(set(unique_industries))


def filter_by_industry(jobs, industry):
    industry_list = []

    for job in jobs:
        if job["industry"] == industry != "":
            industry_list.append(job)

    return industry_list


def get_max_salary(path):
    results = read(path)
    max_salary = []

    for job in results:
        if job["max_salary"].isdigit():
            max_salary.append(int(job["max_salary"]))

    return max(max_salary)


def get_min_salary(path):
    results = read(path)
    min_salary = []

    for job in results:
        if job["min_salary"].isdigit():
            min_salary.append(int(job["min_salary"]))

    return min(min_salary)


def matches_salary_range(job, salary):

    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError(
            "A chave min_salary ou max_salary estão ausentes no dicionário"
        )
    if type(job["min_salary"]) != int or type(job["max_salary"]) != int:
        raise ValueError(
            "A chave min_salary ou max_salary tem valores não-numéricos"
        )
    if job["min_salary"] > job["max_salary"]:
        raise ValueError(
            "o valor de min_salary é maior que o valor de max_salary;"
        )
    if type(salary) != int:
        raise ValueError("o parâmetro salary tem valores não numéricos")

    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
