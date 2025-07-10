def user(name, * args, education ="BE", **kwargs):
    print(name)
    print(args)
    print(education)
    print(kwargs)
user("ppp",[2,3,4],a =67,b=5)