# Demonstrates how to use the dictionary data type to code the linked list structure.

head = { "value":11,
         "next" : {
            "value":3,
            "next" : { 
                "value":23,
                "next" : {
                    "value":7,
                    "next" : None
                }
            }
         }

}

print(head['next']['next']['value'])