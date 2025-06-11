stack = []

while True:
    print("\nChoose: push / pop / peek / is_empty / size")
    choice = input("Enter your choice: ").strip().lower()

    if choice == "push":
        value = input("Enter value to push: ")
        stack.append(value)
        print(f"✅ '{value}' pushed to stack.")

    elif choice == "pop":
        if len(stack) == 0:
            print("⚠️ Stack is empty. Nothing to pop.")
        else:
            popped = stack.pop()
            print(f"🗑️ Popped item: {popped}")

    elif choice == "peek":
        if len(stack) == 0:
            print("⚠️ Stack is empty. Nothing to peek.")
        else:
            print(f"👀 Top item: {stack[-1]}")

    elif choice == "is_empty":
        print(f"📭 Is empty?: {'Yes' if len(stack) == 0 else 'No'}")

    elif choice == "size":
        print(f"📦 Stack size: {len(stack)}")

    else:
        print("❌ Invalid choice. Try again.")
