class Shop:
   p_count = 0
   p_price = 0
   p_total = 0
   p_visitor = 0
   p_vavg = 0

   def total_price(self):
       self.p_total = "총 결제금액은" + str((self.p_count * self.p_price)) + "원 입니다."
       return self.p_total