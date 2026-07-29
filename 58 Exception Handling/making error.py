class InsultError(Exception):
    """Custom error for inappropriate inputs"""

    def __init__(self, message, input_value):
        self.input_value = input_value
        # Store the original message too
        self.message = message
        super().__init__(f"{message} (You entered: {input_value})")


try:
    number = int(input("Enter a number: "))

    if number < 0:
        raise InsultError("We don't do negatives here!", number)
    elif number == 0:
        raise InsultError("Zero? Really?!", number)  # Reuse your custom error

    result = 1 / number
    print(f"Result: {result}")

except ZeroDivisionError:
    print("You can't divide by zero IDIOT!")
except ValueError:
    print("Enter only numbers please!")
except InsultError as e:
    print(f"❌ Custom error: {e}")
    print(f"📝 Offending value: {e.input_value}")
    print(f"💬 Original message: {e.message}")  # Access the stored message
except Exception as e:
    print(f"⚠️ Something went wrong: {e}")
finally:
    print("🧹 Do some cleanup here")
    print("--- Program ended ---")