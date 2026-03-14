def profile(**user):
    fname, lname = user.values()
    return f"Hello {fname} {lname}"


user = {"fname":"Waqas","lname":"Ahmad"}
user_2 = {"fname":"Ali","lname":"Khan"}
print(profile(**user))
print(profile(**user_2))
