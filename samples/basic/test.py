from db_modules import Studentsfrom flask_restful
import reqparse, Resource
class StudentsAPI(Resource): 
    def__init__(self):
        self.parser = reqparse.RequestParser() 
        self.parser.add_argument("st_id", type = str) 
        self.parser.add_argument("name", type =        str)
        self.parser.add_argument("classID", type = str)
        self.parser.add_argument("remark", type = str)
    
    def get(self):
         args = self.parser.parse_args() 
         key_st_id = args.st_id 
         key_name = args.name 
         key_classID =  args.classID
         key_remark = args.remark
         all_results = Students.query.filter_by(classID = key_classID).all()
         data_list = list() 
         if all_results:
              for i in all_results:
                   dict_one = i.to_dict()
                   print(dict_one,      "--------") 
                   data_list.append(dict_one) value_msg = "success"
        else :
            value_msg = "couldn't search any infomation"
            result = {
                "status": 200,
                "msg": value_msg,
                "result": data_list
            }
            return result