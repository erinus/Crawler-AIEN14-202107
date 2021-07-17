import requests

def main():
    l = [200, 200.3, 220.1, 215, 230]
    b = []
    for p in l:
        if p > 210:
            b.append(p)
    print(b)
    b = [
        p
        for p in l
        if p > 210
    ]
    print(b)

if __name__ == '__main__':
    main()