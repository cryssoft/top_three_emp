#!/usr/bin/python3
#
#  Watched https://www.youtube.com/watch?v=IbEg3jxnTpk on YouTube
#
#  Seemed like using a ton of Pandas data frames and their associated
#  calls was overkill.  It looks nice, and it might actually be what
#  the assignment required, but you can do a lot with simpler data
#  formats, list comprehensions, set() to deduplicate, etc.
#
#  Chris Petersen, Crystallized Software, 2025/04/15
#


#  Simulating database tables
#  EMPLOYEES = id: int, name: varchar, salary: int, departmentId: int
G_EMPLOYEES = [
    { "id": 1, "name": "Alice", "salary": 100_000, "departmentId": 1 },
    { "id": 2, "name": "Bob", "salary": 110_000, "departmentId": 1 },
    { "id": 3, "name": "Charles", "salary": 120_000, "departmentId": 1 },
    { "id": 4, "name": "David", "salary": 120_000, "departmentId": 1 },
    { "id": 5, "name": "Edward", "salary": 130_000, "departmentId": 1 },
    { "id": 6, "name": "Frank", "salary": 90_000, "departmentId": 1 },
    { "id": 7, "name": "Gerold", "salary": 95_000, "departmentId": 1 },
    #
    { "id": 8, "name": "Amy", "salary": 195_000, "departmentId": 2 },
    { "id": 9, "name": "Bruce", "salary": 185_000, "departmentId": 2 },
    { "id": 10, "name": "Carlos", "salary": 175_000, "departmentId": 2 },
    { "id": 11, "name": "Damien", "salary": 175_000, "departmentId": 2 },
    { "id": 12, "name": "Eddy", "salary": 155_000, "departmentId": 2 },
    { "id": 13, "name": "Fiona", "salary": 165_000, "departmentId": 2 },
    { "id": 14, "name": "Graham", "salary": 165_000, "departmentId": 2 },
    #
    { "id": 15, "name": "Andi", "salary": 195_000, "departmentId": 3 },
    { "id": 16, "name": "Bryce", "salary": 185_000, "departmentId": 3 },
    { "id": 17, "name": "Candy", "salary": 185_000, "departmentId": 3 },
    { "id": 18, "name": "Darlene", "salary": 185_000, "departmentId": 3 },
    { "id": 19, "name": "Effie", "salary": 175_000, "departmentId": 3 },
    { "id": 20, "name": "Francesca", "salary": 165_000, "departmentId": 3 },
    { "id": 21, "name": "Gertrude", "salary": 155_000, "departmentId": 3 },
    { "id": 22, "name": "Hermione", "salary": 155_000, "departmentId": 3 },
]
#  DEPARTMENTS = id: int, name: varchar
G_DEPARTMENTS = [
    { "id": 1, "name": "Sales" },
    { "id": 2, "name": "Marketing" },
    { "id": 3, "name": "IT" },
]


def department_name_from_id(p_departmentId: int, p_departments: list[dict]) -> str:
    """
    Trivial function to search for a matching department ID since we have a list of dicts
    and not something easy to search in-line in the function below.

    NOTE:  It would be nice to make this an @functools.cache or lru_cache function,
    but that relies on the argument(s) being hash-able in a way that ours are not.
    """
    l_returns: str = "(unknown)"

    for l_department in p_departments:
        if (l_department["id"] == p_departmentId):
            l_returns = l_department["name"]
            break

    return(l_returns)


def return_top_three_by_salary_stratum(p_employees: list[dict], p_departments: list[dict]) -> list[dict]:
    """
    Trivial function to return a list of dictionaries of department, employee, salary for the top 3
    salary strata per department.  Not sure if this is exactly the meaning of the "leetcode" bullshit
    task, but it's what they did in the YouTube video I was watching on the subject.

    NOTE:  This will fail if there are less than three salary strata for a department because of the
    explicit [-3] in the calculation of l_cutoff.  The work-around would be pretty straightforward
    based on the length of the unduplicated (by set()) list.
    """
    l_returns: list[dict] = []

    for l_departmentId in set([x["departmentId"] for x in p_employees]):
        l_cutoff: int = sorted(set([x["salary"] for x in p_employees if (x["departmentId"] == l_departmentId)]))[-3]
        for l_employee in [x for x in p_employees if ((x["departmentId"] == l_departmentId) and (x["salary"] >= l_cutoff))]:
            l_returns.append({"Department": department_name_from_id(l_employee["departmentId"], p_departments), "Employee": l_employee["name"], "Salary": l_employee["salary"]})

    return(l_returns)


def main() -> None:
    """
    The usual main() function to keep ourselves out of trouble when building import-able modules.
    In this case, just call the function we really care about print the output.
    """
    l_top_three_by_salary: list[dict] = return_top_three_by_salary_stratum(G_EMPLOYEES, G_DEPARTMENTS)
    for l_returned in l_top_three_by_salary:
        print(l_returned)

    return


#  The caller for if this script/program is run directly instead of being import-ed somewhere
if (__name__ == "__main__"):
    main()