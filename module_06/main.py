import argparse
import asyncio
from aiopath import AsyncPath
from aioshutil import copyfile
import logging

"""
--source [-s] picture
--output [-o]
"""

parser = argparse.ArgumentParser(description='Sorting folder')
parser.add_argument("--source", "-s", help="Source folder", required=True)
parser.add_argument("--output", "-o", help="Output folder", default="dist")

args = vars(parser.parse_args())

source = args.get("source")
output = args.get("output")
output_folder = AsyncPath(output)


async def read_folder(path: AsyncPath) -> None:
    async for el in path.iterdir():
        if await el.is_dir():
            await read_folder(el)
        else:
            await copy_file(el)


async def copy_file(file: AsyncPath) -> None:
    ext = file.suffix
    new_path = output_folder / ext[1:]
    try:
        await new_path.mkdir(exist_ok=True, parents=True)
        await copyfile(file, new_path / file.name)
    except OSError as err:
        logging.info(err)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    base_folder = AsyncPath(source)
    asyncio.run(read_folder(base_folder))
    logging.info('Sorting is complete!')
