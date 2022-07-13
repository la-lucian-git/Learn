string = "Brave-Bold War-band is sneaky-strong."
ssn = "111-22-3333"
white = " Just some text "
url = "https://youtube.com/"
busted_url = "This%20url%20is%20encoded."

title_split = string.split()  # String to list
ssn_split = ssn.split("-")  # Split at whitespace by default
white_strip = white.strip()  # Remove white space at both ends
title_white_upper = white_strip.upper()
title_white_lower = white_strip.lower()
is_home = url.endswith(".com/")  # Return bool
is_shop = url.endswith(".com/shop")
is_absolute = url.startswith("https://")
busted_url_clean = busted_url.replace("%20", " ")

print("")
print("string = Brave-Bold War-band is sneaky-strong. --->", string)
print("ssn = 111-22-3333 --->", ssn)
print("white =  Just some text --->", white)
print("url = https://youtube.com/ --->", url)
print("busted_url = This%20url%20is%20encoded. --->", busted_url)
print("")

print("title_split = string.split() --->", title_split)
print("ssn_split = ssn.split() --->", ssn_split)
print("white_strip = white.strip() --->", white_strip)
print("white_strip = white.strip() --->", white_strip)
print("title_white_upper = white_strip.upper() --->", title_white_upper)
print("title_white_lower = white_strip.lower() --->", title_white_lower)
print('is_home = url.endswith(".com/") --->', is_home)
print('is_home = url.endswith(".com/shop") --->', is_shop)
print('is_absolute = url.startswith("https://") --->', is_absolute)
print('busted_url_clean = busted_url.replace("%20", " ") --->', busted_url_clean)

