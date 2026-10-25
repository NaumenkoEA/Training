friends = {"Alina", "Sasha", "Zhenya", "Max"}
colleagues = {"Zhenya", "Max", "Oleg", "Ivan"}

print("и друзья, и коллеги." , friends & colleagues)
print("хотя бы в одном множестве.", friends | colleagues)
print("друзья, но не коллеги.", friends - colleagues)
print("коллеги, но не друзья.", colleagues -friends )