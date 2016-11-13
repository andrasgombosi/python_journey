def cheese_and_crackers(chese_count,boxes_of_crackers):
        print("You have %d cheeses!") % chese_count
        print("You have %d bpxes of crackers") % boxes_of_crackers
        print ("\n")

print("direct call")

cheese_and_crackers(20,30)


print("with vars")

cheese = 12
crackers = 14

cheese_and_crackers(cheese,crackers)

print("maths inside")
cheese_and_crackers(cheese + 12,crackers -8)
