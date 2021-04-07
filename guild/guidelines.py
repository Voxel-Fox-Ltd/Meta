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
            "Obvious copypasta",
            (
                "Delete the message and add a warn to the user.",
                "Mute the user (1h) if they continue.",
                "Ban the user (1d) if they continue.",
            ),
        ),
        (
            "Users sending a single large chunk of text with no context",
            (
                "Delete the message and add a warn to the user.",
                "Mute the user (1h) if they continue.",
                "Ban the user (1d) if they continue.",
            ),
        ),
        (
            "Users sending a single large chunk of text within context of the conversation",
            (
                "This is fine.",
                "If it starts taking up a large chunk of chat (ie the users are sending essays to each other) then tell the users to move to DMs.",
                "If they continue, moderate as if there were no context.",
            ),
        ),
        (
            "Users sending multiple short messages over a short time",
            (
                "This is generally what most people refer to as spamming.",
                "Ban (1d).",
            )
        ),
        (
            "Users sending multiple long messages over a short time",
            (
                "This is generally what most people refer to as spamming.",
                "Ban (1d).",
            ),
        ),
        (
            "Users screaming into VCs",
            (
                "Server mute and warn the user.",
            ),
        ),
        (
            "Users with annoying background audio in VCs",
            (
                "Ask the user nicely to mute themselves.",
                "If they don't, server mute them. Do not warn them."
            ),
        ),
    ),
    (
        "Stay respectful and kind to all users on the server",
        (
            "People using slurs",
            (
                "Delete the message. Mute the user (2h).",
                "If they repeat this, ban the user (30d).",
            ),
        ),
        (
            "Insulting other users",
            (
                "Tell the user to be respectful towards others",
                "If they continue to be agressive and rude, mute the user (10m)",
                "If they continue, mute the user (2h).",
                "If they continue, ban the user (1d).",
            ),
        ),
        (
            "Insulting other users when we know those users to be friends",
            (
                "Keep an eye on the conversation, but this is generally fine.",
                "If the insults start getting personal or agressive, tell the users they might be going too far.",
                "This is in place to allow \"Kae you cuck\" but disallow \"fuck you Kae this is why nobody loves you\".",
                "If they continue, moderate as if the users didn't know each other.",
            ),
        ),
        (
            "Users insulting themselves",
            (
                "A bit of a downer on conversations so I don't really want this in my server any more.",
                "Remind users that they need to be respectful towards themselves - not necessarily nice, but not explicitly a cunt.",
                "\"I don't like myself\" is fine. \"I fucking hate myself\" is not. This will require context to moderate.",
                "Mute the user (10m) if they continue.",
                "This is not a bannable offense.",
            ),
        ),
        (
            "Deliberately starting [agressive] arguments",
            (
                "This is reserved for _agressive_ arguments. Users are allowed to argue.",
                "Remind the user to be respectful to others and to stop the topic if they cannot."
                "If they continue, mute the user (30m).",
                "If they continue, ban the user (1d).",
            ),
        ),
        (
            "Posting flashing images/gifs",
            (
                "Delete the image. Tell the user to avoid posting flashing images.",
            ),
        ),
    ),
    (
        "Don't post personally identifying information (PII)",
        (
            "Posting full names",
            (
                "Remind the user to not post PII.",
                "Mute (30m) if they continue.",
                "Ban (1d) if they continue.",
            ),
        ),
        (
            "Posting phone numbers",
            (
                "Remind the user to not post PII.",
                "Mute (30m) if they continue.",
                "Ban (1d) if they continue.",
            ),
        ),
        (
            "Posting obviously fake phone numbers (555 numbers)",
            (
                "Remind the user to not post PII, and the fact that it's fake just makes real ones harder to moderate.",
                "Mute (30m) if they continue.",
            ),
        ),
        (
            "Posting addresses",
            (
                "Remind the user to not post PII.",
                "Mute (30m) if they continue.",
                "Ban (1d) if they continue.",
            ),
        ),
    ),
    (
        "Don't post NSFW (not safe for work) content",
        (
            "Posting sexually suggestive text",
            (
                "Delete the message and remind the user to keep SFW.",
                "Warn if they continue.",
                "Mute (10m) if they continue.",
                "Ban (1d) if they continue.",
            ),
        ),
        (
            "Posting sexually suggestive images/gifs",
            (
                "Delete the message and remind the user to keep SFW.",
                "Mute (1h) if they continue.",
                "Ban (1d) if they continue.",
            ),
        ),
        (
            "Posting sexually explicit text",
            (
                "Delete the message and add a warn to the user.",
                "Ban (7d) if they continue.",
            ),
        ),
        (
            "Posting sexually explicit images",
            (
                "Ban the user (30d).",
                "Optionally report them to Discord Trust and Safety (https://dis.gd/report).",
            ),
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
            (
                "Generally fine.",
                "If they start _only_ talking in short phrases, remind the user to keep to English or to keep their non-English messages to a minimum.",
            ),
        ),
        (
            "Sending whole-ass sentences in other languages",
            (
                "Verbally remind the user to keep to English.",
                "If they continue, mute the user (10m).",
                "If they continue, mute the user (2h).",
            )
        ),
        (
            "Straight up conversing with another user in another language",
            (
                "This generally would apply to the new users joining who don't primarily speak English.",
                "Verbally remind the user to keep to English.",
                "If they continue, mute the user (30m).",
                "If they continue, ban the user (1d).",
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
            (
                "_A few_ bot commands are fine, as well as the interactions (hug/kiss/etc) and paint being generally alright.",
                "Repeated bot commands should have a verbal warning saying to keep to <#490991441255071745>.",
                "Continued bot commands should have a mute (10m).",
            ),
        ),
        (
            "Off-topic messages in the coding channel",
            (
                "This is generally Kae's domain to deal with.",
                "If someone posts there about topics that are irrelevant to the current discussion or things that definitely don't belong, verbal warning.",
                "Continuing on these conversations should come with a mute (10m).",
                "Continuing on these conversations should come with a mute (2h).",
            ),
        ),
        (
            "Off-topic messages in the art channel",
            (
                "Verbally warn the user that they need to keep on the topic of the art or the channel.",
                "Continuing conversation should result in a mute (10m).",
                "Continuing conversation should result in a mute (2h).",
            ),
        ),
        (
            "Conversing in the bot support/ideas channels",
            (
                "Verbally tell the user to keep on topic.",
                "Continuing conversation should result in a mute (10m).",
                "Continuing conversation should result in a mute (2h).",
            ),
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
            (
                "Delete the message. Add the art ban role to the user.",
            ),
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
                "This rule is specifically here to deal with things that are shitty but aren't explicitly stated.",
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
