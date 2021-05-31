
print(2+2)
print(4/5)
print(int(4/5))
print("2"+" 2")
user = "Patrick"
x = "7"
x = 7
x= 7.0
#float
print(x+3)


y = input()
print(y)

print ("quel est ton age?")
age = int(input())
print(age)
print("His age is " + str(age))

x +=3
x *=2
x =x+3
print(x)

voiture="bleu"
voiture+="rouge"
print(voiture)
voiture="bleu"
voiture*=3000
print(voiture)
#En programmation informatique, un booléen est un type de variable à deux états,
# destiné à représenter les valeurs de vérité de la logique et l'algèbre booléenne. Il est nommé ainsi d'après George Boole,
# fondateur dans le milieu du XIXᵉ siècle de l'algèbre portant son nom.

#spam = 7
#if spam > 5:
 #  print("five")
#if spam > 8:
 #  print("eight")

#num = 12
#if num > 5:
#    print("Bigger than 5")
 #   if num <=47:
 #       print("Between 5 and 47")

 #x = 4
#if x == 5:
#    print("Yes")
#else:
#    print("No")

#num = 3
#if num == 1:
#    print("One")
#else:
#    if num == 2:
#        print("Two")
#    else:
#        if num == 3:
#            print("Three")
#        else:
#            print("Something else")

#num = 3
#if num == 1:
#    print("One")
#elif num == 2:
#    print("Two")
#elif num == 3:
#    print("Three")
#else:
#    print("Something else")

#words = ["Hello", "world", "!"]

#number = 3
#things = ["string", 0, [1, 2, number], 4.56]
#print(things[1])
#print(things[2])
#print(things[2][2])

#str = "Hello world!"
#print(str[6])

nums = [7, 7, 7, 7, 7]
nums[2] = 5
print(nums)

nums = [1, 2, 3]
print(nums + [4, 5, 6])
print(nums * 3)

words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)




nums = [10, 9, 8, 7, 6, 5]

nums[0] = nums[1] - 5

if 4 in nums:

  print(nums[3])

else:

  print(nums[4])




  nums = [1, 2, 3]
  print(not 4 in nums)
  print(4 not in nums)
  print(not 3 in nums)
  print(3 not in nums)


  nums = [1, 2, 3]
  nums.append(4)
  print(nums)


  words = ["Python", "fun"]
  index = 1
  words.insert(index, "is")
  print(words)



  from datetime import datetime

  now = datetime.now()

  current_time = now.strftime("%H:%M:")
  print("Current Time =", current_time)

  current_time = now.strftime("%H")
  print("Current time=", current_time, "h")
  current_time = int(current_time)
  print(type(current_time))

  spam = 7

  if spam > 5:
    print("five")

  if spam > 8:
    print("eight")




  num = 12
  if num > 5:
    print("Bigger than 5")
    if num <= 47:
      print("Between 5 and 47")



  x = 4
  if x == 5:
    print("Yes")
  else:
    print("No")




  num = 3
  if num == 1:
    print("One")
  else:
    if num == 2:
      print("Two")
    else:
      if num == 3:
        print("Three")
      else:
        print("Something else")




  num = 3
  if num == 1:
    print("One")
  elif num == 2:
    print("Two")
  elif num == 3:
    print("Three")
  else:
    print("Something else")



  words = ["Hello", "world", "!"]




  number = 3
  things = ["string", 0, [1, 2, number], 4.56]
  print(things[1])
  print(things[2])
  print(things[2][2])

  str = "Hello world!"
  print(str[6])

  nums = [7, 7, 7, 7, 7]
  nums[2] = 5
  print(nums)

  nums = [1, 2, 3]
  print(nums + [4, 5, 6])
  print(nums * 3)

  words = ["spam", "egg", "spam", "sausage"]
  print("spam" in words)
  print("egg" in words)
  print("tomato" in words)

  nums = [10, 9, 8, 7, 6, 5]

  nums[0] = nums[1] - 5

  if 4 in nums:

    print(nums[3])

  else:

    print(nums[4])

  nums = [1, 2, 3]
  print(not 4 in nums)
  print(4 not in nums)
  print(not 3 in nums)
  print(3 not in nums)

  nums = [1, 2, 3]
  nums.append(4)
  print(nums)

  words = ["Python", "fun"]
  index = 1
  words.insert(index, "is")
  print(words)


