from uagents import Agent, Context, Bureau
import asyncio
loop=asyncio.new_event_loop()
asyncio.set_event_loop(loop)
omnitrix=Agent(name="Omnitrix", seed="Omnitrix function override code 10", endpoint="http://127.0.0.1/omnitrix")
@omnitrix.on_interval(period=3)
async def introduce(ctx: Context):
    ctx.logger.info(f'Hello my name is: {omnitrix.name}')

if __name__ == "__main__":
    omnitrix.run()
