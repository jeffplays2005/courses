def read_data(filename):
    file = open(filename)
    lines = file.read().split("\n")
    file.close()
    return [ (line.split(":")[0], ([float(value) for value in line.split(":")[1].split("\t")])) for line in lines ]
    
# 1 line
def read_data(filename):
    return [ (line.split(":")[0], ([float(value) for value in line.split(":")[1].split("\t")])) for line in open(filename).read().split("\n") ] # file.close()


data = read_data("mean_rainfall1.txt")
print(data)
print(type(data))
print(type(data[0]))
print(type(data[0][0]), type(data[0][1]), type(data[0][1][0]))