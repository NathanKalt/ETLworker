from factory.utils.utils import object_from_settings
import factory.settings as settings
import asyncio


async def run():
    cls = object_from_settings(settings.FEED_PIPELINE)
    await cls.start()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run())


