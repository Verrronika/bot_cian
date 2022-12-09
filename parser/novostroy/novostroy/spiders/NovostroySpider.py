import scrapy
import ast
import json
from ..items import NovostroyItem
 
name_to_num = {}

class NovostroySpiderSpider(scrapy.Spider):
 
    name = 'novostroy_spider'
    allowed_domains = ['www.novostroy.ru']
    # index = 0
 
    def start_requests(self):
        url_pattern = 'https://www.novostroy.ru/buildings/?Building_page='
 
        for page_number in range(1, 50):
            yield scrapy.Request(url=f'{url_pattern}{page_number}', callback=self.parse)
 
    def parse(self, response):    
        info = response.xpath("//script[@type='application/ld+json']/text()").extract_first()
        info = ast.literal_eval(info)
        for info_item in info["itemListElement"]:
            # info = ast.literal_eval(info)
            # info_item = info_list["itemListElement"]
            # print(info_item)
            # # print(type(item_list))
            # name = info_item["name"]
            link = 'https://www.novostroy.ru' + info_item["@id"]

            print(link)
            print()
            yield response.follow(link, callback=self.parse_link) 
 
 
    def parse_link(self, response):    
        items = NovostroyItem()
 
        info = response.xpath("//script[@type='application/ld+json']/text()").extract_first()
        info = json.loads(info)
        # print(info["name"].encode().decode())
        # info = ast.literal_eval(info)
        # items["name"] = ''.join(response.xpath("//meta[@name='keywords']/@content").extract_first()).replace('\u0416\u041a', 'as')
        # print("name:   ", items["name"].encode())
        # name = items["name"]
        if not("image" in info) and not("name" in info):
            return
        items["image"] = info["image"]
        items['name'] = info['name']
        items['room_types'] = []
        items['studio'] = -1
        items['one_room'] = -1
        items['two_room'] = -1
        items['three_room'] = -1
        items['four_room'] = -1
        items['multiroom'] = -1
        if len(response.xpath('//div[@class="preview-slider_adress"]/a/text()').extract()) == 0:
            return
        items['district'] = response.xpath('//div[@class="preview-slider_adress"]/a/text()').extract_first()
        if not('offers' in info):
            return

        for room_info in info["offers"]:
            if (room_info["name"] == "квартиры-студии"):
                items["room_types"].append('studio')
                items["studio"] = int(room_info["lowPrice"])
            elif (room_info["name"] == "1-комнатные квартиры"):
                items["room_types"].append('one_room')
                items["one_room"] = int(room_info["lowPrice"])
            elif (room_info["name"] == "2-комнатные квартиры"):
                items["room_types"].append('two_room')
                items["two_room"] = int(room_info["lowPrice"])
            elif (room_info["name"] == "3-комнатные квартиры"):
                items["room_types"].append('three_room')
                items["three_room"] = int(room_info["lowPrice"])
            elif (room_info["name"] == "4-комнатные квартиры"):
                items["room_types"].append('four_room')
                items["four_room"] = int(room_info["lowPrice"])
            elif (room_info["name"] == "многокомнатные квартиры"):
                items["room_types"].append('multiroom')
                items["multiroom"] = int(room_info["lowPrice"])

        if len(items["room_types"]) == 0:
            return
        # if items["room_types"] == []:
        #     return
 
        yield items