import random




def get_all_giveaway_users(giveaway_id):
    try:
        raw = giveaways.find({"giveawayId": f"{giveaway_id}"})
        for key in raw:
            return key["users"]
    except Exception as e:
        print("Error while fetching users: {}".format(e))


async def draw_winner(users, winners):

    if "x" in users:
        users.remove("x")
    choosen = random.sample(users, winners)
    return choosen


