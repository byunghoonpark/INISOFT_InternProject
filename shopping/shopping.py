class Customer :
    def __init__(self, id, pw, name, ph, address, email, registration_number):
        self.id = id
        self.pw = pw
        self.name = name
        self.ph = ph
        self.address = address
        self.email = email
        self.registration_number = registration_number
        self.mylist = []

        print("")
        print(" 로그인 성공! 쇼핑을 진행하세요! ")
        print("")

    def getUserID(self):
        return self.id

    def getShoppingList(self):
        return self.mylist

    def showShoppingList(self):
        print(" ", self.name, "'s list : " ,self.mylist )
        print("")

class Product :

    def __init__(self, product_name):
        self.prodcut_name = prodcut_name

    def check_list() :
        product_list = [ "무스탕", "패딩" , "코트", "후드", "스트라이프", "라이더자켓" ]
        print(" 상품 목록을 보여줍니다. ", product_list )

        good = input(" 원하는 상품을 입력하시오: ")
        for name in product_list :
            if good == name :
                print(" 원하는 상품이 존재합니다! ")
                print("")
                return good

        else :
            print(" 원하는 상품이 존재하지 않습니다! ")
            print("")
            return 0

class Shopping_Cart_Ui:
    def show():
        print(" 1. 장바구니 진행 / 2. 장바구니 종료 ")
        num = int(input(" "))
        print("")
        return num

class Shopping_Cart( Customer, Product ):

    def __init__(self, userID, product_name):
        self.userID = userID
        self.prodcut_name = product_name

    def enrollProduct(self, mylist, product_name):
        mylist.append(product_name)
        print(" ", product_name, " 이 쇼핑카트에 담겼습니다! ")

class Payment_Ui :
    def show():
        print( " 결제를 진행합니다. ")
        print( " 1. 카드 결제 / 2. 현금 결제 / 3. 결제 취소 ")
        num = int(input(" "))
        return num

class Bank:
    def choose_bank():
        bank_list = [ '국민', '우리', '신한', 'IBK', '하나', '농협' ]
        print(" 결제를 희망하는 은행을 선택하시오: ", bank_list)
        bank = input(" 은행 선택 : ")
        return bank

class Payment:

    def __init__(self, user_id) :
        self.user_id = user_id

    def pay(self, uesr_id, pay_means) :
        print("")
        print("", self.user_id, "님! 결제를 진행합니다." )

        if pay_means == "현금" :
            print(" 수단은 ", pay_means, " 입니다. ")
        else :
            print(" 수단은 ", pay_means, " 카드 입니다. ")

        print("")
        print( " 3일 후 배송 됩니다! ^_^ " )
        print("")

class Card_Payment(Payment) :

    def __init(self, user_id):
        super().__init__(user_id)

    def pay(self, user_id, pay_means):
        super().pay(user_id, pay_means)

class Cash_Payment(Payment) :
    def __init(self, user_id):
        super().__init__(user_id)

    def pay(self, user_id, pay_means):
        super().pay(user_id, pay_means)


class Join :
    def join():
        id = input(" 사용자 아이디를 입력하시오: ")
        pw = int(input(" 사용자 비밀번호를 입력하시오. 단, 숫자로만 입력하시오: "))
        name = input(" 사용자 이름을 입력하시오: ")
        ph = input(" 사용자 전화번호를 입력하시오: ")
        address = input(" 사용자 주소를 입력하시오: ")
        email = input(" 사용자 이메일을 입력하시오: ")
        registration_number = input(" 사용자 주민등록 번호를 입력하시오: ")
        return id, pw, name, ph, address, email, registration_number

class Ui:
    def show():
        print("")
        print(" **************************************************** ")
        print("                                                      ")
        print(" *** Welcome to Byunghoon & Sujin's Shopping Mall *** ")
        print(" ***       First, Join our Shopping Mall          *** ")
        print("                                                      ")
        print(" **************************************************** ")
        print("")


if __name__ == "__main__":

    Ui.show()
    id, pw, name, ph, address, email, registration_number = Join.join()
    C = Customer(id, pw, name, ph, address, email, registration_number)

    while True :

        while True: # 장바구니
            shoppingCart_check = Shopping_Cart_Ui.show()
            if shoppingCart_check == 1:
                product_name = Product.check_list()
                if not product_name == 0:
                    Cart = Shopping_Cart( C.getUserID(), product_name )
                    Cart.enrollProduct( C.getShoppingList(), product_name)
                    C.showShoppingList()
            else :
                print(" 장바구니를 종료합니다! ")
                print("")
                break

        pay_check = Payment_Ui.show()

        if pay_check == 1 : # 카드 결제
            bank = Bank.choose_bank()
            cp = Card_Payment( C.getUserID() )
            cp.pay( C.getUserID(), bank  )

        elif pay_check == 2 : # 현금 결제
            cp = Cash_Payment( C.getUserID() )
            cp.pay( C.getUserID(), "현금" )

        else : # 결제 종료
            print(" 결제를 종료합니다.")
            break

        print(" 계속 쇼핑을 하시겠습니까? 1. YES / 2. NO")
        num = int(input(" "))
        if num == 1 :
            print( " 쇼핑을 계속합니다! " )
            print( "" )
            continue
        else :
            print( " 이용해주셔서 감사합니다! " )
            break
