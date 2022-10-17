from ds.project_social.data import users, interests, friendship_pairs, salaries_and_tenures

from collections import Counter, defaultdict

friendships = {user["id"]: [] for user in users}

for user, pair in friendship_pairs:
    friendships[user].append(pair)
    friendships[pair].append(user)


def number_of_friends(user):
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friend_ids)


num_users = len(users)
total_connections = sum(number_of_friends(user) for user in users)
avg_connections = total_connections / num_users

# (user_id, number_of_friends)
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users].sort(
    key=lambda id_and_friends: id_and_friends[1], reverse=True)


def friends_of_friends(user):
    # foaf - friend of a friend
    user_id = user["id"]
    return Counter(
        foaf_id
        for friend_id in friendships[user_id]
        for foaf_id in friendships[friend_id]
        if foaf_id != user_id and foaf_id not in friendships[user_id]
    )


def users_who_like(target_interest: str):
    return [
        user_id for user_id, user_interest in interests
        if user_interest == target_interest
    ]


user_ids_by_interest, interests_by_user_id = defaultdict(list), defaultdict(list)

for user_id_, interest in interests:
    user_ids_by_interest[interest].append(user_id_)
    interests_by_user_id[user_id_].append(interest)


def most_common_interests_with(user):
    return Counter(
        interested_user_id
        for user_interest in interests_by_user_id[user["id"]]
        for interested_user_id in user_ids_by_interest[user_interest]
        if interested_user_id != user["id"]
    )


salary_by_tenure = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

average_salary_by_tenure = {
    tenure: sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
}


def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"


salary_by_tenure_bucket = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

average_salary_by_bucket = {
    tenure_bucket: sum(salaries) / len(salaries)
    for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}


def predict_paid_or_unpaid(years_experience):
    if years_experience < 3.0:
        return "paid"
    elif years_experience < 8.5:
        return "unpaid"
    else:
        return "paid"


words_and_counts = Counter(
    word
    for user, interest in interests
    for word in interest.lower().split()
)

for word, count in words_and_counts.most_common():
    if count > 1:
        print(word, count)
