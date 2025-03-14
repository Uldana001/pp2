import re
filepath = "/Users/uldanakonyratbaeva/Desktop/row.txt"
with open(filepath, "r", encoding="utf-8") as file:
    text = file.read()

items = re.findall(r"\d+\.\n(.*?)\n\d+,\d{3} x \d{1,3} ?\d{0,3},\d{2}", text, re.DOTALL)
prices = re.findall(r"(\d+,\d{3}) x (\d{1,3} ?\d{0,3},\d{2})\n(\d{1,3} ?\d{0,3},\d{2})", text)
total = re.search(r"ИТОГО:\n([\d\s]+,\d{2})", text)
receipt_number = re.search(r"Чек №(\d+)", text)
date_time = re.search(r"Время: ([\d.]+ [\d:]+)", text)


print("Найденные товары:")
for i, item in enumerate(items):
    qty, price, total_price = prices[i][:3]
    print(f"{i+1}. {item.strip()} - {qty} шт. * {price} = {total_price}")

if total: 
    print(f"\nОбщая сумма покупки: {total.group(1)}")

if receipt_number and date_time:
    print(f"\n Номер чека: {receipt_number.group(1)}")
    print(f"Дата и время: {date_time.group(1)}")