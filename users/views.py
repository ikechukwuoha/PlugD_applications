# from django.shortcuts import render

# from django.contrib.auth import get_user_model
# User = get_user_model()
# from .serializers import UserSerializer

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import permissions, status

# class SignupView(APIView):
#     permission_classes = (permissions.AllowAny, )

#     def post(self, request):
#         try:
#             data = request.data

#             first_name =  data['first_name']
#             last_name =  data['last_name']
#             username =  data['username']
#             email = data['email']
#             email = email.lower()
#             password = data['password']
#             re_password = data['re_password']
#             is_pd_staff = data['is_pd_staff']


#             if is_pd_staff == 'True':
#                 is_pd_staff = True
#             else:
#                 is_pd_staff = False


#             if password == re_password:
#                 if len(password) >=8:
#                     if not User.objects.filter(email=email).exists():
#                         if not is_pd_staff:
#                             User.objects.create_user(
#                                 email=email,
#                                 username=username, 
#                                 first_name=first_name, 
#                                 last_name=last_name,
#                                 password = password
#                             )

#                             return Response(
#                                 {'success': 'User created Successfully...'},
#                                 status=status.HTTP_201_CREATED
#                             )

#                         else:
#                             User.objects.create_is_pd_staff(
#                                 email=email,
#                                 username=username, 
#                                 first_name=first_name, 
#                                 last_name=last_name,
#                                 password = password
#                             )

#                             return Response(
#                                 {'success': 'Pd_Account created Successfully...'},
#                                 status=status.HTTP_201_CREATED
#                             )

#                     else:
#                         return Response(
#                             {'error': 'User With this Email Already Exist....'},
#                             status=status.HTTP_400_BAD_REQUEST
#                         )
                        
#                 else:
#                     return Response(
#                         {'error': 'Password Must be at Least 8 Characters'},
#                         status=status.HTTP_400_BAD_REQUEST
#                     )
            
#             else:
#                 return Response(
#                     {'error': 'password Mismatched....'},
#                     status=status.HTTP_400_BAD_REQUEST
#                 )
            
#         except:
#             return Response(
#                 {'error': 'Something Went Wrong While Registering an Account...'},
#                 status=status.HTTP_500_INTERNAL_SERVER_ERROR
#             )



# class RetrieveUserView(APIView):
#     def get(self, request, format=None):
#         try:
#             user = request.user
#             user = UserSerializer(user)

#             return Response(
#                 {'user': user.data},
#                 status=status.HTTP_200_OK
#             )

#         except:
#               return Response(
#                 {'error': 'Something Went wrong While Retrieving User Detail'},
#                 status=status.HTTP_500_INTERNAL_SERVER_ERROR
#             )
