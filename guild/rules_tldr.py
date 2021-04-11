RULES = (
    (
        "TL;DR",
        [
            "Don't break Discord's ToS",
            "Don't be NSFW",
            "Be nice to other people",
            "Stick to English",
        ],
    ),
)


for index, (title, description) in enumerate(RULES):
    description_items = [f"* {item}" for item in description]
    await channel.send(embed=utils.Embed(
        title=title,
        description="\n\n".join(description_items),
        colour=0xffffff,
    ))
await message.delete()
