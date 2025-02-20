import statistics

def enrollment_stats(universities):
    enrollments = [uni[1] for uni in universities]
    tuitions = [uni[2] for uni in universities]
    return enrollments, tuitions

def mean(values):
    return sum(values) / len(values)

def median(values):
    return statistics.median(values)

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

enrollments, tuitions = enrollment_stats(universities)

total_students = sum(enrollments)
total_tuition = sum(tuitions)

print("******************************")
print(f"Total students: {total_students:,}")
print(f"Total tuition: $ {total_tuition:,}\n")
print(f"Student mean: {mean(enrollments):,.2f}")
print(f"Student median: {median(enrollments):,}")
print(f"\nTuition mean: $ {mean(tuitions):,.2f}")
print(f"Tuition median: $ {median(tuitions):,}")
print("******************************")
