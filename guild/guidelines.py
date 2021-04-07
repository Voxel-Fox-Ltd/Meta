COLOURS = (0xff0018, 0xffa52c, 0xffff41, 0x008018, 0x0000f9, 0x86007d)
RULES = (
    (
        "Types of punishment",
        (
            "Verbal Warning",
            (
                "These basically mean nothing.",
                "This is the first port of call when it comes to reminding users of the rules.",
            ),
        ),
        (
            "Warn",
            (
                "A warning given with Yags.",
                "These can be pulled up again with the `warnings` command.",
                "These generally aren't considered a punishment, but rather a note for how to deal with later punishments.",
            ),
        ),
        (
            "Mute",
            (
                "A way to stop the user from talking in the server.",
                "The first stop to giving real punishments to the user.",
                "Mutes should _always_ be temporary, as they're a way to keep the user from being in chat for a bit while still being able to interact with the server.",
            ),
        ),
        (
            "Kick",
            (
                "A kick removes the user from the server, if only temporarily.",
                "Kicks should be used in instances where the user is breaking some rules, but not directly harming the server by breaking it.",
                "An example for this would be having an NSFW profile picture - the user isn't harming the server but is directly breaking a rule.",
            ),
        ),
        (
            "Ban",
            (
                "The last resort - removing the user from the server, possibly indefinitely.",
                "Bans should be used where the user is harming the server directly and they are a risk to the Good Vibes:tm:.",
            ),
        ),
    ),
    (
        "Don't break Discord's terms of service (https://discord.com/terms) and follow their guidelines (https://discord.com/guidelines)",
        (
            "Users claiming to be under 13",
            (
                "Ask if they're sure because users under 13 aren't allowed on Discord (https://support.discord.com/hc/en-us/articles/360040724612).",
                "If they don't get the hint, ban for the duration that they would be under 13 for (eg if they say they're 12, ban for 1 year).",
            ),
        ),
        (
            "Users ban evading",
            (
                "Confirm that they _are_ the user who's claiming to be ban evading. Screenshots of DMs from other users are acceptable for this.",
                "Permanently ban the user.",
            ),
        ),
        (
            "Users sending IP loggers",
            (
                "An IP logger is a website that's designed to log the IP of the user who clicks the link.",
                "Most common IP loggers are handled by Yags' automoderator, so you won't see this come up a lot.",
                "Permanently ban the user.",
            ),
        ),
        (
            "Promoting suicide/self harm",
            (
                "This would include just talking or joking about it - we've had people complain that their \"joking\" about suicide was serious so they shoudn't be warned for it.",
                "Delete the message.",
                "Warn the user.",
                "Mute the user (1h) if they don't shut up.",
                "Continue to mute the user (24h) if they still don't shut up over the course of a week.",
            ),
        ),
    ),
    (
        "Don't spam or flood",
        (
            "Users sending a large chunk of text with no context",
        ),
        (
            "Users sending a large chunk of text within context of the conversation",
        ),
        (
            "Users sending multiple short messages over a short time",
        ),
        (
            "Users sending multiple long messages over a short time",
        ),
    ),
    (
        "Stay respectful and kind to all users on the server",
    ),
    (
        "Don't post personally identifying information (PII)",
        (
            "Posting full names",
        ),
        (
            "Posting phone numbers",
        ),
        (
            "Posting obviously fake phone numbers (555 numbers)",
        ),
        (
            "Posing addresses",
        ),
        (
            "Catfishing",
            (
                "Is this something we should even deal with?",
            )
        ),
    ),
    (
        "Don't post NSFW (not safe for work) content",
        (
            "Posting sexually suggestive text",
        ),
        (
            "Posting sexually suggestive images/gifs",
        ),
        (
            "Posting sexually explicit text",
        ),
        (
            "Posting sexually explicit images",
        ),
    ),
    (
        "Don't advertise",
        (
            "Unsolicited DM ads",
            (
                "This refers to sending members adverts via DMs.",
                "This includes but is not limited to server invites, YouTube channels/videos, and Twitch streams.",
                "When reported, verify that the user in question actually sent a DM ad and that the user is on VFL.",
                "If that is the case, ban the user (2d).",
            ),
        ),
        (
            "Ads in the server",
            (
                "This includes but is not limited to server invites, YouTube channels/videos, and Twitch streams.",
                "Delete the advert and warn the user.",
                "If they continue to advertise, or if they advertised in multiple channels, ban the user (1d).",
            ),
        ),
    ),
    (
        "Keep conversations in English",
        (
            "Sending short phrases in other languages",
        ),
        (
            "Sending whole-ass sentences in other languages",
        ),
        (
            "Straight up conversing with another user in another language",
            (
                "This generally would apply to the new users joining who don't primarily speak English.",
            ),
        ),
    ),
    (
        "Have a typable nickname",
        (
            "Users don't have a typable nickname",
            (
                "Change the user's nickname.",
                "If they change it back, add the name change ban role to the user.",
            ),
        ),
    ),
    (
        "Keep your messages within the topic of the given channel",
        (
            "Bot commands in general",
        ),
        (
            "Off-topic messages in the coding channel",
        ),
        (
            "Off-topic messages in the art channel",
        ),
        (
            "Conversing in the bot support/ideas channels",
        ),
    ),
    (
        "Source all artwork you post in the art channel",
        (
            "Posting work without a source",
            (
                "Delete the message. Remind the user that all works must be sourced.",
                "If they continue to post unsourced work, add the art ban role to them.",
            ),
        ),
        (
            "Users claiming other people's work as their own",
        ),
    ),
    (
        "If you ask to be punished, you will more than likely receive that punishment",
        (
            "People asking for punishments",
            (
                "If it's a ban, just fuckin give it to em (1d, 0ddays).",
                "Kicks and mutes I don't particularly want to encourage being asked for, however.",
                "If someone asks for a kick, offer them a ban.",
                "If someone asks for a mute, say no but then offer them a ban if they're being assholes about it.",
            ),
        ),
    ),
    (
        "Situations that are not explicitly stated in the rules and negatively impact the server experience may still be punishable offenses",
        (
            "People doing anything",
            (
                "This rule is specifically here to deal with things athat are shitty but aren't explicitly stated.",
                "As someone who's been on the internet forever I know that everyone will follow every opportunity to break the rules.",
                "If people are being cucks, this is here so you can tell them not to be.",
                "_Do not rely on this to moderate_. Look at the other rules first. You are here to make the server a better place, not go on an ego trip.",
            ),
        ),
    ),
    (
        "MarriageBot Commands",
        (
            "`m!copyfamilytoguild <user_id> <guild_id>`",
            (
                "Copies a user's MarriageBot family to a guild's MarriageBot Gold family.",
            ),
        ),
        (
            "`m!copyfamilytoguildwithdelete <user_id> <guild_id>`",
            (
                "Copies a user's family to a guild's MarriageBot Gold family and deletes the current Gold tree.",
                "This should be used if `copyfamilytoguild` has thrown an error - if the users have already started making a family in their server.",
            ),
        ),
        (
            "`m!addserverspecific <guild_id> <user_id>`",
            (
                "Adds a guild to the MarriageBot Gold whitelist.",
            ),
        ),
        (
            "`m!removeserverspecific <guild_id>`",
            (
                "Remove a guild from the MarriageBot Gold whitelist.",
            ),
        ),
        (
            "`m!getgoldpurchase <user_id>`",
            (
                "Lists a user's Gold purchases.",
            ),
        ),
        (
            "`m.runstartupmethod`",
            (
                "After adding users to a MarriageBot Gold family, run this command.",
            ),
        ),
    ),
    (
        "YAGPDB Commands",
        (
            "`-ban <user> -d <time> -ddays <time> <reason>`",
            (
                "`-d` - Days to ban the user for.",
                "`-ddays` - Days to delete messages for.",
                "Most - if not all - bans should have a duration tied to them.",
            ),
        ),
        (
            "`-mute <user> <time> <reason>`",
            (
                "Gives the `Muted` role to the user for the specified amount of time.",
            ),
        ),
        (
            "`-warn <user> <reason>`",
            (
                "Adds a note to the user's account",
            ),
        ),
    ),
    (
        "Other",
    ),
)


index = 0
for title, *fields in RULES:
    embed = utils.Embed(
        title=title,
        colour=COLOURS[index % len(COLOURS)],
    )
    for item in fields:
        try:
            name, value = item
        except ValueError:
            name, value = item[0], ""
        embed.add_field(name, "\n".join([f"* {i}" for i in value]) or "\u200b", inline=False)
    await channel.send(embed=embed)
    index += 1
await message.delete()
