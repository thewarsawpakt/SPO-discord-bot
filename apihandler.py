import requests
import discord
headers = {
    'TRN-Api-Key': '57ff22ef-349c-456e-bffa-6cffcf82b764',
    'Accept': 'application/json',
    'Accept-Encoding': 'gzip'}



def getProfile(profile):
    r = requests.get(f"https://public-api.tracker.gg/v2/division-2/standard/profile/uplay/{profile}", headers=headers)
    try:
        json = dict(r.json())['data']
    except:
        error = discord.Embed(name="Error: ", title="That user does not exist!", color=0xff0000)
        error.add_field(name="Error: ", value="User does not exist.")
        return error
    body = discord.Embed(name="Division 2 stats", title=f"Stats for {json['platformInfo']['platformUserHandle']}", color=0x0080ff)
    body.set_thumbnail(url=f"{json['platformInfo']['avatarUrl']}")
    body.add_field(name="-- Basic Stats -- ",value=f"""Uplay Name: {json['platformInfo']['platformUserHandle']}
    Time Played: {json['segments'][0]['stats']['timePlayed']['displayValue']}
    DZ Rank: {json['segments'][0]['stats']['rankDZ']['value']}
    Highest Player Level (On most recently created character): {json['segments'][0]['stats']['highestPlayerLevel']['displayValue']}
    NPC Kills:  {json['segments'][0]['stats']['killsNpc']['displayValue']}""")
    body.add_field(name="-- Advanced Stats --", value=f"""
    Hyena Enemies Killed: {json['segments'][0]['stats']['killsFactionBlackbloc']['displayValue']}
    Outcast Enemies Killed: {json['segments'][0]['stats']['killsFactionCultists']['displayValue']}
    True Son Enemies Killed: {json['segments'][0]['stats']['killsFactionMilitia']['displayValue']}
    Black Tusk Enemies Killed: {json['segments'][0]['stats']['killsFactionEndgame']['displayValue']}
    """)
    return body




# Intresting keys:
"""
data:
    - platformInfo
        platformUserHandle
    segments:
        stats:
            - rankDZ
            - timePlayedPve
            - xPTotal
            - xPClan
            - killsNpc
            - timePlayed

"""