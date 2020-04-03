users = {
    "simone" : "active",
    "ciccio" : "inactive",
    "pippo" : "active"
}

active_users = {}
inactive_users = {}

for user,status in users.items():
    if status == "inactive":
        inactive_users[user] = status
    else:
        active_users[user] = status

print(active_users)
print(inactive_users)
