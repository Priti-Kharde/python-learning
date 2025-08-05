while True:
    try:
        number = int(input("Enter number: "))
    except ValueError:
        print("Please type an integer")
    except Exception:
        print("Unexpected error")
    else:
        print(f"User input = {number}")
        break

    finally:
        print("finally always executes..")