"""
Please write the render_person function required to print a a string like the following:
Bob is a 23 years old male born in 05/22/1983 with green eyes
"""
def render_person(name,dob,eye_color,age,gender):
    return (f"{name} is {age} years old male born in {dob} with {eye_color}")

print(render_person(name='Bob', dob='05/22/1983', eye_color='green', age=23, gender='male'))

