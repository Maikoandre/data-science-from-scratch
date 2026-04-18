import marimo

__generated_with = "0.23.1"
app = marimo.App(width="medium")


@app.cell
def _():
    users = [
        { "id": 0, "name": "Hero" },
        { "id": 1, "name": "Dunn" },
        { "id": 2, "name": "Sue" },
        { "id": 3, "name": "Chi" },
        { "id": 4, "name": "Thor" },
        { "id": 5, "name": "Clive" },
        { "id": 6, "name": "Hicks" },
        { "id": 7, "name": "Devin" },
        { "id": 8, "name": "Kate" },
        { "id": 9, "name": "Klein" }
    ]

    friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                        (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]
    return friendship_pairs, users


@app.cell
def _(friendship_pairs, users):
    friendships = {user['id']: [] for user in users}

    for i, j in friendship_pairs:
        friendships[i].append(j)
        friendships[j].append(i)
    return (friendships,)


@app.cell
def _(friendships):
    def number_of_friends(user):
        user_id = user["id"]
        friends_ids = friendships[user_id]
        return len(friends_ids)

    print(number_of_friends({'id': 1, 'name': 'Dunn'}))
    return (number_of_friends,)


@app.cell
def _(number_of_friends, users):
    total_connections = sum(number_of_friends(user) for user in users)
    print(total_connections)
    return (total_connections,)


@app.cell
def _(total_connections, users):
    num_users = len(users)
    avg_connections = total_connections / num_users
    print(avg_connections)
    return


@app.cell
def _(number_of_friends, users):
    num_friends_by_id = [(user['id'], number_of_friends(user)) for user in users]
    num_friends_by_id.sort(
        key=lambda id_and_friends: id_and_friends[1],
        reverse=True
    )
    print(num_friends_by_id)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
