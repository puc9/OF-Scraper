r"""
                                                             
 _______  _______         _______  _______  _______  _______  _______  _______  _______ 
(  ___  )(  ____ \       (  ____ \(  ____ \(  ____ )(  ___  )(  ____ )(  ____ \(  ____ )
| (   ) || (    \/       | (    \/| (    \/| (    )|| (   ) || (    )|| (    \/| (    )|
| |   | || (__     _____ | (_____ | |      | (____)|| (___) || (____)|| (__    | (____)|
| |   | ||  __)   (_____)(_____  )| |      |     __)|  ___  ||  _____)|  __)   |     __)
| |   | || (                   ) || |      | (\ (   | (   ) || (      | (      | (\ (   
| (___) || )             /\____) || (____/\| ) \ \__| )   ( || )      | (____/\| ) \ \__
(_______)|/              \_______)(_______/|/   \__/|/     \||/       (_______/|/   \__/
                                                                                      
"""
import traceback

import ofscraper.actions.download.utils.globals as common_globals
from ofscraper.actions.download.utils.log import get_medialog
from ofscraper.actions.metadata.utils.change import change_metadata
from ofscraper.classes.download_retries import download_retry


async def metadata(c, ele, model_id, username):
    try:
        async for _ in download_retry():
            return await change_metadata(c, ele, username, model_id)
    except Exception as E:
        common_globals.log.debug(f"{get_medialog(ele)} exception {E}")
        common_globals.log.debug(
            f"{get_medialog(ele)} exception {traceback.format_exc()}"
        )
        common_globals.log.traceback_(f"{get_medialog(ele)} Metadata Failed\n")
        return "skipped", 0