import character as char


def main():
    print("Welcome to character customizer")
    carol = char.Character("Carol")
    carol.randomize_ancestry()
    carol.randomize_background()
    carol.randomize_class()
    print("Carol's ancestry is "+carol.ancestry)
    print("Carol's background is "+carol.background)
    print("Carol's class is "+carol.job)
    
if __name__ == "__main__":
    main()