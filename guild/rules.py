import string


COLOURS = (0xff0018, 0xffa52c, 0xffff41, 0x008018, 0x0000f9, 0x86007d)
RULES = (
    (
        "{n}) Don't break Discord's terms of service (https://discord.com/terms) and follow their guidelines (https://discord.com/guidelines).",
        [
            "{n}) If you are (or claim to be) under 13, then you will be banned.",
            "{n}) Evading server blocks or bans (such as using a VPN and alt account) will get you immediately [re]banned.",
            "{n}) Do not use bots to evade user blocks (eg pinging users using StalkerBot, etc).",
            "{n}) If a DM conversation between two members who are on the server is reported for breaking the Discord ToS, it will be dealt with as if it had occurred on the server.",
        ],
    ),
    (
        "{n}) Don't spam or flood.",
        [
            "{n}) Spamming would be sending multiple messages when only one is required, to an extreme measure. Sending a sentence word-by-word would be spamming, for example.",
            "{n}) Flooding would be sending one message that's intended to just fill the screen. Sending 200 \"a\"s or a chunk of song lyrics, for example, would be flooding.",
            "{n}) Examples of spam and flooding include sending several out-of-context lines of a movie/song; excessively sending emojis or adding reactions to messages; repeating the same message several times; anything intended to disrupt the flow of conversation. This is by no means an exhaustive list.",
            "{n}) This applies to VCs as well - loud noises, playing music down your microphone, and screaming would also count as spamming."
        ],
    ),
    (
        "{n}) Stay respectful and kind to all users on the server.",
        [
            "{n}) Do not use slurs (remarks meant to degrade or insult someone based on their race, sexuality, abilities, gender, etc) while in the server.",
            "{n}) Joking around with friends is fine as long as the joking doesn't go to far - threatening someone, calling another user names, or general toxicity is guaranteed to grab a mod's attention.",
            "{n}) Deliberately starting arguments is not allowed. 'Argumentative' topics are allowed as long as they remain respectful and do not harm someone's identity (religious beliefs, sexuality, gender identity, etc).",
            "{n}) Do not post flashing images/videos/gifs/emojis.",
        ],
    ),
    (
        "{n}) Don't post personally identifying information (PII) of other users.",
        [
            "{n}) Information such as an address, a surname, an IP address, etc is classed as PII.",
            "{n}) Information that isn't personally identifying (a first name, a city, etc) is allowed.",
        ],
    ),
    (
        "{n}) Don't post NSFW (not safe for work) content.",
        [
            "{n}) NSFW content is anything sexually suggestive. Just because your post isn't explicit doesn't mean it's SFW.",
            "{n}) Extreme violence and gore counts as NSFW.",
            "{n}) Talking or joking about sexual assault/harrassment, school shootings, child abuse, and animal abuse is strictly prohibited.",
            "{n}) Having an NSFW profile picture, username, or status will get you removed from the server if not changed.",
        ],
    ),
    (
        "{n}) Don't advertise.",
        [
            "{n}) Unsolicited advertising of your own brand, server, bot, service, etc is prohibited.",
            "{n}) Any advertising (examples above) done through DMs will be treated the same as if it were in the server.",
            "{n}) Asking for Nitro will be treated as advertising.",
            "{n}) This rule is waived in <#505965232779296783> when linking sources to posted artwork.",
        ],
    ),
    (
        "{n}) Keep conversations in English.",
        [
            "{n}) The staff team can only moderate chat when it is spoken in English (since that is the only language they all know).",
        ],
    ),
    (
        "{n}) Have a typable nickname.",
        [
            "{n}) \"Typable\" refers to being able to type the name on a standard English ASCII keyboard.",
            "{n}) Three or more consecutive alphanumeric characters are required for a nickname.",
        ],
    ),
    (
        "{n}) Keep your messages within the topic of the given channel.",
        [
            "{n}) Bot commands should stay in <#490991441255071745> and memes should stay in <#538854509179568149>, for example; this is waived if the command/media supports the topic at hand and doesn't flood the channel.",
            "{n}) Keep on topic in relevant channels such as <#636085718002958336> and <#505965232779296783>.",
        ],
    ),
    (
        "{n}) Source all artwork you post in the art channel.",
        [
            "{n}) Simply saying \"not my art\" is not sufficient - link to the artist.",
            "{n}) If you are posting your own work, simply indicate this - you don't need to link to anything.",
            "{n}) If your work is derivative of someone else's work (eg a simple edit or tracing) then you must link to the original.",
        ]
    ),
    (
        "{n}) If you ask to be punished, you will more than likely receive that punishment.",
        [
            "{n}) Any punishment duration (eg a ban for 3 days, a mute for 5 minutes, etc) requested may be increased (eg a ban for 7 days, a mute for 5 hours, etc) as long as the requesting party agrees to the new time.",
            "{n}) Any punishments delivered through this rule must have a time-limit (no permanent mutes or bans)",
            "{n}) The punished user may DM the staff member who punished them at any time to get their punishment removed",
        ],
    ),
    (
        "{n}) Situations that are not explicitly stated in the rules and negatively impact the server experience may still be punishable offenses.",
        [
            "{n}) The staff team consists of humans, therefore mistakes may be made. Feel free to question a staff member's decision, either by email (`discord@voxelfox.co.uk`), in the server feedback channel (<#826398233986334802>, accessible privately via <@604059714963243056> with code `SFEED`), or by DMing Kae directly (<@141231597155385344>).",
            "{n}) A verbal warning may be delivered before any real punishments are made if a situation isn't explicitly stated in the rules.",
            "{n}) Making joke or deliberately false reports/tickets is not allowed.",
        ],
    ),
)


for index, (title, description) in enumerate(RULES):
    description_items = [item.format(n=f"{index + 1}{string.ascii_lowercase[string_index]}") for string_index, item in enumerate(description)]
    await channel.send(embed=utils.Embed(
        title=title.format(n=index + 1),
        description="\n\n".join(description_items),
        colour=COLOURS[index % len(COLOURS)],
    ))
await message.delete()
