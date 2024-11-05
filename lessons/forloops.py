def name(list1: list[str]) -> None:
    for dog_name in list1:
        print(f"Good boy, {dog_name}!")


name(list1=["tummy", "yummy", "gummy"])

names_list: list[str] = ["Ava", "Ramya", "Neha"]
for idx in range(0, len(names_list)):
    print(f"{idx}: {names_list[idx]}")
