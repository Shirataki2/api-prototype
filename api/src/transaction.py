from typing import Optional
import aiohttp

class AioTransaction:
    sess: Optional[aiohttp.ClientSession] = None

    def start(self):
        self.sess = aiohttp.ClientSession()

    async def stop(self):
        await self.sess.close()
        self.sess = None

    def __call__(self) -> aiohttp.ClientSession:
        assert self.sess is not None
        return self.sess

transaction = AioTransaction()
