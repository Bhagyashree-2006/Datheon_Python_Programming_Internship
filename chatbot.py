import re

RESPONSES = [
    (
        re.compile(r"\b(hours|open|close|timing|time)\b"),
        "Maa business hours Monday–Friday, 9 AM–5 PM."
    ),
    (
        re.compile(r"\b(price|cost|shipping|return|refund|warranty)\b"),
        "Product details kosam: price $25, shipping 3–5 business days. "
        "Returns 30 days lopu accept chestam."
    ),
    (
        re.compile(r"\b(features|product|what does it do|about)\b"),
        "Maa product daily tasks-ni simple-ga manage cheyyadaniki help chestundi."
    ),
    (
        re.compile(r"\b(help|support|contact|human|agent)\b"),
        "Support kosam support@example.com ni contact cheyyandi."
    ),
]


def main():
    print("Welcome! Nenu support assistant-ni.")
    print("Business hours, product, shipping, returns gurinchi adagandi.")
    print("Exit avvadaniki bye, exit, leda quit type cheyyandi.")

    while True:
        message = input("\nYou: ").strip().lower()

        if not message:
            print("Bot: Oka question type cheyyandi.")
            continue

        if re.search(r"\b(bye|exit|quit)\b", message):
            print("Bot: Thanks! Bye 👋")
            break

        if re.search(r"\b(hi|hello|hey)\b", message):
            print("Bot: Hi! Meeku ela help cheyyali?")
            continue

        for pattern, response in RESPONSES:
            if pattern.search(message):
                print(f"Bot: {response}")
                break
        else:
            print(
                "Bot: Aa question ardham kaaledu. "
                "Business hours, product, shipping, returns gurinchi adagandi."
            )


if __name__ == "__main__":
    main()