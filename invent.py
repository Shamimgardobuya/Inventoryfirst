#We use dictionary because it is the data type that will allow specificity.
#create a dictionary with the main goods as the variable
#store the subtopic of the goods as key of the dictionary
#Create another dictionary for the values of the key to cover the specific name of items
#Add the number of the items specifically 
#

health_beauty={"Hair":{"conditioner":4,"Wigs":56,"Accessories":34,"Fragrances":13},"Makeup":{"Eyes":57,"lips":87,"face":34},"Oral care":{"children's Dental care":23,"Dental kits":23,"Mouthwash":45}}
gaming={"PlayStation":{"playstation3":4,"playstation4":14},"Digital games":{"Nintendo switch":18,"Xbox360":4},"Nintendo":{"Nintendo 3DS":2}}
fashion={"men's fashion":{"shirts":20,"tanks":12,"pants":67},"women's fashion":{"dresses":34,"Jewelery":1000},"baby":{"baby boys":23,"baby girls":46}}
electronics={"televisions":{"Smart Tvs":12,"Data projectors":12},"cameras":{"compact cameras":14,"SLR Cameras":17},"Home Audio":{"Sony Speakers":56,"sound bars":8}}
garden_outdoor={"Garden":{"Hand Tools":23},"Outdoor":{"Lighting":56}}
print(f"these are the products we have for health and beauty",health_beauty)
print(f"these are the products we have for Gaming",gaming)
print(f"these are the products we have for Fashion ",fashion)
print(f"these are the products we have for Electronics",electronics)
print(f"these are the products we have for Garden and Outdoor",garden_outdoor)


good=health_beauty or gaming or fashion or electronics or garden_outdoor
good=str(input("Enter a good  "))
item=str(input("Enter the item that you would like to see "))
if good=="health_beauty" or "health and beauty" and item=="Hair":
    print(health_beauty["Hair"])
elif good==(("health_beauty" or "health and beauty") and (item=="conditioner")):
    print(health_beauty["Hair"]["conditioner"], f"Is the number of conditioners")
elif good==(("health_beauty" or "health and beauty") and (item=="Wigs")):
    print(health_beauty["Hair"]["Wigs"], f"Are the numbers of wigs")
elif good==(("health_beauty" or "health and beauty") and (item=="Accessories")):
    print(health_beauty["Hair"]["Accessories"], f"Are the numbers of accessories")
elif good==(("health_beauty" or "health and beauty") and (item=="Fragrances")):
    print(health_beauty["Hair"]["Fragrances"], f" Is the number")
if good==(("health_beauty" or "health and beauty") and (item=="Makeup")):
    print(health_beauty["Makeup"])  
elif good==(("health_beauty" or "health and beauty")  and (item=="Eyes")):
    print(health_beauty["Makeup"]["Eyes"], f" are the number of eye makeup")
elif good==(("health_beauty" or "health and beauty")  and (item=="Lips")):
    print(health_beauty["Makeup"]["lips"], f" are the number of lip makeup")
elif good==(("health_beauty" or "health and beauty")  and (item=="face")):
    print(health_beauty["Makeup"]["face"], f" are the number of face makeup")
elif good==(("health_beauty" or "health and beauty")  and (item=="childrens dental care")):
    print(health_beauty["Oral care"]["children's Dental care"], f" are the dental kits for children")
elif good==(("health_beauty" or "health and beauty")  and (item=="mouthwash" or "Mouthwash")):
    print(health_beauty["Oral care"]["Mouthwash"], f" are the number for mouthwash")

if ((good=="gaming") and item==("Playstation3" or "playstation3")) :
    print(gaming["PlayStation"]["playstation3"], f" is the number of Playstation3 present")
elif ((good=="gaming") and (item=="Playstation4" )):
    print(gaming["PlayStation"]["playstation4"], f" is the number of Playstation4 present")
elif ((good=="gaming") and (item=="Nintendo switch")):
    print(gaming["Digital games "]["Nintendo switch"], f" is the number ")
elif good=="gaming" and item=="xBox" :
    print(gaming["Digital games"]["xbox360"], f" is the  number of xbox present")
elif good=="gaming" and item=="Nintendo 3ds" :
    print(gaming["Nintendo"]["Nintendo 3DS"], f" is the  number of Nintendo 3DS")
    
    
elif ((good=="fashion")  and (item=="Women's fashion")) :
    print(fashion["women's fashion"], f" women's fashion you purchased")
elif good=="fashion"  and item=="men's fashion" :
    print(fashion["men's fashion"])
elif good==(("fashion"  )and (item=="dresses" or "women's dress" )):
    print(fashion["women's fashion"]["dresses"])
elif good==(("fashion") and (item=="baby fashion boys" or "baby boy")):
    print(fashion["baby"]["baby boys"] ,f"number of boy items ")
elif ((good=="fashion") and (item=="baby")):
    print(fashion["baby"],f" are items purchased for babies")
elif ((good=="fashion") and (item=="baby girl")):
    print(fashion["baby"]["baby girls"],f" are number of baby girl clothes purchased")
elif good==(("fashion"  )and (item=="jewelry")):
    print(fashion["women's fashion"]["Jewelery"], f"is the number of women jewelry available")
    
    
elif ((good=="electronics") and (item=="Smart tvs" or "smart TV")):
    print(electronics["televisions"]["Smart Tvs"] , f"are the number of Smart tv purchased")
elif good=="electronics" and item=="data projectors" or "projectors":
    print(electronics["televisions"]["Data projectors"] , f"are the number of data projectors purchased")
elif ((good=="electronics") and (item=="cameras")):
    print(electronics["cameras"],f"for the cameras")
elif good==(("electronics") and item==("Home audio")):
    print(electronics["Home Audio"])
    
    
elif good==(("garden_outdoor" )and item==("Hand Tools")):
    print(garden_outdoor["Garden"]["Hand Tools"] ,f"are the number of hand tools present")
elif good==(("garden_outdoor" )and item==("Lighting")):
    print(garden_outdoor["Outdoor"]["Lighting"] ,f"are the number of lighting equipments")









