import requests
from typing import Literal

BASE_URL = "http://127.0.0.1:8001/api/v1"




def get_student_detail(email:str):
    """
    Provide the email id to get the information about the student, course and refund status 

    Example :- 
    (Args) : email = 'rohit@gmail.com' 
    (return) : {
                "email": "rohit@gmail.com",
                "total_purchases": 1,
                "purchases": [
                    {
                    "student_id": 5,
                    "email": "rohit@gmail.com",
                    "login_date": "2026-11-05",
                    "purchase_id": 24,
                    "course_id": "DSA101",
                    "course_name": "Data Structures and Algorithms",
                    "purchase_date": "2026-11-05T13:00:00",
                    "refund_status": "active"
                    }
                ]
                }
    """ 
    try:
        response = requests.get(url=f"{BASE_URL}/students/purchases",params={"email": email},timeout=10)
        data = response.json()
        return data

    except Exception as e:
        print(e)


def update_refund_status(purchase_id:int,refund_reason:str,refund_status:Literal['active','pending','non-applicable']):
    """
    Update refund status function
    Provide the  purchase_id,refund_reason and refund_status choose refund_status out of these literal = ['active','pending','non-applicable'] to update refund status of that status 

    if refund_reason is 
    'active' means Student is using that course and not asked for refund
    'pending' means refund is being processed
    'not-applicable' means student is not eligible for refund
    Example :- 
    (Args) : purchase_id =17 ,refund_reason='No reason', refund_status = 'pending' 
    (return) : {
            "message": "Refund status updated successfully",
            "purchase": {
                "purchase_id": 17,
                "student_id": 1,
                "course_id": "SQL101",
                "enroll_date": "2026-11-02T11:00:00",
                "refund_status": "pending"
            }
            }

    """ 
    try:
        response = requests.put(url=f"{BASE_URL}/purchases/{purchase_id}/refund-status",json={"refund_status":refund_status,"refund_reason":refund_reason},timeout=10)
        data = response.json()
        return data

    except Exception as e:
        print(e)

def get_refund_policy():
    "Our Refund policy call this function for our refund policy"

    return "As per our return policy if student is only eligible for course refund if its enrolled date is not older than 7 days  otherwise we cannot return and we accept any reason for refund we do not judge by the reason only if it is not older than 7 days"                        