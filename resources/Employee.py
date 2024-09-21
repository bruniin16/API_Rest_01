from flask_restful import Resource, reqparse

employees = [{"id_emp" : 1, "nome" : "Ronaldo", "email" : "ronny@gmail.com"},
             {"id_emp" : 2, "nome" : "Marquito", "email" : "marquitodelas@hotmail.com"}]

class Employee(Resource):

    args = reqparse.RequestParser()
        
    args.add_argument("id_emp")
    args.add_argument("nome")
    args.add_argument("email")

    def get(self):
        return employees
    
    def post(self):

        dados = Employee.args.parse_args()

        new_employee = {
            "id_emp" : int(dados["id_emp"]),
            "nome" : dados["nome"],
            "email" : dados["email"]
        }

        employees.append(new_employee)

        return new_employee, 200
    
    def get_emp(id):
        for i in employees:
            if int(i["id_emp"]) == id:
                return i
            return None
    
    def put(self, id):

        
        dados = Employee.args.parse_args()

        new_employee = {
            "id_emp" : int(dados["id_emp"]),
            "nome" : dados["nome"],
            "email" : dados["email"]
        }

        #employee = Employee.get_emp(id)
        
        employee_index = None
        for i, emp in enumerate(employees):
            if int(emp["id_emp"]) == id:
                employee_index = i
                break

        if employee_index is not None:
            employees[employee_index] = new_employee
            return new_employee, 200
        else:
            employees.append(new_employee)
            
            return new_employee, 201
        
    def delete(self, id):
        global employees

        employees = [emp for emp in employees if emp["id_emp"] != id]

        return {"message" : "Employee deleted."}