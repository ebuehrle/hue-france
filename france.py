import asyncio
import HueBLE
import itertools
import time

async def main():
    devices = await HueBLE.discover_lights()
    light = HueBLE.HueBleLight(devices[0])
    print(await light.poll_light_name())

    blue = (0.191, 0.143)
    white = (0.308, 0.326)
    red = (0.623, 0.330)
    france = (blue, white, red)

    for color in itertools.cycle(france):
        await light.set_colour_xy(*color)
        time.sleep(2)

if __name__ == '__main__':
    asyncio.run(main())
