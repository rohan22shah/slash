WALMART = {
    'site': 'walmart',
    'url': 'https://www.walmart.com/search?q=',
    'item_component': 'div',
    'item_indicator': {
        'data-item-id': True
    },
    'title_indicator': 'span.lh-title',
    'price_indicator': 'div.lh-copy',
    'link_indicator': 'a',
}

AMAZON = {
    'site': 'amazon',
    'url': 'https://www.amazon.com/s?k=',
    'item_component': 'div',
    'item_indicator': {
        'data-component-type': 's-search-result'
    },
    'title_indicator': 'h2 a span',
    'price_indicator': 'span.a-price span',
    'link_indicator': 'h2 a.a-link-normal',
}

# work in progress, not ready yet
TARGET = {
    'site': 'target',
    'url': 'https://www.target.com/s?searchTerm=',
    'item_component': 'div',
    'item_indicator': {
        'data-test': 'product-card-default'
    },
    'title_indicator': 'a[data-test~=product-title]',
    'price_indicator': 'span.a-price span',
    'link_indicator': 'h2 a.a-link-normal',
}

COSTCO = {
    'site': 'costco',
    'url': 'https://www.costco.com/CatalogSearch?dept=All&keyword=',
    'item_component': 'div',
    'item_indicator': {
        'class': 'product-tile-set'
    },
    'title_indicator': 'span a',
    'price_indicator': 'div.price',
    'link_indicator': 'span.description a',
}

BESTBUY = {
    'site': 'bestbuy',
    'url': 'https://www.bestbuy.com/site/searchpage.jsp?st=',
    'item_component': 'li',
    'item_indicator': {
        'class': 'sku-item'
    },
    'title_indicator': 'h4.sku-header a',
    'price_indicator': 'div.priceView-customer-price span',
    'link_indicator': 'a.image-link',
}

CONFIGS = [WALMART, AMAZON, COSTCO, BESTBUY]
