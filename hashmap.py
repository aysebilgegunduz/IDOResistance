
import hashlib


class IDORUtil:
    """
    Hashing Library for users ID to avoid IDOR
    """

    def __init__(self):
        self.SALT = "[MY_SALT_MY_SALT]"


    def computeFrontID(self, realUserID):
        if realUserID != None and realUserID.strip():
            tmp = self.SALT + realUserID
            digester = hashlib.sha1(tmp.encode('utf-8'))
            hash = digester.hexdigest()
        return hash

if __name__ == "__main__":
    idorObj = IDORUtil()

    #Example
    print(idorObj.computeFrontID("user1"))
    print(idorObj.computeFrontID("user2"))


