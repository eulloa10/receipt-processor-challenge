import math

class ReceiptScorer:

    TOTAL_CENTS_REWARD = 50
    TOTAL_MULTIPLE_REWARD = 25
    ITEMS_COUNT_REWARD = 5
    ITEM_DESC_REWARD_MULT = 0.2
    PURCHASE_DATE_REWARD = 6
    PURCHASE_TIME_REWARD = 10

    def __init__(self, payload):
        self.retailer = payload.get('retailer')
        self.purchase_date = payload.get('purchaseDate')
        self.purchase_time = payload.get('purchaseTime')
        self.items = payload.get('items')
        self.total = payload.get('total')
        self.receipt_score = 0

    def score_retailer_name(self):
        alpha_num_count = 0
        for char in self.retailer:
            if char.isalnum():
              alpha_num_count += 1
        return alpha_num_count

    def score_total_cents(self):
        cents = self.total[-2:]
        if cents == '00':
          return self.TOTAL_CENTS_REWARD
        return 0

    def score_total_multiple(self):
        if float(self.total) % .25 == 0:
            return self.TOTAL_MULTIPLE_REWARD
        else:
            return 0

    def score_receipt_items(self):
        item_count = len(self.items)
        return (item_count // 2) * self.ITEMS_COUNT_REWARD

    def score_item_descriptions(self):
        total_points = 0
        for item in self.items:
            description = item['shortDescription'].strip()
            if len(description) % 3 == 0:
                total_points += math.ceil(float(item['price']) * self.ITEM_DESC_REWARD_MULT)
        return total_points


    def score_purchase_date(self):
        day = int(self.purchase_date.split('-')[2])
        if day % 2 == 0:
          return 0
        return self.PURCHASE_DATE_REWARD

    def score_purchase_time(self):
        time = int(self.purchase_time.replace(":", ""))
        if time > 1400 and time < 1600:
            return self.PURCHASE_TIME_REWARD
        return 0

    def calculate_total_score(self):
        self.receipt_score = (
          self.score_retailer_name() +
          self.score_total_cents() +
          self.score_total_multiple() +
          self.score_receipt_items() +
          self.score_item_descriptions() +
          self.score_purchase_date() +
          self.score_purchase_time()
        )
        return self.receipt_score
