from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst

def remove_newlines_and_spaces(value):
    return ' '.join(value.split()).strip()

class JobItemLoader(ItemLoader):
    default_output_processor = TakeFirst()

    job_title_in = MapCompose(remove_newlines_and_spaces)
    description_in = MapCompose(remove_newlines_and_spaces)
    location_in = MapCompose(remove_newlines_and_spaces)
    price_in = MapCompose(remove_newlines_and_spaces)
    proposal_in = MapCompose(remove_newlines_and_spaces)
    link_in = MapCompose(remove_newlines_and_spaces)
