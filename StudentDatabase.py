import random
from datetime import datetime, timedelta

# Predefined data for names and addresses
first_names = [
    "Oliver", "Charlotte", "Jack", "Amelia", "William", "Olivia", "Noah", "Isla", 
    "James", "Ava", "Henry", "Mia", "Thomas", "Grace", "Liam", "Sophia", "Ethan", 
    "Harper", "Alexander", "Zoe", "Lucas", "Ruby", "Elijah", "Lily", "Mason", 
    "Ella", "Harrison", "Evie", "Samuel", "Emily", "Sebastian", "Sophie", "Leo", 
    "Chloe", "Hunter", "Scarlett", "Isaac", "Isabella", "Archer", "Matilda", 
    "Hudson", "Ivy", "Cooper", "Willow", "Levi", "Georgia", "Oscar", "Hannah", 
    "Archie", "Layla"
]

last_names = [
    "Smith", "Jones", "Williams", "Brown", "Taylor", "Wilson", "Thomas", "White", 
    "Martin", "Anderson", "Thompson", "Nguyen", "Walker", "Harris", "Edwards", 
    "Robinson", "Evans", "Murphy", "King", "Wright", "Wood", "Campbell", "Johnson", 
    "Clarke", "Lee", "Turner", "Moore", "Hill", "Scott", "Green", "Adams", 
    "Mitchell", "Hall", "Cooper", "Carter", "Phillips", "Parker", "Evans", 
    "Kelly", "Ward", "Watson", "Allen", "Young", "Harrison", "Stewart", "Hughes"
]

# Generate 1000 unique full names
names = [f"{random.choice(first_names)} {random.choice(last_names)}" for _ in range(1000)]

street_names = [
    "George St", "Pitt St", "Queen St", "King St", "Elizabeth St", 
    "Oxford St", "Flinders St", "Collins St", "Smith St", "High St", 
    "Bridge St", "Station St", "Market St", "Victoria St", "Church St"
]

cities = [
    "Sydney", "Melbourne", "Brisbane", "Perth", "Adelaide", 
    "Canberra", "Hobart", "Darwin", "Gold Coast", "Newcastle"
]

states = ["NSW", "VIC", "QLD", "WA", "SA", "TAS", "ACT", "NT"]

# Postcode ranges based on state
postcode_ranges = {
    "NSW": range(2000, 2600),
    "VIC": range(3000, 3800),
    "QLD": range(4000, 4800),
    "WA": range(6000, 6700),
    "SA": range(5000, 5800),
    "TAS": range(7000, 7800),
    "ACT": range(2600, 2900),
    "NT": range(800, 1000),
}

# Generate a random postcode for a state
def get_random_postcode(state):
    return random.choice(list(postcode_ranges[state]))

# Generate 1,000 unique addresses
addresses = []
for _ in range(1000):
    street_number = random.randint(1, 999)
    street = random.choice(street_names)
    city = random.choice(cities)
    state = random.choice(states)
    postcode = get_random_postcode(state)
    address = f"{street_number} {street}, {city}, {state} {postcode}"
    addresses.append(address)

sections = ["A", "B", "C", "D", "E"]
grade_letters = ["A", "B", "C", "D", "F"]
subjectNames = ["Maths", "English", "Physics", "Chemistry", "Geography"]
deptNames = ["Mathematics", "Language", "Science", "Social Studies"]

# Generate random dates
def random_date(start_year=2000, end_year=2020):
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return (start_date + timedelta(days=random_days)).strftime('%Y-%m-%d')

# Generate random phone numbers
def random_phone():
    return ''.join([str(random.randint(0, 9)) for _ in range(10)])

# Create insert statements for all tables
def create_insert_statements():
    inserts = []
    staff_ids = []
    parent_ids = []
    dept_ids = []
    class_ids = []
    subject_ids = []
    grade_ids = []
    student_ids = []

    # Generate staff data
    for i in range(1, 100):
        staff_id = i
        staff_name = random.choice(names)
        address = random.choice(addresses)
        phone = random_phone()
        staff_ids.append(staff_id)
        inserts.append(f"INSERT INTO staff VALUES ({staff_id}, '{staff_name}', '{address}', '{phone}');")

    # Generate class data
    for i in range(1, 4):
        class_id = i
        section = sections.pop(random.randrange(len(sections)))
        class_ids.append(class_id)
        inserts.append(f"INSERT INTO class VALUES ({class_id}, '{section}');")

    # Generate department data
    for i in range(1, 4):
        dept_id = i
        dept_name = deptNames.pop(random.randrange(len(deptNames)))
        dept_ids.append(dept_id)
        inserts.append(f"INSERT INTO department VALUES ({dept_id}, '{dept_name}');")

    # Generate parent data
    for i in range(1, 6):
        parent_id = i
        parent_name = random.choice(names)
        address = random.choice(addresses)
        phone = random_phone()
        staff_id = random.choice(staff_ids)
        parent_ids.append(parent_id)
        inserts.append(f"INSERT INTO parent VALUES ({parent_id}, '{parent_name}', '{address}', '{phone}', {staff_id});")

    # Generate grade data
    for i in range(1, 6):
        grade_id = i
        grade_letter = grade_letters.pop(random.randrange(len(grade_letters)))
        mark = random.randint(50, 100)
        grade_ids.append(grade_id)
        inserts.append(f"INSERT INTO grade VALUES ({grade_id}, '{grade_letter}', {mark});")

    # Generate subject data
    for i in range(1, 6):
        subject_id = i
        subject_name = subjectNames.pop(random.randrange(len(subjectNames)))
        dept_id = random.choice(dept_ids)
        subject_ids.append(subject_id)
        inserts.append(f"INSERT INTO subject VALUES ({subject_id}, '{subject_name}', {dept_id});")

    # Generate student data
    for i in range(1, 1000):
        student_id = i
        student_name = random.choice(names)
        dob = random_date()
        address = random.choice(addresses)
        phone = random_phone()
        parent_id = random.choice(parent_ids)
        staff_id = random.choice(staff_ids)
        subject_id = random.choice(subject_ids)
        class_id = random.choice(class_ids)
        grade_id = random.choice(grade_ids)
        student_ids.append(student_id)
        inserts.append(f"INSERT INTO student VALUES ({student_id}, '{student_name}', '{dob}', '{address}', "
                       f"'{phone}', {parent_id}, {staff_id}, {subject_id}, {class_id}, {grade_id});")

    return inserts

# Generate and print the SQL insert statements
insert_statements = create_insert_statements()
with open("insert_statements.txt", "w") as file:
    file.write("\n".join(insert_statements))

print("Insert statements saved to 'insert_statements.txt'.")