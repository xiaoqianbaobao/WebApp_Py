import orm
from models import User, Blog, Comment
import asyncio

async def test(loop):
    await orm.create_pool(loop=loop, user='root', password='csq123', db='awesome')
    u = User(name='test1', email='thest140@exafsample.com', passwd='1k32456789010', image='about:blank')

    await u.save()
    # await User.findAll()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
print('test')
print('success')
loop.close()
