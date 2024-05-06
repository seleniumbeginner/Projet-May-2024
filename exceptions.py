# ItemsInCart = 0
# # 2 items added in the cart by automation

# if ItemsInCart !=2 :
#     raise Exception("products cart count not matching")

# ItemsInCart=0 
# if ItemsInCart !=2 :
#     pass
# assert (ItemsInCart ==0)
try :
     
   with open('text_file.txt','r') as reader: 
    reader.read()
   
except Exception as e :   
    print(e)
    print("intended failure to check ")
    
finally :
    print ("i am going to be python developer")
    