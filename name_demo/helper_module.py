# helper_module.py

def greet(name):
    print(f"👋 Hello, {name}!")

print("✅ helper_module.py 被執行了")
print(f"__name__ in helper_module: {__name__}")

if __name__ == "__main__":
    print("🔧 helper_module.py 自己被執行，所以我會執行這段")
    greet("Tester")
