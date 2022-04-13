import discord


def dbprint(message: str) -> None:
    print(f"[Debug] {message}")


def dbdeftable(rows: dict, tabsize:int=4) -> None:
    keylen = 0

    for key in rows.keys():
        if len(key) > keylen:
            keylen = len(key)

    print()  # Padding line

    for key in rows.keys():
        print(f"{key}{' ' * (keylen - len(key) + tabsize)}{rows[key]}")

    print()  # Padding line


def bot_state(client: discord.Client) -> None:
    if client.user is None:
        dbprint("Bot not logged in.")
        return

    user: discord.ClientUser = client.user

    dbdeftable({
        "Identification": f"{user.name}#{user.discriminator}",
        "ID": str(user.id),
        "Locale": user.locale,
        "Latency": f"{int(client.latency * 1000)} ms",
    })
