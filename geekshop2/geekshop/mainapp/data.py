"""Серилизация данных в json"""
import json


test = [[{'class_list': 'product-small clearfix',
          'a_href': "catalog/products/1/",
          'a_class': "hover-product-link",
          'id': 'product-1'},
         {'a_href': '',
          'a_class': "hover-product-link",
          'class_list': 'product-small product-small-margin clearfix',
          'id': 'product-2'},
         {'a_href': '',
          'a_class': "hover-product-link",
          'class_list': 'product-small product-small-margin clearfix',
          'id': 'product-3'},
         {'a_href': '',
          'a_class': "hover-product-link", 'class_list': 'product-small product-small-margin clearfix',
          'id': 'product-4'}],
        [{'class_list': "tranding-products", 'src': 'product-11.jpg'},
         {'class_list': "tranding-products trending-product-margin-left", 'src': 'product-21.jpg'},
         {'class_list': "tranding-products trending-product-margin-left", 'src': 'product-31.jpg'},
         {'class_list': "tranding-products trending-product-margin-top", 'src': 'product-41.jpg'},
         {'class_list': "tranding-products trending-product-margin-left trending-product-margin-top", 'src': 'product-5.jpg'},
         {'class_list': "tranding-products trending-product-margin-left trending-product-margin-top", 'src': 'product-6.jpg'}],
        [
            {'class_list': 'tranding-products', 'src': 'product-11.jpg'},
            {'class_list': 'tranding-products trending-product-margin-left', 'src': 'product-21.jpg'},
            {'class_list': 'tranding-products trending-product-margin-left', 'src': 'product-31.jpg'},
            {'class_list': 'tranding-products trending-product-margin-top', 'src': 'product-41.jpg'},
            {'class_list': 'tranding-products trending-product-margin-left trending-product-margin-top', 'src': 'product-5.jpg'},
            {'class_list': 'tranding-products trending-product-margin-left trending-product-margin-top', 'src': 'product-6.jpg'},
            {'class_list': 'tranding-products trending-product-margin-top', 'src': 'product-11.jpg'},
            {'class_list': 'tranding-products trending-product-margin-top trending-product-margin-left', 'src': 'product-21.jpg'},
            {'class_list': 'tranding-products trending-product-margin-top trending-product-margin-left', 'src': 'product-31.jpg'},
            {'class_list': 'tranding-products trending-product-margin-top', 'src': 'product-41.jpg'},
            {'class_list': 'tranding-products trending-product-margin-left trending-product-margin-top', 'src': 'product-5.jpg'},
            {'class_list': 'tranding-products trending-product-margin-left trending-product-margin-top', 'src': 'product-6.jpg'},
        ]
        ]

with open('data.json', 'w', encoding='utf-8') as f:
    products = json.dump(test, f)
