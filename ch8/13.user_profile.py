def build_profile(name, last_name, **user_data):
    """Make a user"""

    profile = {}
    profile["first_name"] = name
    profile["last_name"] = last_name
    for index, value in user_data.items():
        profile[index] = value
    return profile


profile = build_profile("Emiliano", "Jouts", job="developer", field="web design")
print(profile)
