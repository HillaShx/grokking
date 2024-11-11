def debug(**args):
    print("debug args:")
    for name, val in args.items():
        print(f"\t{name} = {val}")