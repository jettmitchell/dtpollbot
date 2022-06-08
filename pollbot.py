import os
import asyncio
import twitchio
from twitchio.ext import commands
from twitchio.ext import routines
import datetime
import time
import random

duration = 15.0

class Option:
    def __init__(self, index, option, total):
        self.index = index
        self.option = option
        self.total = total


class Vote:
    def __init__(self, username, option):
        self.username = username
        self.option = option

class Bot(commands.Bot):

    # Class properties
    optionsIndex = []
    optionsList = []
    pollActive = False # initialize to 'not active'
    storedVotes = []
    title = ""
    duration = 0.0
    #voteEnd = datetime.datetime.now() #initializes to now
    ctx = ""


    def __init__(self):
        # Initialise our Bot with our access token, prefix and a list of channels to join on boot...
        super().__init__(token=os.environ['TMI_TOKEN'],
            prefix=os.environ['BOT_PREFIX'],
            initial_channels=[os.environ['CHANNEL']],
            client_id=os.environ['CLIENT_ID'],
            nick=os.environ['BOT_NICK']
        )
    



    # fires whenever someone joins the channel
    async def event_join(self, channel: twitchio.channel, user: twitchio.user):
        # bot can announce itself
        if user.name.lower() == self.nick.lower():
            print(f"Successfully joined #{channel.name}!")
            await channel.send("/me is now online!")

    # fires when the bot joins a channel ... but doesn't seem to be working?
    # async def event_channel_joined(self, channel: twitchio.channel):
    #     # bot can announce itself
    #     print(f"Successfully joined #{channel.name}!")
    #     await channel.send("/me is now online!")



    # fires every time a message is sent in chat
    async def event_message(self, msg: twitchio.message):
        
        # make sure the bot ignores itself
        if msg.echo:
            #print("detected botself's message")
            return

        await self.handle_commands(msg)

        #if message wasn't a command, then see if we need to record votes:
        if self.pollActive and msg.content in self.optionsIndex:

            if alreadyVoted(self.storedVotes, msg.author.name.lower()):
                await msg.channel.send(f"Already counted a vote from @{msg.author.name}!")

            else:
                self.storedVotes.append(Vote(msg.author.name.lower(),msg.content))
                await msg.channel.send(f"Vote for {msg.content} counted from @{msg.author.name}")


    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Send a hello back!
        await ctx.send(f'Hello @{ctx.author.name}!')

    @commands.command()
    async def hell(self, ctx: commands.Context):
        # Send a hello back!
        await ctx.send(f"I've saved a place for you, {ctx.author.name}")

    @commands.command()
    async def hewwo(self, ctx: commands.Context, *args):
        if ":3" in args:
            await ctx.send(f'Hewwo! :3')
        else:
            await ctx.send(f'H.. hewwo?')

    @commands.command()
    async def dtpoll(self, ctx: commands.Context, title, dur, *options):
        self.duration = float(dur)#datetime.timedelta(minutes=float(duration))
        self.title = title
        self.optionsList = list(options) # replace any past options with current set
        self.ctx = ctx

        start_poll.start()


    # @commands.command()
    # async def endpoll(self, ctx: commands.Context):
    #     if pollActive:
    #         await end_poll(ctx)
    #     else:
    #         await ctx.send(f'There is no active poll')


@routines.routine(seconds=duration, iterations=2)
async def start_poll():
    pass # poll is active...

    #     if pollActive and datetime.datetime.now() < voteEnd:
#         print(f"there is an active poll")
#     else:
#         end_poll(ctx)


# @start_poll.error
# async def poll_on_error(error: Exception):
#     print(f'{error}')


@start_poll.before_routine
async def poll_before():
    bot.pollActive = True #Start accepting votes
    bot.storedVotes = [] # Clear past votes
    bot.optionsIndex = [] # Clear past options
    #bot.voteEnd = datetime.datetime.now() + bot.duration

    text = "Starting a new poll ("+str(duration)+" seconds): "+bot.title+" "

    for count, option in enumerate(bot.optionsList):
        text += str(count+1)+". "+option+" "
        #optionsList.append(option)
        bot.optionsIndex.append(str(count+1))

    print(f"started a new poll with {len(bot.optionsList)} options")

    await bot.ctx.channel.send(text)


@start_poll.after_routine
async def end_poll():
    bot.pollActive = False # Stop accepting votes

    # Count all votes and determine winner(s)

    finalResults = []

    print(f"there were {len(bot.optionsList)} options in this poll")

    for count, option in enumerate(bot.optionsList):
        
        #votesForThisOpt = filter(voteForOption(count, bot.storedVotes), bot.storedVotes)
        #votesForThisOpt = filter(lambda vote: voteForOption(vote,count), bot.storedVotes)   # 'vote' should be one item from 'bot.storedVotes'

        votesForThisOpt = [vote for vote in bot.storedVotes if vote.option == str(count+1)]

        print(f"option {str(count+1)} got {len(votesForThisOpt)} votes")

        temp = Option(count+1, option, len(votesForThisOpt))
        finalResults.append(temp)

    textTemp = ""
    winner = Option(0, "no winner", 0)

    for result in finalResults:
        if winner.total < result.total:
            winner = result

        textTemp = textTemp + (f"option {result.index} got {result.total} votes. ")
 
    textTemp = textTemp + (f"Winning option is: {winner.index}. {winner.option}")


    # TO DO: Record ties and gracefully handle abstained polls (ie, no one votes)


    await bot.ctx.channel.send(textTemp)



    

def alreadyVoted(list, username):
    for x in list:
        if x.username == username:
            return True
    return False


# def voteForOption(vote, option):
#     if vote.option == option:
#         return True
#     else:
#         return False




# Main code:

bot = Bot()

if __name__ == "__main__":
    print("Starting up PollBot")
    bot.run()