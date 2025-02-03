import pytest
from .yt_finder import YoutubeSearch


@pytest.mark.asyncio
class TestSearch:

    async def test_init_defaults(self):
        search = YoutubeSearch("test")
        videos = await search.search()
        assert search.max_results is None
        assert 1 <= len(videos)

    async def test_init_max_results(self):
        search = YoutubeSearch("test", max_results=10)
        videos = await search.search()
        assert 10 == search.max_results
        assert 10 == len(videos)

    async def test_dict(self):
        search = YoutubeSearch("test", max_results=10)
        await search.search()
        assert isinstance(search.to_dict(), list)

    async def test_json(self):
        search = YoutubeSearch("test", max_results=10)
        await search.search()
        assert isinstance(search.to_json(), str)

    async def test_language(self):
        search = YoutubeSearch("test", max_results=10, language="en")
        await search.search()
        assert search.language == "en"

    async def test_region(self):
        search = YoutubeSearch("test", max_results=2, region="US")
        videos = await search.search()
        # for video in videos:
        #     print(video.get_views())
        assert search.region == "US"

    async def test_link_to_search(self):
        search = YoutubeSearch("https://www.youtube.com/watch?v=dQw4w9WgXcQ", max_results=2, region="US")
        videos = await search.search()
        for video in videos:
            print("=" * 20)
            print(f"Title: {video.get_title()}")
            print(f"URL: {video.get_yt_url()}")
            print("=" * 20)
        assert search.region == "US"