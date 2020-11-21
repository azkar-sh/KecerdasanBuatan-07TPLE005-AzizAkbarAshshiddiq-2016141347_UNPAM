from sklearn.datasets import load_iris

#datasets
#merek = 0 is alisan, 1 is president, 2 is boss, 3 is stanley, 4 is polo
#warna = 0 is putih, 1 is biru, 2 is hijau, 3 is kuning, 4 is merah
#size = 0 is small, 1 is medium, 2 is large, 4 is extralarge
#jenis = 0 is panjang, 1 is pendek
#merek            #warna        #size       #jenis
x = [
    [0,                 0,                  0,              0],
    [0,                 0,                  0,              1],
    [1,                 0,                  0,              0],
    [2,                 1,                  0,              0],
    [2,                 2,                  1,              0],
    [2,                 2,                  1,              1],
    [1,                 2,                  1,              1],
    [0,                 1,                  0,              0],
    [0,                 2,                  1,              0],
    [2,                 1,                  1,              0],
    [0,                 1,                  1,              1],
    [1,                 1,                  0,              1],
    [1,                 0,                  1,              0],
    [2,                 1,                  0,              1],
    [2,                 2,                  2,              0],
    [2,                 2,                  3,              0],
    [2,                 3,                  3,              0],
    [3,                 3,                  3,              0],
    [3,                 4,                  3,              0],
    [4,                 3,                  2,              1],
    [4,                 4,                  2,              1],
]
y = [0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1,1,1,0,0,0,0,1,1,1,0]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)


def prog() :
    merek = int(input("merek? (0 is alisan, 1 is president, 2 is boss, 3 is stanley, 4 is polo) : "))
    warna = int(input("warna? (0 is putih, 1 is biru, 2 is hijau, 3 is kuning, 4 is merah) : "))
    size = int(input("Size? (0 is small, 1 is medium, 2 is large, 4 is extralarge) : "))
    jenis = int(input("Jenis? 0 panjang, 1 pendek : " ))

    if clf.predict([[merek, warna, size, jenis]]):
        print("\nSaya akan pergi ke Supermarket")
    else:
        print("\nNongkrong di Rumah aja!")


prog()

