FILE_PATH = "document.txt"

user_freq = {}
action_freq = {}

max_user = ""
max_user_count = 0
max_action = ""
max_action_count = 0

with open(FILE_PATH, "r") as f:
    line = f.readline()
    while(line):
        line = line.strip()
        timestamp, user, action = line.split(",")

        # upadate user freq map
        if user in user_freq:
            user_freq[user] += 1
        else:
            user_freq[user] = 1
            
        # update max user count
        if max_user_count < user_freq[user]:
            max_user_count = user_freq[user]
            max_user = user
        
        #update action freq map
        if action in action_freq:
            action_freq[action] += 1
        else:
            action_freq[action] = 1

        #update max action count
        if max_action_count < action_freq[action]:
            max_action_count = action_freq[action]
            max_action = action

        line = f.readline()

# most active user
print(f"user: {max_user}, count:{max_user_count}")
print(f"user: {max_action}, count:{max_action_count}")