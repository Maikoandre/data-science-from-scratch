import marimo

__generated_with = "0.23.1"
app = marimo.App(width="medium")


@app.cell
def _():
    users = [
        {'id': 0, 'name': 'Hero'},
        {'id': 1, 'name': 'Dunn'},
        {'id': 2, 'name': 'Sue'},
        {'id': 3, 'name': 'Chi'},
        {'id': 4, 'name': 'Thor'}
    ]

    friendship_pairs = [(0, 1), (3, 4), (1, 2), (1, 3), (2, 3)]
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
    return


if __name__ == "__main__":
    app.run()
