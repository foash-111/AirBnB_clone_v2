def do_create(self, args):
        # """ Create an object of any class"""
        # # seperate args
        # d_args = args.split(' ')
        # cls_name = d_args[0]
        # if not cls_name:
        #     print("** class name missing **")
        #     return
        # elif cls_name not in HBNBCommand.classes:
        #     print("** class doesn't exist **")
        #     return
        # # sepreare paramteres, put it into dictionary
        # new_instance = HBNBCommand.classes[cls_name]()
        # for i in d_args[1:]:
        #     i = i.split('=')
        #     value = i[1]
        #     # finds and replaces the _ and the "
        #     value = value.replace('_', " ")
        #     # case string
        #     if value[0] == '"':
        #         value = value.replace('"', "")
        #         if '"' in value:
        #             value = value.replace('"', '\"')
        #     # case float
        #     elif '.' in value:
        #         value = float(value)
        #     # case integer
        #     else:
        #         value = int(value)
        #     key = i[0]
        #     new_instance.__dict__[key] = value
        # my_class = HBNBCommand.classes[cls_name]
        # my_class.save(new_instance)
        # print(new_instance.id)
