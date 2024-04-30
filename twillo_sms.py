import pymysql.cursors
from twilio.rest import Client

def outgoing_sms():
    # Your Account SID and Auth Token from console.twilio.
    try:
        account_sid = "AC93a368f6304c1dd05e1697120f3d40af"
        auth_token  = "f677961f5b4a7ffe1c1d8bc34146f431"
        client = Client(account_sid, auth_token)
        connection = pymysql.connect(host='mura-db-poc.c1ddjzxizuua.us-east-1.rds.amazonaws.com',
                                user='admin',
                                password='Mura2024',
                                database='mura',
                                cursorclass=pymysql.cursors.DictCursor)
        with connection:
            with connection.cursor() as cursor:
                # Create a new record
                query = "SELECT idclient_jobs,cust_mobile FROM mura.client_jobs where status='to-be-confirmed'"
                cursor.execute(query)
                myresult = cursor.fetchall()
                for x in myresult:
                    if x['cust_mobile'] and x['cust_mobile']!="NULL":
                        message = client.messages.create(
                            to=f"{x['cust_mobile']}",
                            from_="+18889265591",
                            body="Conformed appointment")
                        print(message.sid)
                        update_query = f"UPDATE mura.client_jobs SET status = 'Confirmation_sent' WHERE idclient_jobs = {x['idclient_jobs']};"
                        cursor.execute(update_query)
                        connection.commit()
        return "records updated"
    except Exception as e:
        print(e)
        return "records not updated"