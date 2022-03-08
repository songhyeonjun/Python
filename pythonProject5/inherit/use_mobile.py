from inherit.mobile import Phone, SamsungPhone, ApplePhone

m1 = Phone()
m1.call()
m1.text()

sp = SamsungPhone()
sp.name = "hong"
sp.game()
sp.internet(3)

ap = ApplePhone()
ap.size = 11
ap.text()
ap.youtube(2, "스포츠")
