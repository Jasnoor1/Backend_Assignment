from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer
from django.http import HttpResponse
from .resources import EmployeeResource
from rest_framework import status
from rest_framework.decorators import api_view
from .filters import EmployeeFilter
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from  rest_framework import mixins
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
import json

# Create your views here.
# users/
class UsersList(generics.ListAPIView):
        queryset = Employee.objects.all()
        serializer_class = EmployeeSerializer
        filter_class = EmployeeFilter
        filter_fields = ('first_name','last_name')
        ordering_fields = ('age')
        ordering = ('age',)


        @api_view(["GET"])
        def employee_list(request):
            employee = Employee.objects.all()[:5]
            # page = request.GET.get('page',1)
            # paginator = Paginator(employee,10)
            serializer = EmployeeSerializer(employee,many=True)
            # try:
            #     employee = paginator.page(page)
            # except PageNotAnInteger:
            #     employee = paginator.page(1)
            # except EmptyPage:
            #     employee = paginator.page(paginator.num_pages)
            #
            # return render(request, 'template/user_list.html', {'employee': employee})
            return Response(serializer.data)

# user/
class EmployeeCreateView(generics.CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    @api_view(["POST"])
    def create_employee(request):
        serializer = EmployeeSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#return Response(serializer.data)
    # def get_post_user(self,request):
    #     print('Hi, I am in function')
    #     if request.method == 'GET':
    #         print('Hi, I am in Get Method')
    #         users = Users.objects.all()[:5]
    #         serializer = UsersSerializer(users,many=True)
    #         return Response(serializer.data)
    #     elif request.method == 'POST':
    #         return Response(request.DATA, status=status.HTTP_201_CREATED)
# # users/create/
# class EmployeeCreateView(generics.CreateAPIView):
#     serializer_class = EmployeeSerializer
#
#     def create_employee(request):
#         serializer = EmployeeSerializer(request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message":"User created"})
#         else:
#             data = {
#                 "error" : True,
#                 "errors" : serializer.errors,
#             }
#             return Response(data)
# posts/detail/
# class EmployeeDetailView(generics.RetrieveAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#
#     @api_view(["GET"])
#     def employee_details(request,pk):
#         employee = Employee.objects.get(id=pk)
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data)
# posts/
class UsersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    @api_view(["GET"])
    def employee_details(request,pk):
        employee = Employee.objects.get(id=pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)


    # def put(self, request, *args, **kwargs):
    #     print("I am in put function")
    #     data = request.data
    #     print(data)
    #     put = Employee.objects.all()
    #     serializer = EmployeeSerializer(put, data = data,many=True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        print("I am in delete function")
        # item_id = Employee.objects.get(pk)
        # print(item_id)
        if request.method == 'POST':
            print("I am in Post Function")
            #serializer = EmployeeSerializer()
            item_id = int(request.POST.get('item_id'))
            item = Employee.objects.get(id=item_id)
            item.delete()
            # ob = Employee.objects.get().pk
            # print(ob)
            # snippet = self.get_object(pk)
            # print(snippet)
            # snippet.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

# delete/
class EmployeeDeleteView(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def delete_employee(request,pk):
        employee = get_object_or_404(Employee,id=pk)
        employee.delete()
        return Response({"message":"Deleted"})
    #serializer_class = EmployeeSerializer


# update/
class EmployeeUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    @api_view(["GET","PUT"])
    def employee_update(request,pk):
        employee = Employee.objects.get(id=pk)
        if request.method == "PUT":
            print("I am in PUT Method")
            serializer = EmployeeSerializer(employee,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    # def get(self,request):
    #     users = Employee.objects.all()[:5]
    #     serializer = (users, many=True)
    #     return Response(serializer.data)
# post/
# class users_post(APIView):
#
#
#     def post(self,request):
#         data = {
#             'first_name':request.data.get('first_name'),
#             'last_name': request.data.get('last_name'),
#             'company_name':request.data.get('company_name'),
#             'age': int(request.data.get('age')),
#             'city':request.data.get('city'),
#             'state':request.data.get('state'),
#             'zip':int(request.data.get('zip')),
#             'email':request.data.get('email'),
#             'web':request.data.get('web'),
#         }
#         serializer = EmployeeSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

