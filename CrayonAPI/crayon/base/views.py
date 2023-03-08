from django.shortcuts import render
import requests
import base64
import json



clientId = '33731c54-94b6-430b-872f-be0ca64f7bd5'
clientSecret = '5bb1a205-a7ab-49f5-bd57-105e832aab0e'
userName = 'api@testcustomer.com'
password = 'ePLE8129087%'


# Encoding clientid and clientsecret into base64
sample_string = clientId+":"+clientSecret
sample_string_bytes = sample_string.encode("ascii")
base64_bytes = base64.b64encode(sample_string_bytes)
encorded = base64_bytes.decode("ascii")
  



def home(request):
    url = 'https://api.crayon.com/api/v1/connect/token/'

    headers={
        "Accept " : "application/json",
        "Content-Type":"application/x-www-form-urlencoded",
        "Authorization":"Basic  " + encorded
        }
    
    data ={
        "grant_type": "password",
        "username": userName,
        "password": password,
        "scope": "CustomerApi"
    }

    res = requests.post(url,headers=headers,data=data).json()

    token = res['AccessToken']

    request.session['token_value'] = token
    
    return render(request,'base/home.html',{"token":token})



def getOrganizations(request):
    token = request.session['token_value']
    
    if token:
        search = ''
        page = ''
        pageSize = ''

        url = f'https://api.crayon.com/api/v1/organizations/?search={search}&page={page}&pageSize={pageSize}'

        headers={
            "Accept " : "application/json",
            "Content-Type":"application/x-www-form-urlencoded",
            "Authorization":"Bearer " + token
            }
        
        
        res = requests.get(url,headers=headers).json()
    else:
        res = "Token missing"

    return render(request,'base/get_organization.html',{"res":res})



def getUsers(request):
    token = request.session['token_value']
    
    if token:
        search = ''
        page = ''
        pageSize = ''
        userRole = ''

        url = f'https://api.crayon.com/api/v1/users/?search={search}&page={page}&pageSize={pageSize}&role={userRole}'

        headers={
            "Accept " : "application/json",
            "Content-Type":"application/x-www-form-urlencoded",
            "Authorization":"Bearer " + token
            }
        
        
        res = requests.get(url,headers=headers).json()
    else:
        res = "Token missing"

    return render(request,'base/get_users.html',{"res":res})

   

def getCusomerTenent(request):
    token = request.session['token_value']
    res = ''
    if request.method == 'POST':
        if token:
            organizationId = request.POST['orgid']
            search = ''
            page = ''
            pageSize = ''
            userRole = ''

            url = f' https://api.crayon.com/api/v1/customertenants/?organizationId={organizationId}&search={search}&page={page}&pageSize={pageSize}'

            headers={
                "Accept " : "application/json",
                "Content-Type":"application/x-www-form-urlencoded",
                "Authorization":"Bearer " + token
                }
            
            
            res = requests.get(url,headers=headers).json()
        else:
            res = "Token missing"

    return render(request,'base/get_cusomer_tenent.html',{"res":res})


def getSingleCusomerTenent(request):
    token = request.session['token_value']
    res = ''
    if request.method == 'POST':
        if token:
            Id = request.POST['id']
            
            url = f'https://api.crayon.com/api/v1/customertenants/{Id}/detailed/'

            headers={
                "Accept " : "application/json",
                "Content-Type":"application/x-www-form-urlencoded",
                "Authorization":"Bearer " + token
                }
            
            
            res = requests.get(url,headers=headers).json()
        else:
            res = "Token missing"

    return render(request,'base/get_single_cusomertenent.html',{"res":res})



def createCusomerTenet(request):
    token = request.session['token_value']
    res = ''
    if request.method == 'POST':
        if token:
            data = {
                    "Tenant": {
                        "Name": "My test costomer QWERTY",
                        "Publisher": {
                        "Id": "2"   
                        },
                        "DomainPrefix": "mycustomerprefix",
                        "CustomerTenantType": "2",
                        "Organization": {
                        "Id": "4016913"
                        },
                        "InvoiceProfile": {
                        "Id": "7"
                        }
                    },
                    "Profile": {
                        "Contact": {
                        "FirstName": "shamil test",
                        "LastName": "user",
                        "Email": "shamil.user@email.com",
                        "PhoneNumber": "000-12345689"
                        },
                        "Address": {
                        "FirstName": "Firstname",
                        "LastName": "Lastname",
                        "AddressLine1": "Streetaddress 4",
                        "City": "City",
                        "Region": "Region",
                        "PostalCode": "123456",
                        "CountryCode": "US"
                        }
                    },
                    "Company": {
                        "OrganizationRegistrationNumber": "4016913"
                    }
                }
            
            url = 'https://api.crayon.com/api/v1/customertenants/'

            headers={
                "Accept " : "application/json",
                "Content-Type":"application/x-www-form-urlencoded",
                "Authorization":"Bearer " + token
                }
            
            
            res = requests.post(url,headers=headers,json=data).json()
            
            
        else:
            res = "Token missing"

    return render(request,'base/create_costomer_tenent.html',{"res":res})


